Site Pyladies Brasil
====================
[![Build Status](https://app.codeship.com/projects/bca2dab0-d874-0134-15a2-326e4d300ce2/status?branch=master)](https://app.codeship.com/projects/bca2dab0-d874-0134-15a2-326e4d300ce2/status?branch=master)

Contribuindo
------------

Para contribuir com o projeto veja o guia de [Contribuição](https://github.com/pyladies-brazil/br-pyladies-pelican/blob/master/CONTRIBUTING.md). Lá você encontrará instruções detalhadas de como fazer a sua contribuição.

Instalando e Rodando
--------------------

- Para apenas rodar localmente o site, você precisa do [virtualenv](https://virtualenv.pypa.io/en/stable/)
instalado na sua máquina. Para verificar se ele está instalado, execute o
seguinte comando e observe a saida:

```console
$ virtualenv --version
```
- Se a saida for uma numeração, como `16.1.0`, isso significa que o virtualenv já
esta instalado. Caso contrario, para instalar o virtualenv basta fazer:

```console
$ pip install virtualenv
```
- O mesmo procedimento pode ser feito para o git. Verifique se já esta instalado,
com o comando:
``` console
$ git --version
```

- Se a saida for algo como `git version 2.17.1`, significa que o git já esta
instalado. Caso contrario, para instalar o git basta fazer:
``` console
$ sudo apt install git
```

> Obs.: Esse comando funciona apenas em sistemas operacionais que utilizam o
apt gerenciador de pacotes. Caso não seja o seu caso, verifique como
instalar o git no seu sistema.

- Assumindo que seu git e virtualenv já estão configurados, faça o clone do repositório

``` console
$ git clone git@github.com:pyladies-brazil/br-pyladies-pelican.git
```
- Após conclusão do clone, acesse o diretório recém-criado

``` console
$ cd br-pyladies-pelican
```
- Rode o comando para criação de ambiente virtual e instalação das dependências

``` console
$ make install
```
> Obs.: Esse comando criará uma virtual env, então rode-o fora de qualquer ambiente virtual.

- Rode o projeto

``` console
$ make up
```

Abra o browser em [localhost:8000](http://localhost:8000) para ver o conteúdo gerado.

Links Úteis
-----------

* Documentação Pelican - http://docs.getpelican.com/en/3.6.3/
* Virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
* Pyenv - https://github.com/yyuu/pyenv
* Criar um grupo PyLadies - https://brazilpyladies.gitbooks.io/handbook/content/
