import os
#basic function
def Hello(m):
    return '{} namasthe'.format(m)
print(Hello('hasi'))


# two types are arguments= positional and keyyword
# key word= def fun(a=,b=)

# *args and **kwargs
def Student(*args,**kwargs):
    print("total marks are ", sum(args))
    print("student deatils are as follows : ")
    for i in kwargs:
        print(i ,"-", kwargs[i])
        
marks=[1,2,3]
details={'name':'hasini','age':'20','gender':'F'}

Student(*marks,**details)

## find num of days in a month
days=[0,31,28,30,31,30,31,30,31,30,31,30,31]
def leap_year(year):
    return year%4==0 and (year%100!=0 or year%400==0)
def find_days(year,month):
    if not 1<=month<=12:
        return 'Invalid month'
    if leap_year(year):
        return 29
    return days[month]

print(find_days(2020,2))

## FUNCTIONS BY PURPOSE ###

#2)check if passkey is minimum of 8 length
def check_pass(password):
    return len(password)>=8

#3)check if valid email
def is_valid_email(id):
    return '@' in id and "." in id

##############  ORCHESTRATION  ###########
    
def correct_email(id):
    return id.strip().lower()
    
def writee_log(message):
    path = r"C:\Users\haasi\Desktop\newfilee.txt"
    with open(path,"a") as file:
        file.write(message+"\n")

def email_detail(id):
    name,ver=id.split('@')
    return name,ver

email=input("enter your email: ")
crt_mail=correct_email(email)

if is_valid_email(crt_mail):
    writee_log("correct email")
    name,ver=email_detail(crt_mail)
    writee_log(f"name is : {name}")
    writee_log(f"domain is {ver}")
else:
    writee_log("incorrect email")
    
###########LAMBDA#########
#-> OUTPUT = LAMBDA x:EXPRESSION where x is i/p
prices=[120,30,300,80]
l=list(filter(lambda x:x>100,prices))
print(l)  

priced=['$120','$30','$300','$80']
h=list(map(lambda x: float(x.replace('$',"")),priced))
print(h)

students=[['Maria',85],
          ['Kumar',90],
          ['Max',60]]
print(list(filter(lambda x:x[0].startswith('M'),students)))

    
    
    
    



