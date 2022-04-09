'''
Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
'''

def narcissistic( value ):
    
    value_list=list(str(value))
    sum=0
    for i in range(len(value_list)):
        sum+=int(value_list[i])**len(value_list)
        
    if sum==value:
        print (True)
    else:
        print (False)

narcissistic(7)