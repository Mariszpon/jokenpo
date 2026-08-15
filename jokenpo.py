# Oi professora!! É a Mari :) Eu fiz algumas anotações no código porque fico bastante nervosa em trabalhos.
# Assim sei exatamente o que falar, espero que entenda!!

# - - - Menu - - -
print()
print("\033[95m────୨ৎ────\033[0m" * 3)
print("\033[33m⋆˚꩜｡ Mᴇɴᴜ: J𖹭ᴋᴇɴᴘ𖹭̂.ᐟ ⋆˚࿔\033[0m".center(38))
print()
print("\033[36m𐔌՞. .՞𐦯 M𖹭ᴅ𖹭s ᴅᴇ ᴊ𖹭ɢ𖹭: ᶻ 𝗓 𐰁 \033[0m".center(30))
print("⤷ Hᴜᴍᴀɴ𖹭 x Hᴜᴍᴀɴ𖹭 (1) ⋆˚࿔")
print("⤷ Hᴜᴍᴀɴ𖹭 x Mᴀ́ǫᴜɪɴᴀ (2) ⋆˚࿔")
print("⤷ Mᴀ́ǫᴜɪɴᴀ x Mᴀ́ǫᴜɪɴᴀ (3) ⋆˚࿔")
print("⤷ Sᴀɪʀ ᴅ𖹭 Pʀ𖹭ɢʀᴀᴍᴀ (4) ⋆˚࿔")
print()
print("\033[95m────୨ৎ────\033[0m" * 3)

# O código usa print() com símbolos e cores para deixar o menu mais bonito;
# O menu mostra quatro modos de jogo.

verify = 0
while verify == 0:
    gameMode = int(input("\033[33m⤷ Sᴇʟᴇᴄɪ𖹭ɴᴇ 𖹭 ᴍ𖹭ᴅ𖹭 ᴅᴇ ᴊ𖹭ɢ𖹭: \033[0m"))
    if 4 >= gameMode > 0:
        verify = verify + 1
    else:
        print()
        print("\033[95m(╥﹏╥) Vᴀʟ𖹭ʀ Iɴᴠᴀ́ʟɪᴅ𖹭 !! *ੈ✩‧₊˚\033[0m")
        print()

# Enquanto o verify for igual a 0, o programa continua pedindo pro usuário escolher um modo.
# Se o usuário digital um número válido (Entre 1 e 3), verify passa a ser 1 e o loop termina.
# Se o número for inválido (>3 ou 0>=), aparece a mensagem de erro e o programa volta a pedir a escolha.

# - - - Humano x Humano - - -

