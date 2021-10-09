FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y gnupg ca-certificates
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | tee /etc/apt/sources.list.d/mono-official-stable.list
RUN apt update
RUN apt-get install -y mono-devel
RUN apt-get install -y mono-complete
RUN apt-get install -y clang libglib2.0-dev
RUN apt-get install -y gcc g++
RUN apt-get install -y git

RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple uvicorn
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple fastapi
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple wheel
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycparser
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pythonnet