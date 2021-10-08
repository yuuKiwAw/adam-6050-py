FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y gnupg2
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee /etc/apt/sources.list.d/mono-xamarin.list
RUN apt-get update
RUN apt-get install -y mono-complete
RUN apt-get install -y clang libglib2.0-dev
RUN apt-get install -y gcc g++
RUN apt-get install -y git

RUN apt-get install -y python3.8.5
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple wheel
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycparser
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pythonnet
