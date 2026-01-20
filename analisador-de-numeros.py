lancamentos = []

while True:

    print("Escolha um opção")
    print("1 - Inserir novo valor")
    print("2 - Analisar")
    print("3 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        valor = int(input("Insira um valor: "))

        lancamentos.append({
            "valor": valor,
        
        })
        
    elif opcao == "2" :
        quant_impar = 0
        quant_par = 0
        soma = 0
        maior = lancamentos[0]["valor"]

        if len(lancamentos) == 0:
            print("Nenhum valor inserido.")

        else :
            maior = lancamentos[0]["valor"]
            for item in lancamentos :
                valor = item["valor"]

                if valor % 2 == 0 :
                    quant_par += 1

                else :
                    quant_impar += 1

                soma += valor

                if valor > maior:
                    maior = valor
            
            media = soma / len(lancamentos)

    
        print(f"A soma dos valores inseridos é de {soma}.")

        print(f"Dos quais são {quant_par} Par e {quant_impar} Ímpar.")

        print(f"O maior valor inserido foi {maior}.")

        print(f"A média dos valores inseridos é {media}.")


    elif opcao == "3" :
        break 

