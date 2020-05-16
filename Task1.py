string1=input("ENTER YOUR FIRST NAME:  ")
string2=input("ENTER YOUR LAST NAME: ")
username=string1.upper()+"_"+string2.capitalize()
hash=hash(string1)
id=str(abs(hash+(len(string2))))
string3="Hi Your Name, Hope you are fine!! We are inviting you to test our beta version of CHRIST University Official app. \n Your Username: %s \n Your Password: {}"
string4=string3.replace("Your Name",string1)
print(string4.format(id) % username)