fruits = ['π', 'π', 'π', 'π', 'π', 'π']
smoothie = fruits
smoothie.remove('π')
smoothie.remove('π')
smoothie.remove('π')

print(smoothie)  # ['π', 'π', 'π']
print(fruits)  # ['π', 'π', 'π']
print(smoothie == fruits)  # True
print(smoothie is fruits)  # True

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
b = a
print(a is b)  # True

fruits = ['π', 'π', 'π', 'π', 'π', 'π']
smoothie = fruits.copy()
smoothie = fruits[::]  # ΡΠ΅Π·ΡΠ»ΡΡΠ°Ρ ΡΠΎΠΉ ΡΠ°ΠΌΠΈΠΉ
smoothie.remove('π')
smoothie.remove('π')
smoothie.remove('π')

print(smoothie)  # ['π', 'π', 'π']
print(fruits)  # ['π', 'π', 'π', 'π', 'π', 'π']
print(smoothie == fruits)  # False
print(smoothie is fruits)  # False
