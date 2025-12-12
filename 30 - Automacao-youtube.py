import pyautogui
import os 
import time 
import pyperclip
import webbrowser

os.system("cls")

texto_pesquisa = "Copa do mundo"

#1 PASSO  - Abrir o navegador e acessar o site do youtube
webbrowser.open("https://www.youtube.com")
time.sleep(4)

#2 PASSO -  Mover o mouse até a barra de pesquisa do youtube e clicar
pyautogui.moveTo(709, 97, duration=5)
pyautogui.click(709, 97) 


#3 PASSO - Digitar o texto na barra de pesquisa
pyperclip.copy(texto_pesquisa) 
pyautogui.hotkey("crtl", "v")
#pyautogui.write("Aulas Python")
pyautogui.press("enter")

#4 PASSO - Clicar em um determinado video
#Scroll para cima = numeros positivos 
#Scrool para baixo = números negativos
time.sleep(4)
pyautogui.scroll(-2700)

#5 PASSO - Mover o mouse até o video e clicar 
pyautogui.moveTo(681, 617, duration=3)
pyautogui.click(681, 617)


print("Você tem 5 segundos para posicionar o mouse em algum lugar na tela")
time.sleep(5)
print(f"Posição atual do mouse: {pyautogui.position()}")