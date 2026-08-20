import pyautogui
import time
from openpyxl import load_workbook
import pyperclip
from decimal import Decimal, ROUND_HALF_UP
import PegarPosicoes as pos
from pathlib import Path
# shift +  tab ao invez de dar um salto para frente voce da um salto para traz
PASTA_PROJETO = Path(__file__).parent
CAMINHO_PLANILHA = PASTA_PROJETO / "Comparação de Encerrantes.xlsx"
wb = load_workbook(CAMINHO_PLANILHA)
aba = wb.active

lista_bicos = []
lista_nomes = []
lista_diferenca = []
lista_bicos_nomes = []
execelInicio = input("Qual é o numero da linha inicial dos dados na TABELA: ")
execelFim = input("Qual é o numero da linha final dos dados na TABELA: ")
datas = input("Digite a DATA que voce quer fazer o encerrante: ")
datas2 = input("Digite a DATA2 que voce quer fazer o encerrante: ")
nomeDoTecnico = input("Digite o nome do tecnico: ")
cnpj = input("Digite o cnpj: ")
cpf = input("Digite o cpf: ")

# Esse for e para pegar aquele valor da linha do execel que vamos pular.
opcaoDeQuererPularLinhas = input("Nesse excel possui linhas que vão ser ignoradas? (S/N): ").upper()
if(opcaoDeQuererPularLinhas == 'S'):
    lista_linhas_Execel_Ignoradas = []
    quantLinhasIgnoradas = int(input("Quantas linhas serao ignoradas: "))
    for i in range(quantLinhasIgnoradas):
        linhaIgnorada = int(input(f"Digite o  {i+1} número da linha do execel que vai ser ignorada: "))
        lista_linhas_Execel_Ignoradas.append(linhaIgnorada)

    print(lista_linhas_Execel_Ignoradas)
# Fim da lista das linhas ignoradas ================================

    for linha in aba['A'+execelInicio:'A'+execelFim]:
        for linhaIgnorada in lista_linhas_Execel_Ignoradas:
            if(linha == linhaIgnorada):
                break
        celula = linha[0]
        lista_bicos.append(celula.value)

    print(lista_bicos)

    for linha in aba['B'+execelInicio:'B'+execelFim]:
        for linhaIgnorada in lista_linhas_Execel_Ignoradas:
            if(linha == lista_linhas_Execel_Ignoradas):
                break
        celula = linha[0]
        lista_nomes.append(celula.value)

    print(lista_nomes)

    for linha in aba['F'+execelInicio:'F'+execelFim]:
        for linhaIgnorada in lista_linhas_Execel_Ignoradas:
            if(linha == lista_linhas_Execel_Ignoradas):
                break
        celula = linha[0]
        lista_diferenca.append(celula.value)

    print(lista_diferenca)

    #Aqui estou juntando dois array lista_bicos e lista_nomes formando isso por exemplo: 10-GASOLINA COMUM e coloando isso na lista (lista_bicos_nomes)
    for item_x,item_y in zip(lista_bicos,lista_nomes):
        combinacao = f"{item_x}-{item_y}"
        lista_bicos_nomes.append(combinacao)
    #Fim da junção das duas lista e formando outra lista ========================

    print(lista_bicos_nomes)
    
else:
    for linha in aba['A'+execelInicio:'A'+execelFim]:
        celula = linha[0]
        lista_bicos.append(celula.value)
    for linha in aba['B'+execelInicio:'B'+execelFim]:
        celula = linha[0]
        lista_nomes.append(celula.value)
    for linha in aba['F'+execelInicio:'F'+execelFim]:
        celula = linha[0]
        lista_diferenca.append(celula.value)

    #Aqui estou juntando dois array lista_bicos e lista_nomes formando isso por exemplo: 10-GASOLINA COMUM e coloando isso na lista (lista_bicos_nomes)
    for item_x,item_y in zip(lista_bicos,lista_nomes):
        combinacao = f"{item_x}-{item_y}"
        lista_bicos_nomes.append(combinacao)
    #Fim da junção das duas lista e formando outra lista ========================

bicoAtual = 0 #padrao é 0
input("Pronto para iniciar a automação ? (Dê Enter aqui)") # Uma trava aqui só para verificar se está tudo nos conformes (Caso não precise mais é só tirar)

# Automação começa aqui ============================
pyautogui.moveTo(pos.x1,pos.y1,1.00)
pyautogui.click()
pyautogui.moveTo(pos.x2,pos.y2,1.00)
pyautogui.click()

while (bicoAtual < int(lista_bicos[-1])):
    pyautogui.click()
    time.sleep(1)
    pyautogui.write(lista_bicos_nomes[bicoAtual],1.00)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(datas)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.write(datas2)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.moveTo(pos.x3,pos.y3)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(pos.x4,pos.y4)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(pos.x5,pos.y5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    encerranteInicial = pyperclip.paste().replace(",",".")
    time.sleep(1)
    valorCelula = Decimal(lista_diferenca[bicoAtual])
    valorCelulaFormatado = valorCelula.quantize(Decimal('0.000'),rounding=ROUND_HALF_UP)
    consertoDoEncerrante = valorCelulaFormatado + Decimal(encerranteInicial)
    formatadoConsertoDoEncerrante = consertoDoEncerrante.quantize(Decimal('0.000'),rounding=ROUND_HALF_UP)
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
    pyautogui.write(nomeDoTecnico)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(cnpj)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(cpf)
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