# # Recusion vs iterative method 

# # Factorial calculation using the iterative approach

# def factorial_iterative(n):
#     fac =  1 
#     for i in range(n):  # It gets started from zero ( THE INDEX )
#         fac = fac * (i+1) 
#     return fac 

# number = int(input("Enter the number ")) 
# print("The value of iterative factorial is " , factorial_iterative(number))



# # Factorial calculation using the recursive approach

# def factorial_recursive(n):
#     if n == 1 or n == 0 : 
#         return 1 
#     else : 
#         return n * factorial_recursive(n-1)
    

# print("The value of RECURSIVE factorial is " , factorial_recursive(number))


# Applying the recursive concept to fabonacci series 
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13( adding the previous two numbers )

num = int(input("Enter the num"))


def febo(n):
    if n == 1 :
        return 0 
    elif n == 2 : 
        return 1 
    else :
        return febo(n-2) + febo(n-1)

print("The value of series term is " , febo(num)) 




# __name__ ( this is underscore underscore name and then again underscore underscore )

# PRO-TIP 
# Make your functions in one file and use them by importing it to your new script file by
# making use of import function 
# So all function in one place and access them from there . 

