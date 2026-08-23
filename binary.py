#binary encrypter and decrypter including a login window specified to a username and password
import sys
def main():
    login()
    welcome()
    while True:
        print("\n\n\nBinary Terminal\n\n1.Encode\n2.Decode\n3.Exit")
        ch=int(input("Choose an option.\n> "))
        match ch:
            case 1:
                encode()
            case 2:
                decode()
            case 3:
                print("...exiting...")
                print("="*74)
                print("Thank you.\nOink Oink :)\n\n~Adyasha")
                sys.exit()
            case _:
                print("Choose from the menu.\n...redirecting to menu...\n")
def welcome():
    print("="*74)
    print("\t\tBINARY FRIENDSHIP TERMINAL (>_<)")
    print("="*74)
    print("\n\nBuilt with Python.\nOne evening.\nOne Laptop.\nAnd way too many goofy ideas meoww:3")
def login():
    while True:
            username=input("Name?\n> ").strip().capitalize()
            password=input("password(DDMMYYYY)\n> ").strip()
            if username!="Adyasha":
                print('Only "Adyasha" can open this :)')
            elif password!="02082026":
                print("yk wht's it; try again :3")
            else:
                print("\n\nAccess granted (^o^)\n")
                print("...logging in...\n")
                print(f"Welcome {username}.\n\nBefore you continue...\n\nHappy Friendship Day <3")
                break
#Thank you for accidentally\nmaking into my first python project :)\n\n
 #print("username: Adyasha\tpassword:02082026\nTry again :3")        
def encode():
    sentence=input("Encode:\n> ") 
    c=len(sentence)
    count=1
    for j in range(c):
        y=sentence[j]
        x=ord(y)
        ch=[0]*7
        i=0
        while i<7:
            if x%2==1:
               ch[i]=1
            else:
               ch[i]=0
            i+=1
            x=x//2
        tmp=[0]*7
        i=6
        for _ in range(7):
            tmp[_]=ch[i]
            i-=1
        print(f"0",end="")
        for _ in range(7):
            print(tmp[_],end="") 
        print(end=" ")
        if count%5==0:
           print()
        count+=1
    print("\n\nEncoding complete !")
def decode():
    binary_code=input().strip()
    print("-"*74)
    print("Decoded message:\n")
    for block in binary_code.split():
        print(chr(int(block, 2)),end="")
    print()
    print("-"*74)
main()