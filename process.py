def DecimalBinary(x):
    y=0
    l=[]
    z=''
    while x!=0:
        y=x%2
        x=x//2
        l.append(y)
        p=len(l)
    while p!=0:
        z=z+str(l[p-1])
        p=p-1
    return (z)

def BinaryDecimal(x):
    x=str(x)
    n=1
    total=0
    check=['1','0']
    for i in (x):
        if (i in check):
            y=int(i)*(2**((len(x)-n)))
            n=n+1
            total=total+y
            if n==len(x)+1:
                return (total)
        else:
            print("Please input a Valid Number")
            break

def DecimalOCtal(x):
    y=0
    l=[]
    z=''
    while x!=0:
        y=x%8
        x=x//8
        l.append(y)
        p=len(l)
    while p!=0:
        z=z+str(l[p-1])
        p=p-1
    return (z)

def OctalDecimal(x):
    x=str(x)
    n=1
    total=0
    check=['0','1','2','3','4','5','6','7']
    for i in (x):
        if (i in check):
            y=int(i)*(8**((len(x)-n)))
            n=n+1
            total=total+y
            if n==len(x)+1:
                return int(total)
        else:
            print(x," is not in Octal, Please input a Valid Number")
            break

def DecimalHex(x):
    y=0
    l=[]
    z=''
    while x!=0:
        y=x%16
        x=x//16
        if y>=10:
            if y==10:
                y='A'
            elif y==11:
                y='B'
            elif y==12:
                y='C'
            elif y==13:
                y='D'
            elif y==14:
                y='E'
            elif y==15:
                y='E'
        l.append(y)
    p=len(l)
    while p!=0:
        z=z+str(l[p-1])
        p=p-1
    return (z)

def HexDecimal(x):
    x=str(x)
    n=1
    total=0
    check=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in (x):

        if (i in check):
            if i == 'A':
                i = 10
            elif i == 'B':
                i = 11
            elif i == 'C':
                i = 12
            elif i == 'D':
                i = 13
            elif i == 'E':
                i = 14
            elif i == 'F':
                i = 15
            y=int(i)*(16**((len(x)-n)))
            n=n+1
            total=total+y
            if n==len(x)+1:
                return (int(total))
        else:
            print("Please input a Valid Number")
            break

def BinaryOctal(x):
    p=BinaryDecimal(x)
    ans=DecimalOCtal(p)
    return ans

def OctalBinary(x):
    p=OctalDecimal(x)
    ans=DecimalBinary(p)
    return ans

def BinaryHex(x):
    p=BinaryDecimal(x)
    ans=DecimalHex(p)
    return ans

def HexBinary(x):
    p=HexDecimal(x)
    ans=DecimalBinary(p)
    return ans

def OctalHex(x):
    p=OctalDecimal(x)
    ans=DecimalHex(p)
    return ans

def HexOctal(x):
    p=HexDecimal(x)
    ans=DecimalOCtal(p)
    return ans

def command(f,t):
    if f==2 and t==10:
        x=int(input("Enter the Binary Number: "))
        print("Answer=" ,BinaryDecimal(x))

    elif f==2 and t==8:
        x = int(input("Enter the Binary Number: "))
        print("Answer=" ,BinaryOctal(x))

    elif f == 2 and t == 16:
        x = input("Enter the Binary Number: ")
        print("Answer=" ,BinaryHex(x))

    elif f == 8 and t == 2:
        x = int(input("Enter the Octal Number: "))
        print("Answer=" ,OctalBinary(x))

    elif f == 8 and t == 10:
        x = int(input("Enter the Octal Number: "))
        print("Answer=" ,OctalDecimal(x))

    elif f == 8 and t == 16:
        x = int(input("Enter the Octal Number: "))
        print("Answer=" ,OctalHex(x))

    elif f==10 and t==2:
        x = int(input("Enter the Decimal Number: "))
        print("Answer=" ,DecimalBinary(x))

    elif f == 10 and t == 8:
        x = int(input("Enter the Decimal Number: "))
        print("Answer=" ,DecimalOCtal(x))

    elif f == 10 and t == 16:
        x = int(input("Enter the Decimal Number: "))
        print("Answer=" ,DecimalHex(x))

    elif f == 16 and t == 2:
        x = input("Enter the HexaDecimal Number: ")
        print("Answer=" ,HexBinary(x))

    elif f == 16 and t == 8:
        x = input("Enter the HexDecimal Number: ")
        print("Answer=" ,HexOctal(x))

    elif f == 16 and t == 10:
        x = input("Enter the HexaDecimal Number: ")
        print("Answer=" ,HexDecimal(x))

    else:
        print("Your Input is not valied! Try Again!")
        enter()
    print("\nThe Command Set:  1=Try on different Base\t2=Keep this base\tDone=Exit")
    runner()

def enter():
    print("The Command Set:  2=Binary\t 8=Octal\t 10=Decimal\t 16=Hex \n")
    global f
    global t
    f=int(input("Enter the 'convert from' Value: "))
    t = int(input("Enter the 'convert to' Value: "))
    command(f,t)

print("\t\t\t\tWelcome To Converter Programme")
print("""             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE Python! |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________," """)

print("""
    ______                                 __
   / ____/____   ____  _   __ ___   _____ / /_ ___   _____
  / /    / __ \ / __ \| | / // _ \ / ___// __// _ \ / ___/
 / /___ / /_/ // / / /| |/ //  __// /   / /_ /  __// /
 \____/ \____//_/ /_/ |___/ \___//_/    \__/ \___//_/
                                        developed by: Danushka
                                                                    """)

print("Enter 1 for convert and Done for Exit")

def runner():
    runner=input("Enter the Command: ").lower()
    if runner=='1':
        enter()
    elif runner=='done':
        print("Thank you for using this Software")
        print(quit())
    elif runner=='2':
        command(f,t)
    else:
        enter()

runner()


