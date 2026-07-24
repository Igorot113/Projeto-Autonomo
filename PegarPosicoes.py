import time
import pyautogui
import re

opcao = input("Salvamos as posições do seu monitor caso queira refazer digite ['y'] ou ['n']")
if(opcao == 'y'):
    print("Posição da aba Encerrantes:")
    time.sleep(5)
    x1,y1 = pyautogui.position()
    print(x1,y1)
    input("Precione enter")
    print("Posicao do placeholder")
    time.sleep(5)
    x2,y2 = pyautogui.position()
    print(x2,y2)
    input("Precione enter")
    print("Posição Encerrante")
    time.sleep(5)
    x3,y3 = pyautogui.position()
    print(x3,y3)
    input("Precione enter")
    print("Posição do botão Alterar Encerrante")
    time.sleep(5)
    x4,y4 = pyautogui.position()
    print(x4,y4)
    input("Precione enter")
    print("Posição do botão Pegar o valor correto (seta para baixo)")
    time.sleep(5)
    x5,y5 = pyautogui.position()
    print(x5,y5)
    input("Precione enter")

    with open("posicoes.txt","w") as f:
        f.write(f"{x1},{y1}\n")
        f.write(f"{x2},{y2}\n")
        f.write(f"{x3},{y3}\n")
        f.write(f"{x4},{y4}\n")
        f.write(f"{x5},{y5}\n")
else:
    with open("posicoes.txt","r",encoding="utf-8",errors="ignore") as f:
        linhas = f.readlines()

    x1,y1 = map(int,re.findall(r"\d+",linhas[0]))
    x2,y2 = map(int,re.findall(r"\d+",linhas[1]))
    x3,y3 = map(int,re.findall(r"\d+",linhas[2]))
    x4,y4 = map(int,re.findall(r"\d+",linhas[3]))
    x5,y5 = map(int,re.findall(r"\d+",linhas[4]))