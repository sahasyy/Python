import os
import platform
import mysql.connector
import datetime
global z
mydb=mysql.connector.connect(user='root',password='admin',
                               host='localhost',
                               database='airline')
mycursor=mydb.cursor()
global s
global f
def registercust():
    L=[]
    name=input('Enter name:')
    L.append(name)
    addr=input('Enter address:')
    L.append(addr)
    jr_date=input('Enter date of journey:')
    L.append(jr_date)
    source=input('Enter source:')
    L.append(source)
    destination=input('Enter destination:')
    L.append(destination)
    cust=(L)
    sql='insert into pdata(custname,addr,jrdate,source,destination) values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql,cust)
    mydb.commit()
 
 
def ticketprice():
    global s
    print('Do you want to see class type available? Enter 1 for yes:')
    ch=int(input('Enter your choice:'))
    if ch==1:
        sql='select * from classtype'
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    print('We have the following rooms for you:-')
    print('1. type First class--->rs 6000 PN\-')
    print('2. type Business class--->rs 4000 PN\-')
    print('3. type Economy class--->rs 2000 PN\-')
    x=int(input('Enter your class type:'))
    n=int(input('Enter No. of Passengers:'))
    if x==1:
        print('you have opted First class.')
        s=6000*n
    elif x==2:
        print('you have opted Business class.')
        s=4000*n
    elif x==3:
        print('you have opted Economy class.')
        s=2000*n
    else:
        print('Please select a class type.')
    print('your room rent is =',s,'\n')
    return s
 
 
   
 
def orderitem():
    global f
    print('Do you want to see menu available? Enter 1 for yes:')
    ch=int(input('Enter your choice:'))
    print('We have the following menus for you:-')
    print('1. Tea')
    print('2. cofee')
    print('3. colddrinks')
    print('4. samosa')
    print('5. sandwitch')
    print('6. dhokla')
    print('7. kachori')
    print('8. milk')
         
    print('What do you want to purchase from above list? Enter your choice.')
    d=int(input('Your choice:'))
    if d==1:
        print('You have ordered Tea.')
        a=int(input('Enter quantity:'))
        f=10*a
        print('Your amount for Tea is:',f,'\n')
    elif d==2:
        print('You have ordered Coffee.')
        a=int(input('Enter quantity:'))
        f=10*a
        print('Your amount for Coffee is:',f,'\n')
    elif d==3:
        print('You have ordered Colddrink.')
        a=int(input('Enter quantity:'))
        f=20*a
        print('Your amount for Colddrink is:',f,'\n')
    #else:
        #print('Please enter your choice from the menu.')
    return f
def luggagebill():
    global z
    print('Do you want to see rate for luggage? if yes press y and if no press n')
    ch=input('Enter your choice:')
    if ch=='y':
        y=int(input('Enter luggage weight,of extra luggage:'))
        z=y*100
        print('Your luggage bill:',z,'\n')
    
       
 
def ticketamount():
    b=input("Enter your boarding_no=")
    print('Luggage bill:',z)
    print('Food bill:',f)
    print('Ticket price',s)
    total=z+f+s
    print("Total amount is==",total)
    sql='update pdata set total={} where bording_no={}'.format(total,b)
    mycursor.execute(sql)
    mydb.commit()
   
 
    
    
 
def Menuset():
    print('Enter 1: To enter customer data.')
    print('Enter 2: To view class.')
    print('Enter 3: For viewing food menu.')
    print('Enter 4: For luggage bill.')
    print('Enter 5: For complete amount.')
    print('Enter 6: Exit.')
 
    userinput=int(input('Enter your choice:'))
    if userinput==1:
        registercust()
    elif userinput==2:
        ticketprice()
    elif userinput==3:
        orderitem()
    elif userinput==4:
        luggagebill()
    elif userinput==5:
        ticketamount()
    elif userinput==6:
        quit()
    else:
        print('Enter correct choice.')
 
Menuset()
def runagain():
    runagn=input('\nWant to run again? y/n:')
    while runagn=='y':
        if platform.system=='windows':
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input('\nWant to run again? y/n:')
runagain()
