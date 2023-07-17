import numpy as np
import pandas as pd

def met_americano(divida, taxa_juros, n_periodos):#juros constantes

    periodo = [0]
    juros_periodo = [0]
    amortizacao_periodo = []
    pagamento_periodo = []
    divida_periodo = [divida]

    #Atribuição dados dos períodos
    for p in range(1,n_periodos+1):

        periodo.append(p)
        juros_periodo.append(divida_periodo[p-1]*taxa_juros)
        amortizacao_periodo.append(0)
        divida_periodo.append(divida - amortizacao_periodo[p-1])
        pagamento_periodo.append(juros_periodo[p-1]+amortizacao_periodo[p-1])

    #Ajuste último período
    amortizacao_periodo.append(divida)
    pagamento_periodo.append(divida+juros_periodo[1])
    divida_periodo[n_periodos] = 0

    #cria um dicionario com elemntos para tebela
    tabela = {
        'periodos': periodo,
        'juros': juros_periodo,
        'amortizacao': amortizacao_periodo,
        'pagamento': pagamento_periodo,
        'divida': divida_periodo
    }



    # Cria o DataFrame usando o dicionário
    df = pd.DataFrame(tabela)

    return df.round(2)

def met_frances(divida, taxa_juros, n_periodos):# pagamentos constantes

    r = parcela(divida,taxa_juros,n_periodos)
    periodo = [0]
    juros_periodo = [0]
    amortizacao_periodo = [0]
    pagamento_periodo = [0]
    divida_periodo = [divida]

    #Atribuição dados dos períodos
    for p in range(1,n_periodos+1):

        periodo.append(p)
        juros_periodo.append(divida_periodo[p-1]*taxa_juros)
        pagamento_periodo.append(r)
        amortizacao_periodo.append(r-juros_periodo[p])
        divida_periodo.append(divida_periodo[p-1] - amortizacao_periodo[p])

    #cria um dicionario com elemntos para tebela
    tabela = {
        'periodos': periodo,
        'juros': juros_periodo,
        'amortizacao': amortizacao_periodo,
        'pagamento': pagamento_periodo,
        'divida': divida_periodo
    }



    # Cria o DataFrame usando o dicionário
    df = pd.DataFrame(tabela)

    return df.round(2)

def met_hamburgues(divida, taxa_juros, n_periodos):# amortização constante

    a = divida/n_periodos
    periodo = [0]
    juros_periodo = [0]
    amortizacao_periodo = [0]
    pagamento_periodo = [0]
    divida_periodo = [divida]

    #Atribuição dados dos períodos
    for p in range(1,n_periodos+1):

        periodo.append(p)
        juros_periodo.append(divida_periodo[p-1]*taxa_juros)
        amortizacao_periodo.append(a)
        pagamento_periodo.append(amortizacao_periodo[p]+juros_periodo[p])
        divida_periodo.append(divida_periodo[p-1] - amortizacao_periodo[p])

    #cria um dicionario com elemntos para tebela
    tabela = {
        'periodos': periodo,
        'juros': juros_periodo,
        'amortizacao': amortizacao_periodo,
        'pagamento': pagamento_periodo,
        'divida': divida_periodo
    }



    # Cria o DataFrame usando o dicionário
    df = pd.DataFrame(tabela)

    return df.round(2)
def parcela (principal,juros,periodos, uniformidade=1):
    parcela = principal * (juros * ((1 + juros)**periodos)) / ((1 + juros)**periodos - 1)
    return parcela



