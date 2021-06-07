
print("Enter Number to check of prime or not")

a = int(input("Enter a Number:"))
Prime  = True
for b in range (2,a):
    if(a%b  == 0):
       Prime = False
       break
if Prime:
  print("This number is prime") 
else:
  print("This number is not prime")