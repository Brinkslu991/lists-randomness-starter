# Lucas Brinks
# 10/22/24
# randomnes
import random as rd
colors = ['red', 'blue', 'green', 'yellow','crimson']

randomcolor = rd.randrange(0,len(colors)-1)

print(colors[randomcolor])

animals = ['Wolf', 'Bear', 'Lion', 'Bull', 'Rhino']

for i in range(3):
    rananimals = rd.randrange(0,len(animals)-1)
    print(animals[rananimals])

numbers = [10, 14, 27, 98, 44, 36, 84]

rdnumbers = rd.randrange(0,len(numbers)-1)

print(numbers[rdnumbers])

fruits = ['cherry', 'apple', 'banana', 'grape']

ranfruit = rd.randrange(0,len(fruits)-1)

print(fruits[ranfruit])

names = ['Joshua', 'Thayer', 'Apollos', 'Bryce', 'Isaac']

for i in names:
    print(f'{i} has a score of {rd.randint(0,100)}')


movies = ['How to Train Your Dragon', 'Transformers', 'Interstellar', 'Deadpool', 'The Dark Knight']

ranmovies = rd.randint(0,len(movies)-1)

print(movies[ranmovies])