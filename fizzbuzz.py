def fizzbuzz():

    for num in range(1, 100):

        if num % 15 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)


fizzbuzz()
