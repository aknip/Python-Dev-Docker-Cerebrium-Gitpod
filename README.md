# Cerebrium Simple Service

## Run in Gitpod
https://gitpod.io/#https://github.com/aknip/Python-Dev-Docker-Cerebrium-Gitpod


## Local dev
This script setups an virtual environment form scratch using uv. Active venv is deactived before, existing venv is deleted. 
- Install dependencies and activate
    - `source setup.sh`	
- Deactivate environment
	- `deactivate`

## Docker Compose

docker-compose up --build

Folder src can be edited 

### Execute commands inside Docker
- Use `run` for a single one-off execution and starting a container.
- Use `exec` for executing a command in a running container.
Examples:
- docker-compose run myapp bash
- docker-compose exec myapp bash
- docker-compose run myapp python3 --version
- docker-compose run myapp python src/marimoapp.py


## Docker
docker build -t my_app .  
docker run -p 8080:8080 -it my_app













## Develop local: Virtual environment using uv
- Install: curl -LsSf https://astral.sh/uv/install.sh | sh
- Install dependencies and switch to Python >=3.12
	- `uv sync`
- Activate environment
	- `source .venv/bin/activate`


## Run
cerebrium login
cerebrium deploy


Go to https://dashboard.cerebrium.ai, 
Copy Curl example and edit URL (including function name) and bearer token

Example:
curl --location --request POST 'https://api.cortex...../hello-world/run' \
--header 'Authorization: Bearer ....' \
--header 'Content-Type: application/json' \
--data '{"param_1": "hello", "param_2": "world" }'


## Source
https://docs.cerebrium.ai/cerebrium/getting-started/introduction


