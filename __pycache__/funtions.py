# write a function to calculate Area
# and perimeter of a rectangle

# def peri_rect(lenght,breath):
#     peri =2*(lenght+breath)
#     area= lenght*breath
#     print(f'the perimeter of a rectangle is {peri} and the area is {area} given lenght as {lenght} and breath as {breath}')
# peri_rect(int(input('input your lenght')),int(input('input your breath')))

# write a function that accepts a number and prints out 
# the fibbonacci sequence that matches the number
# fib (100)
# a fibboacci sequence is the integer sequence of 0,1,1,2,3,5,8,13,21,34

# def fib(n):
#     first_num=0
#     sec_num=1
#     print(first_num)
#     print(sec_num)
#     nxt_num=first_num+sec_num
#     print ( nxt_num)
#     for i in range(4,n):
        
#         first_num=sec_num
#         sec_num= nxt_num
#         nxt_num= first_num+sec_num
# terms = int(input('enter the no of terms'))
# fib(terms)


# write a function that accepts
# a number and prints its factorial

# import math
# def factorial():
#     num=int(input('input the number you want to see the factors'))
#     print(f'the factorial of num is {math.factorial(num)}')
# factorial()
                    # or
                    
def factorial(n):
    for i in range(1,n):
        n*=i
    print(n)
factorial(5)
