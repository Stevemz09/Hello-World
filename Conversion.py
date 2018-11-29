'''
Convert from F to C , and from C to F
'''
degree = input("Enter c for Celsius , or f for Fahreinheit :")
temperature = int(input(" Enter the temperature value :"))

if degree =='f':
    C = (temperature - 32)*5/9
    print(" The temperature in celsius is ", round(C))
elif degree == 'c':
    F = temperature*9/5 + 32
    print("The temperature in Fahreinheit is :",round(F))
else :
    print("There is no such type of degree like :", degree)

exit()