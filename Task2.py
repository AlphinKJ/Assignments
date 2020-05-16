Students=["Aasta","Abin","Ashrith","Bhaviya","Binu","Christina","Don","Emil","Fayas","Gouri","Kevin","Lithiya","Sandi","Sara","Vandana","Zakariya",]
Python_Students=["Ashrith","Don","Sandi","Sara"]
HTML_Students=["Abin","Binu","Christina","Zakariya"]
DCF_Students=["Emil","Fayas","Lithiya","Vandana"]
choice=input("CHOSE A OPTION FROM MENU\n1)FIND THE REGISTER NUMBER OF A STUDENT\n2)CHECK WHETHER STUDENT HAVE ENROLLED IN ANY COURSE OR NOT \n")
name = input("ENTER THE NAME OF THE STUDENT: ")
if (choice == "1"):
    if (type(name) is int):
        print("PLEASE ENTER A VALID NAME")
    if name in Students:
        print(str(1841001+Students.index(name)))
    else:print("STUDENT NOT FOUND IN THE LIST")
elif (choice == "2"):
    if name in Python_Students or name in HTML_Students or name in DCF_Students:
        print("STUDENT IS ENROLLED IN A COURSE")
    elif (name not in Python_Students and name not in HTML_Students and name not in DCF_Students):
        print("OOPS!! STUDENT IS NOT ENROLLED IN ANY COURSE YET!!")

