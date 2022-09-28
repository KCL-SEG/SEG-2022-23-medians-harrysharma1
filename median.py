"""Median calculator.
https://www.w3schools.com/python/python_lists.asp was used for help with list syntax
"""
def median(number):
     n=0
     number.sort()
     n=len(number)
 
     if(n%2==0):
         x=n//2
         mid1=number[x]
         mid2=number[x-1]
         median=(mid1+mid2)/2
         print(f'The median is {median}')
     else:
        middle=n//2
        print (f'The median is {number[middle]}')
        
         
  
    

    
    
    

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
median(numbers)



