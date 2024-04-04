import mysql.connector

mycursor=None
mycon=None
sp=""



#CHECK CONNECTION

def check_connection():

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password"
    )
    if mycon.is_connected():
        print("Successfully connected to MySQL")
        print("Information : ",mycon)
        return 1
    else:
        print("check")
        return 0

print("check")
check_connection()



#SPACE FUNCTION
    
def space(V):
    global sp
    sp=""
    l=15-len(str(V))
    for i in range(l):
        sp=sp+" "
    return sp

  

#DATABASE - elec_bills

def create_database():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password"
    )

    global mycursor

    mycursor = mycon.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS  elec_bills")
    mycon.commit()

    print("Database created or used")

    for x in mycursor:
      print(x)
      
create_database()




# BASIC INFO TABLE-Sector A1 and B1

def create_table():

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    mycursor = mycon.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS SECTOR_A1(H_No VARCHAR(20),Name VARCHAR(20),Ph_no INT(10),Bill_issued DATE,Units_consumed INT(5), Total_amt INT(8),Paid_Unpaid VARCHAR(20))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS SECTOR_B1(H_No VARCHAR(20),Name VARCHAR(20),Ph_no INT(10),Bill_issued DATE,Units_consumed INT(5), Total_amt INT(8),Paid_Unpaid VARCHAR(20))")

    mycon.commit()

    print("Tables under elec_bills: ")

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
      print(x)




#ADDING RECORDS - SECTOR_A1

def add_new_record_a():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )
    mycursor = mycon.cursor()

    
    sql="INSERT INTO SECTOR_A1(H_No,Name,Ph_no,Bill_issued,Units_consumed, Total_amt, Paid_Unpaid) VALUES(%s,%s,%s,%s,%s,%s,%s)"

    SECTOR_A1 =[("1A","Aditya",22710001,"2020-10-28",400,2600,"UNPAID"),
               ("2A","Raghav",22710002,"2020-10-28",410,2665,"PAID"),
               ("3A","Arun",22710003,"2020-10-28",410,2665,"PAID"),
               ("4A","Aditi",22710004,"2020-10-28",450,2925,"UNPAID"),
               ("5A","Vipul",22710005,"2020-10-28",468,3042,"PAID"),
               ("6A","Kashish",22710006,"2020-10-28",402,2613,"PAID"),
               ("7A","Pratham",22710007,"2020-10-28",500,3250,"PAID"),
               ("8A","Rochak R",22710008,"2020-10-28",460,2990,"UNPAID"),
               ("9A","Divyanshi S",22710009,"2020-10-28",458,2977,"PAID"),
               ("10A","Prachi",22710010,"2020-10-28",472,3068,"UNPAID"),
               ("11A","Lakshit",22710011,"2020-10-28",510,3315,"PAID"),
               ("12A","Avanti",22710012,"2020-10-28",506,3289,"PAID"),
               ("13A","Surbhi J",22710013,"2020-10-28",488,3172,"UNPAID"),
               ("14A","Nandu",22710014,"2020-10-28",450,2925,"PAID"),
               ("15A","Karamjeet S",22710015,"2020-10-28",420,2730,"PAID"),
               ("16A","Ishpreet",22710016,"2020-10-28",600,3900,"PAID"),
               ("17A","Ishan",22710017,"2020-10-28",620,4030,"PAID"),
               ("18A","Rajni",22710018,"2020-10-28",782,5083,"PAID"),
               ("19A","Shruti K",22710019,"2020-10-28",558,3627,"PAID"),
               ("20A","Aashi A",22710020,"2020-10-28",562,3653,"PAID"),
               ("21A","Sahiba",22710021,"2020-10-28",410,2665,"PAID"),
               ("22A","Samyak",22710022,"2020-10-28",476,3094,"UNPAID"),
               ("23A","Hardik",22710023,"2020-10-28",472,3068,"PAID"),
               ("24A","Yash",22710024,"2020-10-28",700,4550,"UNPAID"),
               ("25A","Ainish U",22710025,"2020-10-28",712,4628,"PAID"),
               ("26A","Himanshu R",22710026,"2020-10-28",752,4888,"PAID"),
               ("27A","Aman J",22710027,"2020-10-28",410,2665,"PAID"),
               ("28A","Prisha",22710028,"2020-10-28",458,2977,"PAID"),
               ("29A","Priyanka",22710029,"2020-10-28",462,3003,"PAID"),
               ("30A","Uma",22710030,"2020-10-28",650,4225,"PAID")]

    
    mycursor.executemany(sql,(SECTOR_A1))

    mycon.commit()




