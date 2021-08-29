'''
Create a function named divisors/Divisors that takes an integer n > 1 and 
returns an array with all of the integer's divisors(except for 1 and the 
number itself), from smallest to largest. If the number is prime return 
the string '(integer) is prime' (null in C#) (use Either String a in 
Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''

def divisors(n):
    arr = []
    c = 0
    # m = n+1
    for i in range(1,n):
        if (n%i==0):
            arr.append(i)
            c+=1
    if (c==1):
        print(f"{n} is prime")
    else:
        arr.pop(0)
        print(arr)
    return 

divisors(12)
divisors(25)
divisors(13)



