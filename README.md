# Cerebrium Simple Service

## Local dev
This setups an virtual environment form scratch using uv. Active venv is deactived before, existing venv is deleted. 
- Install dependencies and activate
    - `source setup.sh`
- Check Python version
	- `python3 --version`	
- Deactivate environment
	- `deactivate`

## Docker

docker-compose up --build

Folder src can be edited 

docker build -t my_app .  
docker run -p 8080:8080 -it my_app


## Run in Gitpod
https://gitpod.io/#https://github.com/aknip/Python-Dev-Docker-Cerebrium-Gitpod









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


