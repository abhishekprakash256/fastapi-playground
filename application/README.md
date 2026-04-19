## FastAPI Playground 

The fastapi playground repo is developed for testing the fastapi for the login system using the auth 0 and integrate in the frontend when users login 


### For the FAST Api running

```bash

cd fastapi-playground
uvicorn application.main:app --reload   #when using the folder application
uvicorn app:app --reload       #when using the folder name app
```



### Reqs - 

- uv package manager


### UV steps -- 

```bash

uv init
uv venv
uv add [package name]

#to update and lock if package missing
uv lock --upgrade
uv sync

```

### When initilaizing the repo using UV

```bash

git clone <your-repo-url>
cd your-project

curl -Ls https://astral.sh/uv/install.sh | sh

uv venv #make the venv

uv sync #to install all the dependecies

source .venv/bin/activate   # Mac/Linux

uv run main.py

```


## Notes -- 

- .env file should be in the root level
- pyproject.toml and uv.lock should be in root level as well

### End Points -- 

- http://127.0.0.1:8000/api/public


### Links -- 

- https://fastapi.tiangolo.com/
- https://auth0.com/docs/quickstart/backend/fastapi
- https://docs.astral.sh/uv/getting-started/installation/#installation-methods
- https://docs.astral.sh/uv/guides/projects/#managing-dependencies