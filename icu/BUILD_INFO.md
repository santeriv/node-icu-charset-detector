19.4.2014
---------
Downloaded
	wget http://download.icu-project.org/files/icu4c/53.1/icu4c-53_1-src.tgz
	tar xzvf icu4c-53_1-src.tgz

ICU static library configured with following settings

	export CFLAGS=-O
        export CXXFLAGS=-O 
        ./runConfigureICU Linux --enable-static --disable-shared

built with

	make install DESTDIR=icu
