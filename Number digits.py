'''
Find the number of digits in a given integer
'''

num = int(input("Enter the number :"))  # Enter the number using keyboard

div = 1  # Start with 1 the first power of 10 in the integer division
while num// 10**div != 0:     # Check the condition: is the quotient of the # integer division num divided by 10 to the power of div
                           # while loop it keeps executing the loop body as long as the condition is true.
                          # integer division num divided by 10 to the power of div
                           # not equal to zero?
    div = div + 1          # If yes execute the loop body

print("the number :", num, "has ", div, "digits")       # if no, get out of the loop and print
                        # the message


