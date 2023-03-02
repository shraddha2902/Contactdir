'''
main file
=========
'''
def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():
    fp=open('data.txt','a')
    n=input("Enter Name:")
    mn=input("Enter your mobile number:")
    print()
    res=validate_mob(mn)
    #print(res)
    if res==1:
            a,b=searchmob(mn)
            if b==1:
                print("Number Already Exist")
                print()
            else:
                d=n+":"+mn+"\n"
                fp.write(d)
                fp.close()
                print("Contact created successfully!!")
    else:
            print("Please enter valid mobile number")

def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("========Contact Directory========")
    print()
    print(d)
    print("==================================")
def searchmob(n):
    fp=open('data.txt','r')
    data=fp.readlines()
    for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("Contact found:")
                #print(x)
                return x,1
               
    else:
                return ' ',0
    
    print("==================================")

def serchname():
    print("Search contact number by name")
    ns=input("Enter Name:")
    fp=open('data.txt','r')
    data=fp.readlines()
    #print(data)
    flag=0
    for x in data:
        #print(x)
        l=x.split(":")
        #print(l)
        #print(l[0])
        if ns.upper()==l[0].upper():
            print("Contact found")
            print(x)
            flag=1
        if flag==0:
            print("Record not found!!")
            
        fp.close()
    

print("Welcome to contact Directory console application ")
print()
while True:
    print("1.create contact")
    print("2.view contacts")
    print("3.search by name")
    print("4.searchsh by mobile number")
    print("5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        create_contact()
    elif ch==2:
        display()
    elif ch==3:
        serchname()
    elif ch==4:
        ms=input("Enter mobile number to be search:")
        a,b=searchmob(ms)
        print(a)
        print(b)
        if b==1:
            print("Number Found!!!")
        else:
            print("Not Found")
    elif ch==5:
        break
    else:
        print("Please enter vaild option!!")

print("Thanks for using application")
