Title: Criando o site oficial do seu capítulo PyLadies
Slug: criando-um-site-para-o-seu-capitulo-pyladies
Date: 2020-10-16 03:40:57
Tags: dica, site
Author: Juliana Karoline

Você sabia que é possível usar a infraestrutura do PyLadies Global para hospedar
o site do seu capítulo PyLadies?

## Infraestrutura do PyLadies Global
Recentemente o PyLadies Global foi estruturado para gerenciar os recursos que
são destinados ao PyLadies de forma global. Dentro do PyLadies Global há alguns
projetos, sendo um deles o de tecnologia e infraestrutura que é responsável, dentre outras
coisas, pelo suporte aos sites dos capítulos PyLadies.

Através do time de infra é possível obter um domínio _.pyladies.com_ personalizado
com o nome do seu capítulo, além de hospedagem gratuita para o site. O processo de solicitação
leva poucos minutos para ser iniciado e o time de infra costuma responder bem
rápido. A criação do site do PyLadies São Carlos, por exemplo, foi completada em
menos de 24h após a solicitação.


## Etapas do processo de solicitação
O processo de solicitação é feito através do repositório
[chapter-websites](https://github.com/pyladies/chapter-websites) no GitHub, onde fica centralizado
os sites de todos os capítulos que estão na infraestrutura do PyLadies Global.
No README do repositório tem as informações sobre como fazer a
requisição. Vale ressaltar que, por enquanto, **o processo é feito todo em
inglês.**


Para iniciar o pedido é preciso abrir uma _issue_ com algumas
informações sobre o capítulo e também sobre as tecnologias que serão usadas
no site. A _issue_ possui um template para ajudar no
preenchimento dos dados, além de uma lista com os passos que devem ser
cumpridos para a solicitação ser atendida. Após a abertura da _issue_, é preciso
notificar o time de infra no canal #project-tech-infra.

Quando o time de infra receber o seu pedido, será criado um repositório para o
site do seu capítulo, onde você poderá personalizar o template padrão
fornecido, ou até mesmo criar o seu próprio _design_. Após finalizar a
edição do site nesse repositório, você precisará abrir um _pull request_ para adicioná-lo como
um submódulo do repositório
[chapter-websites](https://github.com/pyladies/chapter-websites).

Assim que o seu _pull request_ for aprovado e mergeado, o site estará no ar!


## Como fazer o pedido
Acesse o repositório
[chapter-websites](https://github.com/pyladies/chapter-websites), vá para a aba
_Issues_ e clique em _New issue_.

<img src="/images/criando-site/repo-issues.png">

Será exibido uma lista de templates disponíveis, escolha _Requesting a new
PyLadies Chapter website_ clicando em _Get started_.

<img src="/images/criando-site/issues-templates.png">

Você deve preencher as informações solicitadas no template, sendo elas:

* **qual o nome do capítulo que está solicitando o site?**

São Carlos, por exemplo.

* **o capítulo está cadastrado no diretório de capítulos do PyLadies?**

O capítulo precisa estar devidamente cadastrado para que a solicitação seja
aceita. Caso o seu capítulo ainda não esteja oficializado, há um link para o
formulário de cadastro no template. Após o cadastro você pode continuar com o
pedido.

* **qual é o domínio personalizado desejado?**

O domínio será _.pyladies.com_. Você pode escolher o que colocar como prefixo
(_saocarlos.pyladies.com_, por exemplo).

* **quais organizadoras terão permissão de edição no repositório do site?**

Será criado um time para o seu capítulo, que terá permissão de edição no
repositório do site. Como o repositório será criado dentro da organização do
PyLadies, é preciso listar as organizadoras que serão inseridas no time. Os
dados necessários são: nome, usuário do GitHub,
  usuário do Slack do PyLadies Global e o "cargo" dentro do capítulo
  (organizadora ou cofundadora, por exemplo).

* **você gostaria de usar um template para gerar o site, ou prefere que ele seja
  criado em branco?**

Você pode escolher entre usar um template padrão do PyLadies no Netlify, forkar
um design que você já tenha em algum repositório, ou criar o site em branco.

* **onde você vai hospedar o site?**

Você pode escolher entre hospedar no GitHub Pages (para sites estáticos) ou no
Heroku. Caso você queira hospedar em outro local, é preciso informar onde será,
para que o time de infra possa fazer as configurações de DNS.

Após as perguntas, há um _checklist_ com duas seções para acompanhar o
andamento do pedido. A primeira seção deve ser preenchida por você e a segunda é
preenchida pelo time de infra. Para finalizar o pedido, você deve responder às
perguntas acima (feito!) e mandar uma mensagem no canal \#project-tech-infra no
Slack para que o time de infra veja a sua _issue_. Esses são os dois primeiros
passos do _checklist_ (pode marcá-los no template), os próximos serão feitos
quando o seu pedido for respondido. Agora, basta clicar em _Submit new issue_ e
aguardar.


## O que fazer após enviar o pedido?
Quando o seu pedido for visualizado pelo time de infra, será criado um time na
organização do PyLadies no GitHub para o seu capítulo, com as organizadoras que
foram listadas no pedido. É preciso aceitar o convite para fazer parte do time.
Além do time, será criado um repositório para o site do seu capítulo. O link
para o repositório será adicionado na _issue_ que você abriu, portanto é preciso
acompanhar a discussão pelo GitHub.

Tendo acesso ao repositório, você e as outras organizadoras poderão personalizar
o site para deixá-lo como vocês quiserem. Assim que a a edição estiver
finalizada, será preciso abrir um _pull request_ para adicionar o repositório do
site como um submódulo do
repositório [chapter-websites](https://github.com/pyladies/chapter-websites).


## Como criar um submódulo do seu novo site
Primeiramente você precisará fazer um fork do repositório
[chapter-websites](https://github.com/pyladies/chapter-websites) e cloná-lo na
sua máquina. Em seguida, você irá adicionar o repositório do seu site como um
submódulo no repositório
[chapter-websites](https://github.com/pyladies/chapter-websites). Para isso,
você precisará informar a URL (https) de clonagem do repositório e a branch de produção do seu site
(caso a hospedagem seja no GitHub Pages, a branch de produção é _gh-pages_). Após a criação do submódulo, basta
inicializá-lo para que o último commit do site seja fixado no
[chapter-websites](https://github.com/pyladies/chapter-websites).

Para fazer isso, execute os comandos:

```
$ cd chapter-websites # entra na pasta do repo
$ git submodule add -b <BRANCH_DE_PRODUÇÃO> <URL_DO_REPOSITÓRIO> <NOME_DO_CAPÍTULO>
# exemplo: git submodule add -b gh-pages https://github.com/pyladies/pyladies-sao-carlos-website.git saocarlos
$ git submodule init
```

O último comando criará uma entrada no arquivo _.gitmodules_ com a configuração
do seu submódulo. Você precisará fazer um commit com as alterações e abrir um
_pull request_ do seu fork para o repositório original.

<img src="/images/criando-site/commit-submodulo.png">

## Criando o _pull request_ para adicionar o seu submódulo
Acesse o seu fork do repositório e clique no botão _Pull request_.

<img src="/images/criando-site/repo-pr.png">

Escolha _pyladies/chapter-websites_ como _base repository_ e _main_ como _base_,
escolha o seu fork como _head repository_ e _main_ como _compare_.
Se tudo estiver correto, aparecerá a mensagem _Able to merge_.

<img src="/images/criando-site/branches-pr.png">

Clique no botão _Create pull request_ e aparecerá um template parecido com o da
_issue_ do pedido. As informações pedidas no template são:

* **esse capítulo já estava no repositório monolito do PyLadies?**

Essa pergunta é para os sites que existiam antes da infraestrutura nova do
PyLadies Global ser criada, portanto marque Não.

* **caso você tenha marcado sim, você já deletou do monolito?**

Como o seu site é novo, essa pergunta não se aplica, portanto pode deixá-la em
branco.

* **esse _pull request_ está adicionando um site de capítulo?**

Como você está adicionando o seu site novo, marque Sim.

* **se você marcou sim, o capítulo está registrado no diretório de capítulos do
  PyLadies?**

Você já confirmou que o seu capítulo está cadastrado lá na criação do pedido,
certo? Portanto, marque Sim.

* **se você marcou não, por favor registre o seu capítulo. Você conseguiu fazer
  o cadastro?**

Novamente, não se aplica à capítulos cadastrados, pode deixá-la em branco
também.

* **esse _pull request_ está atualizando um site já existente?**

No futuro, quando você precisar atualizar o site, será preciso abrir um PR igual
à esse. No momento da criação, pode marcar Não.

* **checklist do _pull request_**

Marque para indicar que você preencheu as seções acima.

Com o template preenchido, clique em _Create pull request_. Será gerado um
número de identificação do seu _pull request_ (\#14, por exemplo). O terceiro
item do _checklist_ da _issue_ que você abriu para fazer o pedido pede esse
número. Você pode editar a _issue_ para adicioná-lo. É importante fazer essa
atualização para ficar mais fácil de associar o seu _pull request_ com a sua
_issue_.

Com o _pull request_ devidamente criado, você completou todas as etapas! Assim
que o time de infra aceitá-lo e mergeá-lo, o site estará no ar
e você poderá utilizá-lo para divulgar o seu capítulo.


# Atualizações
Caso você precise editar o site no futuro, será preciso atualizar o submódulo
para que ele utilize o último commit do repositório do site. Para isso, você
precisará acessar o seu fork do repositório
[chapter-websites](https://github.com/pyladies/chapter-websites) e fazer um
pull dentro da pasta do seu submódulo. Isso irá atualizá-lo para o último commit
realizado no repositório do site. Após isso, será necessário fazer um commit
para salvar as alterações e abrir um _pull request_ para atualizar o repositório
[chapter-websites](https://github.com/pyladies/chapter-websites).

Os comandos para isso são:

```
$ cd chapter-websites/<NOME_DO_CAPÍTULO>
$ git checkout <BRANCH_DE_PRODUÇÃO>
$ git pull
$ cd ..
$ git add <NOME_DO_CAPÍTULO>
$ git commit -m "Update submodule for chapter <NOME_DO_CAPÍTULO>"
$ git push <BRANCH_DE_PRODUÇÃO>

```

Para abrir o _pull request_ de atualização, siga os mesmos passos do _pull
request_ de criação. O template será o mesmo, mas lembre-se de responder
Sim à pergunta "esse _pull requst_ está atualizando um site já existente?".
Novamente, basta aguardar a aceitação do _pull request_ para que as atualizações
entrem em produção.

