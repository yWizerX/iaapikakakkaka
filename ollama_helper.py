import ollama

def gerar_resposta(user_prompt: str, system_prompt: str = "Você é um assistente prestativo.", model: str = "qwen2.5-coder:1.5b") -> str:
    try:
        ollama.pull(model=model)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        response = ollama.chat(model=model, messages=messages)
        return response['message']['content']
    except Exception as e:
        return f"Erro ao processar: {str(e)}"
