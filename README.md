# SOC

Initial setup:
--------------
python -m venv venv
python -m pip install --upgrade pip 
pip install fastapi uvicorn pydantic
pip list

To activate env: venv\Scripts\activate
deactivate 

To run app: uvicorn app.main:app --reload
