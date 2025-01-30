import random
def escolher_palavra():
    return random.choice(['python','java','javascript','php','código','erro'])

pc=escolher_palavra()
if pc is None:
    raise ValueError("Erro ao escolher a palavra!")

palavra_oculta = ["_" for _ in pc]
tentativas=6
while "_" in palavra_oculta and tentativas > 0:
    pj = input("Digite uma letra: ").strip().lower()

    if pj in pc:  # Se a letra estiver na palavra
        for i, letra in enumerate(pc):
            if letra == pj:
                palavra_oculta[i] = pj
    else:
        tentativas -= 1
        print(f"Letra errada! Você tem {tentativas} tentativas restantes.")

    print("Palavra:", " ".join(palavra_oculta))

# Verifica se o jogador venceu ou perdeu
if "_" not in palavra_oculta:
    print("Parabéns! Você acertou a palavra:", pc)
else:
    print("Você perdeu! A palavra era:", pc)
