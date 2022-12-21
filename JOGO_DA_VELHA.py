'''
Jogo da velha
'''
import os
palavra = input("Informe uma palavra:")
letra_acertada = ''
tentativas = len(palavra)
letras_ja_incluidas = ''
os.system("cls")
while True:
    letra_digitada = input("Informe uma letra:")

    if letra_digitada in letras_ja_incluidas:
        print("Essa letra já digitada, informe uma outra!")
    else:
        letras_ja_incluidas += letra_digitada
   
    if len(letra_digitada) > 1:
        os.system("cls")
        print("Informe apenas UMA letra!")
        continue
    
    if len(letra_digitada) < 1:
        print("Nenhuma letra foi digitada, informe uma letra!")
        continue
    
    print((f"Letra já digitada '{letras_ja_incluidas}' "))

    if letra_digitada in palavra:
        letra_acertada += letra_digitada
    else:
        os.system("cls")
        tentativas -= 1 
        print(f"Letra errada, ainda tem {tentativas}, tente novamente!")
        print(letras_ja_incluidas)
    
    palavra_formada = ''
   
    for letra_oculta in palavra:
        if letra_oculta in letra_acertada:
            palavra_formada += letra_oculta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    
    

    if palavra_formada == palavra:
        os.system("cls")
        print(f'a palavra era {palavra_formada}')
        print("Parabéns você ganhou!")
        break

    if tentativas == 0:
        print("Você perdeu")
        break