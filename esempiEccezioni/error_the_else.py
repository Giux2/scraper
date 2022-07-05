def linux_interaction():
    print('Doing something.')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Stampo la condizione else')