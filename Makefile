SRCDIR=./src
PROG=lisp
PYTHON=$(shell which python)

$(PROG): $(SRCDIR)/*.py $(SRCDIR)/*/*.py
	@python -m zipapp $(SRCDIR) -o $(PROG) -p "$(PYTHON)"

.PHONY: clean
clean:
	@rm $(PROG) -f
