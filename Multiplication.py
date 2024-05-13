import random
Passed , Failed, Missed = 0, 0, 0

print( "Test Your Multiplication Skills :)" )
try:
    n = int(input("Enter the number of times you want to be tested: "))
except ValueError:
    n = 0
    print("Enter the input")
    n = int(input("Enter the number of times you want to be tested: "))

for i in range(n):
    first = random.randint(10, 50)
    second = random.randrange(20, 60)
    print(first, "X", second, "=", end = " " )

    try:
        ans = int(input())
    
    except ValueError:
        Missed += 1
        ans = 0
    
    if(ans == first * second):
        continue
    else:
        Failed += 1
        
print('No of questions attempted:', n - Missed)
print('Your score is :', n - Failed)
print('Missed ones:', Missed)
        



    
    
    


