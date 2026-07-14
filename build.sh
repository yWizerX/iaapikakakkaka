#!/usr/bin/env bash
# Interrompe o script se houver qualquer erro
set -o errexit

# 1. Instala as dependências do Django e Ollama Python
pip install -r requirements.txt

# 2. Baixa o binário do Ollama se ele não existir na pasta
if [ ! -f "./ollama" ]; then
    echo "-> Baixando o binário do Ollama para ambiente Linux..."
    curl -L https://ollama.com -o ollama.tgz
    tar -xzf ollama.tgz ollama
    rm ollama.tgz
    chmod +x ollama
    echo "-> Ollama preparado com sucesso para a inicialização!"
fi
