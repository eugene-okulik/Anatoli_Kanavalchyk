python -m venv api_venv
source api_venv/bin/activate
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results

