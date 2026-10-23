# ==========================================
#              MAIN PROGRAM
# ==========================================

# ====== Part 1: Importing Libraries =======

#from fileOpenning.nameFile import 


# ========== Part 2: Main Program ==========

# Input Of Important Variables
SIMULATED_STATION_FILE_NAME = "/Users/kauad/OneDrive/Documentos/Universidade Federal de Minas Gerais/CEMTEC/Automatizacao_estacao_solarimetrica/simulation/simulatedData.txt"

# Number Of Checks
while True:
    try:
        NUMBER_OF_CHECKS = int(input("Enter the number of program checks: "))
        break
    except:
        continue

# Waiting Time
while True:
    try:
        WAITING_TIME = int(input("Enter the waiting time: "))
        break
    except:
        continue

# Start Checks
for specific_verification_number in range(NUMBER_OF_CHECKS):

    # File Opening
    open_file(SIMULATED_STATION_FILE_NAME)

# PROCURAR SABER SE É POSSÍVEL EU USAR UMA FUNÇÃO DESSE JEITO PARA ABRIR UM ARQUIVO