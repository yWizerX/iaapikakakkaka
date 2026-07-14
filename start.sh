#!/usr/bin/env bash

# 1. Baixa o binário do Ollama caso ele não exista
if [ ! -f "./ollama" ]; then
    echo "Baixando o Ollama..."
    curl -L https://ollama.com -o ollama.tgz
    tar -xzf ollama.tgz ollama
    rm ollama.tgz
fi

# 2. Inicia o servidor do Ollama em segundo plano
echo "Iniciando o servidor Ollama em segundo plano..."
./ollama serve &

# 3. Aguarda alguns segundos até o servidor estar pronto
sleep 5

# 4. Inicia o Gunicorn com o Django
echo "Iniciando o Gunicorn..."
gunicorn wsgi
