""" Напишите программу для проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """

print('Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')

claim_1 = False
claim_2 = False
for x in range(2):
    for y in range(2):
        for z in range(2):
            claim_1 = not (bool(x) or bool(y) or bool(z))
            claim_2 = not bool(x) and not bool(y) and not bool(z)
            print(f'При значении предикат X, Y, Z = [{bool(x)}, {bool(y)}, {bool(z)}]', end=', ')
            print(f'утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z = {claim_1 == claim_2}')