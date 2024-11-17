from fake_math import divide as fake
from dz.true_math import divide as true

result1 = int(fake(35, 5))
result2 = fake(321, 0)
result3 = int(true(42, 7))
result4 = true(14214, 0)

print(result1)
print(result2)
print(result3)
print(result4)

