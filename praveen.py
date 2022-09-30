import re
dictionary = {}

def register():
    while True:
        email = input("Enter Your email Id : ")
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
        if not re.search(regex,email):
            print("Invalid email")
            continue
        password = input("Enter Your password : ")
        if len(password)<5 or len(password)>12:
            print("Invalid password")
            continue
        special = '^[*@!#%&()^~{}]+'
        lower = '^[a-z]+'
        upper = '^[A-Z]+'
        number = '^[0-9]+'
        if not re.search(special, password) or not re.search(lower,email) or not re.search(upper,email) or not re.search(number,email):
            return email, password
        print("Invalid Password")
        

def main():
    dictionary = {}
    f = open("file.txt", "r")
    emails = f.read()
    entries = emails.split(',')
    print(entries)
    for entry in entries:
        if ":" in entry:
            details = entry.split(':')
            dictionary[details[0]] = details[1]
    f = open("file.txt","a")
    while True:
        print("Press 1 for registration")
        print("Press 2 for Log in")
        print("Press 3 for Forgot password")
        print("Press 4 to break")
        option = int(input())
        if option == 1:
            email,password = register()
            dictionary[email] = password
            f.write(email+":"+password+",")
            print("Registration Successful")
        if option == 2:
            email = input("Please Enter your email:")
            password = input("Please Enter your password:")
            if not email in dictionary or dictionary[email] != password:
                print("Credentials not found Please register or press Forgot password")
                continue
            print("Logged In Successfully")
            break
        if option == 3:
            email = input("Please Enter your email:")
            if email not in dictionary:
                print("No user found Please REgister")
                continue
            print("Your password is : " + dictionary[email])
        if option == 4:
            break
        
          
if __name__=="__main__":
    main()
    
    