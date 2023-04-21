import mysql.connector
import prettytable
def mainwindow():
    print("""+--------------------------------------------------------------------------------------------------------------------+
        |                                                                                                                    |
        |    |      |    |  | _/   |      /----\                                                                             |
        |    |      |    |  |<_    |      |____|                                   -------                 ------            |
        |    |      |    |  |  \   |      |    |                        -------                                              |
        |    +----  +----+  +   +  +----  +    +                          ----           /\    ------                        |
        |                                                           ------   -------    /-_\           --------              |
        |    /----\  -----  |---\  |---\  -----  |---\  -----              ---- /\     /_  -\  -----                         |
        |    |____|    |    |___/  |___/  |   |  |___/    |                    /- \   /__----\              --------         |
        |    |    |    |    |  \   |      |   |  |  \     |   -------       /\/  --\ /   _____\  /\                          |
        |    +    +  -----  +   +  +      +---+  +   +    +                /- \/\   /-----     \/  \__-_        ---------    |
        |                                                           ___-__/   / -\ /__  -------/   -\   \___                 |
        |----------------------------------------------------------/_____/________/____________/____________\----------------|
        |                                                                                                                    |
        +--------------------------------------------------------------------------------------------------------------------+""")
con=mysql.connector.connect(host='localhost',
                                user='root',
                                password='3456')#===============CHANGE HERE FOR YOUR RESTPECTIVE COMPUTER
cur=con.cursor()
cur.execute("DROP DATABASE IF EXISTS AIRPORT")
cur.execute("CREATE DATABASE AIRPORT")
cur.execute("USE AIRPORT")
Messages={623101:[],623102:[],623103:[],623104:[],623105:[],623106:[],623107:[],623108:[],623109:[],623110:[],623111:[],
          623112:[],623113:[],623114:[],623115:[],623116:[],623117:[],623118:[],623119:[],623120:[],623121:[],623122:[],
          623123:[],623124:[],623125:[],623126:[],623127:[],623128:[],623129:[],623130:[],623131:[],623132:[],623133:[]}
