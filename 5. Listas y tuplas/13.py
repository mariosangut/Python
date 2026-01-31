n = input('Dame una lista de numeros separados por (,): ')
n = [float(a.strip().replace(' ', '')) for a in n.split(',')]
media = sum(n) / len(n)
desv = 0
print(f'Media: {media}')
for num in n: desv += ((num - media) ** 2) / sum(n)
print(f"Desviación típica: {(desv ** 0.5):0.2f}")