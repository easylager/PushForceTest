list_testing = list((2, 3, 5, 5))
print(list_testing)
pop_one = list_testing.pop(0)
print(list_testing)
print(f'pop_one:{pop_one}')
print(type(item for item in list_testing))

generator_testing = (item for item in list_testing)



if __name__ == "__main__":
    gen_func = generator_testing_function()
    a = next(gen_func)
    print(a)
    print(next(gen_func))
    print(next(gen_func))
