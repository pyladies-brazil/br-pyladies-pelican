---
title: "post-mortem: quebra de build no site da pyladies"
layout: post
date: 2023-10-17
headerImage: false
author: giovanamorais
category: blog
---

absolutamente tudo quebrou. codeship se tornou pago e o buildpack do heroku estava
desatualizado.
[nenhum build funcionava.](https://github.com/pyladies-brazil/br-pyladies-pelican/issues/441)

respiramos fundo, arregaçamos as mangas e fomos descobrir o que estava
acontecendo. essa postagem é a descrição de todo o processo pra tentar resolver
o bug dos builds. spoiler: o problema foi resolvido!

# investigação
o meu primeiro passo foi entender como era o fluxo inteiro de deploy do site. o
que eu descobri é que era bem simples: quando um PR do repositório era mergeado,
o Codeship iniciava uma tarefa de enviar as atualizações pro Heroku e o Heroku
fazia o deploy do site.

quando o Codeship se tornou uma ferramenta paga, deletou todas as contas
gratuitas. a partir disso tentei fazer o deploy direto pelo Heroku de uma forma
manual, a fim de validar o que estava dando errado e por que estava dando
errado. logo no primeiro deploy que tentei fazer, encontrei um erro: o Python
não estava sendo instalado corretamente.

## heroku e o buildpack
o Heroku usa _buildpacks_ pra instalar bibliotecas, linguagens, ferramentas e
qualquer coisa que você precise pro seu projeto. existem buildpacks
[oficialmente suportados pelo
Heroku](https://devcenter.heroku.com/articles/buildpacks#officially-supported-buildpacks),
como o buildpack para Python, e os buildpacks que são feitos por terceiros e
pela comunidade, como o [builpack para o
Pelican](https://github.com/getpelican/heroku-buildpack-pelican) e o
[buildpack para o
nginx](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-nginx).

o site da PyLadies usava um buildpack que foi
[criado a partir do buildpack do Pelican](https://github.com/pyladies-brazil/heroku-buildpack-pelican),
mas customizado para o nosso site.

### tentativa 1: atualizar o buildpack da PyLadies
ao analisar o buildpack da PyLadies, notei que os passos eram bem simples. ele
instalava o Python em uma versão fornecida, rodava o Pelican para gerar o
conteúdo do blog e então instalava o nginx e dava acesso à pasta com os arquivos
.html gerados no passo anterior.

tentar atualizar as versões necessárias no buildpack não funcionou. o maior
motivo era porque o método de instalação do Python estava defasado.

conferi no buildpack oficial do Python como era feita essa instalação e até
pensei em ajustar o nosso buildpack, mas aí me veio a pergunta: "será que vale a
pena?"

e essa pergunta foi muito importante. se um dia mudassem o endereço que eu
deveria usar para fazer o download do Python *de novo*, eu teria que arrumar *de
novo* esse buildpack. isso é um retrabalho, já que as pessoas que mantêm o
buildpack oficial do Python vão fazer isso por nós. dessa forma, decidi partir
pra minha segunda abordagem.

### tentativa 2: combinar o buildpack da PyLadies com buildpacks oficiais
a ideia aqui era simples: em vez de instalar o python dentro do nosso buildpack,
eu ia usar o buildpack oficial do python + o nosso buildpack. dessa forma,
teríamos sempre a instalação mais atual do Python e manteríamos no nosso
buildpack apenas o que era essencial.

o problema dessa abordagem é que eu notei que não tinha nada demais acontecendo
no nosso buildpack, então mais uma vez era retrabalho. precisaríamos sempre
atualizar os métodos de instalação do nginx e não valia a pena ficar fazendo
algo que já está sendo feito porquem mantém o buildpack do nginx.

rapidamente fui para minha terceira tentativa.

### tentativa 3: trocar tudo por buildpacks oficiais
aqui, troquei o nosso buildpack velho e capenga por dois buildpacks: um
buildpack de Python, que instala o Python e todas as bibliotecas que a gente
precisa, e um buildpack do nginx, que vai ser responsável por fazer nosso site
aparecer.

criei um arquivo Procfile, que é um indicativo pro Heroku do que ele precisa
rodar enquanto faz o deploy. o nosso Procfile é bem simples, ele gera as oáginas
do Pelican e então roda o nginx.

testei tudo e os builds estavam 100%. ótimo!

fui para o meu próximo passo: github actions.

## github actions
tudo que eu estava fazendo até agora era manualmente. eu gerava as mudanças na
minha máquina e fazia o deploy direto no Heroku. isso não é bem o que a gente
quer. a gente quer que, toda vez que um Pull Request seja mergeado, uma
mágica aconteça e essa mudança também seja refletida no site. dei uma fuçada na
documentação do github actions e encontrei uma que servia para fazer o deploy no
Heroku. fiz o que precisava ser feito e criei um PR teste. o build rodou
perfeitamente! as coisas estavam dando certo! até que fui entrar no site
pra conferir e...

![img](/images/404_not_found.png)

## giovana vs pelican
o nginx não estava achando a pasta com o
conteúdo do site e eu passei muito tempo tentando entender o porquê.

o github actions estava ok, os builds do heroku estavam ok também, mas **algo**
estava acontecendo porque o nginx não estava conseguindo achar a pasta com o
conteúdo. depois de fuçar muito dentro dos logs dos builds finalmente achei uma
explicação:

```shell
CRITICAL UndefinedError: 'pelican.contents.Article object' has no attribute 'tags'
```

e aí eu percebi que o problema não estava no nginx que eu tinha passado os
últimos dois dias investigando. o problema tava no *safado* do pelican e no
template.

fiz o que todo hacker faz e joguei o erro no google. não surpreendentemente,
achei uma pessoa com exatamente
[o mesmo problema que o meu](https://github.com/getpelican/pelican/issues/2910)
e descaradamente roubei a ideia de só colocar uma validação a respeito do
atributo de "tags". não é uma solução de fato, mas o objetivo de todo o trabalho
era consertar o build. a atualização do template fica pra depois.

uma vez que o template foi consertado e o merge feito, o github action fez o
trabalho dele e o deploy aconteceu. mais do que isso: o deploy funcionou!
:rocket:


## agradecimentos
tudo isso aconteceu ao som desse
[vídeo de 3 horas com vários álbuns de drum & bass](https://www.youtube.com/watch?v=1zGaTE2AmsU),
que é a minha obsessão atual pra estudar porque me sinto em um videogame. então
o meu agradecimento pricipal vai pro canal do Youtube `Mr Fredericks.`. obrigada!