if gameMode == 1:
    print("⤷ Hᴜᴍᴀɴ𖹭 x Hᴜᴍᴀɴ𖹭 (1) ⋆˚࿔")
    print()

    # Se o usuário escolheu 1 no menu, o programa entra nesse bloco.

    vitoria1 = 0
    vitoria2 = 0
    empate = 0

    verify2 = 0
    while verify2 == 0:

        # Aqui começa outro loop, terminando apenas se verify2 for diferente de 0.
        # Isso significa que o jogo continua rodando até o jogador decidir não jogar novamente.
        # Os outros servem para o placar.

        print("Sᴇʟᴇᴄɪ𖹭ɴᴇ ᴜᴍᴀ 𖹭ᴘçã𖹭 ᴇɴᴛʀᴇ ᴘᴇᴅʀᴀ, ᴘᴀᴘᴇʟ ᴇ ᴛᴇs𖹭ᴜʀᴀ !!")
        jogador1 = input("\033[33m(˶ˆᗜˆ˵) J𖹭ɢᴀᴅ𖹭ʀ 1, ʀᴇᴀʟɪᴢᴇ sᴜᴀ ᴊ𖹭ɢᴀᴅᴀ, ᴘ𖹭ʀ ғᴀᴠ𖹭ʀ !! ۶ৎ Aɢ𖹭ʀᴀ ᴇsᴄ𖹭ʟʜᴀ: \033[0m").lower()

        if jogador1 != "pedra" and jogador1 != "papel" and jogador1 != "tesoura":
            print("\033[95m(╥﹏╥) J𖹭ɢᴀᴅᴀ Iɴᴠᴀ́ʟɪᴅᴀ !! *ੈ✩‧₊˚\033[0m")
            print()
            continue

        # O programa avisa as opções válidas e pede para o Jogador1 digitar sua jogada.
        # .lower() transforma o texto em minúsculo, para evitar erro se o jogador digitar "Pedra" ou "PEDRA".
        # Depois, o programa verifica se o que o jogador digitou é diferente das opções, se for inválido, dá erro.
        # Verify2 = 0 mantém o loop rodando, ou seja, o jogador terá que tentar novamente.
        # o continue faz pular imediatamente para a próxima interação do loop.

        else:
            print("\n" * 20)

            # A parte "\n" dá espaço de 20 linhas para o Jogador1 não ver a resposta do Jogador2.

            verify3 = 0
            while verify3 == 0:
                jogador2 = input(
                    "\033[33m(˶ˆᗜˆ˵) J𖹭ɢᴀᴅ𖹭ʀ 2, ʀᴇᴀʟɪᴢᴇ sᴜᴀ ᴊ𖹭ɢᴀᴅᴀ, ᴘ𖹭ʀ ғᴀᴠ𖹭ʀ !! ۶ৎ Aɢ𖹭ʀᴀ ᴇsᴄ𖹭ʟʜᴀ: \033[0m").lower()
                if jogador2 != "pedra" and jogador2 != "papel" and jogador2 != "tesoura":
                    print("\033[95m(╥﹏╥) J𖹭ɢᴀᴅᴀ Iɴᴠᴀ́ʟɪᴅᴀ !! *ੈ✩‧₊˚\033[0m")
                    print()
                    verify3 = 0
                else:
                    verify3 = 1

        # Depois que o Jogador1 escolhe, o programa pede a escolha do Jogador2.
        # O mesmo processo acontece: Começa outro loop, terminando se verify3 != 0;
        # Ou seja, se for inválido, repete até ser válido.

        if jogador1 == jogador2:
            print()
            print("\033[36m ݁ ˖Ი𐑼⋆ Eᴍᴘᴀᴛᴇ !! ⋆˚࿔\033[0m")
            empate += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Jᴏɢᴀᴅᴏʀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Jᴏɢᴀᴅᴏʀ 2'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()

            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('\033[95mRᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!\033[0m')
                    print()
                    respostaValida = 0

        # Ao final da jogada, será adicionado 1 ponto ao empate.
        # Assim, mostrará no placar que os jogadores cada um receberam 1 ponto.

        # Se o Usuário escolher digitar 1 na variável "jogarNovamente", ele joga mais uma vez!
        # Caso contrário, o jogo termina.
        # O "respostaValida" funciona para caso a pessoa não digitar 1 ou 2,
        # o sistema não volte ao início do modo do jogo ou termine a operação.

        elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
            print("\033[36m ݁ ˖Ი𐑼⋆ J𖹭ɢᴀᴅ𖹭ʀ 1 ɢᴀɴʜ𖹭ᴜ !! Pᴀʀᴀʙᴇ́ɴs !! ⋆˚࿔\033[0m")

            vitoria1 += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Jᴏɢᴀᴅᴏʀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Jᴏɢᴀᴅᴏʀ 2'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()

# Ao final da jogada, será adicionado 1 ponto ao vitória1.
# Assim, mostrará no placar que o jogador 1 recebeu 1 ponto.

            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('\033[95mRᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!\033[0m')
                    print()
                    respostaValida = 0

        # Se não digitar 1 ou 2 não continua o código.
        # Vitória do jogador1.

        else:
            print("\033[36m ݁ ˖Ი𐑼⋆ J𖹭ɢᴀᴅ𖹭ʀ 2 ɢᴀɴʜ𖹭ᴜ !! Pᴀʀᴀʙᴇ́ɴs !! ⋆˚࿔\033[0m")
            vitoria2 += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Jᴏɢᴀᴅᴏʀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Jᴏɢᴀᴅᴏʀ 2'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()

            # Ao final da jogada, será adicionado 1 ponto ao vitória2.
            # Assim, mostrará no placar que o jogador 2 recebeu 1 ponto.

            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('\033[95mRᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!\033[0m')
                    print()
                    respostaValida = 0

