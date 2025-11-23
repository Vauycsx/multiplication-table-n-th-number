name = input('Your name: ')
print("hello", name)

num = int(input('enter an number: '))

for i in range(1,11):
    result = num * i
    print(num,'*', i, '=', result)

print(name, 'this is your multiplication table for', num)