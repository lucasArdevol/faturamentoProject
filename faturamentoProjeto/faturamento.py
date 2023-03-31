import json

with open('faturamento.json') as file:
    faturamento = json.load(file)

dias = len(faturamento)
soma = sum(faturamento.values())
media = soma / dias

menor = min(faturamento.values())
maior = max(faturamento.values())

dias_acima_media = sum(1 for f in faturamento.values() if f > media)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")