#ADDING RECORDS - SECTOR_B1

def add_new_record_b():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )
    mycursor = mycon.cursor()
    sql="INSERT INTO SECTOR_B1(H_No,Name,Ph_no,Bill_issued,Units_consumed, Total_amt, Paid_Unpaid) VALUES(%s,%s,%s,%s,%s,%s,%s)"

    SECTOR_B1 =[("1B","Shashank",22710031,"2020-10-29",416,2704,"UNPAID"), 
                ("2B","Arpit S",22710032,"2020-10-29",392,1372,"UNPAID"),
                ("3B","Karan",22710033,"2020-10-29",498,3237,"PAID"),
                ("4B","Ishu J",22710034,"2020-10-29",522,3393,"PAID"),
                ("5B","Suhaani",22710035,"2020-10-29",348,1218,"PAID"),
                ("6B","Vanshika",22710036,"2020-10-29",350,1225,"PAID"),
                ("7B","Vansh",22710037,"2020-10-29",600,3900,"PAID"),
                ("8B","Tomy K",22710038,"2020-10-29",798,5187,"PAID"),
                ("9B","Jodha",22710039,"2020-10-29",416,2704,"PAID"),
                ("10B","Raju",22710040,"2020-10-29",410,2665,"PAID"),
                ("11B","Manju R",22710041,"2020-10-29",420,2730,"PAID"),
                ("12B","Rajkumar A",22710042,"2020-10-29",450,2925,"UNPAID"),
                ("13B","Namya",22710043,"2020-10-29",700,4550,"PAID"),
                ("14B","Debansha",22710044,"2020-10-29",648,4212,"PAID"),
                ("15B","Sonam G",22710045,"2020-10-29",676,4394,"PAID"),
                ("16B","Rajesh",22710046,"2020-10-29",522,3393,"PAID"),
                ("17B","Suresh M",22710047,"2020-10-29",598,3887,"PAID"),
                ("18B","Riddhi",22710048,"2020-10-29",798,5187,"UNPAID"),
                ("19B","Aprajita",22710049,"2020-10-29",566,3679,"PAID"),
                ("20B","Kiara",22710050,"2020-10-29",650,4225,"PAID"),
                ("21B","Fawad",22710051,"2020-10-29",476,3094,"PAID"),
                ("22B","Siddharth S",22710052,"2020-10-29",498,3237,"UNPAID"),
                ("23B","Chaitanya K",22710053,"2020-10-29",358,1253,"PAID"),
                ("24B","Mahesh",22710054,"2020-10-29",678,4407,"PAID"),
                ("25B","Lakshita",22710055,"2020-10-29",710,4615,"PAID"),
                ("26B","Pooja D",22710056,"2020-10-29",418,2717,"PAID"),
                ("27B","Anshit",22710057,"2020-10-29",506,3289,"PAID"),
                ("28B","Dhruv",22710058,"2020-10-29",576,3744,"PAID"),
                ("29B","Sugandha",22710059,"2020-10-29",498,3237,"PAID"),
                ("30B","Shaurya",22710060,"2020-10-29",410,2665,"UNPAID")]

    
    mycursor.executemany(sql,(SECTOR_B1))

    mycon.commit()



 
#RESIDENTS PASSWORDS

