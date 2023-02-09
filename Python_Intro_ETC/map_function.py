my_list = [1, 2, 3, 4, 5]
my_list1 = ["a", "b", "c"]
# classic way
new_list = []
for _ in my_list:
    new_list.append(_*_)

# list comprehension
result = [x*x for x in my_list]
print(result)

# map() / lambda variante
new_list3 = list(map(lambda y: y.upper(), my_list1))
print(f"new char: {new_list3=} ")
