import os
import subprocess
import time
from urllib.request import urlopen
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Configura o caminho do binário do Ollama na pasta do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OLLAMA_PATH = os.path.join(BASE_DIR, "ollama")

# 1. Baixa o binário do Ollama se ele não estiver no servidor do Render
if not os.path.exists(OLLAMA_PATH):
    print("-> Baixando o binário do Ollama...")
    url = "https://ollama.com"
    tar_path = os.path.join(BASE_DIR, "ollama.tgz")
    
    # Faz o download usando utilitários nativos do Python
    with urlopen(url) as response, open(tar_path, 'wb') as out_file:
        out_file.write(response.read())
        
    # Extrai o arquivo tar
    import tarfile
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extract("ollama", path=BASE_DIR)
        
    # Remove o arquivo compactado temporário
    os.remove(tar_path)
    
    # Dá permissão de execução ao binário extraído
    os.chmod(OLLAMA_PATH, 0o755)
    print("-> Ollama instalado com sucesso.")

# 2. Inicia o servidor do Ollama em segundo plano
try:
    print("-> Inicializando o serviço Ollama serve...")
    subprocess.Popen([OLLAMA_PATH, "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)  # Aguarda 5 segundos para o servidor subir completamente
except Exception as e:
    print(f"-> Erro ao iniciar o Ollama: {e}")

# 3. Inicializa a aplicação padrão do Django para o Gunicorn
application = get_wsgi_application()
