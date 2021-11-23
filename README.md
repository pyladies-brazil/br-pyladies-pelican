Site PyLadies Brasil
====================
[![Build Status](https://app.codeship.com/projects/bca2dab0-d874-0134-15a2-326e4d300ce2/status?branch=master)](https://app.codeship.com/projects/bca2dab0-d874-0134-15a2-326e4d300ce2/status?branch=master)

Contribuindo
------------

Para contribuir com o projeto veja o guia de [Contribuição](https://github.com/pyladies-brazil/br-pyladies-pelican/blob/master/CONTRIBUTING.md). Lá você encontrará instruções detalhadas de como fazer a sua contribuição.

Instalando e Rodando
--------------------
* [Requisitos Mínimos](#requisitos-minimos)
* [Instalação no Linux](#instalação-no-linux)
  - [Usando ambiente virtual](#usando-ambiente-virtual)
  - [Usando docker-compose](#usando-docker-compose)
* [Instalação no Windows](#instalação-no-windows)
  - [Usando o docker-compose](#usando-o-docker-compose)

Requisitos Mínimos
-----
* Python 3.6
* [pip](https://pip.pypa.io/en/stable/)

Instalação no Linux
===============

Usando ambiente virtual
----
- Para apenas rodar localmente o site, você precisa do [virtualenv](https://virtualenv.pypa.io/en/stable/)
instalado na sua máquina. Para verificar se ele está instalado, execute o
seguinte comando e observe a saída:

```console
$ virtualenv --version
```
- Se a saída for uma numeração, como `16.1.0`, isso significa que o virtualenv já
está instalado. Caso contrario, para instalar o virtualenv basta fazer:

```console
$ pip install virtualenv
```
- O mesmo procedimento pode ser feito para o git. Verifique se já está instalado,
com o comando:
```console
$ git --version
```

- Se a saída for algo como `git version 2.17.1`, significa que o git já está
instalado. Caso contrário, para instalar o git basta fazer:
``` console
$ sudo apt install git  # para ubuntu
```

> **Observação**: Esse comando funciona apenas em sistemas operacionais que utilizam o
`apt` gerenciador de pacotes. Caso não seja o seu caso, [verifique como instalar](https://git-scm.com/download/linux) o git no seu sistema.

- Assumindo que seu git e virtualenv já estão configurados, faça o clone do repositório

```console
$ git clone https://github.com/pyladies-brazil/br-pyladies-pelican.git
```
- Após conclusão do clone, acesse o diretório recém-criado

```console
$ cd br-pyladies-pelican
```
- Rode o comando para criação de ambiente virtual e instalação das dependências

```console
$ virtualenv .venv 	# cria ambiente virtual
$ source .venv/bin/activate	# ativa o ambiente
$ pip install -r requirements.txt	# instala as dependências

```

- Rode o projeto

```console
$ make up
```

Abra o browser em [localhost:8000](http://localhost:8000) para ver o conteúdo gerado.

**Observação**: Se sua porta 8000 já estiver em uso, você pode especificar uma porta diferente ao
usar o parâmetro `PORT`. Por exemplo:

```console
$ make up PORT=8001
```

E então acessar [localhost:8001](http://localhost:8001). Atenção! Algumas [portas são reservadas](https://pt.wikipedia.org/wiki/Lista_de_portas_dos_protocolos_TCP_e_UDP).

Para desativar o ambiente virtual

```console
$ deactivate
```
Para mais informações a respeito do `Makefile` e suas opções, digite

```console
$ make help
```

Usando docker-compose
--------------------------

Instale [o docker no seu computador](https://docs.docker.com/install/) em seguida execute os passos abaixo:

``` console
$ git clone git@github.com:pyladies-brazil/br-pyladies-pelican.git
$ cd br-pyladies-pelican
$ docker-compose up
```


Instalação no Windows
===============

Usando o docker-compose
--------------------------
- [Opcional] Instale o [Visual Studio Code](https://code.visualstudio.com/) para fazer códigos legais;
- [Opcional mas fortemente indicado] Instale o [Github Desktop](https://desktop.github.com/) para uma interface legal também;
- Python 3.8 está disponível na loja do Windows e você deve instalar também. Só procurar e clicar em obter que está tudo certo;
- Abra o Windows Powershell como administrador e faça a instalação do [chocolatey](https://chocolatey.org/install). Com ele poderemos instalar o comando make que será utilizado junto ao Docker;
- Com o comando *choco* sendo reconhecido no Windows, [instale o make](https://chocolatey.org/packages/make) com `choco install make`;
- Por último, faça a instalação do [Docker](https://docs.docker.com/docker-for-windows/install/), certifique-se que os requisitos mínimos estão sendo cumpridos. Para o Windows 10 Home, é recomendado que atualize o sistema antes da instalação (Configurações → Atualização e Segurança → Windows Update)
    - Atente-se se o WSL2 está rodando na sua máquina. Se ainda for o WSL, [atualize](https://docs.microsoft.com/pt-br/windows/wsl/wsl2-kernel).
- Faça fork do [repositório](https://github.com/pyladies-brazil/br-pyladies-pelican);
- Reinicie o computador para garantir que todas as mudanças foram efetuadas e salvas;
- Agora você tem duas formas de rodar o projeto seguindo o:
    - Comando `make up`
    - Comando `docker-compose up`
- Utilizando o terminal:
    ``` console
    $ git clone git@github.com:pyladies-brazil/br-pyladies-pelican.git
    $ cd br-pyladies-pelican
    $ docker-compose up
    ```
    ou

    ``` console
    $ git clone git@github.com:pyladies-brazil/br-pyladies-pelican.git
    $ cd br-pyladies-pelican
    $ make up
    ```
Nota:
-----------

* [Suporte no caso do Windows Home e Single Language](https://github.com/pyladies-brazil/br-pyladies-pelican/issues/430) 


Links Úteis
-----------

* [Criar um grupo PyLadies](https://brazilpyladies.gitbooks.io/handbook/content/)
* [Documentação Docker](https://docs.docker.com/)
* [Documentação git](https://git-scm.com/doc)
* [Documentação Pelican](http://docs.getpelican.com/en/3.6.3/)
* [pyenv](https://github.com/yyuu/pyenv)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Dúvidas?
---------

Qualquer dúvida ou problema durante a instalação, abra uma [issue](https://github.com/pyladies-brazil/br-pyladies-pelican/issues/new/choose)!

Esse repositório é mantido com :heart: pelo @pyladies-brazil/tech-team
