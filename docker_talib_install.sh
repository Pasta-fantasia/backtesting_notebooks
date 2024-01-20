# https://cloudstrata.io/install-ta-lib-on-ubuntu-server/
# https://stackoverflow.com/questions/72231796/install-talib-on-docker
# arch64-unknown-linux-gnu

wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz

cd ta-lib

arch=` uname -i `
if [ "$arch" == "x86_64" ] ; then
  ./configure
else
  ./configure --build=aarch64-unknown-linux-gnu
fi

make
make install

# rm -fR /talib-src/
