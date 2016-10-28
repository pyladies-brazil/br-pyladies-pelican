VIRTUALENV = virtualenv
VENV := $(shell echo $${VIRTUAL_ENV-.venv})

PY=$(VENV)/bin/python
PELICAN?=$(VENV)/bin/pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

GITHUB_PAGES_BRANCH=gh-pages

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

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make up                             generate the web site and serve    '
	@echo '   make install                        install python dependencies        '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make newpost NAME="POST NAME"       create new post with input name    '
	@echo '   make newpage NAME="PAGE NAME"       create new ppage with input name   '
	@echo '   make clean                          remove the generated files         '
	@echo '   make dist-clean                     remove gen. files and dependencies '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '   make virtualenv                     create default virtual environment '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

up: html serve

install: virtualenv
	$(VENV)/bin/pip install -U pip
	$(VENV)/bin/pip install -U -r requirements.txt

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

distclean: clean
	rm -rf .venv/

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	@echo "Starting test server is running on http://0.0.0.0:$(PORT)"
	$(at_output) && $(BASEDIR)/$(PY) -m pelican.server $(PORT)
else
	@echo "Starting Test server is running on http://0.0.0.0:8000"
	$(at_output) && $(BASEDIR)/$(PY) -m pelican.server
endif

serve-global:
ifdef SERVER
	@echo "Starting server is running on :$(SERVER):80"
	$(at_output) && $(BASEDIR)/$(PY) -m pelican.server 80 $(SERVER)
else
	@echo "Starting server is running on :http://0.0.0.0:80"
	$(at_output) && $(BASEDIR)/$(PY) -m pelican.server 80 0.0.0.0
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	$(BASEDIR)/develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

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
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newpost NAME='"'"'Post Name'"'"
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
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newpage NAME='"'"'Page Name'"'"
endif

virtualenv:
	$(VIRTUALENV) $(VENV)


.PHONY: up html help clean regenerate serve serve-global devserver publish github newpost newpage
