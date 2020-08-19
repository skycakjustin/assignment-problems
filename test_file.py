
number = 5
twice_the_number = 10

print('testing on number {}...'.format(number))

assert twice_the_number == 2*number, 'twice_the_number is {} whereas it should be {}'.format(twice_the_number, 2*number)

print('PASSED')


