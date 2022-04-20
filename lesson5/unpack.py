fruits = ('🍑', '🍌', '🍏')
# fruits = ['🍑', '🍌', '🍏']
peach, banana, apple = fruits

print(peach)
print(banana)
print(apple)

fruits = ('🍑', '🍌', '🍏', '🍊')
peach, banana, apple, _ = fruits

print(peach)
print(banana)
print(apple)

peach, banana = banana, peach
peach, banana = (banana, peach)
print(peach, banana)
fruits = banana, peach
print(fruits)
