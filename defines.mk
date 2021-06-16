
-include my-defines.mk


#
# Handle multiple Python installs. What python are we using?
#

ifeq ($(PLATFORM), Linux)

SHELL=/usr/bin/bash

else ifeq ($(PLATFORM), Darwin) # MacOS

SHELL=/usr/local/bin/bash

else


endif

PLATFORM=$(shell uname)

# PIP3=$(shell which pip3)
PIP3=pip3
# PYTHON3=$(shell which python3)
PYTHON3=python3

PYTHON ?= $(PYTHON3)
PIP ?= $(PIP3)


ifeq ($(PYTHON),)
$(error Python not found)
endif
ifeq ($(PIP),)
$(error pip not found)
endif


export PLATFORM PYTHON PIP
