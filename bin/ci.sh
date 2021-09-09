[ -d venv ] || python -m venv
source  venv/Scripts/activate
pip install -r requirements.txt
pytest --junitxml=junit.xml --alluredir=allure_results service/test