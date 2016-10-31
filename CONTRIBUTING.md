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
- Antes de mais nada, verifique se você tem o **Python 2.7** instalado na sua maquina.
- Se você não possui, instale a ferramenta [virtualenv](https://virtualenv.pypa.io/),
  que permite a criação de ambientes virtuais em Python.

(Atenção: se você estiver usando um **MacOS X** para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/))

Crie uma ``virtualenv`` e instale os requisitos de desenvolvimento com o comando:

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

Para adicionar novos eventos, basta editar o arquivo `data/events.yml` . Ele possui o seguinte formato:

```yaml
- url: URL DO SEU EVENTO
  name: NOME DO EVENTO
  date: DATA EVENTO (Formato DD-MM-YYYY)
  local: LOCAL EVENTO
```

Caso o evento seja novo, ele será automaticamente inserido em Novos Eventos. Caso contrário, já ficará na lista de Eventos passados.


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


Atualizando o site
------------------

Nós temos um ambiente de teste, também conhecido como staging \o/
Todo commit feito no branch master deste repositório irá disparar a atualização do ambiente de staging.

__** Atenção: Sempre confira se as alterações no ambiente de staging se comportam como o esperado antes de atualizar o ambiente de produção **__

Este projeto está com deploy automático para o ambiente de staging. Então, para verificar se as suas alterações já estão no ambiente de teste acesse o [Snap-CI](https://snap-ci.com/pyladies-brazil/br-pyladies-pelican/branch/master), que é a ferramenta de integração contínua que utilizamos neste projeto.

![Exemplo](https://cloud.githubusercontent.com/assets/2524981/19616847/6cca90c4-97fd-11e6-988d-6297e18aa247.png)

Depois que o texto da caixinha da penúltima coluna ficar verde, significa que as alterações já estarão disponíveis para teste. Para verificar se tudo funciona conforme o esperado, acesse [o ambiente de teste](http://staging-brasil-pyladies.herokuapp.com/). Depois de testar manualmente as suas alterações, basta informar a alguma das pessoas abaixo para que as alterações sejam aplicadas no ambiente de produção, também conhecido como [nosso site](http://brasil.pyladies.com/) \o//

- [@aninhalacerda](https://github.com/aninhalacerda)
- [@darlenedms](https://github.com/darlenedms)
- [@I-am-Gabi](https://github.com/I-am-Gabi)
- [@lidymonteirowm](https://github.com/lidymonteirowm)
- [@pgrangeiro](https://github.com/pgrangeiro)
- [@roselmamendes](https://github.com/roselmamendes)
- [@taniaa](https://github.com/taniaa)
