import time

print('*'*20)
print("O personagem é Henrique um menino orfão de apenas 7 anos")
print('*'*20)

def print_pause(message):
    print(message)
    time.sleep(2)  # Pausa para criar suspense

def intro():
    print_pause("Henrique está em uma floresta escura e misteriosa.")
    print_pause("Dizem que um tesouro perdido está escondido aqui...")
    print_pause("Mas ouviu rumores de uma criatura perigosa que guarda o tesouro.")
    print_pause("Agora, a missão do garoto é encontrar o tesouro... ou escapar com vida!")

def cave():
    print_pause("\nHenrique encontra uma caverna escura.")
    choice = input("Ele vai entrar na caverna? [sim/não]\n").lower()
    if choice == "sim":
        print_pause("Ele entra na caverna e sente uma brisa fria.")
        print_pause("De repente vê algo brilhando ao fundo...")
        treasure_room()
    elif choice == "não":
        print_pause("Ele decide que entrar na caverna seria perigoso.")
        print_pause("Ele volta para a floresta.")
        forest()
    else:
        print_pause("Não entendi essa resposta.")
        cave()

def river():
    print_pause("\nHenrique encontra um rio com águas agitadas.")
    choice = input("Ele quer tentar atravessar o rio? [sim/não]\n").lower()
    if choice == "sim":
        print_pause("Ele começa a atravessar o rio...")
        print_pause("As águas são fortes e quase perde o equilíbrio!")
        print_pause("Mas consegue chegar do outro lado.")
        print_pause("Encontra um caminho secreto!")
        treasure_room()
    elif choice == "não":
        print_pause("Decide não arriscar atravessar o rio.")
        print_pause("Volta para a floresta.")
        forest()
    else:
        print_pause("Não entendi essa resposta.")
        river()

def treasure_room():
    print_pause("\nParabéns! Henrique encontrou o tesouro perdido!")
    print_pause("Mas de repente, a criatura guardiã aparece para mata-lo...")
    choice = input("Quer lutar ou fugir? (lutar/fugir)\n").lower()
    if choice == "lutar":
        print_pause("Ele se prepara para a batalha com sua espada...")
        print_pause("A criatura é feroz, mas o orfão é corajoso!")
        print_pause("Após uma luta intensa, ele arranca a cabeça da criatura e conquista o tesouro!")
        end_game("Henrique é o novo guardião do tesouro perdido e deixa a cabeça da criatura como exemplo para outras ameaças futuras!")
    elif choice == "fugir":
        print_pause("Ele decide que o tesouro não vale sua vida.")
        print_pause("Ele corre de volta para a segurança da floresta.")
        end_game("Escapou com vida, mas sem o tesouro.")
    else:
        print_pause("Não entendi essa resposta.")
        treasure_room()

def forest():
    print_pause("\nHenrique está de volta à floresta. Para onde quer ir?")
    choice = input("Escolha um caminho: caverna ou rio.\n").lower()
    if choice == "caverna":
        cave()
    elif choice == "rio":
        river()
    else:
        print_pause("Não entendi essa resposta.")
        forest()

def end_game(message):
    print_pause(f"\n{message}")
    print_pause("Fim da aventura.")
    replay = input("Gostaria de jogar novamente? [sim/não]\n").lower()
    if replay == "sim":
        start_game()
    else:
        print("Obrigado por jogar! Até a próxima aventura!")

def start_game():
    intro()
    forest()

# Iniciar o jogo
start_game()