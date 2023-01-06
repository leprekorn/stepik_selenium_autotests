# python_edu

Answers for 4 Chapter ("Page Object) on course Selenium Web Driver on Stepik.org: https://stepik.org/course/575

(Selenium web driver should be installed and added to PATH)
Upgrade pip:
python -m pip install --upgrade pip

Create new virtual environment:
python -m venv ..\venv
cd  ..\venv\Scripts\
.\Activate.ps1

Install requirements:
pip install --upgrade pip
pip install -r requirements.txt

Examples how to run tests:
pytest -v --tb=line --language=en test_main_page.py
pytest -s -v --tb=line test_product_page.py
