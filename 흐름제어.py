name=str(input("What is your name? : "))

if name=="bird":
    print("I could fly to you")
else:
    print("I could walk to you")

num = int(input("Multiplicaition table of : "))
for i in range(1, 10):
    print(num, 'x', i, '=', num*i)

num = int(input("Multiplicaition table of : "))
i=1
while i<10:
    print(num, 'x', i, '=', num * i)
    i+=1

print('\n')
print('구구단')
for i in range(2, 10):
    print(i, '단')
    for j in range(1, 10):
        print("%2d x %2d = %4d" %(i, j, i*j))
    print('\n')

