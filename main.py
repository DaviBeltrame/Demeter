from voice.recognition import ouvir_usuario
from voice.speech import falar

def main():
    falar("Sistema Deméter iniciado. Como posso ajudar?")
    while True:
        comando = ouvir_usuario()
        if comando:
            falar(f"Você disse: {comando}")
            # Aqui você pode adicionar lógica para processar o comando
            if "sair" in comando:
                falar("Encerramento do sistema Deméter.")
                break

            elif "status" in comando:
                falar("Todos os sistemas estão operando normalmente.")
          
            else:
                falar("Desculpe, não reconheço esse comando ainda, tente outra coisa.")

if __name__ == "__main__":
    main()