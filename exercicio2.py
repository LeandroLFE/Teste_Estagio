def fib(numero):
    '''
    Funcão que calcula a sequência de Fibonacci até alcançar um certo número
    '''
    i, j = 0, 1
    soma = i + j
    lista_fib = [i, j, soma]

    while (soma < numero):
        i = j
        j = soma
        soma = i + j
        lista_fib += [soma]

    print(f"Sequência de Fibonacci: {lista_fib}")
    return numero in lista_fib


if __name__ == '__main__':
    titulo = "Programa que verifica se dado número pertence ou não a sequência de Fibonacci"
    print(f"""{"-" * len(titulo)}""")
    print(titulo)
    print(f"""{"-" * len(titulo)}""")
    entrada = ''
    while(not entrada.isnumeric()):
        entrada = input("\nInforme um número: ")
        if(not entrada.isnumeric()): #Informa a digitação incorreta para o usuário 
            print("Número inválido, tente novamente")

    entrada = int(entrada)       
    saida = f"O número {entrada} PERTENCE a sequencia de Fibonacci\n" if fib(entrada) else f"O número {entrada} NÃO pertence a sequencia de Fibonacci\n"
    print(saida)