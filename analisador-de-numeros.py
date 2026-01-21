

def mostrar_menu():

    print("***********************")
    print("Escolha um opção")
    print("1 - Inserir novo valor")
    print("2 - Analisar")
    print("3 - Limpar")
    print("4 - Sair")
    print("***********************")

def inserir_valor(lancamentos):

    valor = int(input("Insira um valor: "))

    lancamentos.append({
        "valor": valor,
        
    })

    return lancamentos

def analisar_lancamentos(lancamentos):

    quant_impar = 0
    quant_par = 0
    soma = 0

    if len(lancamentos) == 0:
        return None

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

        return {
            "soma" : soma,
            "pares" : quant_par,
            "impares" : quant_impar,
            "maior" : maior,
            "media" : media
        }

def mostrar_analise(estatistica):
    print(f"A soma dos valores inseridos é de {estatistica['soma']}.")
    print(f"Dos quais são {estatistica['pares']} Par e {estatistica['impares']} Ímpar.")
    print(f"O maior valor inserido foi {estatistica['maior']}.")
    print(f"A média dos valores inseridos é {estatistica['media']}.")

def limpar_lancamentos(lancamentos):
    confirmacao = input("Você realmente quer apagar todos os lançamentos? s/n ")

    if confirmacao == "s":
        lancamentos.clear()
        print("A lista foi resetada.")
    
    elif confirmacao == "n":
        print("Operação cancelada.")
    
    else:
        print("Opção Ínvalida.")

    return lancamentos

def main():
    lancamentos = []
    
    while True:
        mostrar_menu()
        opcao = input("Digite a opção desejada: ")
        print(" ")

        if opcao == "1":
           lancamentos = inserir_valor(lancamentos)
            
        elif opcao == "2" :
            estatistica = analisar_lancamentos(lancamentos)
            
            if estatistica is None:
                print("Nenhum valor inserido.")
            else:
                mostrar_analise(estatistica)

        elif opcao == "3" :
           lancamentos = limpar_lancamentos(lancamentos)
            
        elif opcao == "4" :
            break 

if __name__ == "__main__":
    main()