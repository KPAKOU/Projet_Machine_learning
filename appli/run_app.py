import subprocess
import socket

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def find_available_port(initial_port):
    port = initial_port
    while is_port_in_use(port):
        port += 1
    return port

def run_backend():
    initial_port = 8001
    port = find_available_port(initial_port)
    print(f"Starting backend on port {port}")
    subprocess.Popen(["uvicorn", "appli.tpi:app", "--reload", "--port", str(port)])

def run_frontend():
    initial_port = 8502
    port = find_available_port(initial_port)
    print(f"Starting frontend on port {port}")
    subprocess.Popen(["streamlit", "run", "appli/global.py", "--server.port", str(port)])

if __name__ == "__main__":
    run_backend()
    run_frontend()
