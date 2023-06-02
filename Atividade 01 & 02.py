from os import system
system('cls')

print('**************************************')
print('******* Adivinhe qual o número *******')
print('**************************************')

NUMERO_SECRETO = 83 

rodada = 1
total_de_tentativas = 3

while (rodada <= total_de_tentativas):
    tentativa = input('Tente acertar o número: ')
    print('Você digitou: ', tentativa)
    print(f'\nTentativa {rodada:02d} de {total_de_tentativas:02d}')
    rodada += 1

    try:
        tentativa_int = int(tentativa)
    except ValueError:
        print('Valor invalído, escreva números inteiros. Por favor!')
        exit()
    except Exception as e:
        print(f'ERRO: {e}')
        exit()
    else:
        pass
    
    finally:
        pass



    # if (NUMERO_SECRETO == tentativa_int):
    #     print('Boa tentativa. ACERTOU!')
    # else:
    #     print(f'Você errou! O número não é {tentativa}.')
    #     if (tentativa_int > NUMERO_SECRETO):
    #         print('Sua tentiva foi MAIOR do que o número secreto.')
    #     else:
    #         print('Sua tentativa foi MENOR que o número secreto.')
    #     print('GAME OVER!')
    # print('Obrigado por participar!')


    acerto = tentativa_int == NUMERO_SECRETO
    ehmaior = tentativa_int > NUMERO_SECRETO
    ehmenor = tentativa_int < NUMERO_SECRETO

    if acerto:
        print('Você acertou o número secreto!')
        break
    else:
        print(f'Você errou o número secreto. (Não é {tentativa})')

        if ehmaior:
            print('O número escolhido é maior que o número secreto.')
        if ehmenor:
            print('O número escolhido é menor que o número secreto.')
        print("-GAME OVER-")
    print('Obrigado por participar!')