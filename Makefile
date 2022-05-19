# install the dw hw package on danwand

PY_LIB="/usr/local/danwand/lib"

make:
	@echo "Install the sw package on the danwand\n"
	@echo "make install \tinstall all in /user/local/danwand/lib\n"
	@echo "make battery \tinstall the battery module


battery:
	cp -r battery $(PY_LIB)

