VENV := $(shell echo ${VIRTUAL_ENV})

PY=$(VENV)/bin/python
PELICAN?=$(VENV)/bin/pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py

PAGESDIR=$(INPUTDIR)/pages
DATE := $(shell date +'%Y-%m-%d %H:%M:%S')
SLUG := $(shell echo '${NAME}' | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
EXT ?= md
EDITOR ?= vim

at_output=mkdir -p $(OUTPUTDIR) && cd $(OUTPUTDIR)

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile para um website usando Pelican                                   	'
	@echo '                                                                          	'
	@echo 'Uso:	                                                                 	'
	@echo '   make up                             gera o site e o serve na porta     	'
	@echo '   make html                           (re)gera o site		         	'
	@echo '   make newpost NAME="POST NAME"       cria um novo post com o nome de entrada   '
	@echo '   make newpage NAME="PAGE NAME"       cria nova página com o nome de entrada	'
	@echo '   make clean                          remove os arquivos gerados		'
	@echo '   make serve [PORT=8000]              serve o site em http://localhost:8000	'
	@echo '                               		                                        '
	@echo 'Especifique a variável DEBUG=1 para habilitar debugging, ex. make DEBUG=1 up	'
	@echo '                                                                          	'

up: html serve

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	@echo "Starting test server is running on http://0.0.0.0:$(PORT)"
	$(at_output) && $(PY) -m pelican.server $(PORT)
else
	@echo "Starting test server is running on http://0.0.0.0:8000"
	$(at_output) && $(PY) -m pelican.server
endif


newpost:
ifdef NAME
	echo "Title: $(NAME)" >  $(INPUTDIR)/$(SLUG).$(EXT)
	echo "Slug: $(SLUG)" >> $(INPUTDIR)/$(SLUG).$(EXT)
	echo "Date: $(DATE)" >> $(INPUTDIR)/$(SLUG).$(EXT)
	echo "Tags: " >> $(INPUTDIR)/$(SLUG).$(EXT)
	echo ""              >> $(INPUTDIR)/$(SLUG).$(EXT)
	echo ""              >> $(INPUTDIR)/$(SLUG).$(EXT)
	${EDITOR} ${INPUTDIR}/${SLUG}.${EXT}
else
	@echo 'Variável NAME não está definida.'
	@echo 'Faça make newpost NAME='"'"'nome do post'"'"
endif

newpage:
ifdef NAME
	echo "Title: $(NAME)" >  $(PAGESDIR)/$(SLUG).$(EXT)
	echo "Description: " >  $(PAGESDIR)/$(SLUG).$(EXT)
	echo "Slug: $(SLUG)" >> $(PAGESDIR)/$(SLUG).$(EXT)
	echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
	echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
	${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
else
	@echo 'Variável NAME não está definida.'
	@echo 'Faça make newpage NAME='"'"'Nome da página'"'"
endif

.PHONY: up html help clean serve newpost newpage
