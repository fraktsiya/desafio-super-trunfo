import random
import os

# Função para limpar o console (funciona em Windows, Mac e Linux)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Definição da classe Carta
class Carta:
    def __init__(self, nome, ataque, defesa, inteligencia, poder):
        self.nome = nome
        self.atributos = {
            'Ataque': ataque,
            'Defesa': defesa,
            'Inteligência': inteligencia,
            'Poder': poder
        }

    def __str__(self):
        return f"--- {self.nome} ---"

# Criação do baralho com personagens de anime
baralho = [
    Carta("Goku", 100, 90, 70, 100),
    Carta("Vegeta", 95, 85, 80, 98),
    Carta("Naruto", 90, 80, 85, 95),
    Carta("Sasuke", 88, 82, 90, 93),
    Carta("Eren Yeager", 80, 70, 75, 85),
    Carta("Levi Ackerman", 92, 60, 95, 88),
    Carta("Saitama", 100, 100, 50, 100),
    Carta("Luffy", 93, 88, 70, 94),
    Carta("Zoro", 91, 85, 65, 90),
    Carta("All Might", 98, 95, 80, 99),
    Carta("Madara Uchiha", 96, 92, 94, 98),
    Carta("Itachi Uchiha", 85, 80, 98, 92),
    Carta("Go jo Satoru", 99, 97, 96, 100),
    Carta("Sukuna", 99, 94, 97, 100),
    Carta("Light Yagami", 50, 60, 100, 70),
    Carta("L Lawliet", 40, 70, 100, 65),
]

def jogar():
    random.shuffle(baralho)
    metade = len(baralho) // 2
    mao_jogador = baralho[:metade]
    mao_computador = baralho[metade:]

    rodada = 1
    jogador_da_vez = "jogador" # Começa com o jogador

    while mao_jogador and mao_computador:
        limpar_tela()
        print(f"--- RODADA {rodada} ---")
        print(f"Você tem {len(mao_jogador)} cartas. O computador tem {len(mao_computador)} cartas.")
        print("\nSua vez de escolher!" if jogador_da_vez == "jogador" else "\nVez do computador escolher...")
        input("\nPressione Enter para ver sua próxima carta...")

        carta_jogador = mao_jogador[0]
        carta_computador = mao_computador[0]

        limpar_tela()
        print("Sua carta é:")
        print(carta_jogador)
        for i, (atr, val) in enumerate(carta_jogador.atributos.items(), 1):
            print(f"{i}. {atr}: {val}")

        # Lógica da escolha do atributo
        if jogador_da_vez == "jogador":
            escolha = ""
            while escolha not in ['1', '2', '3', '4']:
                escolha = input("\nEscolha um atributo (1-4): ")
            atributo_escolhido = list(carta_jogador.atributos.keys())[int(escolha) - 1]
        else:
            # IA simples: escolhe o maior atributo da sua carta
            atributo_escolhido = max(carta_computador.atributos, key=carta_computador.atributos.get)
            print(f"\nO computador escolheu: {atributo_escolhido}")

        valor_jogador = carta_jogador.atributos[atributo_escolhido]
        valor_computador = carta_computador.atributos[atributo_escolhido]
        
        print("\n--- COMPARANDO ---")
        print(f"Atributo: {atributo_escolhido}")
        print(f"Sua carta: {carta_jogador.nome} ({valor_jogador})")
        print(f"Carta do computador: {carta_computador.nome} ({valor_computador})")

        # Compara os valores e determina o vencedor da rodada
        if valor_jogador > valor_computador:
            print("\nVocê venceu a rodada!")
            mao_jogador.append(mao_jogador.pop(0))
            mao_jogador.append(mao_computador.pop(0))
            jogador_da_vez = "jogador"
        elif valor_computador > valor_jogador:
            print("\nO computador venceu a rodada!")
            mao_computador.append(mao_computador.pop(0))
            mao_computador.append(mao_jogador.pop(0))
            jogador_da_vez = "computador"
        else:
            print("\nEmpate! As cartas vão para o 'monte'.")
            # Em caso de empate, as cartas são movidas para o final de cada baralho
            mao_jogador.append(mao_jogador.pop(0))
            mao_computador.append(mao_computador.pop(0))

        rodada += 1
        input("\nPressione Enter para continuar...")

    # Fim de jogo
    limpar_tela()
    if not mao_jogador:
        print("FIM DE JOGO! Você perdeu, ficou sem cartas. :(")
    else:
        print("FIM DE JOGO! Parabéns, você venceu! O computador não tem mais cartas. :)")

if __name__ == "__main__":
    jogar()
