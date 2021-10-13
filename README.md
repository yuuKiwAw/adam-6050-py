# adam-6050-py
- python 3.8.3
- pythonnet 2.5.2
- fastapi 0.63.0
- uvicorn 0.13.4
- toml 0.10.1

# TO-DO
- 2021.10.09 add webserver
- 2021.10.11 add toml config file

# Docker
- sudo docker import - adam_server_211031 < adam_server_211031.tar
- sudo docker run -it -p 8000:8000 --name adam_server_2  adam_server_211031:latest /bin/bash
- ./autorun.sh
- exit
- sudo docker start ca7fbf73b9a0
- sudo docker exec -it ca7fbf73b9a0 /bin/bash
- ./autorun.sh
