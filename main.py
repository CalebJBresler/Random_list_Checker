import random
from logic import check

Rnum = [5, 1, 2, 1]
final = 1

c = 0
while final == 1:
    final, posit = check(Rnum)
    if final == 1:
        c += 1
        Rnum[posit] = random.randint(0,5)
        final, posit = check(Rnum)

print(f"Rnum:{Rnum}; {c}")