# Vitória do jogador2.

# - - - Humano x Máquina - - -

if gameMode == 2:
    print("⤷ Hᴜᴍᴀɴ𖹭 x Mᴀ́ǫᴜɪɴᴀ (2) ⋆˚࿔")
    print()

    contador = 0
    verify2 = 0
    vitoria1 = 0
    vitoria2 = 0
    empate = 0

# contador: Controla a jogada da máquina.
# verify2: mantém o loop do jogo ativo.
# vitoria1: conta quantas vezes o jogador humano venceu.
# vitoria2: conta quantas vezes a máquina venceu.
# vitoria3: conta quantos empates aconteceram.

    while verify2 == 0:
        print("Sᴇʟᴇᴄɪ𖹭ɴᴇ ᴜᴍᴀ 𖹭ᴘçã𖹭 ᴇɴᴛʀᴇ ᴘᴇᴅʀᴀ, ᴘᴀᴘᴇʟ ᴇ ᴛᴇs𖹭ᴜʀᴀ !!")
        jogador1 = input("\033[33m(˶ˆᗜˆ˵) J𖹭ɢᴀᴅ𖹭ʀ 1, ʀᴇᴀʟɪᴢᴇ sᴜᴀ ᴊ𖹭ɢᴀᴅᴀ, ᴘ𖹭ʀ ғᴀᴠ𖹭ʀ !! ۶ৎ Aɢ𖹭ʀᴀ ᴇsᴄ𖹭ʟʜᴀ: \033[0m").lower()
        if jogador1 != "pedra" and jogador1 != "papel" and jogador1 != "tesoura":
            print("\033[95m(╥﹏╥) J𖹭ɢᴀᴅᴀ Iɴᴠᴀ́ʟɪᴅᴀ !! *ੈ✩‧₊˚\033[0m")
            verify2 = 0

        contador = contador + 1
        resto = contador % 3
        if resto == 0:
            jogadaMaquina = "pedra"
        elif resto == 1:
            jogadaMaquina = "papel"
        else:
            jogadaMaquina = "tesoura"

# Cada vez que o jogador humano faz uma jogada, o contador aumenta em +1.
# Ele funciona como um "marcador de rodadas".

        if jogador1 == jogadaMaquina:
            print("\033[36m ݁ ˖Ი𐑼⋆ Eᴍᴘᴀᴛᴇ !! ⋆˚࿔\033[0m")
            empate += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Jᴏɢᴀᴅᴏʀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 1'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()
            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('Rᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!')
                    respostaValida = 0


        elif (jogador1 == "pedra" and jogadaMaquina == "tesoura") or (jogador1 == "papel" and jogadaMaquina == "pedra") or (jogador1 == "tesoura" and jogadaMaquina == "papel"):
            print("\033[36m ݁ ˖Ი𐑼⋆ J𖹭ɢᴀᴅ𖹭ʀ 1 ɢᴀɴʜ𖹭ᴜ !! Pᴀʀᴀʙᴇ́ɴs !! ⋆˚࿔\033[0m")
            vitoria1 += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Jᴏɢᴀᴅᴏʀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 1'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()
            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('Rᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!')
                    respostaValida = 0


        else:
            print("\033[36m ݁ ˖Ი𐑼⋆ A ᴍᴀ́ǫᴜɪɴᴀ ᴠᴇɴᴄᴇᴜ !! ⋆˚࿔\033[0m")
            vitoria2 += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Jᴏɢᴀᴅᴏʀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 1'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()
            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('Rᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!')
                    respostaValida = 0

# - - - Máquina x Máquina - - -

