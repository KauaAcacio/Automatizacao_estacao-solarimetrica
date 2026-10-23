###### COLETANDO OS DADOS E ARMAZENANDO EM UMA VARIÁVEL ######

#---------------------BIBLIOTECAS UTILIZADAS---------------------#
import time
from datetime import datetime
import random

#-----------------------FUNÇÕES UTILIZADAS-----------------------#

#Para coletar a útima linha
def coletar_ultima_linha(nome_arquivo):
    file_ultima_linha = open(nome_arquivo, "r", encoding="UTF-8")
    contador = 0
    last_line = ""
    for i in reversed(file_ultima_linha.readlines()):
        if contador == 1:
            break
        else:
            last_line = i
        contador += 1
    file_ultima_linha.close()
    return last_line

#Para pegar uma informação em alguma linha (linha, posição da informação)
def dado_especifico(linha, n):
    lista_dados = linha.split(sep=",")
    lista_dados[0] = lista_dados[0].replace('"', "")
    lista_dados[1] = lista_dados[1].replace('"', "")
    informacao_desejada = lista_dados[n-1]
    return informacao_desejada

#-------INFORMAÇÕES SOBRE A REPETIÇÃO E O INTERVALO DE TEMPO-------#

nome_arquivo = "/Users/kauad/OneDrive/Documentos/Universidade Federal de Minas Gerais/CEMTEC/Automatizacao_estacao_solarimetrica/simulation/simulatedData.txt"

#Quantos segundos total é para o programa rodar
while True:
    try:
        tempo_total = int(input("Digite a quantidade de segundos que o programa funcionará (s): "))
        break
    except:
        continue

#Intervalo de tempo para cada medição
while True:
    try:   
        intervalo_tempo = int(input("Digite a quantidade de segundos de espera para cada repetição (s): "))
        break
    except:
        continue

#Quantidade de laços de repetição
quantidade_lacos = round(tempo_total/intervalo_tempo)

#-------------COLETA DOS DADOS E INSERÇÃO NA SIMULAÇÃO-------------#

#Record atual antes de iniciar o laço de repetição
ultima_linha = coletar_ultima_linha(nome_arquivo)
ultimo_record = int(dado_especifico(ultima_linha, 2))

#Inicializar as variáveis
records_lista = list()

for i in range(quantidade_lacos):
    
    #Timestamp
    data_e_hora = str((datetime.now()).replace(microsecond=0))

    #Record
    record = ultimo_record + 1
    ultimo_record = record
    records_lista.append(record)


    #Temp_Ar
    temperatura_do_ar = float(random.gauss(25.46, 1))
    temperatura_do_ar = max(19.5, min(temperatura_do_ar, 33.6))
    temperatura_do_ar = round(temperatura_do_ar, 1)
    str(temperatura_do_ar)

    #Humid_Ar
    humidade_do_ar = float(random.gauss(63.71, 2))
    humidade_do_ar = max(45, min(humidade_do_ar, 80))
    humidade_do_ar = round(humidade_do_ar, 1)
    str(humidade_do_ar)

    #Ponto_Orvalho_act
    ponto_de_orvalho = float(random.gauss(17.59, 1))
    ponto_de_orvalho = max(11.2, min(ponto_de_orvalho, 22))
    ponto_de_orvalho = round(ponto_de_orvalho, 1)
    str(ponto_de_orvalho)

    #Press_Ar
    pressao_do_ar = float(random.gauss(923, 1))
    pressao_do_ar = max(920, min(pressao_do_ar, 927))
    pressao_do_ar = round(pressao_do_ar, 1)
    str(pressao_do_ar)

    #Vento_avg
    velocidade_do_vento = float(random.gauss(1.5288262540652409, 00.1))
    velocidade_do_vento = max(0.0, min(velocidade_do_vento, 1000.0))
    velocidade_do_vento = round(velocidade_do_vento, 1)
    str(velocidade_do_vento)

    #Dir_Vento_act
    direcao_do_vento = float(random.gauss(112.24947217085317, 2))
    direcao_do_vento = max(0.0, min(direcao_do_vento, 1000.0))
    direcao_do_vento = round(direcao_do_vento, 1)
    str(direcao_do_vento)

    #Intens_Chuva
    intensidade_da_chuva = float(random.gauss(0.06516907344390402, 0.005))
    intensidade_da_chuva = max(0.0, min(intensidade_da_chuva, 48.4))
    intensidade_da_chuva = round(intensidade_da_chuva)
    str(intensidade_da_chuva)

    #Chuva_Diff
    diferenca_de_chuva = float(random.gauss(0.00018075467104157125, 0.005))
    diferenca_de_chuva = max(0.0, min(diferenca_de_chuva, 0.23))
    diferenca_de_chuva = round(diferenca_de_chuva)
    str(diferenca_de_chuva)

    #Chuva_Diff_Tot
    total_acumulado_da_diferenca = float(random.gauss(0.00018075467104157125, 0.005))
    total_acumulado_da_diferenca = max(0.0, min(total_acumulado_da_diferenca, 0.23))
    total_acumulado_da_diferenca = round(total_acumulado_da_diferenca)
    str(total_acumulado_da_diferenca)

    #-------------------JUNTAR OS DADOS EM UMA LINHA------------------#

    linha_nova = f'\n"{data_e_hora}",{record},{temperatura_do_ar},{humidade_do_ar},{ponto_de_orvalho},{pressao_do_ar},{velocidade_do_vento},{direcao_do_vento},{intensidade_da_chuva},{diferenca_de_chuva},{total_acumulado_da_diferenca}'

    #-------------------ADICIONAR A LINHA NO ARQUIVO------------------#

    file = open(nome_arquivo, "a", encoding="UTF-8")
    file.write(linha_nova)
    file.close()

    #-----------------CONFIRMAÇÃO DO LAÇO DE REPETIÇÃO----------------#
    print(f"O registro de número {record} foi adicionado com sucesso! ✔️")

    time.sleep(intervalo_tempo)

#---------------------MENSAGEM DE FIM DA EXECUÇÃO---------------------#
print("------------"*5)
print("PROGRAMA FINALIZADO ✅")
print(f"AS GRAVAÇÕES ADICIONADAS FORAM: {records_lista}")
print(f"TOTAL DE GRAVAÇÕES ADICIONADAS: {len(records_lista)}")