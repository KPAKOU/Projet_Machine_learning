import subprocess

def run_backend():
    subprocess.Popen(["uvicorn", "appli.tpi:app", "--reload"])

def run_frontend():
    subprocess.Popen(["streamlit", "run", "appli/global.py"])

if __name__ == "__main__":
    run_backend()
    run_frontend()