def setUpPasswords():
  userPasswords["1A"] = "HELLOWORLD"
  userPasswords["2A"] = "MUSIC"
  userPasswords["3A"] = "zdkvgs"
  userPasswords["4A"] = "odihjteoi"
  userPasswords["5A"] = "GIOERGNVK"
  userPasswords["6A"] = "KFGBK"
  userPasswords["7A"] = "AERHUI"
  userPasswords["8A"] = "KFBEFW"
  userPasswords["9A"] = "LGNLRE"
  userPasswords["10A"] = "GMKRTL"
  userPasswords["11A"] = "FMREKLGNMEKL"
  userPasswords["12A"] = "DION"
  userPasswords["13A"] = "FNOLEF"
  userPasswords["14A"] = "INFGI"
  userPasswords["15A"] = "GERGER"
  userPasswords["16A"] = "REGREG"
  userPasswords["17A"] = "REGRRG"
  userPasswords["18A"] = "IUFBIH"
  userPasswords["19A"] = "GRGRE"
  userPasswords["20A"] = "4G5T4GF"
  userPasswords["21A"] = "SCGCF"
  userPasswords["22A"] = "AHDBED"
  userPasswords["23A"] = "REVGRE"
  userPasswords["24A"] = "EQQAH"
  userPasswords["25A"] = "SFBLJK"
  userPasswords["26A"] = "FNKLSEFN"
  userPasswords["27A"] = "2J4GKJ"
  userPasswords["28A"] = "3K25GKJ"
  userPasswords["29A"] = "FIKBW3"
  userPasswords["30A"] = "KUFBUI3"
  userPasswords["1B"] = "KARATE"
  userPasswords["2B"] = "EVERYONE"
  userPasswords["3B"] = "SDHBRT"
  userPasswords["4B"] = "FGDHRH"
  userPasswords["5B"] = "REHJR"
  userPasswords["6B"] = "AFGHS"
  userPasswords["7B"] = "64JSFBVKSD"
  userPasswords["8B"] = "DYFVGUD"
  userPasswords["9B"] = "JDSBFJ"
  userPasswords["10B"] = "BFJEKB"
  userPasswords["11B"] = "AONDI"
  userPasswords["12B"] = "UGFDUI"
  userPasswords["13B"] = "UIDBFIUB"
  userPasswords["14B"] = "GFUYG"
  userPasswords["15B"] = "JBSDCKB"
  userPasswords["16B"] = "BCIOBC"
  userPasswords["17B"] = "UJCBFIUD"
  userPasswords["18B"] = "CVKBC"
  userPasswords["19B"] = "QIUDKB"
  userPasswords["20B"] = "JBKDFKJDBC"
  userPasswords["21B"] = "87GFUYIG"
  userPasswords["22B"] = "VSADHI"
  userPasswords["23B"] = "SDJBVUFI"
  userPasswords["24B"] = "IVBSHJBX"
  userPasswords["25B"] = "IUGEB"
  userPasswords["26B"] = "8WQGBD"
  userPasswords["27B"] = "IKWNDQBON"
  userPasswords["28B"] = "UYSAVF"
  userPasswords["29B"] = "SLKFHU"
  userPasswords["30B"] = "DFIVONF"



  
#UPDATE LOGS BY ADMIN

def updateLog(originalInfo, newInfo):
  f = open("logs.txt","a")
  f.write("\nNew Entry:\nOriginal Details:\n{}\n\nNew Details:\n{}\n\n\n".format(originalInfo, newInfo))
  f.close()



#FINDING INFO FOR ADMIN IN SECTOR A1

