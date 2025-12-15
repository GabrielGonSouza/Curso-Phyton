import pyautogui
import time
import webbrowser
import pandas as pd
import os

# --- CONFIGURAÇÕES GLOBAIS ---
pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

# --- DADOS ---
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    EXCEL_FILE_PATH = os.path.join(script_dir, 'clientes.xlsx')
    df = pd.read_excel(EXCEL_FILE_PATH)
except NameError:
    EXCEL_FILE_PATH = 'clientes.xlsx'
    try:
        df = pd.read_excel(EXCEL_FILE_PATH)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{EXCEL_FILE_PATH}' não foi encontrado.")
        exit()
except FileNotFoundError:
    print(f"Erro: O arquivo '{EXCEL_FILE_PATH}' não foi encontrado.")
    exit()

# --- COORDENADAS ---
COORD_URL = 'https://practice.expandtesting.com/register'
COORD_USERNAME = (815, 612)
COORD_PASSWORD = (843, 698)
COORD_CONFIRM = (854, 779)
COORD_REGISTER = (877, 817)

# --- FUNÇÃO ---
def preencher_registro(username, password):
    pyautogui.click(COORD_USERNAME)
    pyautogui.write(username, interval=0.05)
    time.sleep(1)

    pyautogui.click(COORD_PASSWORD)
    pyautogui.write(password, interval=0.05)
    time.sleep(1)

    pyautogui.click(COORD_CONFIRM)
    pyautogui.write(password, interval=0.05)
    time.sleep(1)

    pyautogui.click(COORD_REGISTER)
    time.sleep(3)

# --- EXECUÇÃO ---
print("Iniciando a automação...")
webbrowser.open(COORD_URL)
time.sleep(5)

print("Você tem 5 segundos para posicionar o mouse...")
time.sleep(5)
print(f"Posição atual do mouse: {pyautogui.position()}")

for index, linha in df.iterrows():
    username = linha.get('Usuário')
    password = linha.get('Senha')

    if pd.isna(username) or pd.isna(password):
        print(f"Linha {index} ignorada (dados vazios)")
        continue

    print(f"Processando registro: {username}")
    preencher_registro(username, password)

print("=================================================================")
print("Automação concluída! Todos os registros foram processados!")
