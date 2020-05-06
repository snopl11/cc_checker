loop = True


def valid(number):
    length = len(str(number))
    i = 0
    sum1 = 0
    sum2 = 0
    n = str(number)
    while i < length:
        if i % 2 == 0:
            temp = int(n[i]) * 2
            temp = str(temp)
            if len(temp) == 2:
                k = int(temp[0]) + int(temp[1])
            else:
                k = int(temp[0])
            sum1 = sum1 + k
        else:
            sum2 = sum2 + int(n[i])
        i += 1
        
    if ((sum1+sum2) % 10 == 0):
        return True
    else:
        return False

                  
while loop:
    loop = False
    num = input("Enter Number: ")
    if valid(num) is True:
        if num[0:2] == ["34", "37"] and len(num) == 15:
            print("AMEX\n")
        elif num[0:2] in ["51", "52", "53", "54", "55"] and len(num) == 16:
            print("MASRECARD\n")
        elif num[0] == "4" and len(num) == 16:
            print("VISA\n")    
        else:
            print("Invalid")
            loop = True
    else:
        print("Invalid")
        loop = True
