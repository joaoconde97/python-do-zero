lancamentos = []

def mostrar_menu():

    print("***********************")
    print("Escolha um opção")
    print("1 - Inserir novo valor")
    print("2 - Analisar")
    print("3 - Limpar")
    print("4 - Sair")
    print("***********************")

def inserir_valor():

    valor = int(input("Insira um valor: "))

    lancamentos.append({
        "valor": valor,
        
    })

def analisar_lancamentos():

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

def limpar_lancamentos():
    confirmacao = input("Você realmente quer apagar todos os lançamentos? s/n ")

    if confirmacao == "s":
        lancamentos.clear()
        print("A lista foi resetada.")
    

while True:
    mostrar_menu()
    opcao = input("Digite a opção desejada: ")
    print(" ")

    if opcao == "1":
        inserir_valor()
        
    elif opcao == "2" :
        analisar_lancamentos()

    elif opcao == "3" :
        limpar_lancamentos()
        
    elif opcao == "4" :
        break 

