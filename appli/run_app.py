import subprocess

def run_backend():
    subprocess.Popen(["uvicorn", "appli.tpi:app", "--reload", "--port", "8001"])

def run_frontend():
    subprocess.Popen(["streamlit", "run", "appli/global.py", "--server.port", "8502"])

if __name__ == "__main__":
    run_backend()
    run_frontend()