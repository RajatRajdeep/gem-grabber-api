# Gem Grabber API

## Project Structure

- **app/:** This directory is FastAPI application directory.
  - **app/main.py:** This file is the generic entry point and the root of our FastAPI application.
  - **app/crud.py:** This file contains functions which interacts with database to perform the create, read, update, and delete operations.
  - **app/models.py:** This file contains database models.
  - **app/schemas.py:** This file contains Pydantic models for data validation.
- **.gitignore:** .gitignore file specifies intentionally untracked files that Git should ignore. Files already tracked by Git are not affected.
- **requirements.txt:** This file stores information about all the libraries, modules, and packages that are used to build the project.

## Project Setup/ Installation Guide

- Clone the repository using the below git clone command.

```
    git clone git@github.com:RajatRajdeep/gem-grabber-api.git
```

- Install [python 3.10.4](https://www.python.org/downloads/release/python-3104) which comes with pip3.
- Change your current directory to gem-grabber-api/.
- Install Virtualenv and create a virtual environment using pip3. Follow the below commands for macOS:

```
pip3 install virtualenv
virtualenv <env_name>
```

- Activate the virtual environment and install dependencies. Follow the below commands for macOS:

```
source <env_name>/bin/activate
pip3 install -r requirements.txt
```

- The setup is complete! Run the FastAPI application using the below command.

```
uvicorn app.main:app
```

## Built With

- [FastAPI 0.95.0](https://fastapi.tiangolo.com)
- [Python 3.10.4](https://www.python.org/downloads/)

## Authors

- [**Rajat Rajdeep**](https://rajatrajdeep.in)
