def inverte_string(string_entrada):
    '''
    Função que inverte os caracteres de uma string
    '''
    # return string_entrada[::-1] Solução simples ignorada para fins do teste 
    
    tamanho_string = len(string_entrada)

    i = tamanho_string-1

    string_reversa = ""
    while(i>=0):
        string_reversa += string_entrada[i]
        i-=1
    return string_reversa


if __name__ == '__main__':
    titulo = "Programa que inverte uma string"
    print(f"""{"-" * len(titulo)}""")
    print(titulo)
    print(f"""{"-" * len(titulo)}""")
    string_entrada = input("\nInforme a string de entrada: ")
    print("\nA string invertida é: {0} \n".format(inverte_string(string_entrada)))