cur.execute("""create table PLANE (FlightId INT(10) PRIMARY KEY NOT NULL, Airline VARCHAR(10) NOT NULL, Date DATE NOT NULL, GoingTo VARCHAR(10) NOT NULL, ComingFrom VARCHAR(10) NOT NULL, Departure TIME, Arrival TIME, Timing VARCHAR(10) NOT NULL)""")
sql = "INSERT INTO PLANE (FlightId, Airline, Date, GoingTo, ComingFrom, Departure, Arrival, Timing ) VALUES (%s, %s, %s, %s ,%s ,%s ,%s ,%s)"
val = [
    (2020111501, 'Air India', '2020-11-15', 'Lukla'    , 'New Delhi', None          , '01:00:00', 'ON TIME'),
    (2020111502, 'Etihad'   , '2020-11-15', 'Lukla'    , 'Kathmandu', None          , '03:00:00', 'DELAYED'),
    (2020111503, 'Indigo'   , '2020-11-15', 'Lukla'    , 'Patna'    , None          , '05:00:00', 'ON TIME'),
    (2020111504, 'Indigo'   , '2020-11-15', 'Kathmandu', 'Lukla'    , '07:00:00', None          , 'ON TIME'),
    (2020111505, 'Air India', '2020-11-15', 'New Delhi', 'Lukla'    , '09:00:00', None          , 'ON TIME'),
    (2020111506, 'Air Asia' , '2020-11-15', 'Lukla'    , 'Patna'    , None          , '11:0:000', 'ON TIME'),
    (2020111507, 'Vistara'  , '2020-11-15', 'Lukla'    , 'Kathmandu', None          , '13:00:00', 'ON TIME'),
    (2020111508, 'Etihad'   , '2020-11-15', 'Patna'    , 'Lukla'    , '15:00:00', None          , 'ON TIME'),
    (2020111509, 'Air India', '2020-11-15', 'Lukla'    , 'Patna'    , None          , '17:00:00', 'ON TIME'),
    (2020111510, 'Vistara'  , '2020-11-15', 'Kathmandu', 'Lukla'    , '21:00:00', None          , 'ON TIME'),

    (2020111601, 'Air Asia' , '2020-11-16', 'Kathmandu', 'Lukla'    , '01:00:00', None          , 'ON TIME'),
    (2020111602, 'Etihad'   , '2020-11-16', 'Lukla'    , 'Patna'    , None          , '03:00:00', 'ON TIME'),
    (2020111603, 'Vistara'  , '2020-11-16', 'Lukla'    , 'Kathmandu', None          , '05:00:00', 'ON TIME'),
    (2020111604, 'Air India', '2020-11-16', 'Patna'    , 'Lukla'    , '07:00:00', None          , 'ON TIME'),
    (2020111605, 'Indigo'   , '2020-11-16', 'Lukla'    , 'New Delhi', None          , '09:00:00', 'ON TIME'),
    (2020111606, 'Indigo'   , '2020-11-16', 'New Delhi', 'Lukla'    , '11:00:00', None          , 'ON TIME'),
    (2020111607, 'Vistara'  , '2020-11-16', 'New Delhi', 'Lukla'    , '13:00:00', None          , 'ON TIME'),
    (2020111608, 'Air India', '2020-11-16', 'Lukla'    , 'Patna'    , None          , '15:00:00', 'ON TIME'),
    (2020111609, 'Etihad'   , '2020-11-16', 'Kathmandu', 'Lukla'    , '17:00:00', None          , 'ON TIME'),
    (2020111610, 'Air India', '2020-11-16', 'New Delhi', 'Lukla'    , '21:00:00', None          , 'ON TIME'),
]
cur.executemany(sql, val)
cur.execute("CREATE TABLE STAFF (StaffId NUMERIC(6) PRIMARY KEY NOT NUll, Name VARCHAR(30) NOT NUll, DOB DATE NOT NUll, Occupation VARCHAR(40) NOT NUll, Passcode VARCHAR(7) NOT NUll, Salary NUMERIC(7) NOT NULL, Activity VARCHAR(15))")
sql2 = "INSERT INTO STAFF (StaffId, Name, DOB, Occupation, Passcode, Salary, Activity) VALUES (%s, %s, %s, %s ,%s, %s, %s)"
val2 = [
    ( 623101, 'Prem Mahajan', '1979-11-05', 'Air Traffic Controller', 'pre@101', 4000000, "Active"),
    ( 623102, 'Aditya Maharaj', '1991-04-10', 'Air Traffic Controller', 'adi@102', 3500000, "Left"),
    ( 623103, 'Aradhana Karpe', '1982-12-16', 'Flight Dispatcher', 'ara@103', 2500000, "Active"),
    ( 623104, 'Miraya Goyal', '1994-03-05', 'Flight Dispatcher', 'mir@104', 2500000, "Active"),
    ( 623105, 'Nilima Handa', '1979-06-01', 'Dispatcher', 'nil@105', 3100000, "Active"),
    ( 623106, 'Darika Mutti', '1989-11-08', 'Dispatcher', 'dar@106', 3000000, "Active"),
    ( 623107, 'Adah Bose', '1993-01-07', 'Engineer', 'ada@107', 1800000, "Active"),
    ( 623108, 'Anjali Arya' , '1984-10-02', 'Engineer', 'anj@108', 1700000, "Active"),
    ( 623109, 'Sonam Shukla', '1996-10-03', 'Aircraft Maintainence Technician', 'son@109', 655000, "Active"),
    ( 623110, 'Dipti Sheth', '1998-09-04', 'Aircraft Maintainence Technician', 'dip@110', 650000, "Active"),
    ( 623111, 'Pratibha Kakar', '1995-04-30', 'Flight Attendent', 'pra@111', 850000, "Active"),
    ( 623112, 'Shanaya Roy' , '1996-04-29', 'Flight Attendent', 'sha@112', 500000, "Active"),
    ( 623113, 'Tanvi Comar' , '1998-10-21', 'Flight Attendent', 'tan@113', 500000, "Active"),
    ( 623114, 'Diya Parmar' , '1997-07-06', 'Flight Attendent', 'diy@114', 500000, "Active"),
    ( 623115, 'Shakti Radhakrishnan', '1998-02-09', 'Flight Attendent', 'sha@115', 500000, "Active"),
    ( 623116, 'Akhil Mathur', '1979-05-15', 'Security Supervisor', 'akh@116', 810000, "Active"),
    ( 623117, 'Dayaram Deshmukh', '1980-08-12', 'Security Guard', 'day@117', 200000, "Active"),
    ( 623118, 'Sarvesh Bawa', '1980-01-30', 'Security Guard', 'sar@118', 200000, "Active"),
    ( 623119, 'Sandip Soni', '1987-08-25', 'Security Guard', 'san@119', 200000, "Active"),
    ( 623120, 'Aarav Lal', '1981-07-28', 'Flight Pilot', 'aar@120', 2600000, "Active"),
    ( 623121, 'Sunil Sinha', '1992-03-31', 'Flight Pilot', 'sun@121', 2300000, "Active"),
    ( 623122, 'Madhur Palan', '1981-09-11', 'Janitor', 'mad@122', 180000, "Active"),
    ( 623123, 'Indrajit Reddy', '1983-09-13', 'Janitor', 'ind@123', 180000, "Active"),
    ( 623124, 'Rajiv Agate', '1986-11-14', 'Janitor', 'raj@124', 180000, "Active"),
    ( 623125, 'Pravin Ben', '1995-05-27', 'Receptionist', 'pra@125', 750000, "Active"),
    ( 623126, 'Adnan Narang', '1990-05-26', 'Baggage Transporter', 'adn@126', 190000, "Active"),
    ( 623127, 'Harsh Pandya', '1990-08-24', 'Baggage Transporter', 'har@127', 190000, "Active"),
    ( 623128, 'Anuj Prabhu', '1982-09-17', 'Baggage Transporter', 'anu@128', 190000, "Active"),
    ( 623129, 'Anik Gupta', '1984-11-23', 'Baggage Transporter', 'ani@129', 190000, "Active"),
    ( 623130, 'Abhinav Sodhi', '1988-07-19', 'Paramedic', 'abh@130', 1400000, "Active"),
    ( 623131, 'Anuj Luthra', '1996-06-18', 'Paramedic', 'anu@131', 1100000, "Active"),
    ( 623132, 'Ankur Saini' , '1985-04-20', 'Cook', 'ank@132', 450000, "Active"),
    ( 623133, 'Adityawardhan Mishra', '1989-12-22', 'Manager', 'aditya1', 1610000, "Active")
]
cur.executemany(sql2, val2)
cur.execute("CREATE TABLE PASSENGER (TicketId NUMERIC(6) PRIMARY KEY NOT NUll, Name VARCHAR(30) NOT NUll, FlightId NUMERIC(10) NOT NUll, Seat VARCHAR(3) NOT NUll)")
sql3 = "INSERT INTO PASSENGER (TicketId, Name, FlightId, Seat) VALUES (%s, %s, %s, %s)"
val3 = [
    ( 7201,'Samson Ellwood', 2020111504, '01A'),
    ( 7202,'Hester Milner', 2020111504, '01B'),
    ( 7203,'Della Turner', 2020111504, '02A'),
    ( 7204,'Willie Fisher', 2020111504, '02B'),
    ( 7205,'Kailash Gole', 2020111504, '03A'),
    ( 7206,'Swarna Gole', 2020111504, '03B'),
    ( 7207,'Kalyani Upadhyay', 2020111504, '04A'),
    ( 7208,'Ayush Gill', 2020111504, '04B'),
    ( 7209,'Suman Bhagat', 2020111504, '05A'),
    ( 7210,'Morris Erickson', 2020111504, '05B'),
    ( 7211,'Bhavana Bora', 2020111504, '06A'),
    ( 7212,'Abraham Harris', 2020111504, '06B'),
    ( 7213,'Maria Harris', 2020111504, '07A'),
    ( 7214,'Camille Burrows', 2020111504, '07B'),
    ( 7215,'Shreya Sinha', 2020111504, '08A'),
    ( 7216,'Zoya Samra', 2020111504, '08B'),
    ( 7301,'Ivan Joseph', 2020111505, '01A'),
    ( 7302,'Fay Crossley', 2020111505, '01B'),
    ( 7303,'Karson Peralta', 2020111505, '02A'),
    ( 7304,'Maxwell Peralta', 2020111505, '02B'),
    ( 7305,'Roger Sherman', 2020111505, '03A'),
    ( 7306,'Halle Stephens', 2020111505, '03B'),
    ( 7307,'Harish Ghosh', 2020111505, '04A'),
    ( 7308,'Dhruv Srinivas', 2020111505, '04B'),
    ( 7309,'Dev Mukherjee', 2020111505, '05A'),
    ( 7310,'Vihaan Sampath', 2020111505, '05B'),
    ( 7311,'Julia Henry', 2020111505, '06A'),
    ( 7312,'Timothea Hopkins', 2020111505, '06B'),
    ( 7313,'Rishi Pradhan', 2020111505, '07A'),
    ( 7314,'Gautam Choudhary', 2020111505, '07B'),
    ( 7315,'Radha Garg', 2020111505, '08A'),
    ( 7316,'Richa Divan', 2020111505, '08B'),
]
cur.executemany(sql3, val3)
m=1
tr=1
print(">>> Are you running this program in fullscreen? (Enter y/n)")
yn1=input("""
>>> """)
while m!=0:
    if yn1=="y" and tr ==1:
        mainwindow()
        print("""                                           Welcome to The Lukla Airport Software(Trial0.01)
                                               Software Created by Adityawardhan Mishra
                                        The Lukla Airport Software Helps You to Easily navigate
                                          our various services with way more easy and privacy 

                                   This software is made for usage by anyone present at the Airport
                                      and has various uses too. We sincerely hope you are able to
                                        enjoy your experience here on our cyberspace enviroment
                                            Please use the Guide option provided on the Main
                                              Menu to learn how to navigate through our
                                                               Software.

                                                                  ^-^""")
    if yn1=="n" and tr ==1:
        print("""
>>> Welcome to The Lukla Airport Software(Trial0.01)
    Software Created by Adityawardhan Mishra & Shashank Sundar
    The Lukla Airport Software Helps You to Easily navigate
    our various services with way more easy and privacy. 

    This software is made for usage by anyone present at the Airport
    and has various uses too. We sincerely hope you are able to
    enjoy your experience here on our cyberspace enviroment
    Please use the Guide option provided on the Main
    Menu to learn how to navigate through our Software.

""")
    print("""
>>> Would you like to...

    1. Use Guide       (Enter 1)
    2. Use Program     (Enter 2)
    3. Exit            (Enter 3)""")       
    q_0_0=int(input("""
>>> """))
    while q_0_0==1:
        print("""
>>> These are some of the common issues that our users face

    1. How to Enter the Responses?
    Ans. The answer is simple. If you want to select the 
    Administrator amongst these three,
              
        1. Check Ticket
        2. Check Flight
        3. Exit
              
    You can simply type 1 when Enter option is given( This is 
    applicable throughout the system). If there is any other 
    method used, then it's usage technique it described
    ---------------------------------------------------------          

    2. Staff or Passenger, which one to select?
    Ans. Staff Option has been provided for Airport officials,
    So they can easily use it various purposes like loging in
    the system, checking daily issues, etc.

    So if you are just using this software to get on a plane
    or get information regarding a plane, please Use Passenger
    option.
    ---------------------------------------------------------

    3. Will My personal data given during the Order placement 
    be stealed?
    Ans. We assure you that absolute confidentiality will be 
    maintained and Your data will not be given to any third 
    party agents
    ---------------------------------------------------------
    
    4. How to modify or add the data appropriately?
    Ans. Modification or Addition are the options provided to
    certain staff members only.
    ---------------------------------------------------------
    
    We hope that we were able to help you :)
      
    If You still have any queries, please contact Airport 
    Officials.
                            

>>> You will now be redirected to main options...
""")
        tr=0
        break
    leave=0    
    while q_0_0==2 and leave==0:
        print("""
>>> Would you like to use program as...

    1. Staff
    2. Passenger
    3. Exit""")
        q_4_5=int(input("""
>>> """))
        if q_4_5==1:
            print("""
>>> Enter ID""")
            q_0_0_0=int(input("""
>>> """))

            print("""
>>> Enter Passcode""")
            q_0_0_1=input("""
>>> """)
            sql_select_query = """select * from STAFF where StaffId = %s"""
            cur.execute(sql_select_query, (q_0_0_0,))
            reco= cur.fetchall()            
            if cur.rowcount==1:                                                        
                for row in reco:
                    if row[4]==q_0_0_1:
                        k=0
                        while row[3]=="Manager" and k==0:
                            print("""
>>> Welcome,""", row[1] ,"""to the Administrative Menu.
""")
                            print("""
>>> What task would you like to do...

    1. Change/View Records of Staff       (Enter 1)
    2. Change/View Records of Plane       (Enter 2)
    3. Change/View Records of Passenger   (Enter 3)
    4. Send/View Notices                  (Enter 4)
    5. Exit to Main Menu                  (Enter 5)

    """)
                            q_0_1=int(input("""
>>> """))
                            trf0=1                           
                            while q_0_1==1 and trf0==1:
                                print("""
>>> What would you like to do in Staff Records...

    1. Delete Record
    2. Modify Record
    3. Add Record
    4. View Record
    5. Exit """)
                                q_0_1_1=int(input("""
>>> """))
                                if q_0_1_1==1:
                                    trf1=1                                    
                                    while trf1==1:
                                        print("""
>>> Please enter StaffId of the record you want to delete...""")
                                        q_0_2=int(input("""
>>> """))
                                        sql_select_query_1 = """select * from STAFF where StaffId = %s"""
                                        cur.execute(sql_select_query_1, (q_0_2,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==1:                
                                            sql_select_query_9 = """delete from STAFF where StaffId = %s"""
                                            cur.execute(sql_select_query_9, (q_0_2,))
                                            print("""
>>> Record Deleted Successfully...

>>> Do you still want to delete more records(y/n)""")
                                            yn2=input("""
>>> """)
                                            if yn2=="n":
                                                trf1=0
                                            else:
                                                continue
                                        if cur.rowcount==0:
                                            print("""
>>> Please enter valid StaffID...""")
                                            trf1=0                            
                                if q_0_1_1==2:
                                    trf2=1
                                    print("""
>>> Please enter StaffId of the record you want to modify""")
                                    q_0_3=int(input("""
>>> """))
                                    while trf2==1:                                       
                                        sql_select_query_1 = """select * from STAFF where StaffId = %s"""
                                        cur.execute(sql_select_query_1, (q_0_3,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==1:
                                            print("""
>>> What would you like to change...

    1. Name
    2. Date of Birth
    3. Occupation
    4. Passcode
    5. Salary
    6. Activity
    7. Exit
""")
                                            q_0_3_1=int(input("""
>>> """))
                                            if q_0_3_1==1:
                                                print("""
>>> Please Enter the Name replacing the Present Value""")
                                                q_0_3_2=input("""
>>> """)
                                                sql_update_query_0="""UPDATE STAFF SET Name = %s WHERE StaffId = %s"""
                                                val_update_0=(q_0_3_2,q_0_3)
                                                cur.execute(sql_update_query_0,val_update_0)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn2=input("""
>>> """)
                                                if yn2=="n":
                                                    trf2=0
                                                else:
                                                    k=1
                                                    continue                                        
                                            elif q_0_3_1==2:
                                                print("""
>>> Please Enter the Date of Birth replacing the Present Value""")
                                                q_0_3_3=input("""
>>> """)
                                                sql_update_query_2="""UPDATE STAFF SET DOB = %s WHERE StaffId = %s"""
                                                val_update_1=(q_0_3_3,q_0_3)
                                                cur.execute(sql_update_query_2,val_update_1)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn3=input("""
>>> """)
                                                if yn3=="n":
                                                    trf2=0
                                                else:
                                                    k=1
                                                    continue                                        
                                            elif q_0_3_1==3:
                                                print("""
>>> Please Enter the Occupation replacing the Present Value""")
                                                q_0_3_4=input("""
>>> """)
                                                sql_update_query_3="""UPDATE STAFF SET Occupation = %s WHERE StaffId = %s"""
                                                val_update_2=(q_0_3_4,q_0_3)
                                                cur.execute(sql_update_query_3,val_update_2)
                                                print("""
>>> Data Updated Successfully...""")                                                
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn4=input("""
>>> """)
                                                if yn4=="n":
                                                    trf2=0
                                                else:
                                                    k=1
                                                    continue                                        
                                            elif q_0_3_1==4:
                                                print("""
>>> Please Enter the Passcode replacing the Present Value""")
                                                q_0_3_5=input("""
>>> """)
                                                sql_update_query_4="""UPDATE STAFF SET Passcode = %s WHERE StaffId = %s"""
                                                val_update_3=(q_0_3_5,q_0_3)
                                                cur.execute(sql_update_query_4,val_update_3)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn5=input("""
>>> """)
                                                if yn5=="n":
                                                    trf2=0
                                                else:
                                                    continue
                                            elif q_0_3_1==5:
                                                print("""
>>> Please Enter the Salary replacing the Present Value""")
                                                q_0_3_6=input("""
>>> """)
                                                sql_update_query_5="""UPDATE STAFF SET Salary = %s WHERE StaffId = %s"""
                                                val_update_4=(q_0_3_6,q_0_3)
                                                cur.execute(sql_update_query_5,val_update_4)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn6=input("""
>>> """)
                                                if yn6=="n":
                                                    trf2=0
                                                else:
                                                    continue 
                                            elif q_0_3_1==6:
                                                print("""
>>> Please Enter the Activity replacing the Present Value""")
                                                q_0_3_7=input("""
>>> """)
                                                sql_update_query_6="""UPDATE STAFF SET Activity = %s WHERE StaffId = %s"""
                                                val_update_5=(q_0_3_7,q_0_3)
                                                cur.execute(sql_update_query_6,val_update_5)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn6=input("""
>>> """)
                                                if yn6=="n":
                                                    trf2=0
                                                else:
                                                    continue
                                            elif q_0_3_1==7:
                                                trf2=0
                                                continue
                                if q_0_1_1==3:
                                    trf3=1
                                    while trf3==1:
                                        print("""
>>> Please enter new StaffId for the record you want to add...""")
                                        q_9_1=int(input("""
>>> """))
                                        print("""
>>> Please enter Name of the record you want to add...""")
                                        q_9_2=input("""
>>> """)
                                        print("""
>>> Please enter Date of Birth of the record you want to add...""")
                                        q_9_3=input("""
>>> """)
                                        print("""
>>> Please enter Occupation of the record you want to add...""")
                                        q_9_4=input("""
>>> """)
                                        print("""
>>> Please enter Passcode of the record you want to add...""")
                                        q_9_5=input("""
>>> """)
                                        print("""
>>> Please enter Salary of the record you want to add...""")
                                        q_9_6=int(input("""
>>> """))
                                        print("""
>>> Please enter Activity of the record you want to add...""")
                                        q_9_7=input("""
>>> """)
                                        sql_select_query_1 = """select * from STAFF where StaffId = %s"""
                                        cur.execute(sql_select_query, (q_9_2,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==0:                
                                            sql_select_query_10 = "INSERT INTO STAFF (StaffId, Name, DOB, Occupation, Passcode, Salary, Activity) VALUES (%s, %s, %s, %s ,%s, %s, %s)"
                                            cur.execute(sql_select_query_10, (q_9_1,q_9_2,q_9_3,q_9_4,q_9_5,q_9_6,q_9_7))
                                            print("""
>>> Record Added Successfully...

>>> Do you still want to Add more records(y/n)""")
                                            yn7=input("""
>>> """)
                                            if yn7=="n":
                                                trf3=0
                                            else:
                                                continue                                     
                                if q_0_1_1==4:
                                    sql_view="select * from STAFF"
                                    cur.execute(sql_view)
                                    recoview1=cur.fetchall()
                                    table=prettytable.PrettyTable()
                                    table.field_names= ["StaffId", "Name", "DOB", "Occupation", "Passcode", "Salary","Activity"]
                                    for record in recoview1:
                                        table.add_row([record[0], record[1], record[2], record[3], record[4], record[5], record[6]])
                                    print(table)
                                    continue                             
                                if q_0_1_1==5:
                                    trf0=0
                                    continue                          
                            while q_0_1==2 and trf0==1:
                                print("""
>>> What would you like to do in Plane Records...

    1. Delete Record
    2. Modify Record
    3. Add Record
    4. View Record
    5. Exit""")
                                q_0_1_1=int(input("""
>>> """))
                                if q_0_1_1==1:
                                    trf4=1                                    
                                    while trf4==1:
                                        print("""
>>> Please enter FlightId of the record you want to delete...""")

                                        q_0_2=int(input("""
>>> """))
                                        sql_select_query_1 = """select * from PLANE where FlightId = %s"""
                                        cur.execute(sql_select_query_1, (q_0_2,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==1:                
                                            sql_select_query_9 = """delete from PLANE where FlightId = %s"""
                                            cur.execute(sql_select_query_9, (q_0_2,))
                                            print("""
>>> Record Deleted Successfully...

>>> Do you still want to delete more records(y/n)""")
                                            yn2=input("""
>>> """)
                                            if yn2=="n":
                                                trf4=0
                                            else:
                                                continue
                                        if cur.rowcount==0:
                                            print("""
>>> Please enter Valid FlightID...""")
                                            trf4=0                                                            
                                if q_0_1_1==2:
                                    trf5=1
                                    print("""
>>> Please enter FlightId of the record you want to modify""")
                                    q_0_3=int(input("""
>>> """))
                                    while trf5==1:
                                        
                                        sql_select_query_1 = """select * from PLANE where FlightId = %s"""
                                        cur.execute(sql_select_query_1, (q_0_3,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==1:
                                            print("""
>>> What would you like to change...

    1. Airline
    2. Date
    3. To
    4. From
    5. Departure
    6. Arrival
    7. Timing
    8. Exit
""")
                                            q_0_3_1=int(input("""
>>> """))
                                            if q_0_3_1==1:
                                                print("""
>>> Please Enter the Airline of the Flight replacing the Present Value""")
                                                q_0_3_2=input("""
>>> """)
                                                sql_update_query_0="""UPDATE PLANE SET Airline = %s WHERE FlightId = %s"""
                                                val_update_0=(q_0_3_2,q_0_3)
                                                cur.execute(sql_update_query_0,val_update_0)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn2=input("""
>>> """)
                                                if yn2=="n":
                                                    trf5=0
                                                else:
                                                    k=1
                                                    continue                                        
                                            elif q_0_3_1==2:
                                                print("""
>>> Please Enter the Airline of the Flight replacing the Present Value""")
                                                q_0_3_3=input("""
>>> """)
                                                sql_update_query_2="""UPDATE PLANE SET Date = %s WHERE FlightId = %s"""
                                                val_update_1=(q_0_3_3,q_0_3)
                                                cur.execute(sql_update_query_2,val_update_1)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn3=input("""
>>> """)
                                                if yn3=="n":
                                                    trf5=0
                                                else:
                                                    k=1
                                                    continue                                        
                                            elif q_0_3_1==3:
                                                print("""
>>> Please Enter the Destination of the Flight replacing the Present Value""")
                                                q_0_3_4=input("""
>>> """)
                                                sql_update_query_3="""UPDATE PLANE SET GoingTo = %s WHERE FlightId = %s"""
                                                val_update_2=(q_0_3_4,q_0_3)
                                                cur.execute(sql_update_query_3,val_update_2)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn4=input("""
>>> """)
                                                if yn4=="n":
                                                    trf5=0
                                                else:
                                                    k=1
                                                    continue             
                                            elif q_0_3_1==4:
                                                print("""
>>> Please Enter the Origin of the Flight replacing the Present Value""")
                                                q_0_3_5=input("""
>>> """)
                                                sql_update_query_4="""UPDATE PLANE SET ComingFrom = %s WHERE FlightId = %s"""
                                                val_update_3=(q_0_3_5,q_0_3)
                                                cur.execute(sql_update_query_4,val_update_3)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn5=input("""
>>> """)
                                                if yn5=="n":
                                                    trf5=0
                                                else:
                                                    continue
                                            elif q_0_3_1==5:
                                                print("""
>>> Please Enter the Salary replacing the value present""")
                                                q_0_3_6=input("""
>>> """)
                                                sql_update_query_5="""UPDATE PLANE SET Departure = %s WHERE FlightId = %s"""
                                                val_update_4=(q_0_3_6,q_0_3)
                                                cur.execute(sql_update_query_5,val_update_4)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn6=input("""
>>> """)
                                                if yn6=="n":
                                                    trf5=0
                                                else:
                                                    continue 
                                            elif q_0_3_1==6:
                                                print("""
>>> Please Enter the Arrival Time replacing the Present Value""")
                                                q_0_3_7=input("""
>>> """)
                                                sql_update_query_6="""UPDATE PLANE SET Arrival = %s WHERE FlightId = %s"""
                                                val_update_5=(q_0_3_7,q_0_3)
                                                cur.execute(sql_update_query_6,val_update_5)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn6=input("""
>>> """)
                                                if yn6=="n":
                                                    trf5=0
                                                else:
                                                    continue
                                            elif q_0_3_1==7:
                                                print("""
>>> Please Enter the TIMING replacing the Present Value""")
                                                q_0_3_8=input("""
>>> """)
                                                sql_update_query_7="""UPDATE PLANE SET Timing = %s WHERE FlightId = %s"""
                                                val_update_6=(q_0_3_8,q_0_3)
                                                cur.execute(sql_update_query_7,val_update_6)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn6=input("""
>>> """)
                                                if yn6=="n":
                                                    trf5=0
                                                else:
                                                    continue
                                            elif q_0_3_1==8:
                                                trf2=0
                                if q_0_1_1==3:
                                    trf6=1
                                    while trf6==1:
                                        print("""
>>> Please enter FlightId of the new record you want to add...""")
                                        q_9_1=int(input("""
>>> """))
                                        print("""
>>> Please enter Airline of the new record you want to add...""")
                                        q_9_2=int(input("""
>>> """))
                                        print("""
>>> Please enter Date of the Flight for the new record you want to add...""")
                                        q_9_3=int(input("""
>>> """))
                                        print("""
>>> Please enter where the Flight is going to for the new record you want to add...""")
                                        q_9_4=int(input("""
>>> """))
                                        print("""
>>> Please enter where the Flight is coming from for the new record you want to add...""")
                                        q_9_5=int(input("""
>>> """))
                                        print("""
>>> Please enter Departure Time of the new record you want to add...""")
                                        q_9_6=int(input("""
>>> """))
                                        print("""
>>> Please enter Arrival Time of the new record you want to add...""")
                                        q_9_7=int(input("""
>>> """))
                                        print("""
>>> Please enter Timing of the Flight for the new record you want to add...""")
                                        q_9_8=int(input("""
>>> """))
                                        
                                        sql_select_query_1 = """select * from PLANE where FlightId = %s"""
                                        cur.execute(sql_select_query_1, (q_9_1,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==0:                
                                            sql_select_query_10 = "INSERT INTO PLANE (FlightId, Airline, Date, GoingTo, ComingFrom, Departure, Arrival, Timing) VALUES (%s, %s, %s, %s ,%s, %s, %s, %s)"
                                            cur.execute(sql_select_query_10, (q_9_1,q_9_2,q_9_3,q_9_4,q_9_5,q_9_6,q_9_7,q_9_8))
                                            print("""
>>> Record Add Successfully...

>>> Do you still want to Add more records(y/n)""")
                                            yn7=input("""
>>> """)
                                            if yn7=="n":
                                                trf6=0
                                            else:
                                                continue
                                        else:
                                            print("""
>>> Please enter valid StaffID...""")
                                            continue         
                                if q_0_1_1==4:
                                    sql_view="select * from PLANE"
                                    cur.execute(sql_view)
                                    recoview2=cur.fetchall()
                                    table=prettytable.PrettyTable()
                                    table.field_names= ["FlightId", "Airline", "Date", "To", "From", "Departure","Arrival", "Timing"]
                                    for record in recoview2:
                                        table.add_row([record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]])
                                    print(table)
                                    continue
                                if q_0_1_1==5:
                                    trf0=0
                                    continue                        
                            while q_0_1==3 and trf0==1:
                                print("""
>>> What would you like to do in Passenger Records...

    1. Delete Record
    2. Modify Record
    3. Add Record
    4. View Record
    5. Exit""")
                                q_0_1_1=int(input("""
>>> """))
                                if q_0_1_1==1:
                                    trf7=1
                                    while trf7==1:
                                        print("""
>>> Please enter TicketId of the record you want to delete...""")

                                        q_0_2=int(input("""
>>> """))
                                        sql_select_query_1 = """select * from PASSENGER where TicketId = %s"""
                                        cur.execute(sql_select_query_1, (q_0_2,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==1:                
                                            sql_select_query_9 = """delete from PASSENGER where TicketId = %s"""
                                            cur.execute(sql_select_query_9, (q_0_2,))
                                            print("""
>>> Record Deleted Successfully...

>>> Do you still want to delete more records(y/n)""")
                                            yn2=input("""
>>> """)
                                            if yn2=="n":
                                                trf7=0
                                            else:
                                                continue
                                        if cur.rowcount==0:
                                            print("""
>>> Please enter valid TicketID...""")
                                            trf7=0
                                                            
                                if q_0_1_1==2:
                                    trf8=1
                                    while trf8==1:
                                        print("""
>>> Please enter TicketId of the record you want to modify""")
                                        q_0_3=int(input("""
>>> """))
                                        sql_select_query_1 = """select * from PASSENGER where TicketId = %s"""
                                        cur.execute(sql_select_query, (q_0_3,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==1:
                                            print("""
>>> What would you like to change...

    1. Name
    2. FlightId
    3. Seat
    4. Exit
""")
                                            q_0_3_1=int(input("""
>>> """))
                                            if q_0_3_1==1:
                                                print("""
>>> Please Enter the Name replacing the present value """)
                                                q_0_3_2=input("""
>>> """)
                                                sql_update_query_0="""UPDATE PLANE SET Airline = %s WHERE FlightId = %s"""
                                                val_update_0=(q_0_3_2,q_0_3)
                                                cur.execute(sql_update_query_0,val_update_0)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn2=input("""
>>> """)
                                                if yn2=="n":
                                                    trf8=0
                                                else:
                                                    k=1
                                                    continue                                        
                                            elif q_0_3_1==2:
                                                print("""
>>> Please Enter the FlightId replacing the present value """)
                                                q_0_3_3=input("""
>>> """)
                                                sql_update_query_2="""UPDATE PLANE SET Date = %s WHERE FlightId = %s"""
                                                val_update_1=(q_0_3_3,q_0_3)
                                                cur.execute(sql_update_query_2,val_update_1)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn3=input("""
>>> """)
                                                if yn3=="n":
                                                    trf2=0
                                                else:
                                                    k=1
                                                    continue                                        
                                            elif q_0_3_1==3:
                                                print("""
>>> Please Enter the Seat replacing the value present""")
                                                q_0_3_4=input("""
>>> """)
                                                sql_update_query_3="""UPDATE PLANE SET GoingTo = %s WHERE FlightId = %s"""
                                                val_update_2=(q_0_3_4,q_0_3)
                                                cur.execute(sql_update_query_3,val_update_2)
                                                print("""
>>> Data Updated Successfully...""")
                                                print("""
>>> Do you want to change more details(y/n)""")
                                                yn4=input("""
>>> """)
                                                if yn4=="n":
                                                    trf2=0
                                                else:
                                                    k=1
                                                    continue
                                            elif q_0_3_1==8:
                                                trf2=0                                            
                                if q_0_1_1==3:
                                    trf3=1
                                    while trf3==1:
                                        print("""
>>> Please enter TicketId of the new record you want to add...""")
                                        q_9_1=int(input("""
>>> """))
                                        print("""
>>> Please enter Name of the new record you want to add...""")
                                        q_9_2=int(input("""
>>> """))
                                        print("""
>>> Please enter FlightId for the new record you want to add...""")
                                        q_9_3=int(input("""
>>> """))
                                        print("""
>>> Please enter The Seatthe new record you want to add...""")
                                        q_9_4=int(input("""
>>> """))                                      
                                        sql_select_query_1 = """select * from PASSENGER where TicketId = %s"""
                                        cur.execute(sql_select_query_1, (q_9_1,))
                                        reco= cur.fetchall()
                                        if cur.rowcount==0:                
                                            sql_select_query_10 = "INSERT INTO PASSENGER (TicketId, Name, FlightId, Seat) VALUES (%s, %s, %s, %s)"
                                            cur.execute(sql_select_query_10, (q_9_1,q_9_2,q_9_3,q_9_4))
                                            print("""
>>> Record Add Successfully...

>>> Do you still want to Add more records(y/n)""")
                                            yn7=input("""
>>> """)
                                            if yn7=="n":
                                                trf3=0
                                            else:
                                                continue
                                        else:
                                            print("""
>>> Please enter valid StaffID...""")
                                            continue                            
                                if q_0_1_1==4:
                                    sql_view="select * from PASSENGER"
                                    cur.execute(sql_view)
                                    recoview2=cur.fetchall()
                                    table=prettytable.PrettyTable()
                                    table.field_names= ["TicketId", "Name", "FlightId", "Seat No."]
                                    for record in recoview2:
                                        table.add_row([record[0], record[1], record[2], record[3]])
                                    print(table)
                                    continue                                    
                                if q_0_1_1==5:
                                    trf0=0
                                    continue                       
                            while q_0_1==4 and trf0==1:
                                print("""
>>> What would you like to do...

    1. Send Messages
    2. View Messages
    3. Exit""")
                                q_6_1=int(input(""">>> """))
                                trf10=1
                                while q_6_1==1 and trf10==1:
                                    print("""
>>> Please Enter the StaffId of the person you would like to send the message to...""")
                                    messagereciever=int(input("""
>>> """))
                                    print("""
>>> Please Enter the Message""")
                                    message=str(input("""
>>> """))
                                    Messages[messagereciever]+=[message]
                                    print("""
>>> Message sent

>>> Would you like to send more messages?(y/n)""")
                                    yn10=input("""
>>> """)
                                    if yn10=="n":
                                        trf10=0
                                    else:
                                        continue
                                if q_6_1==2:
                                    reciever=row[0]
                                    print(">>> Here are all your messages from Security Advisor")
                                    for i in range(0,len(Messages[reciever])):
                                        print("""
        >>> """,Messages[reciever][i])
                                        
                                if q_6_1==3:
                                    trf0=0                    
                            if q_0_1==5:
                                k=1
                        while (row[3]=="Security Supervisor" or row[3]=="Security Guard") and k==0:                                
                            print("""
>>> Welcome,""", row[1] ,"""to the Security Menu.
""")
                            print("""
>>> What task would you like to do...

    1. View Records of Staff              (Enter 1)
    2. View Records of Plane              (Enter 2)
    3. View Records of Passenger          (Enter 3)
    4. Send/View Messages to Manager      (Enter 4)
    5. Exit to Main Menu                  (Enter 5)

    """)
                            q_7_1=int(input("""
>>> """))
                            trf0=1
                            if q_7_1==1:
                                sql_view="select * from STAFF"
                                cur.execute(sql_view)
                                recoview1=cur.fetchall()
                                table=prettytable.PrettyTable()
                                table.field_names= ["StaffId", "Name", "Occupation","Activity"]
                                for record in recoview1:
                                    table.add_row([record[0], record[1], record[3],record[6]])
                                print(table)
                                continue
                            if q_7_1==2:
                                sql_view="select * from PLANE"
                                cur.execute(sql_view)
                                recoview2=cur.fetchall()
                                table=prettytable.PrettyTable()
                                table.field_names= ["FlightId", "Airline", "Date", "To", "From", "Departure","Arrival", "Timing"]
                                for record in recoview2:
                                    table.add_row([record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]])
                                print(table)
                                continue
                            if q_7_1==3:
                                sql_view="select * from PASSENGER"
                                cur.execute(sql_view)
                                recoview2=cur.fetchall()
                                table=prettytable.PrettyTable()
                                table.field_names= ["TicketId", "Name", "FlightId", "Seat No."]
                                for record in recoview2:
                                    table.add_row([record[0], record[1], record[2], record[3]])
                                print(table)
                                continue
                            if q_7_1==4 and trf0==1:
                                print("""
>>> What would you like to do...

    1. Send Messages
    2. View Messages
    3. Exit""")
                                q_6_1=int(input("""
>>> """))
                                trf10=1
                                if q_6_1==1 and trf10==1 and row[3]!="Security Supervisor":
                                    print("""
>>> You are not allowed to Send messages to Manager...""")
                                    continue
                                while q_6_1==1 and trf10==1 and row[3]=="Security Supervisor":
                                    sql_select_query = """select * from STAFF where Occupation = 'Manager'"""
                                    cur.execute(sql_select_query)
                                    admin= cur.fetchall()
                                    chi=1
                                    if cur.rowcount==1 and chi==1:
                                        for kem in admin:
                                            adminId=kem[0]
                                            chi=1
                                            break
                                    print("""
>>> Please Enter the Message""")
                                    message=str(input("""
>>> """))
                                    Messages[adminId]+=[message]
                                    print("""
>>> Message sent

>>> Would you like to send more messages?""")
                                    yn10=input("""
>>> """)
                                    if yn10=="n":
                                        trf10=0
                                    else:
                                        continue
                                if q_6_1==2:
                                    reciever=row[0]
                                    print("Here are all your messages from The Manager")
                                    for i in range(0,len(Messages[reciever])):
                                        print("""
        >>> """,Messages[reciever][i])        
                            if q_7_1==5:
                                k=1
                        k=0
                        while (row[3]!="Security Supervisor" and row[3]!="Security Guard" and row[3]!="Manager") and k==0:
                            print("""
>>> Welcome,""", row[1] ,"""to the Staff Menu.
""")
                            print("""
>>> What task would you like to do...

    1. View Messages From Manager         (Enter 1)
    2. Exit to Main Menu                  (Enter 2)

    """)
                            q_7_1=int(input("""
>>> """))
                            trf0=1
                            if q_7_1==1:
                                reciever=row[0]
                                print("Here are all your messages from The Manager")
                                for i in range(0,len(Messages[reciever])):
                                    print("""
        >>> """,Messages[reciever][i])
                            if q_7_1==2:
                                k=1
                    else:
                        print("""
>>> Invalid Password""")
                        break
            else:
                print("""
>>> Sorry but Id is wrong""")
                continue
        k=0        
        while q_4_5==2 and k==0:
            print("""
>>> Please Enter TicketId...""")
            q_5_1=int(input("""
>>> """))
            sql_select_query = """select * from PASSENGER where TicketId = %s"""
            cur.execute(sql_select_query, (q_5_1,))
            view= cur.fetchall()
            if cur.rowcount==1:                                          
                for row in view:
                    k=row[2]
                    sql_selectplane="""select * from PLANE where FlightId = %s"""
                    cur.execute(sql_selectplane,(k,))
                    plane=cur.fetchall()
                    for row2 in plane:
                        table=prettytable.PrettyTable()
                        table.field_names= ["TicketId", "Name", "FlightId", "Airlines","Seat No.", "Date", "From", "To","Arrival Time", "Departure Time", "Timing"]
                        table.add_row([row[0], row[1], row[2], row2[1], row[3], row2[2], row2[3], row2[4], row2[5], row2[6], row2[7]])
                        print(table)
                        leave2=0
        if q_4_5==3:
            leave=1
    if q_0_0==3:
        m=0
        print("""
>>> Thanks for using :)""")
        break