if gameMode == 3:

    print("⤷ Mᴀ́ǫᴜɪɴᴀ x Mᴀ́ǫᴜɪɴᴀ (3) ⋆˚࿔")
    import random
    verify2 = 0
    vitoria1 = 0
    vitoria2 = 0
    empate = 0
    while verify2 == 0:
        maquina1 = random.randint(1, 3)
        maquina2 = random.randint(1, 3)

        print()
        if maquina1 == 0:
            print("\033[95m⋆˙⟡ Mᴀ́ǫᴜɪɴᴀ 1: ᴘᴇᴅʀᴀ .ᐟ\033[0m")
        elif maquina1 == 1:
            print("\033[95m⋆˙⟡ Mᴀ́ǫᴜɪɴᴀ 1: ᴘᴀᴘᴇʟ .ᐟ\033[0m")
        else:
            print("\033[95m⋆˙⟡ Mᴀ́ǫᴜɪɴᴀ 1: ᴛᴇs𖹭ᴜʀᴀ .ᐟ\033[0m")

        if maquina2 == 0:
            print("\033[95m⋆˙⟡ Mᴀ́ǫᴜɪɴᴀ 2: ᴘᴇᴅʀᴀ .ᐟ\033[0m")
        elif maquina2 == 1:
            print("\033[95m⋆˙⟡ Mᴀ́ǫᴜɪɴᴀ 2: ᴘᴀᴘᴇʟ .ᐟ\033[0m")
        else:
            print("\033[95m⋆˙⟡ 3Mᴀ́ǫᴜɪɴᴀ 2: ᴛᴇs𖹭ᴜʀᴀ .ᐟ\033[0m")

        print()
        if maquina1 == maquina2:
            print("\033[36m ݁ ˖Ი𐑼⋆ Eᴍᴘᴀᴛᴇ !! ⋆˚࿔\033[0m")
            empate += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 2'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()
            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('Rᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!')
                    respostaValida = 0


        elif (maquina1 == 0 and maquina2 == 2) or (maquina1 == 1 and maquina2 == 0) or (maquina1 == 2 and maquina2 == 1):
            print("\033[36m ݁ ˖Ი𐑼⋆ A ᴍᴀ́ǫᴜɪɴᴀ 1 ᴠᴇɴᴄᴇᴜ !! ⋆˚࿔\033[0m")
            vitoria1 += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 2'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()
            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('Rᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!')
                    respostaValida = 0


        else:
            print("\033[36m ݁ ˖Ი𐑼⋆ A ᴍᴀ́ǫᴜɪɴᴀ 2 ᴠᴇɴᴄᴇᴜ !! ⋆˚࿔\033[0m")
            vitoria2 += 1
            print()
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("        PLACAR       ")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print("| Jᴏɢᴀᴅᴏʀ | Vɪᴛᴏʀɪᴀs | Dᴇʀʀᴏᴛᴀs | Eᴍᴘᴀᴛᴇs |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 1'   | {vitoria1} | {vitoria2} | {empate} |")
            print(f"| 'Mᴀ́ǫᴜɪɴᴀ 2'   | {vitoria2} | {vitoria1} | {empate} |")
            print("\033[95m────୨ৎ────\033[0m" * 3)
            print()
            respostaValida = 0
            while respostaValida == 0:
                jogarNovamente = int(input("⋆. 𐙚 ˚ Dᴇsᴇᴊᴀ ᴊ𖹭ɢᴀʀ ɴ𖹭ᴠᴀᴍᴇɴᴛᴇ ?? (1 ᴘᴀʀᴀ sɪᴍ ᴇ 2 ᴘᴀʀᴀ ɴᴀ̃ᴏ): "))
                if jogarNovamente == 1:
                    verify2 = 0
                    respostaValida = 1
                elif jogarNovamente == 2:
                    verify2 = 1
                    respostaValida = 1
                    print()
                    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
                else:
                    print('Rᴇsᴘ𖹭sᴛᴀ ɪɴᴠᴀ́ʟɪᴅᴀ !!!')
                    respostaValida = 0

if gameMode == 4:
    print("\033[95m°❀⋆.ೃ࿔*:･ Tʀᴀʙᴀʟʜ𖹭 ғᴇɪᴛ𖹭 ᴘ𖹭ʀ Lᴜᴄᴀs Dɪɴɴɪᴇs ᴇ Mᴀʀɪᴀɴᴀ P𖹭ɴᴅᴇ́  ‹𝟹\033[0m")
