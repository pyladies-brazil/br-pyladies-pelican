Title: Post Mortem: Incidente de 14 de Novembro de 2019 - Quebra de build
Slug: post-mortem-14-nov
Date: 2019-11-17 11:58:00
Tags: pelican, build, site, staging, codeship, heroku
author: Jessica Temporal
comments: true
Category: Site
summary: O build do ambiente de staging do site do PyLadies Brasil quebrou. Foi resolvido em 17 de Novembro inserindo nova chave de API na configuração do Codeship.

## Resumo
O _build_ do ambiente de _staging_ do site do PyLadies Brasil quebrou. Foi resolvido em 17 de Novembro inserindo nova chave de API na configuração do Codeship.

## Contexto
O site do PyLadies Brasil é escrito em [Pelican](https://blog.getpelican.com/), um gerador de sites estáticos escrito em Python, e tem seu código hospedado no [GitHub](https://github.com/pyladies-brazil/br-pyladies-pelican), uma rede social de compartilhamento de código. Hoje nós temos no ar dois ambientes: o de _staging_ e o de produção. Ambos tem seu _build_ feito e estão no ar usando duas ferrramentas: o [Codeship](https://codeship.com/), ferramenta de integração contínua que usamos para fazer os _builds_ e o [Heroku](http://heroku.com/), uma plataforma para colocar _webapps_ no ar.

No GitHub nós configuramos dois ramos principais, assim conseguimos separar _staging_ de produção: para _staging_ nós usamos o ramo `develop` e para produção usamos a `master`. Toda nova funcionalidade ou adição de informação é inicialmente adicionada no ramo `develop` por meio de um _pull request_. Este ao ser mergeado, desencadeia um _build_ e um deploy para ambiente de _staging_. Após conferência desse primeiro deploy, nós abrimos um _pull request_ secundário de `develop` para `master`, que ao ser mergeado desencadeia novo _build_ e _deploy_, só que dessa vez para produção.

Como uma das mantenedoras do site do PyLadies Brasil, eu tenho acesso ao Codeship e, no dia 14 de Novembro às 12:04, recebi um e-mail notificando a quebra do _build_.

## Investigação
O primeiro passo da investigação foi olhar o _pull request_ que havia sido margeado em `develop` e que em tese gerou a quebra do _build_. O _pull request_ em questão foi o de número #286. Com tantas pessoas mexendo no site, é comum que alguns erros passem desapercebidos no momento do review gerando algum tipo de quebra. Olhando as alterações feitas no _pull request_, nada indicava um motivo para que o _build_ quebrasse.

Com isso a segunda coisa que fiz foi fazer o _build_ de `develop` localmente na minha máquina. Fazendo isso, se o problema fosse algo no código fonte do site eu veria essa quebra também na minha máquina. Mas não foi o caso, o _build_ rodou normalmente.

Por fim, acessei o Codeship para ver se lá existia algum detalhe do que estava quebrando o _build_ do site. Olhando o detalhamento do _build_, mostrava um aviso:

<img src="/images/post-mortem-14-nov-falha-codeship.png">

Com isso cheguei a conclusão que algo aconteceu com a chave de API que usávamos para fazer a comunicação entre o Codeship e o Heroku. Sendo assim, mandei um e-mail na lista que temos no google groups do PyLadies Brasil. Nesse e-mail eu pedi para que as pessoas que tem acesso aos projetos no Heroku (eu não tinha esse acesso até então) pudessem ou me adicionar como colaboradora no projeto lá no Heroku ou que investigassem o ocorrido.

Não muito depois do meu e-mail, uma PyLady me colocou como colaboradora do projeto. Infelizmente, isso não nos ajuda, o que acontece é que a chave de API que o Heroku gera é ligada a uma conta, ou seja, se você tem 10 apps no Heroku, você vai usar a mesma chave de API para todos eles. O que eu imagino que aconteceu é que a dona da app no Heroku regerou a própria chave trancando o acesso do Codeship.

## Solução
Para começar a resolver o problema do _build_, criei uma conta para o PyLadies Brasil no Heroku com o nosso e-mail. Em seguida, acessei o Heroku com a minha conta pessoal e adicionei o perfil do PyLadies Brasil como colaborador do projeto.

<img src="/images/post-mortem-14-nov-plbr-collaborator-heroku.png">

Após adicionar o PyLadies como colaborador, acessei a conta do PyLadies Brasil no Heroku e copiei a chave da conta. Logo depois colei a chave copiada nas configurações do projeto no Codeship. E por fim, manualmente disparei o _build_ que tinha quebrado novamente. Com a nova chave no lugar, o _build_ então passou.

<img src="/images/post-mortem-14-nov-build-passando.png">

## Conclusão
Precisamos ter melhor controle das ferramentas que usamos para o PyLadies Brasil e também um melhor entendimento como essas ferramentas funcionam e mantém as coisas no ar. Espero que esse _post mortem_ assim como a criação da conta do PyLadies Brasil nessas plataformas, ajudem nesse processo.
