# Requisitos - Venda com desconto
Arquivo do programa: vendas.py

## RF01 - Receber o valor da venda
Solicitar ao usuário: "Digite o valor da venda: ".
Receber um valor numérico positivo.

## RF02 - Exibir desconto e total
Chamar calcular_desconto(valor_venda) e obter o desconto.
Exibir o desconto e o total a pagar com duas casas decimais.

## RN01 - Aplicar o desconto
Aplicar 10% quando o valor da venda for igual ou superior a R$ 50.
Para valor menor que R$ 50, o desconto deve ser zero.

## RN02 - Calcular o total
O total a pagar é o valor da venda menos o desconto.

## CA01 - Abaixo do limite
Entrada: 49.99. Desconto: R$ 0.00. Total: R$ 49.99.

## CA02 - No limite
Entrada: 50. Desconto: R$ 5.00. Total: R$ 45.00.

## CA03 - Acima do limite
Entrada: 70. Desconto: R$ 7.00. Total: R$ 63.00.
