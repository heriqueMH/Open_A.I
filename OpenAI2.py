import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = ("")

# Configuração do módulo de síntese de voz
engine = pyttsx3.init()

def obter_resposta_do_modelo(dialogo):
    if not dialogo:
        # Caso o diálogo esteja vazio, forneça uma pergunta inicial ou tratamento especial
        return "Olá! Como posso te ajudar?"
    
    resposta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=dialogo,
        max_tokens=400, 
        temperature=0.7,
        n=1,
        stop=None,
    )
    return resposta.choices[0].text.strip()

# Função para reconhecer fala e retornar o texto e status
def reconhecer_fala():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando pergunta...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você perguntou:", texto)
        if texto.lower() == "sair do programa" or texto.lower() == "Encerrar programa": 
            print("Encerrando o programa...")
            return texto, False
        return texto, True
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
        return "", True
    except sr.RequestError as e:
        print("Erro no serviço de reconhecimento de fala: {0}".format(e))
        return "", True

# Diálogo inicial
dialogo = "Start"

while True:
    # Solicita entrada do usuário por voz
    mensagem, status = reconhecer_fala()

    if not status:
        break

    dialogo += "\nUsuário: " + mensagem

    # Obtém a resposta do modelo
    resposta = obter_resposta_do_modelo(dialogo)

    dialogo += resposta

    engine.say(resposta)
    engine.runAndWait()
    
    print("AI:", resposta)
