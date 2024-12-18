# define variables

STREAMLIT_APP = global.py
FASTAPI_APP = tpi

.PHONY: frontend backend run_app

frontend:
	streamlit run $(STREAMLIT_APP)

backend:
	uvicorn $(FASTAPI_APP):app --reload &

run_app: backend frontend 