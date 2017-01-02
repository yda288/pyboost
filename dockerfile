FROM continuumio/anaconda3

RUN set -o xtrace \
  && : ===  DOWNLOAD SLIM SOURCE === \
    && mkdir -p /usr/src/boost \
    && cd /usr/src/boost \
    && git clone https://github.com/boostorg/boost.git . \
    && git submodule update --init \
      libs/array \
      libs/assert \
      libs/bind \
      libs/concept_check \
      libs/config \
      libs/conversion \
      libs/core \
      libs/detail \
      libs/filesystem \
      libs/foreach \
      libs/function \
      libs/functional \
      libs/graph \
      libs/integer \
      libs/iterator \
      libs/lexical_cast \
      libs/math \
      libs/move \
      libs/mpl \
      libs/multi_index \
      libs/numeric/conversion \
      libs/optional \
      libs/parameter \
      libs/predef \
      libs/preprocessor \
      libs/property_map \
      libs/python \
      libs/range \
      libs/serialization \
      libs/smart_ptr \
      libs/static_assert \
      libs/throw_exception \
      libs/tuple \
      libs/type_traits \
      libs/type_index \
      libs/typeof \
      libs/unordered \
      libs/utility \
      libs/wave \
      libs/container \
      tools/build \
      tools/inspect

RUN apt-get install build-essential -y
#RUN apt-get install gcc-4.9 -y

RUN cat > /root/user-config.jam
RUN echo "# Configure specific Python version." >> /root/user-config.jam
RUN echo "using python : 3.5" >> /root/user-config.jam
RUN echo ": /opt/conda/bin" >> /root/user-config.jam
RUN echo ": /opt/conda/include/python3.5m #directory that contains pyconfig.h" >> /root/user-config.jam
RUN echo ": /opt/conda/lib   #directory that contains python27.lib" >> /root/user-config.jam
RUN echo ": <toolset>gcc ;" >> /root/user-config.jam


WORKDIR /usr/src/boost

RUN ./bootstrap.sh --with-libraries=python
RUN ./b2 headers
RUN ./b2 cxxflags='-fPIC'

WORKDIR /usr/src/boost

##BELOW STEPS YET TO BE AUTOMATED

#COPY FILE
#sudo docker cp %SOURCE_LOCATION_ON_HOST%/main.cpp %RUNNING_CONTAINER_NAME%:/usr/src/%SOURCE_LOCATION_ON_CONTAINER%

##RUN g++ -Wall -fexceptions -O2 -fPIC -std=c++11 -L/usr/src/boost -L/opt/conda/lib/python3.5m -I/usr/src/boost -I/opt/conda/include/python3.5m  -c main.cpp -o main.o

##RUN g++ -shared -L/usr/src/boost -L/opt/conda/lib/python3.5 -L/opt/conda/lib/python3.5m -L/usr/src/boost -L/opt/conda/lib/python3.5 -L/opt/conda/include/python3.5m main.o  -o BoostTest.so -s  /usr/src/boost/stage/lib/libboost_python3.so,/usr/src/boost/stage/lib/libboost_numpy3.so

#SET for shared object import
#export LD_LIBRARY_PATH=$(pwd)