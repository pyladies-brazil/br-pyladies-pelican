Menu
====
0. Aviso sobre a Síndrome do Impostor
1. Primeiros Passos
  * [Contribuindo](#contribuindo)
  * [Preparando o ambiente local](#preparando-o-ambiente-local)

2. Criando e Adicionando
  * [Criar um novo post](#criar-um-novo-post)
  * [Adicionar eventos](#adicionar-eventos)
  * [Adicionar ladies](#adicionar-ladies)
  * [Adicionar nova localização](#adicionar-nova-localização)
  * [Adicionar vídeos](#adicionar-vídeos)

3. Deploy
  * [Atualizando o site](#atualizando-o-site)

Aviso sobre Síndrome do Impostor 
============

A gente precisa da sua ajuda. Sério!

Pode ser que haja uma vozinha na sua cabeça dizendo que você não está pronta;
que você precisa fazer mais um tutorial ou aprender mais um framework, talvez
escrever mais algumas postagens no seu blog antes de conseguir nos ajudar com 
esse projeto.

Ignora essa voz. A gente te garante que esse não é o caso.

Tentamos deixar esse guia de contribuição o mais claro possível, mas este é um 
documento vivo, então qualquer dúvida, basta abrir uma [issue](https://github.com/pyladies-brazil/br-pyladies-pelican/issues/new/choose) 
e seguiremos melhorando!

Como você verá no decorrer do documento, nem toda contribuição é feita código. Você 
pode contribuir por meio de postagens, ideias e discussões, adicionando o 
evento do seu capítulo, adicionando o seu capítulo e etc.

Esse pequeno aviso foi traduzido [desse repositório](https://github.com/adriennefriend/imposter-syndrome-disclaimer). 

Obrigada por contribuir!


Contribuindo
============

1. Fork o projeto
2. Crie uma branch para a feature em que trabalhará: `git checkout -b my-new-feature`
3. Faça commit das suas alterações: `git commit -m 'Add some feature'`
4. Faça push desses commits para sua branch: `git push origin my-new-feature`
5. Envie um pull request para o nosso repositório

Obs.: Nós usamos português como linguagem padrão dos commits (:


Preparando o ambiente local
--------------------------
- Antes de mais nada, verifique se você tem o **Python 3.6.4** instalado na sua máquina.

(Atenção: se você estiver usando um **MacOS X** para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/))

Para criar uma `virtualenv` e instalar os pacotes necessários para rodar o projeto, siga as orientações do capítulo "Instalando e Rodando" do [Readme](https://github.com/pyladies-brazil/br-pyladies-pelican/blob/develop/README.md)

(Obs: se você pretende usar o ambiente virtual instalado via *make*, ele se encontra em `.venv/`.)

Criar um novo Post
------------------

Para criar um novo post, rode o comando:

	make newpost NAME='NOME DO SEU POST'

Ele irá criar um novo arquivo `nome-do-seu-post.md` na pasta `content` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar o post, renderize-o com o comando:

	pelican content

Se tudo deu certo, seu novo post já estará disponível na página.


Criar uma nova Página
---------------------

Para criar uma nova página, rode o comando:

	make newpage NAME='NOME PAGINA'

Ele irá criar um novo arquivo `nome-pagina.md` na pasta `content/pages` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar de editar a página, renderize-a com o comando:

	pelican content

Se tudo deu certo, sua página já estará disponível em `/slug-pagina/`.


Adicionar Eventos
-----------------

Existem duas formas de incluir eventos no site, manualmente e através de um evento no Facebook.

Para adicionar novos eventos manualmente, basta editar o arquivo `data/events.yml`. Ele possui o seguinte formato:

```yaml
- url: URL DO SEU EVENTO
  name: NOME DO EVENTO
  date: DATA EVENTO (Formato DD-MM-YYYY)
  local: LOCAL EVENTO
  facebook_id: ID DO EVENTO NO FACEBOOK (se houver)
```

Caso o evento seja novo, ele será automaticamente inserido em Novos Eventos. Caso contrário, já ficará na lista de Eventos passados.

É possível também importar os eventos do Facebook de páginas de grupos PyLadies espalhados pelo Brasil, para isso, primeiramente verifique se o ID do Facebook da página do seu grupo (aquele que aparece na URL quando acessado) se encontra na listagem de grupos em `utils/__init__.py`.

O próximo passo é obter um token de acesso do Facebook para o seu usuário. Você pode facilmente obte-lo no link https://developers.facebook.com/tools/explorer e copiando o campo "Token de acesso". Não compartilhe seu token de usuário com outras pessoas.

Em seguida, abra uma linha de comando e atribua seu token a uma variável de ambiente com o comando (não esqueça as aspas):

    export FACEBOOK_TOKEN="{seu-token}"

Agora é só rodar o comando abaixo, lembrando que o conteúdo gerado é estático, ou seja, para atualizá-lo é necessário re-executar o comando:

    make load-facebook-events


Adicionar nova Localização
--------------------------

Para adicionar uma nova localização de grupo de pyladies, edite o arquivo `data/locations.yml`. O formato é o seguinte:


```yaml
- city: CIDADE - ESTADO
  image: PATH IMAGEM LOCAL (Padrão: /images/locais/location.png)
  twitter: URL completa do twitter (rede social opcional)
  instagram: URL completa do Instagram (rede social opcional)
  youtube: URL completa para o canal do Youtube (rede social opcional)
  facebook: URL completa da página do facebook (rede social opcional)
  email: Email oficial do capítulo (@pyladies.com)
  url: Site oficial do capítulo (pyladies.com) (opcional)
```

**Atenção:** A imagem precisa ser `100px por 100px`.

O arquivo está dividido por estado, então, procura o teu e adiciona o capítulo nesse trecho do código. Além disso, informa apenas 03 (três) redes sociais, tá?! Quando passa disso a página fica um pouco desconfigurada.


Adicionar vídeos
----------------

Para adicionar um novo vídeo verifique qual categoria o vídeo irá se encaixar: Depoimentos, Dojos, Palestras ou Tutoriais, edite o arquivo correspondente a categoria que você escolheu `data/videos_depo.yml`,`data/videos_dojos.yml`,`data/videos_talks.yml` ou `data/videos_tutorials.yml` com o nome do vídeo e seu link. Ele possui o seguinte formato:

```yaml
- # Nome do Vídeo
  url: //www.youtube.com/embed/XXXXXXXXXXX
```

**Atenção:** O link do vídeo é aquele que se encontra na aba de incorporamento do youtube e não na de compartilhamento:
![Exemplo](https://cloud.githubusercontent.com/assets/6595551/19491891/59d9ff6a-9553-11e6-8163-0c65ca58d241.png "Link correto do youtube")

**Lembre-se** de colocar como comentário o título do vídeo antes do link:
![Exemplo](https://cloud.githubusercontent.com/assets/6595551/19491947/97e5df18-9553-11e6-9ed3-d1294f37a291.png "Comentário nos vídeos")


Editar Layout
-------------

O site PyLadies utiliza um framework CSS chamado [Foundation](http://foundation.zurb.com/sites.html). Antes de escrever estilos para algo em particular, recomendamos verificar se o framework não oferece a funcionalidade ou estilo desejado, bastando que seja aplicada uma classe específica ao HTML.


Atualizando o site
------------------

Todo pull-request aberto para o branch `master` irá disparar uma série de automações que checam a integridade do site e geram uma preview dele. 
Além disso, o time responsável por manter o site será marcado para revisar as mudanças propostas.

Para verificar se suas mudanças estão da forma que você espera, basta verificar o status check de deploy preview, clicar em detalhes e você vai ser redirecionada para um site com as suas mudanças.

Se estiver tudo certo, basta esperar que alguém revise e integre seu pull-request em `master`, o que vai disparar um deploy automático para o ambiente de produção, também conhecido como [nosso site](http://brasil.pyladies.com/).
