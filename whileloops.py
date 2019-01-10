'''
1) Swap two variables
'''
#a=5
#b=10
#print('a=',a,'b=',b)


# Create a temporary variable temp
#temp=a # Save the value of a in the temp variable
#a=b # a is getting the value in b
#b=temp


#print('The new variables a =',a,'b=',b)

# write all integers between 1 and 9 using a while loop

#x=1
#while x <10:
#    print(x, end=' ')
#    x=x+1
row=1
col=1

while row <10:
    while col<5:
        print(row, col, ' ',end='')
        col=col+1
    print()
    row=row+1
    col=1



# Fibonacci sequence
# 1,1,2,3,5,8,13,21,34,....

x=1
y=1
cont= 'c'

while cont=='c':
    print('A new Fibonacci is :', x+y)

    temp =x
    x=y
    y=y+temp
    cont=input('If you want another number press c, else press any other key')