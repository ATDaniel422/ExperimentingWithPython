def dogYears(humYears):
    return int(humYears) * 7

print('Hello, What is your name?')
name = input()
print('Hello, ' + name + ', what is your dog\'s name?')
petName = input()
print('How old is ' + petName + '?')
petAge = input()
print(name + ', your dog, ' + petName + ' is ' + str(dogYears(petAge)) + ' years old in dog years')
