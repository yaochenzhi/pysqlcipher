[[ install

    yum install openssl-devel
    yum install openssl
    yum install tcl
    yum install gcc

    git clone https://github.com/sqlcipher/sqlcipher.git

    ./configure
    ./configure --enable-tempstore=yes CFLAGS="-DSQLITE_HAS_CODEC" LDFLAGS="-lcrypto"
    make
    make install

    python -m pip install pysqlcipher
    python3 -m pip install pysqlcipher3

        [ manually
        
            yum install python-devel
            git clone https://github.com/leapcode/pysqlcipher
            python setup.py build
            python setup.py install

            yum install python36-devel
            git clone https://github.com/rigglemania/pysqlcipher3.git
            python36 setup.py build
            python36 setup.py install
        ]
]]