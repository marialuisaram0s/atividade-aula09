# Atividade individual - Aula 9
# Complete a função antes de entregar a primeira versão.

def calcular_desconto(valor_venda):
    if valor_venda >= 60:
        return valor_venda * 0.10
    return 0.0


valor_venda = float(input("Digite o valor da venda: "))
desconto = calcular_desconto(valor_venda)
total = valor_venda - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
