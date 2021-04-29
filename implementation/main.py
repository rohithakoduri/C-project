##small project on fee payment
import os
import pickle as p
def add_record():
  f=open("student.dat","ab")
  r=input("enter rollno")
  name=input("enter name")
  fee=input("enter first installment maximum fee 2000")
  d={"rollno":r,"Name":name,"Fee":fee}
  p.dump(d,f)
  f.close()
def show():
  f=open("student.dat","rb")  
  try:
    while True:
      d=p.load(f)
      print("Rollno=",d["rollno"])
      print("Name=",d["Name"])
      print("Fee=",d["Fee"])
      print()
  except EOFError:
    pass
  f.close()
def search():
  f=open("student.dat","rb")
  rollno1=input("enter rollno to be searched")
  flag=0
  try:
    while True:
      d=p.load(f)
      if d["rollno"]==rollno1:
        print("Rollno=",d["rollno"])
        print("Name=",d["Name"])
        print("Fee=",d["Fee"])
        print()
        flag=1
        break
  except EOFError:
    pass
  f.close()
  if flag==0:
    print("record not found")
def Modify_name():
  f=open("student.dat","rb")
  f1=open("studentcopy.dat","wb")
  rollno1=input("enter rollno to be searched")  
  flag=0
  try:
    while True:
      d=p.load(f)
      if d["rollno"]==rollno1:
        nn=input("Enter name to be modify")
        d["Name"]=nn
        flag=1
        p.dump(d,f1)
      else:
        p.dump(d,f1)      
  except EOFError:
    pass
  f.close()
  f1.close()
  if flag==0:
    print("record not found")
  os.remove("student.dat")
  os.rename("studentcopy.dat","student.dat")
def Delete_data():
  f=open("student.dat","rb")
  f1=open("studentcopy.dat","wb")
  rollno1=input("enter rollno to be searched")
  flag=0
  try:
    while True:
      d=p.load(f)
      if d["rollno"]!=rollno1:
        p.dump(d,f1)
      else:
        flag=1
  except EOFError:
    pass
  f.close()
  f1.close()
  if flag==0:
    print("record not found")
  os.remove("student.dat")
  os.rename("studentcopy.dat","student.dat")
def update_fee():
  f=open("student.dat","rb")
  f1=open("studentcopy.dat","wb")
  rollno1=input("enter rollno to be searched")
  flag=0
  try:
    while True:
      d=p.load(f)
      if d["rollno"]==rollno1:
        flag=1
        print("fee to be paid=",2000-int(d["Fee"]))
        if (2000-int(d["Fee"])==0):
          print("full payment done you need not to pay money")
        else:
          feepay=input("enter amount to be paid")
          total=int(d["Fee"])+int(feepay)
          if total>2000:
            print("please check the amount")
          else:
            d["Fee"]=str(total)
      p.dump(d,f1)
  except EOFError:
    pass
  f.close()
  f1.close()
  if flag==0:
    print("record not found")
  os.remove("student.dat")
  os.rename("studentcopy.dat","student.dat")
def check_feebalance():
  f=open("student.dat","rb")
  rollno1=input("enter rollno to be searched")
  flag=0
  try:
    while True:
      d=p.load(f)
      if d["rollno"]==rollno1:
        flag=1
        print("fee to be paid=",2000-int(d["Fee"]))
  except EOFError:
     pass
  f.close()
  if flag==0:
    print("record not found")
while(1):
  print("1) Enter record")
  print("2) Show")
  print("3) Search")
  print("4) Modify Name")
  print("5) Exit")
  print("6) Delete")
  print("7) Update_fee")
  print("8) Check fee balance")
  ch=int(input("enter your choice="))
  if ch==1:
    add_record()
  elif ch==2:
    show()
  elif ch==3:
    search()
  elif ch==4:
    Modify_name()
  elif ch==5:
    break
  elif ch==6:
    Delete_data()
  elif ch==7:
    update_fee()
  elif ch==8:
    check_feebalance()
  else:
    print("Please enter value between 1-8")
