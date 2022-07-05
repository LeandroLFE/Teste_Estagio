dados = {
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "OUTROS" : 19849.53,
}

def calcula_total_mensal(dados):
    '''
    Função que calcula o total de faturamento através da soma dos dados brutos
    '''
    total = 0

    for estado in dados.keys():
        total += dados[estado]
    
    return total

def calcula_porcentagem_estado(faturamento_estado, total):
    '''
    Função que calcula o percentual de representação de cada estado dentro do valor total mensal da distribuidora
    '''
    return faturamento_estado * 100.0 / total 


if __name__ == '__main__':
    titulo = "Programa que calcula o percentual de representação que cada estado teve dentro do valor total da distribuidora"
    print(f"""{"-" * len(titulo)}""")
    print(titulo)
    print(f"""{"-" * len(titulo)}""")
    total = calcula_total_mensal(dados)
    print(f"\nO valor total do faturamento mensal foi de R$ {total}")
    for estado in dados.keys():
        representacao = calcula_porcentagem_estado(dados[estado], total)
        if estado != "OUTROS": 
            print(f"O fatumento do estado {estado} representou {representacao:.2f}%")
        else:
            print(f"Outros estados representaram {representacao:.2f}%\n")