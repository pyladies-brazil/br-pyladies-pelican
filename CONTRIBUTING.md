Contribuindo
============

1. Fork o projeto
2. Crie uma branch para a feature em que trabalhará: `git checkout -b my-new-feature`
3. Faça commit das suas alterações: `git commit -m 'Add some feature'`
4. Faça push desses commits para sua branch: `git push origin my-new-feature`
5. Envie um pull request para o nosso repositório

Obs.: Nós usamos inglês como linguagem padrão dos commits (:


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


Atualizar Github Pages
----------------------

Após realizar todos os testes locais, para fazer o upload do novo conteúdo no github pages, rode o comando:

	make github

Você poderá ir na página oficial e já observar suas alterações.
