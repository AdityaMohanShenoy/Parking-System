n=range(1,2*10^5)  
for i in n:
     if i%3==0 and i%5==0:
         print("FizzBuzz")
     elif i%3==0:
         print("Fizz")
     elif i%5==0:
         print("Buzz")
     else:
         print(i) 