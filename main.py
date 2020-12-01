import string
import random

if __name__ == "__main__":
    s1= string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4=string.punctuation
   # print(s4)
    s=[]
    while True:
        try:
            passlen=int(input("Enter password length: ")) #Todo: exception handling
            break
        except:
            print("Please provide input as integer only")

    s.extend(list(s1))
    s.extend(list(s1))
    s.extend(list(s3))
    s.extend(list(s4))
            #print(s)
    random.shuffle(s)
    p=("".join(s[0:passlen]))  # to join al the elements seperated by " ", and get printed as a single string
    print(p)
    file= open("passwords.txt","a")
    file.write(p)
    file.write("\n")
    file.close()