import openai

# Configuração da chave de API da OpenAI
openai.api_key = ''

# Função para enviar uma solicitação à API e obter uma resposta
def obter_resposta_do_modelo(dialogo):
    resposta = openai.Completion.create(
        engine='text-davinci-003',  # Especifica o modelo de linguagem a ser usado
        prompt=dialogo,
        max_tokens=50,  # Define o limite máximo de tokens na resposta
        temperature=0.7,  # Controla a aleatoriedade da resposta gerada
        n=1,  # Define quantas respostas gerar
        stop=None,  # Define um critério de parada personalizado (opcional)
        include_prompt=False  # Exclui o prompt da resposta gerada
    )
    return resposta.choices[0].text.strip()

# Diálogo inicial
dialogo = "Usuário: Olá!\nAI: Oi, como posso te ajudar?"

while True:
    # Solicita entrada do usuário
    mensagem = input("Usuário: ")

    # Adiciona a mensagem do usuário ao diálogo
    dialogo += "\nUsuário: " + mensagem

    # Obtém a resposta do modelo
    resposta = obter_resposta_do_modelo(dialogo)

    # Adiciona a resposta do modelo ao diálogo
    dialogo += "\nAI: " + resposta

    # Exibe a resposta do modelo
    print("AI:", resposta)
