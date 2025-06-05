# Simula funil de conversão no terminal

stages = ['Visit', 'Signup', 'Purchase']
values = [1000, 400, 150]

for i, val in enumerate(values):
    print(f"{stages[i]}: {'■' * (val // 10)}")
