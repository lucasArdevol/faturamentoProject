import json
from random import randint

faturamento = {}

for dia in range(1, 31):
    if randint(0, 1): # 50% de chance de ter faturamento nesse dia
        faturamento[dia] = round(randint(1000, 50000) + randint(0, 99) / 100, 2)

with open('faturamento.json', 'w') as file:
    json.dump(faturamento, file)