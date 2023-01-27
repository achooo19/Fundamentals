import math

numb_of_people = int(input())
capacity = int(input())

course = math.ceil(numb_of_people / capacity)

print(course)