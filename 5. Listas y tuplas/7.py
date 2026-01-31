import string
abc = [x for x in string.ascii_lowercase]
abc.insert(abc.index('n')+1,'ñ')
abc = [x for i, x in enumerate(abc) if i % 3 != 0]