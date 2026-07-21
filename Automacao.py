import pyautogui
import time
from openpyxl import load_workbook
import pyperclip
from decimal import Decimal, ROUND_HALF_UP
import PegarPosicoes as pos
# shift +  tab ao invez de dar um salto para frente voce da um salto para traz

wb = load_workbook("C:/Users/Master-Data/Desktop/ProjetoAutonomo/ProjetoAutonomo/ProjetoAutonomo/Comparação de Encerrantes.xlsx")
aba = wb.active

lista_bicos = []
lista_nomes = []
lista_diferenca = []
lista_bicos_nomes = []

for linha in aba['A6':'A23']:
    celula = linha[0]
    lista_bicos.append(celula.value)
for linha in aba['B6':'B23']:
    celula = linha[0]
    lista_nomes.append(celula.value)
for linha in aba['F6':'F23']:
    celula = linha[0]
    lista_diferenca.append(celula.value)

print(lista_bicos)
print()
print(lista_nomes)
print()
print(lista_diferenca)
print()
for item_x,item_y in zip(lista_bicos,lista_nomes):
    combinacao = f"{item_x}-{item_y}"
    lista_bicos_nomes.append(combinacao)

print(lista_bicos_nomes)
bicoAtual = 0 #padrao é 0

pyautogui.moveTo(pos.x1,pos.y1,1.00) # arrumar um jeito de resolver isso clicar em encerrantes em diferentes tipos de telas (95,41,1.00)
pyautogui.click()
pyautogui.moveTo(pos.x2,pos.y2,1.00) # arrumar um jeito de resolver isso clicar em nomes em diferentes tipos de telas (232,108,1.00)
pyautogui.click()

while (bicoAtual < int(lista_bicos[-1])):
    pyautogui.click()
    time.sleep(1)
    pyautogui.write(lista_bicos_nomes[bicoAtual])
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(pos.datas)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(pos.datas)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    # pyautogui.moveTo(238,226)
    pyautogui.moveTo(pos.x3,pos.y3)
    print("Encerrante.")
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # pyautogui.moveTo(2265,976)
    pyautogui.moveTo(pos.x4,pos.y4)
    print("Botao Alterar Encerrante")
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # pyautogui.moveTo(1709,438)
    pyautogui.moveTo(pos.x5,pos.y5)
    print("Seta para baixo")
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    print("Bico atual = ",bicoAtual)
    print("<=====>")
    encerranteInicial = pyperclip.paste().replace(",",".")
    print(encerranteInicial) # correto
    print("<=====>")
    time.sleep(1)
    valorCelula = Decimal(lista_diferenca[bicoAtual])
    valorCelulaFormatado = valorCelula.quantize(Decimal('0.000'),rounding=ROUND_HALF_UP)
    consertoDoEncerrante = valorCelulaFormatado + Decimal(encerranteInicial)
    formatadoConsertoDoEncerrante = consertoDoEncerrante.quantize(Decimal('0.000'),rounding=ROUND_HALF_UP)
    print(consertoDoEncerrante) # 253337,1
    print("lista_diferenca")
    print(Decimal(lista_diferenca[1]))
    print("Formatado")
    print(formatadoConsertoDoEncerrante)
    print("<=====>")
    time.sleep(1)
    pyautogui.write(str(formatadoConsertoDoEncerrante))
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write("AJUSTE ENCERRANTE")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write('1')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write("DERICK")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write("14082324000120") # 14082324000120
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write("05401287674") # 05401287674
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.moveTo(pos.x1,pos.y1,1.00)
    pyautogui.moveTo(pos.x2,pos.y2,1.00)
    time.sleep(5)
    bicoAtual += 1