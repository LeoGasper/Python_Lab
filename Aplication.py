from sympy import false

print("Selecione uma das opções abaixo")
print("1 - Matematica")
print("2 - ")
print("3 - ")
print("4 - ")
print("5 - ")
opcoes = int(input("Apresente o número da sua opção: "))

while True:
    print("---Entrando na sua opção---")
    if opcoes == 1:
        print("Selecione a conta:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Porcentagem")
        print("6 - Potência")
        Mat = int(input("Apresente o número da opção: "))
        if Mat == 1:
            num1Soma = int(input("Apresente o primeiro número da soma: "))
            num2Soma = int(input("Apresente o segundo número da soma: "))
            somaFinal = num1Soma + num2Soma
            print(f"O valor final da soma é {somaFinal}")
        elif Mat == 2:
            num1Sub = int(input("Apresente o primeiro número da subtração: "))
            num2Sub = int(input("Apresente o segundo número da subtração: "))
            subFinal = num1Sub - num2Sub
            print(f"O valor final da subtração é {subFinal}")
        elif Mat == 3:
            num1Mult = int(input("Apresente o primeiro número da multiplicação: "))
            num2Mult = int(input("Apresente o segundo número da multiplicação: "))
            multFinal = num1Mult * num2Mult
            print(f"O valor final da divisão é {multFinal}")
        elif Mat == 4:
            num1Div = int(input("Apresente o primeiro número da divisão: "))
            num2Div = int(input("Apresente o segundo número da divisão: "))
            divisaoFinal = num1Div/num2Div
            print(f"O valor final da divisão é {divisaoFinal}")
        elif Mat == 5:
            num1Porcen = int(input("Apresente o número: "))
            num2Porcen = int(input("Apresente a porcentagem: "))
            porcenOpcao = int(input("1 - reajuste mais, 2- reajuste menos: "))
            if porcenOpcao == 1:
                reajuste = num1Porcen * num2Porcen/100
                reajusteMais = num1Porcen + reajuste
                print(f"Sua porcentagem é de {reajusteMais:.2f}")
            elif porcenOpcao == 2:
                reajuste = num1Porcen * num2Porcen/100
                reajusteMenos = num1Porcen - reajuste
                print(f"Sua porcentagem é de {reajusteMenos:.2f}")
        elif Mat == 6:
            num1Poten = int(input("Apresente o número: "))
            num2Poten = int(input("Apresente o número que eleva: "))
            potenFinal = num1Poten ** num2Poten
            print(f"O valor final da potência é {potenFinal}")
        else:
            print("Número invalido")
            encerrar = input("Deseja continuar no programa? s/n  - ").lower()
    if encerrar != 's':
        print("Encerrando!!")
        break

