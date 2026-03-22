## FastAPI Playground 

The fastapi playground repo is developed for testing the fastapi for the login system using the auth 0 and integrate in the frontend when users login 


### For the FAST Api 

```bash

fastapi dev

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




### Links -- 

- https://fastapi.tiangolo.com/
- https://auth0.com/docs/quickstart/backend/fastapi
- https://docs.astral.sh/uv/getting-started/installation/#installation-methods
- https://docs.astral.sh/uv/guides/projects/#managing-dependencies