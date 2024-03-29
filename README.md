# oop-py

### Setting up venv and HTTP requests

```
python -m venv ./venv
source venv/bin/activate
pip install requests
pip freeze > requirements.txt
deactivate
```

### FastAPI setup

```
pip install fastapi
pip install uvicorn
pip freeze > requirements.txt
uvicorn main:app --reload
```