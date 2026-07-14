import os
import subprocess
import time
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OLLAMA_PATH = os.path.join(BASE_DIR, "ollama")

# Se o Ollama foi baixado no Build, inicia o serviço em segundo plano
if os.path.exists(OLLAMA_PATH):
    print("-> Iniciando o serviço Ollama em segundo plano...")
    subprocess.Popen([OLLAMA_PATH, "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3) # Pequena pausa para garantir a escuta na porta 11434

application = get_wsgi_application()
