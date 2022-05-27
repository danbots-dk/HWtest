# install the dw hw package on danwand

PY_LIB="/usr/local/danwand/lib"

make:
	@echo "Install the sw package on the danwand\n"
	@echo "make install \tinstall all in /user/local/danwand/lib\n"
	@echo "make battery \tinstall the battery module"


/usr/local/danwand/lib:
	mkdir -p $(PY_LIB)

battery:	/usr/local/danwand/lib
	cp -r battery $(PY_LIB)

py_requirements:
	@echo "Installing Python requirements"
	pip install -r requirements.txt

install: py_requirements battery
	@echo "All hw lib installed"
