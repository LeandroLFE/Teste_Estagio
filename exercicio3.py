def leitura_json_dict(arquivo):
    '''
    Função que realiza a leitura de um arquivo JSON 
    e retorna um dicionário em Python
    '''
    from json import load
    with open(arquivo, 'r') as f:
        dados_json = load(f)
    
    return dados_json

def filtra_dias_sem_faturamento(dados):
    '''
    Função que remove dias sem faturamento para não prejudicar os cálculos
    '''
    novos_dados = []
    for dado in dados:
        if(dado["valor"] != 0.0):
            novos_dados += [dado]
    
    return novos_dados

def calcula_menor_valor_faturamento(dados):
    '''
    Função que retorna o menor valor de faturamento ocorrido em um dia do mês
    '''
    if dados == []:
        print("Não há dados a serem exibidos")
        return
    
    menor_valor = dados[0]["valor"]
  
    for dado in dados:
        if dado["valor"] < menor_valor:
            menor_valor = dado["valor"]

    return menor_valor

def calcula_maior_valor_faturamento(dados):
    '''
    Função que retorna o maior valor de faturamento ocorrido em um dia do mês
    '''
    if dados == []:
        print("Não há dados a serem exibidos")
        return
    
    maior_valor = dados[0]["valor"]
  
    for dado in dados:
        if dado["valor"] > maior_valor:
            maior_valor = dado["valor"]

    return maior_valor

def calcula_media(dados):
    '''
    Função que calcula a média dada uma lista de dados de faturamento
    '''
    soma = 0
    tamanho_lista = len(dados)

    for dado in dados:
        soma += dado["valor"]

    return soma / float(tamanho_lista) 


def calcula_numero_dias_mes_em_que_o_valor_faturamento_foi_superior_a_media_mensal(dados):
    '''
    Função que verifica o numero de dias do mês em que o valor do faturamento foi superior à média mensal
    '''
    media = calcula_media(dados)
    numero_dias = 0
    for dado in dados:
        if dado["valor"] > media:
            numero_dias += 1

    return numero_dias


if __name__ == '__main__':
    titulo = "Programa que calcula o menor e maior valor de faturamento mensal, além do número de dias em que o faturamento diário foi superior no mesmo mês"
    print(f"""{"-" * len(titulo)}""")
    print(titulo)
    print(f"""{"-" * len(titulo)}""")
    dados_faturamento_brutos = leitura_json_dict("dados.json")
    dados_faturamento = filtra_dias_sem_faturamento(dados_faturamento_brutos)
    print(f"\nO menor valor de faturamento ocorrido em um dia do mês foi: {calcula_menor_valor_faturamento(dados_faturamento)}")
    print(f"O maior valor de faturamento ocorrido em um dia do mês foi: {calcula_maior_valor_faturamento(dados_faturamento)}")
    print(f"O número de dias no mês em que o valor de faturamento diário foi superior a media mensal foi: {calcula_numero_dias_mes_em_que_o_valor_faturamento_foi_superior_a_media_mensal(dados_faturamento)}\n")