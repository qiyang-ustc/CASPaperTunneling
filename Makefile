all:

install:
	mkdir -p ~/bin
	ln -s $(PWD)/caspt $(HOME)/bin/caspt
	chmod +x ~/bin/caspt

uninstall:
	rm -f ~/bin/caspt