def viewSingleFromAdmin_A():
  mycon = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aditya",
    auth_plugin="mysql_native_password",
    database="elec_bills"
  )

  mycursor = mycon.cursor()
  H_no =input("Enter your house number ")

  sql_select_query = "select * from SECTOR_A1 where H_no = %s"
  mycursor.execute(sql_select_query, (H_no, ))
  myresult = mycursor.fetchall()
  if (mycursor.rowcount>0):
    
    # Add table column names

    print("--------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("--------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")
  ch = input("Would you like to update details?\n1.Yes\n2.No\n Enter your choice : ")
  if int(ch) == 1:

    mycursor.execute("SELECT * FROM SECTOR_A1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()

    originalInfo = myresult[0]

    ans='y'
    while ans=='y' or ans=='Y':
        ans='n'
        print("*******************************************************************************")
        print("*\t\t      BSES ELECTRICITY BILLING SYSTEM - SECTOR A1             *")
        print("*\t\t                                                              *")
        print("*\t\t        1.  DO YOU WANT TO CHANGE NAME ?                      *")
        print("*\t\t        2.  DO YOU WANT TO CHANGE PHONE NUMBER ?              *")
        print("*\t\t        3.  DO YOU WANT TO CHANGE TOTAL MONTHLY CONSUMPTION ? *")
        print("*******************************************************************************\n\n")

        ch=int(input("enter your choice\t"))
        
        if ch==1:
            Name=input("Enter name to be updated  ")

            namenew=input("Enter new name of the resident  ")

            sql_select_query = "UPDATE SECTOR_A1 set Name =%s WHERE Name = %s"

            input1=(namenew,Name)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")
       
        elif ch==2:
            Ph_no=input("Enter phone no. to be updated  ")

            Phnew=input("Enter new phone no. of the resident  ")

            sql_select_query = "UPDATE SECTOR_A1 set Ph_no =%s WHERE Ph_no = %s"

            input1=(Phnew,Ph_no)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

        elif ch==3:

            total_amt=input("Enter amount to be updated  ")

            amtnew=input("Enter new amount to be paid by the resident  ")

            sql_select_query = "UPDATE SECTOR_A1 set total_amt =%s WHERE total_amt = %s"

            input1=(amtnew,total_amt)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")
        else:
            print("Wrong Choice, Please choose correct option")
            ans=input("Do you want to try again (y for yes, n for no)\t")

    
    mycursor.execute("SELECT * FROM SECTOR_A1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("--------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("--------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")

    newInfo = myresult[0]

    updateLog(" ".join([str(i) for i in originalInfo]), " ".join([str(i) for i in newInfo]))




#FINDING INFO FOR ADMIN IN SECTOR B1

def viewSingleFromAdmin_B():
  mycon = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aditya",
    auth_plugin="mysql_native_password",
    database="elec_bills"
  )

  mycursor = mycon.cursor()
  H_no =input("Enter your house number ")

  sql_select_query = "select * from SECTOR_B1 where H_no = %s"
  mycursor.execute(sql_select_query, (H_no, ))
  myresult = mycursor.fetchall()
  if (mycursor.rowcount>0):
    
    # Add table column names

    print("--------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("--------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")
  ch = input("Would you like to update details?\n1.Yes\n2.No\n Enter your choice : ")
  if int(ch) == 1:

    mycursor.execute("SELECT * FROM SECTOR_B1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()

    originalInfo = myresult[0]

    ans='y'
    while ans=='y' or ans=='Y':
        ans='n'
        print("*******************************************************************************")
        print("*\t\t      BSES ELECTRICITY BILLING SYSTEM - SECTOR B1             *")
        print("*\t\t                                                              *")
        print("*\t\t        1.  DO YOU WANT TO CHANGE NAME ?                      *")
        print("*\t\t        2.  DO YOU WANT TO CHANGE PHONE NUMBER ?              *")
        print("*\t\t        3.  DO YOU WANT TO CHANGE TOTAL MONTHLY CONSUMPTION ? *")
        print("*******************************************************************************\n\n")

        ch=int(input("enter your choice\t"))
        
        if ch==1:
            Name=input("Enter name to be updated  ")

            namenew=input("Enter new name of the resident  ")

            sql_select_query = "UPDATE SECTOR_B1 set Name =%s WHERE Name = %s"

            input1=(namenew,Name)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")
       
        elif ch==2:
            Ph_no=input("Enter phone no. to be updated  ")

            Phnew=input("Enter new phone no. of the resident  ")

            sql_select_query = "UPDATE SECTOR_B1 set Ph_no =%s WHERE Ph_no = %s"

            input1=(Phnew,Ph_no)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

        elif ch==3:

            total_amt=input("Enter amount to be updated  ")

            amtnew=input("Enter new amount to be paid by the resident  ")

            sql_select_query = "UPDATE SECTOR_B1 set total_amt =%s WHERE total_amt = %s"

            input1=(amtnew,total_amt)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")
        else:
            print("Wrong Choice, Please choose correct option")
            ans=input("Do you want to try again (y for yes, n for no)\t")

    
    mycursor.execute("SELECT * FROM SECTOR_B1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("--------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("--------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")

    newInfo = myresult[0]

    updateLog(" ".join([str(i) for i in originalInfo]), " ".join([str(i) for i in newInfo]))


    



#CHECK_MONTHLY_CONSUMPTION_A1

def monthlycon_a(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    mycursor = mycon.cursor()
    
    sql_select_query = "select H_no,Units_consumed from SECTOR_A1 where H_no = %s"
    mycursor.execute(sql_select_query, (H_no, ))
    myresult = mycursor.fetchall()
    if (mycursor.rowcount>0):
        
        print("-------------------------------------------------------------------------------------------")
        print("H_no",space("H_no"),"units_consumed")
        print("-------------------------------------------------------------------------------------------")

        for x in myresult:
            print(x[0],space(str(x[0])),x[1])
            print("-------------------------------------------------------------------------------------------")

    else:
        print("Enter the correct House Number")





#CHECK_MONTHLY_CONSUMPTION_B1

def monthlycon_b(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    mycursor = mycon.cursor()
    
    sql_select_query = "select H_no,Units_consumed from SECTOR_B1 where H_no = %s"
    mycursor.execute(sql_select_query, (H_no, ))
    myresult = mycursor.fetchall()
    if (mycursor.rowcount>0):
        
        print("-------------------------------------------------------------------------------------------")
        print("H_no",space("H_no"),"units_consumed")
        print("-------------------------------------------------------------------------------------------")

        for x in myresult:
            print(x[0],space(str(x[0])),x[1])
            print("-------------------------------------------------------------------------------------------")

    else:
        print("Enter the correct House Number")




#CHECK_TOTAL_AMOUNT_A1

def totalamt_a(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    mycursor = mycon.cursor()

    sql_select_query = "select H_no,Name,total_amt,Paid_Unpaid from SECTOR_A1 where H_no = %s"
    mycursor.execute(sql_select_query, (H_no, ))
    myresult = mycursor.fetchall()
    if (mycursor.rowcount>0):
        
        print("-------------------------------------------------------------------------------------------")
        print("H_no",space("H_no"),"Name",space("Name"),"total_amt",space("total_amt"),"Paid_Unpaid")
        print("-------------------------------------------------------------------------------------------")

        for x in myresult:
            
            print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3])
            print("-------------------------------------------------------------------------------------------")
        
        x = myresult[0]
        if x[3] == "UNPAID":
          print("                                                   ")
          print("Would you like to pay your bill?\n Say Y for yes or N for no: \t")
          ch = input()
          if ch == "Y" or ch == "y":
            sql_select_query = "UPDATE SECTOR_A1 set Paid_Unpaid = \"PAID\" WHERE H_No = %s"

            mycursor.execute(sql_select_query,(H_no,))

            mycon.commit()
            print("Congratulations your bill has been sent over to your registered phone number.\nPlease use a digital mode of currency for payment.\nGo Green!")

        sql_select_query = "select H_no,Name,total_amt,Paid_Unpaid from SECTOR_A1 where H_no = %s"
        mycursor.execute(sql_select_query, (H_no, ))
        myresult = mycursor.fetchall()
        if (mycursor.rowcount>0):
            
            print("-------------------------------------------------------------------------------------------")
            print("H_no",space("H_no"),"Name",space("Name"),"total_amt",space("total_amt"),"Paid_Unpaid")
            print("-------------------------------------------------------------------------------------------")

            for x in myresult:
                
                print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3])
                print("-------------------------------------------------------------------------------------------")

    else:
        print("Enter the correct House Number")





#CHECK_TOTAL_AMOUNT_B1
      
def totalamt_b(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    mycursor = mycon.cursor()

    sql_select_query = "select H_no,Name,total_amt,Paid_Unpaid from SECTOR_B1 where H_no = %s"
    mycursor.execute(sql_select_query, (H_no, ))
    myresult = mycursor.fetchall()
    if (mycursor.rowcount>0):
        
        print("-------------------------------------------------------------------------------------------")
        print("H_no",space("H_no"),"Name",space("Name"),"total_amt",space("total_amt"),"Paid_Unpaid")
        print("-------------------------------------------------------------------------------------------")

        print(myresult)
        for x in myresult:
            
            print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3])
            print("-------------------------------------------------------------------------------------------")
        
        x = myresult[0]
        if x[3] == "UNPAID":
          print("                                                   ")
          print("Would you like to pay your bill?\n Say Y for yes or N for no: \t")
          ch = input()
          if ch == "Y" or ch == "y":
            sql_select_query = "UPDATE SECTOR_B1 set Paid_Unpaid = \"PAID\" WHERE H_No = %s"

            mycursor.execute(sql_select_query,(H_no,))

            mycon.commit()
            print("Congratulations your bill has been sent over to your registered phone number.\nPlease use a digital mode of currency for payment.\nGo Green!")

        sql_select_query = "select H_no,Name,total_amt,Paid_Unpaid from SECTOR_B1 where H_no = %s"
        mycursor.execute(sql_select_query, (H_no, ))
        myresult = mycursor.fetchall()
        if (mycursor.rowcount>0):
            
            print("-------------------------------------------------------------------------------------------")
            print("H_no",space("H_no"),"Name",space("Name"),"total_amt",space("total_amt"),"Paid_Unpaid")
            print("-------------------------------------------------------------------------------------------")

            print(myresult)
            for x in myresult:
                
                print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3])
                print("-------------------------------------------------------------------------------------------")

    else:
        print("Enter the correct House Number")




#CHECK_PERSONAL_DETAILS_A1
      
def ps_details_a(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    mycursor = mycon.cursor()
    
    sql_select_query = "select * from SECTOR_A1 where H_no = %s"
    mycursor.execute(sql_select_query, (H_no, ))
    myresult = mycursor.fetchall()
    if (mycursor.rowcount>0):
        
        print("------------------------------------------------------------------------------------------------------------------")
        print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
        print("------------------------------------------------------------------------------------------------------------------")

        for x in myresult:
            print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
            print("-----------------------------------------------------------------------------------------------------------------")

    else:
        print("Enter the correct House Number")





#CHECK_PERSONAL_DETAILS_B1

        
def ps_details_b(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    mycursor = mycon.cursor()
    
    sql_select_query = "select H_no, Name,Ph_no from SECTOR_B1 where H_no = %s"
    mycursor.execute(sql_select_query, (H_no, ))
    myresult = mycursor.fetchall()
    if (mycursor.rowcount>0):
        
        print("-------------------------------------------------------------------------------------------")
        print("H_no",space("H_no"),"Name",space("Name"),"Ph_no")
        print("-------------------------------------------------------------------------------------------")

        for x in myresult:
            print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2])
            print("-------------------------------------------------------------------------------------------")

    else:
        print("Enter the correct House Number")





#FOR UPDATING IN SECTOR_A1

        
def update_info_a(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )
    mycursor = mycon.cursor()
    
    mycursor.execute("SELECT * FROM SECTOR_A1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("--------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("--------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")
    

    ans='y'
    while ans=='y' or ans=='Y':
        ans='n'
        print("**********************************************************************")
        print("*\t\tBSES ELECTRICITY BILLING SYSTEM - SECTOR A1          *")
        print("*\t\t                                                     *")
        print("*\t\t    1.  DO YOU WANT TO CHANGE YOUR NAME ?            *")
        print("*\t\t    2.  DO YOU WANT TO CHANGE PHONE NUMBER ?         *")
        print("**********************************************************************\n\n")

        ch=int(input("enter your choice\t"))
        
        if ch==1:
            Name=input("Enter name to be updated  ")

            namenew=input("Enter new name of the resident  ")

            sql_select_query = "UPDATE SECTOR_A1 set Name =%s WHERE Name = %s"

            input1=(namenew,Name)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")
       
        elif ch==2:
            Ph_no=input("Enter phone no. to be updated  ")

            Phnew=input("Enter new phone no. of the resident  ")

            sql_select_query = "UPDATE SECTOR_A1 set Ph_no =%s WHERE Ph_no = %s"

            input1=(Phnew,Ph_no)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

        else:
            print("Wrong Choice, Please choose correct option")
            ans=input("Do you want to try again (y for yes, n for no)\t")

    
    mycursor.execute("SELECT * FROM SECTOR_A1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("-------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no")
    print("-------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2])
    print("-------------------------------------------------------------------------------------------")





#FOR UPDATING IN SECTOR_B1

def update_info_b(H_no):
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )
    mycursor = mycon.cursor()
    
    mycursor.execute("SELECT H_no,Name,Ph_no FROM SECTOR_B1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("--------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("--------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")


    ans='y'
    while ans=='y' or ans=='Y':
        ans='n'
        print("**********************************************************************")
        print("*\t\t      BSES ELECTRICITY BILLING SYSTEM - SECTOR B1      *")
        print("*\t\t                                                       *")
        print("*\t\t        1.  DO YOU WANT TO CHANGE YOUR NAME ?          *")
        print("*\t\t        2.  DO YOU WANT TO CHANGE PHONE NUMBER ?       *")
        print("**********************************************************************\n\n")

        ch=int(input("enter your choice\t"))
        
        if ch==1:
            Name=input("Enter name to be updated  ")

            namenew=input("Enter new name of the resident  ")

            sql_select_query = "UPDATE SECTOR_B1 set Name =%s WHERE Name = %s"

            input1=(namenew,Name)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")
       
        elif ch==2:
            Ph_no=input("Enter phone no. to be updated  ")

            Phnew=input("Enter new phone no. of the resident  ")

            sql_select_query = "UPDATE SECTOR_B1 set Ph_no =%s WHERE Ph_no = %s"

            input1=(Phnew,Ph_no)

            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

        else:
            print("Wrong Choice, Please choose correct option")
            ans=input("Do you want to try again (y for yes, n for no)\t")

    
    mycursor.execute("SELECT H_no,Name,Ph_no FROM SECTOR_B1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("-------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no")
    print("-------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2])
    print("-------------------------------------------------------------------------------------------")





#DELETE_ACCOUNT_A1
    
def delete_info_a(H_no):

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      database="elec_bills"
    )


    mycursor = mycon.cursor()
    
    # H_no=input("Enter house no. to delete the existing record")

    sql_select_query = "UPDATE SECTOR_A1 set Name=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_A1 set Ph_no=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_A1 set bill_issued=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_A1 set units_consumed=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_A1 set total_amt=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_A1 set Paid_Unpaid=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()
    

    print(mycursor.rowcount, "record(s) deleted")
    
    mycursor.execute("SELECT * FROM SECTOR_A1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("-------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("-------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")




#DELETE_ACCOUNT_B1
    
def delete_info_b(H_no):

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      database="elec_bills"
    )


    mycursor = mycon.cursor()
    
    # H_no=input("Enter house no. to delete the existing record")

    sql_select_query = "UPDATE SECTOR_B1 set Name=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_B1 set Ph_no=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_B1 set bill_issued=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_B1 set units_consumed=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_B1 set total_amt=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    sql_select_query = "UPDATE SECTOR_B1 set Paid_Unpaid=%s WHERE H_no = %s"

    mycursor.execute(sql_select_query, (None,H_no))

    mycon.commit()

    print(mycursor.rowcount, "record(s) deleted")
    
    mycursor.execute("SELECT * FROM SECTOR_B1 where H_no=%s",(H_no,))

    myresult = mycursor.fetchall()
    
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(str(x[2])),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
        print("-----------------------------------------------------------------------------------------------------------------")


  

#SIGNIN
    
def signin(choice,H_no = 1):
  if choice == 1:
    password="Admin01"
  else:
    password = userPasswords[H_no]

  ans='Y'
  while ans.upper()=='Y':
      pswd=input("\nENTER YOUR PASSWORD : ")

      if(pswd!=password):
          print("\nINCORRECT PASSWORD")
          ans=input("DO YOU WANT TO SIGN IN AGAIN(Y/N) : ")
          while ans.upper()!='Y' and ans.upper()!='N':
              ans=input("DO YOU WANT TO SIGN IN AGAIN(Y/N) : ")

              if ans.upper()=='N':
                  print("\nTHANKS FOR USING BSES ELECTRICITY BILLING SYSTEM ")
     

      elif(pswd==password):
          return True





#FOR CONSUMER MENU SECTOR_A1

def consmenu_a():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )


    ans='y'

    H_no = input("Enter House Number : ")
    signin(2,H_no)

    while ans=='y' or ans=='Y':
        print("**********************************************************************")
        print("*\t\t BSES ELECTRICITY BILLING SYSTEM - SECTOR A1         *")
        print("*\t\t    1.  Check Monthly Consumption                    *")
        print("*\t\t    2.  Check Total Amount to be paid                *")
        print("*\t\t    3.  Check personal Details                       *")
        print("*\t\t    4.  Update Information                           *")
        print("*\t\t    5.  Delete Your Account                          *")
        print("**********************************************************************\n\n")

        ch=int(input("Enter your choice : "))

        if ch==1:
            monthlycon_a(H_no)
        elif ch==2:
            totalamt_a(H_no)
        elif ch==3:
            ps_details_a(H_no)
        elif ch==4:
            update_info_a(H_no)
        elif ch==5:
            delete_info_a(H_no)
        else:
            print("Wrong Choice, please enter values between 1-5")

        print("Cost Per Unit : Rs. 3.5 for 200 to 400 Units")
        print("Cost Per Unit : Rs. 6.5 for 400 to 800 Units")
        print("Last Date of Payment 14th November 2020")
        

        ans=input("go back to the previous menu(y for yes, n for no)\t")




# FOR CONSUMER MENU SECTOR_B1

def consmenu_b():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )

    ans='y'
    
    H_no = input("Enter House Number : ")
    signin(2,H_no)

    while ans=='y' or ans=='Y':
        print("**********************************************************************")
        print("*\t\t    BSES ELECTRICITY BILLING SYSTEM - SECTOR B1      *")
        print("*\t\t        1.  Check Monthly Consumption                *")
        print("*\t\t        2.  Check Total Amount to be paid            *")
        print("*\t\t        3.  Check personal Details                   *")
        print("*\t\t        4.  Update Information                       *")
        print("*\t\t        5.  Delete Your Account                      *")
        print("**********************************************************************\n\n")
 
        ch=int(input("Enter your choice : "))

        if ch==1:
            monthlycon_b()
        elif ch==2:
            totalamt_b()
        elif ch==3:
            ps_details_b()
        elif ch==4:
            update_info_b()
        elif ch==5:
            delete_info_b()
        else:
            print("Wrong Choice, please enter values between 1-4")
        print("Cost Per Unit : Rs. 3.5 for 200 to 400 Units")
        print("Cost Per Unit : Rs. 6.5 for 400 to 800 Units")
        print("Last Date of Payment 14th November 2020")
        

        ans=input("go back to the previous menu(y for yes, n for no)\t")




#ADMIN
    
def admin():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aditya",
      auth_plugin="mysql_native_password",
      database="elec_bills"
    )
     
    signin(1)


    mycursor = mycon.cursor()
    ans='y'
    while ans=='y' or ans=='Y':
        
        print("**********************************************************************")
        print("*\t\t      BSES ELECTRICITY BILLING SYSTEM                *")
        print("*\t\t            Select a Sector :                        *")
        print("*\t\t            1.  SECTOR_A1                            *")
        print("*\t\t            2.  SECTOR_B1                            *")
        print("**********************************************************************\n\n")
        
        ch=int(input("enter your choice\t"))
        if ch==1:
          ch2 = int(input("Would you like to view all residents or a single one?\n\n 1. All\n 2. Selective\n\nEnter your choice : "))
          if ch2 == 1:
            mycursor.execute("select * from SECTOR_A1")
            myresult=mycursor.fetchall()
            print("--------------------------------------------------------------------------------------------------------------------")
            print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
            print("--------------------------------------------------------------------------------------------------------------------")
            
            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
                print("--------------------------------------------------------------------------------------------------------------------")
          elif ch2 == 2:
            viewSingleFromAdmin_A()
          else:
            print("Please choose correct option")

        elif ch==2:
          ch2 = int(input("Would you like to view all residents or a single one?\n\n1. All\n2. Selective\n\n Enter your choice :  "))
          if ch2 == 1:
            mycursor.execute("select * from SECTOR_B1")
            myresult=mycursor.fetchall()
            print("----------------------------------------------------------------------------------------------------------------")
            print("H_no",space("H_no"),"Name",space("Name"),"Ph_no",space("Ph_no"),"bill_issued",space("bill_issued"),"units_consumed",space("units_consumed"),"total_amt",space("total_amt"),"Paid_Unpaid")
            print("----------------------------------------------------------------------------------------------------------------")
            
            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(str(x[1])),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
                print("--------------------------------------------------------------------------------------------------------------------")
          elif ch2 == 2:
            viewSingleFromAdmin_B()
          else:
            print("Please choose correct option")

        ans=input("Back to the main menu(y for yes, n for no)\t")

        

 
# USER

def user():

    ans='y'
    while ans=='y' or ans=='Y':
        
        print("**********************************************************************")
        print("*\t\t      BSES ELECTRICITY BILLING SYSTEM                *")
        print("*\t\t            Select a Sector :                        *")
        print("*\t\t            1.  SECTOR_A1                            *")
        print("*\t\t            2.  SECTOR_B1                            *")
        print("**********************************************************************\n\n")
     
        ch=int(input("Enter your choice : "))
        if ch==1:
            consmenu_a()       
        elif ch==2:
            consmenu_b()
        else:
            print("Wrong Choice, Please choose the correct sector")

        ans=input("Back to the main menu(y for yes, n for no)\t")




#_MAIN_
      
x=check_connection()
if x==1:
    create_database()
    create_table()
else:
    print("Kindly check connection")

mycon = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="aditya",
  auth_plugin="mysql_native_password",
  database="elec_bills"
)
mycursor = mycon.cursor()

sql_select_query = "DROP TABLE SECTOR_A1"

mycursor.execute(sql_select_query)

sql_select_query = "DROP TABLE SECTOR_B1"

mycursor.execute(sql_select_query)

create_table()
add_new_record_a()
add_new_record_b()

userPasswords = {}
setUpPasswords()

ans='y'
while ans=='y' or ans=='Y':
    
    print("**********************************************************************")
    print("*\t\t      BSES ELECTRICITY BILLING SYSTEM                *")
    print("*\t\t              Enter as :                             *")
    print("*\t\t              1.  RESIDENT                           *")
    print("*\t\t              2.  ADMIN                              *")
    print("**********************************************************************\n\n")
 
    ch=int(input("Enter your choice : "))
    if ch==1:
      user()       
    elif ch==2:
      admin()
    else:
        print("Wrong Choice, Please choose the correct sector")

    ans=input("Back to the main menu(y for yes, n for no)\t")
