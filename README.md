# streamlit_dataentry

## Development Env
1. in terminal:
    1. `pip install pipx`
    1. `pipx install poetry`
    1. optional, `poetry env use python3.10` to default to 3.10
    1. `poetry install`
    1. `poetry shell`
    1. `source dev_setup.sh`
    1. `jupyter notebook` to start running
1. misc commands
    1. `poetry env remove list` to find current env
    1. `poetry env remove 3.10` to remove 3.10
    1. `poetry add <packagename>` , then `source dev_setup.sh` to add package
