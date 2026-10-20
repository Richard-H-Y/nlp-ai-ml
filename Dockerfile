FROM python:3.12-slim
WORKDIR /code
COPY . .
RUN pip install fastapi uvicorn scikit-learn pydantic joblib
RUN python app/train.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]