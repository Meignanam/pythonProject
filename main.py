
import mysql.connector
mydb=mysql.connector.connect(host='localhost',port=3306,user='root',password='root',database='BANK_MANAGEMENT')

def OpenAcc():
    n=input("Enter the Name: ")
    ac=input("Enter the Account No: ")
    db=input("Enter the Date of Birth: ")
    add=input("Enter the Address: ")
    cn=input("Enter the Contact Number: ")
    ob=int(input("Enter the Opening Balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=mydb.cursor()
    x.execute()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully...")
    mani()
def DepoAmo():
    amount=input("Enter the amount you want to deposit: ")
    ac = input("Enter the Account No: ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update amount set balance where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def WithdrawAmount():
    amount = input("Enter the amount you want to Withdraw: ")
    ac = input("Enter the Account No: ")
    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update amount set balance where AccNo=%s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def BalEnq():
    ac=input("Enter the account no: ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x.mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance for account: ",ac,"is",result[-1])
    main()

def DisDetails():
    ac = input("Enter the account no: ")
    a = 'select * from amount where AccNo=%s'
    data = (ac,)
    x.mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    ac = input("Enter the account no: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from account where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()

def main():
    print('''
                1.OPEN NEW ACCOUNT
                2.DEPOSITE AMOUNT
                3.WITHDRAW AMOUNT
                4.BALANCE ENQUIRY
                5.DISPLAY CUSTOMER DETAILS
                6.CLOSE AN ACCOUNT''')
    choice=input("Enter the Task you want To perform: ")
    if(choice=='1'):
        OpenAcc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
        WithdrawAmount()
    elif(choice=='4'):
        BalEnq()
    elif(choice=='5'):
        DisDetails()
    elif(choice=='6'):
        CloseAcc()
    else:
        print("Invalid Choice")
        main()

main()