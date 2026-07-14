from django.urls import path
from django.http import JsonResponse
from ollama_helper import gerar_resposta

def executar_ia_view(request):
    # Valores padrão caso nenhum parâmetro seja enviado na URL
    prompt_usuario = request.GET.get('user', 'Olá, quem é você?')
    prompt_sistema = request.GET.get('system', 'Você é um assistente prestativo.')
    modelo = request.GET.get('model', 'qwen2.5-coder:1.5b')
    
    # Chama a função que criamos no arquivo ollama_helper.py
    resposta_ia = gerar_resposta(user_prompt=prompt_usuario, system_prompt=prompt_sistema, model=modelo)
    
    return JsonResponse({"resultado": resposta_ia})

urlpatterns = [
    path('', executar_ia_view),
]
