from datetime import date

register = {'name': [], 'gender': [], 'year': []}
woman30 = []
men = []
cont = sum = average = 0
while True:
    finish = input('Do you wish add anyone? [Y/N]: ')
    if finish in 'Nn':
        print('~' * 30)
        print('       Shutting down...')
        print('~' * 30)
        break
    if finish not in 'Yy':
        print('Type Y for YES or N for NOT.')
        continue

    name = input('Enter name: ').capitalize()
    gender = input('Choose the gender [M/F]: ').upper()
    year = int(input('Enter the year of birth: '))
    print(f'{date.today().year-year} anos')
    register['name'].append(name)
    register['gender'].append(gender)
    register['year'].append(year)
    age = (date.today().year) - year
    if (age < 30) and gender == 'F':
        woman30.append([name])
    cont += 1
    sum += age
    average = sum/cont
for g, s in enumerate(register[1]):
    print(g)

    #  men.append([name])
    # if (age > average) and gender == 'M':


print(f'Total records made: {cont}')
print(f'The average age of this group is {average:0.0f} ')
print(f'Women under 30: {(woman30)}')
print(f'Men over {average:0.0f} years: {(men)}')
print(register)
