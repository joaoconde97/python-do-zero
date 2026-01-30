import json
import os

arquivo_dados = "lancamentos.json"

def mostrar_menu():

    linha()
    print("ANALISADOR DE NÚMEROS")
    linha()
    print("1 - Inserir novo valor")
    print("2 - Analisar valores")
    print("3 - Limpar valores")
    print("4 - Sair")
    linha()

def linha():
    print("=" * 40)

def inserir_valor(lancamentos):

    valor = pedir_inteiro("Insira um valor inteiro: ")

    lancamentos.append({
        "valor": valor,
        
    })
    print(f"Valor {valor} inserido com sucesso.")
    return lancamentos

def analisar_lancamentos(lancamentos):

    if not lancamentos:
        return None
    
    quant_impar = 0
    quant_par = 0
    soma = 0
    menor = lancamentos[0]["valor"]
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

        if valor < menor:
            menor = valor
    
    media = soma / len(lancamentos)

    return {
        "soma" : soma,
        "pares" : quant_par,
        "impares" : quant_impar,
        "maior" : maior,
        "menor" : menor,
        "media" : media
    }

def menor_numero(lancamentos):
    menor = lancamentos[0]["valor"]

    for item in lancamentos:
        valor = item["valor"]

        if valor < menor:

            return menor

def mostrar_analise(estatistica):
    linha()
    print("        ANÁLISE DOS VALORES")
    linha()
    print(f"A soma total: {estatistica['soma']}")
    print(f"Pares: {estatistica['pares']}")
    print(f"Ímpares: {estatistica['impares']}")
    print(f"Maior valor: {estatistica['maior']}")
    print(f"Menor valor: {estatistica['menor']}")
    print(f"Média: {estatistica['media']:.2f}")
    linha()

def carregar_lancamentos():
    if not os.path.exists(arquivo_dados):
        return []
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_lancamentos(lancamentos):
    with open(arquivo_dados, "w", encoding="utf-8") as arquivo:
        json.dump(lancamentos, arquivo, ensure_ascii=False, indent=4)

def limpar_lancamentos(lancamentos):

    if not lancamentos:
        print("A lista já está vazia.")
        return
    

    confirmacao = input("Você realmente quer apagar todos os lançamentos? s/n ")

    if confirmacao == "s":
        lancamentos.clear()
        print("Todos os valores foram removidos.")
    
    elif confirmacao == "n":
        print("Operação cancelada.")
    
    else:
        print("Opção Ínvalida.")

    return lancamentos

def ler_opcao():
    return input("Digite a opção desejada: ")

def tratar_opcao(opcao, lancamentos):

    if opcao == "1":
           inserir_valor(lancamentos)
            
    elif opcao == "2" :
        estatistica = analisar_lancamentos(lancamentos)
        
        if estatistica is None:
            print("Nenhum valor inserido.")
        else:
            mostrar_analise(estatistica)

    elif opcao == "3" :
        return limpar_lancamentos(lancamentos)
        
    elif opcao == "4" :
        salvar_lancamentos(lancamentos)
        print("Encerrando o programa...")
        return "Sair"

    else:
        print("Opção Ínvalida.")

def pedir_inteiro(mensagem):
    while True:
        valor = input(mensagem)

        if valor.isdigit():
            return int(valor)

        else:
            print("Valor ínvalido, insira um valor inteiro.")

def main():
    lancamentos = carregar_lancamentos()
    
    while True:
        mostrar_menu()
        opcao = ler_opcao()
        print(" ")

        resultado = tratar_opcao(opcao, lancamentos)
        input("\n Presione ENTER para continuar...")

        if resultado == "Sair":
            break

        
if __name__ == "__main__":
    main()
