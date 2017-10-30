Menu
====
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



Contribuindo
============

1. Fork o projeto
2. Crie uma branch para a feature em que trabalhará: `git checkout -b my-new-feature`
3. Faça commit das suas alterações: `git commit -m 'Add some feature'`
4. Faça push desses commits para sua branch: `git push origin my-new-feature`
5. Envie um pull request para o nosso repositório

Obs.: Nós usamos inglês como linguagem padrão dos commits (:


Preparando o ambiente local
--------------------------
- Antes de mais nada, verifique se você tem o **Python 2.7** instalado na sua máquina.

(Atenção: se você estiver usando um **MacOS X** para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/))

Para criar uma `virtualenv` e instalar os pacotes necessários para rodar o projeto, execute o seguinte comando:

    make install

Pronto :star2: Agora seu ambiente local está preparado para rodar :tada:!

(Obs: se você pretende usar o ambiente virtual instalado via *make*, ele se
encontra em `.venv/`.)

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


Adicionar Ladies
----------------

Para adicionar uma nova lady, edite o arquivo `data/ladies.yml` . Ele possui o seguinte formato:


```yaml
- name: NOME DA LADY
  github: github da lady (apenas o nome de usuário)
  twitter: twitter da lady (apenas o nome de usuário)
  facebook: facebook da lady (apenas o nome de usuário)
  image: PATH DA IMAGEM DA LADY
```

O `PATH DA IMAGEM DA LADY` pode ser:

#### Path relativo

O endereço da foto em nosso projeto.

*Exemplo:* `/images/ladies/nomedalady.jpg`

Nesse caso, a nova imagem deverá ser inserida no diretório `content/images/ladies`

**Atenção:** A imagem precisa ser `100px por 100px`.

#### Path absoluto

Uma url completa da foto em outro site.

*Exemplo:* `https://gravatar.com/avatar/07ac697bcff40050a82cb4503de9eb69`


Adicionar nova Localização
--------------------------

Para adicionar uma nova localização de grupo de pyladies, edite o arquivo `data/locations.yml`. O formato é o seguinte:


```yaml
- city: CIDADE - ESTADO
  image: PATH IMAGEM LOCAL (Padrão: /images/locais/location.png)
  twitter: Endereço twitter local (URL Completa)
  email: EMAIL DA ORG
  url: SITE DA ORG
```

**Atenção:** A imagem precisa ser `100px por 100px`.


Adicionar vídeos
----------------

Para adicionar um novo vídeo, edite o arquivo `data/videos.yml` com o nome do vídeo e seu link. Ele possui o seguinte formato:

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

Nós temos um ambiente de teste, também conhecido como staging \o/
Todo commit feito no branch `develop` deste repositório irá disparar a atualização do ambiente de staging automaticamente.
O deploy leva cerca de 3 minutos e acontece através da ferramenta de integração contínua [Codeship](https://app.codeship.com/projects/203211).

__** Atenção: Sempre confira se as alterações no ambiente de staging se comportam como o esperado antes de atualizar o ambiente de produção **__

Para verificar se tudo funciona conforme o esperado, acesse [o ambiente de teste](http://staging-brasil-pyladies.herokuapp.com/). Depois de testar manualmente as suas alterações, basta informar a alguma das pessoas abaixo para que as alterações sejam aplicadas no ambiente de produção, também conhecido como [nosso site](http://brasil.pyladies.com/) \o//

- [@aninhalacerda](https://github.com/aninhalacerda)
- [@darlenedms](https://github.com/darlenedms)
- [@I-am-Gabi](https://github.com/I-am-Gabi)
- [@lidymonteirowm](https://github.com/lidymonteirowm)
- [@pgrangeiro](https://github.com/pgrangeiro)
- [@roselmamendes](https://github.com/roselmamendes)
- [@taniaa](https://github.com/taniaa)
