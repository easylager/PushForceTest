print(list_testing)
pop_one = list_testing.pop(0)
print(list_testing)
print(f'pop_one:{pop_one}')
print(type(item for item in list_testing))

generator_testing = (item for item in list_testing)

git = lambda a: a+1
