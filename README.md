Site Pyladies Brasil
====================


Instalando e Rodando
--------------------

- Assumindo que seu git e virtualenv já estão configurados, faça o clone do repositório

		$ git clone git@github.com:pyladies-brazil/br-pyladies-pelican.git

- Crie uma virtualenv (pode chamar `pyladies`). Se você não sabe como criar uma virtualenv, [leia isso](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

(Atenção: se você estiver usando um **MacOS X** para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/))

- Ative seu virtualenv e instale os pacotes necessários para rodar o projeto:

		$ pip install -r requirements.txt

- Rode o projeto

		$ make up

Abra o browser em [localhost:8000](http://localhost:8000) para ver o conteúdo gerado

Contribuindo
------------

Para contribuir com o projeto veja o guia de [Contribuição](https://github.com/pyladies-brazil/br-pyladies-pelican/blob/master/CONTRIBUTING.md)

Links Úteis
-----------

* Documentação Pelican - http://docs.getpelican.com/en/3.6.3/
* Virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
* Pyenv - https://github.com/yyuu/pyenv
