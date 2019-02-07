import random

a = []
q = ['O', 'P', 'f', 'w']
for i in range(22):
    a.append(q[random.randrange(0, 4)])
print(''.join(a))
