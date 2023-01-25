money = int(input('Введите сумму депозита: '))
deposit = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

for values in per_cent.values():
    deposit.append(int(values * money / 100))

# в ТЗ не сказано, что deposit необходимо выводить на экран, поэтому закомментил
# print(deposit)

print(f'Максимальная сумма, которую вы можете заработать — {max(deposit)}')
