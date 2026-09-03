tea_types = ('Black','Green','Oolong')

print(len(tea_types))

moreTea = ('Herbal','Earl Grey')

all_tea = moreTea + tea_types

print(all_tea)

tea_types = all_tea
print(tea_types.count('Herbal'))
print(tea_types)

(herbal,earl) = moreTea
print(herbal)
print(earl)