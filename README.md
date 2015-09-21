Site Pyladies Brasil
====================


Instalando e Rodando
--------------------

- Assumindo que seu git e virtualenv já estão configurados, faça o clone do repositório

		$ git clone https://github.com/pyladies-brazil/br-pyladies-pelican.git

- Crie uma virtualenv (pode chamar `pyladies`). Se você não sabe como criar uma virtualenv, [leia isso](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

(Atenção: se você estiver usando um **MacOS X** para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/))

- Ative seu virtualenv e instale os pacotes necessários para rodar o projeto:

		$ pip install -r requirements.txt

- Rode o projeto

		$ make up

Abra o browser em [localhost:8000](http://localhost:8000) para ver o conteúdo gerado


Criando um novo Post
--------------------

Para criar um novo post, rode o comando:

	make newpost NAME='NOME DO SEU POST'

Ele irá criar um novo arquivo `nome-do-seu-post.md` na pasta `content` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar o post, renderize-o com o comando:

	pelican content

Se tudo deu certo, seu novo post já estará disponível na página.


Criando uma nova Página
--------------------

Para criar uma nova página, rode o comando:

	make newpage NAME='NOME PAGINA'

Ele irá criar um novo arquivo `nome-pagina.md` na pasta `content/pages` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar de editar a página, renderize-a com o comando:

	pelican content

Se tudo deu certo, sua página já estará disponível em `/slug-pagina/`.


Adicionando Eventos
-------------------

Para adicionar novos eventos, basta editar o arquivo `data/events.yml` . Ele possui o seguinte formato:

```yaml
- url: URL DO SEU EVENTO
  name: NOME DO EVENTO
  date: DATA EVENTO (Formato DD-MM-YYYY)
  local: LOCAL EVENTO
```

Caso o evento seja novo, ele será automaticamente inserido em Novos Eventos. Caso contrário, já ficará na lista de Eventos passados.


Adicionando Ladies
------------------

Para adicionar uma nova lady, edite o arquivo `data/ladies.yml` . Ele possui o seguinte formato:


```yaml
- name: NOME DA LADY
  github: github da lady (apenas o nome de usuário)
  twitter: twitter da lady (apenas o nome de usuário)
  facebook: facebook da lady (apenas o nome de usuário)
  image: PATH DA IMAGEM DA LADY (Padrão: /images/ladies/nomedalady.jpg).
```

A nova imagem deverá ser inserida no diretório `content/images/ladies`


Adicionando nova Localização
----------------------------

Para adicionar uma nova localização de grupo de pyladies, edite o arquivo `data/locations.yml`. O formato é o seguinte:


```yaml
- city: CIDADE - ESTADO
  image: PATH IMAGEM LOCAL (Padrão: /images/locais/location.png)
  twitter: Endereço twitter local (URL Completa)
  email: EMAIL DA ORG
  url: SITE DA ORG
```

Atualizando Github Pages
------------------------

Após realizar todos os testes locais, para fazer o upload do novo conteúdo no github pages, rode o comando:

	make github

Você poderá ir na página oficial e já observar suas alterações.


Links Úteis
-----------

* Documentação Pelican - http://docs.getpelican.com/en/3.6.3/
* Virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
