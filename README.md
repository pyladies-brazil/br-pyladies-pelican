Site Pyladies Brasil
====================
[![Build Status](https://app.codeship.com/projects/bca2dab0-d874-0134-15a2-326e4d300ce2/status?branch=master)](https://app.codeship.com/projects/bca2dab0-d874-0134-15a2-326e4d300ce2/status?branch=master)

Contribuindo
------------

Para contribuir com o projeto veja o guia de [Contribuição](https://github.com/pyladies-brazil/br-pyladies-pelican/blob/master/CONTRIBUTING.md). Lá você encontrará instruções detalhadas de como fazer a sua contribuição.

Instalando e Rodando
--------------------
* [Requisitos Mínimos](#requisitos)
* [Instalação no Linux](#linux)
  - [Usando ambiente virtual](#linux-venv)
  - [Usando docker-compose](#linux-docker)
* [Instalação Windows](#windows)
  - [Usando o docker-compose](#windows-docker)

Requisitos Mínimos
-----
* Python 3.6
* [pip](https://pip.pypa.io/en/stable/)

Instalação no Windows
===============

Usando ambiente virtual
-----------

**ATENÇÃO**: adiantamos que essa talvez não seja a melhor opção e pode causar
alguns erros.

- Baixe e instale o [git](https://git-scm.com/download/win);
  * Verifique a instalação no Powershell ou cmd por meio do comando `git --version`;
- Verifique a instalação do `virtualenv` por meio do comando `virtualenv --version`;
  * Se o virtualenv não estiver instalado, rode o comando `pip install virtualenv`;
- Uma vez instalado o virtualenv, vá até a pasta do projeto
```console
virtualenv .venv 		# cria o ambiente virtual
.\venv\Scripts\activate 	# ativa o ambiente virtual
```
- Quando o ambiente virtual estiver funcionando, um `(.venv)` aparecerá no início
da sua linha de comando.
- Após, instale as dependências do projeto usando `pip install -r requirements.txt`;
- Abra mais um terminal e repita o processo de **ativação** do ambiente virtual na
dentro da pasta do projeto;
- No primeiro terminal, vá até a pasta `content` e suba um servidor
```console
.\venv\Scrips\activate		# ativa o ambiente
cd contents
python -m http.server
```
- Deixe esse terminal aberto
- No outro terminal, digite `pelican -r content` e deixe o terminal aberto
- No seu navegador, acesse a URL `https://localhost:8000` e veja o site rodando!

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

Links Úteis
-----------

* [Criar um grupo PyLadies](https://brazilpyladies.gitbooks.io/handbook/content/)
* [Documentação git](https://git-scm.com/doc)
* [Documentação Pelican](http://docs.getpelican.com/en/3.6.3/)
* [pyenv](https://github.com/yyuu/pyenv)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Esse repositório é mantido com :heart: pelo @pyladies-brazil/tech-team
