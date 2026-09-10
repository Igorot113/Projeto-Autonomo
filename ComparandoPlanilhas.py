from openpyxl import Workbook, load_workbook
from pathlib import Path

PASTA_PROJETO = Path(__file__).parent / "Planilhas"

datas =  []
x = 1
for x in range(3):
    dia = input(f"Digite a data{x} dos dias das planilhas ex:(xx/xx/xxxx): ")
    datas.append(dia)

planilhas = [
    {"dia":f"{datas[0]}","arquivo":"Comparação de Encerrantes.xlsx"},
    {"dia":f"{datas[1]}","arquivo":"Comparação de Encerrantes2.xlsx"},
    {"dia":f"{datas[2]}","arquivo":"Comparação de Encerrantes3.xlsx"}
]

colunas = 'F'
linha_inicio = 6
linha_fim = int(input("Digite a ultima linha de dados da planilha: "))

wbs = [load_workbook(PASTA_PROJETO / item["arquivo"], data_only=True) for item in planilhas]
abas = [wb.active for wb in wbs]

wb_consolidado = Workbook()
aba_destino = wb_consolidado.active
aba_destino.title = "Consolidado"

aba_destino.append([
    "Linha Original",
    f"Valor ({planilhas[0]['dia']})",
    f"Valor ({planilhas[1]['dia']})",
    f"Valor ({planilhas[2]['dia']})",
])

faixa1 = abas[0][f"{colunas}{linha_inicio}:{colunas}{linha_fim}"]
faixa2 = abas[1][f"{colunas}{linha_inicio}:{colunas}{linha_fim}"]
faixa3 = abas[2][f"{colunas}{linha_inicio}:{colunas}{linha_fim}"]

for c1, c2, c3 in zip(faixa1, faixa2, faixa3):
    linha = c1[0].row

    val1 = float(c1[0].value or 0)
    val2 = float(c1[0].value or 0)
    val3 = float(c1[0].value or 0)

    diferenca = max(val1,val2,val3) - min(val1,val2,val3)

    aba_destino.append([
        linha,
        val1,
        val2,
        val3,
    ])

saida = PASTA_PROJETO / "Consolidada3Planilhas.xlsx"
wb_consolidado.save(saida)
print(f"Planilha consolidada gerada com sucesso")
