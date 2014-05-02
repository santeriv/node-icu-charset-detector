19.4.2014
---------
Downloaded
	wget http://download.icu-project.org/files/icu4c/53.1/icu4c-53_1-src.tgz
	tar xzvf icu4c-53_1-src.tgz

ICU static library configured with following settings

	export CFLAGS=-O
        export CXXFLAGS=-O 
        # apply patch to ./config/mh-linux : https://issues.apache.org/ooo/show_bug.cgi?id=16151#c0
        ./runConfigureICU Linux --enable-static --disable-shared --with-library-bits=64

built with
        make
	copy ./lib/*.a to node-icu-charset-detector/icu/lib
