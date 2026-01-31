p = input('Introduce una palabra: ')
for v in ['a', 'e', 'i', 'o', 'u']: print(f'La vocal {v} aparece: {p.count(v)} {"vez" if p.count(v) == 1 else "veces"}')