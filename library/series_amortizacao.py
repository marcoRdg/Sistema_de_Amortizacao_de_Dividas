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
        't': periodo,
        'j_t': juros_periodo,
        'a_t': amortizacao_periodo,
        'r_t': pagamento_periodo,
        'p_t': divida_periodo
    }

    # Cria o DataFrame usando o dicionário
    df = pd.DataFrame(tabela)

    return df

