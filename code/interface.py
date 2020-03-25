import tkinter as tk
import tkinter.font as tkFont
import pymysql
import datetime
import os
from PIL import Image, ImageTk
from tkinter import messagebox

#initialize connection to sql server
db = pymysql.connect("localhost","cupid","0000","project")
#cursor object definition
cursor = db.cursor()

root = tk.Tk()
root.title('NTU WeBike')
root.geometry('500x350')
root.configure(background='LightCyan')
f1 = tkFont.Font(family='Helvetica', size=16)
f2 = tkFont.Font(family='Arial Black', size=30)



class frontpage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='WeBike',font=('SentyTang', 50), fg="red", bg='LightCyan')
        self.header.grid(row=0,columnspan=2)

        self.logo = Image.open('logo.jpg')
        self.photo = ImageTk.PhotoImage(self.logo)
        self.labelLogo = tk.Label(self.page, text='logo',image=self.photo,bg="LightCyan",font=f1)
        self.labelLogo.grid(row=1,columnspan=2)

        self.register_button = tk.Button(self.page, text = 'Register', command=self.to_register_page,width=10,fg='red',font=f1)
        self.register_button.grid(row=2,column=0,ipadx=20, padx=30)
        self.login_button = tk.Button(self.page, text = 'Login', command = self.to_login_page,width=10,font=f1)
        self.login_button.grid(row=2,column=1,ipadx=20)

    def to_register_page(self):
        self.page.destroy()
        mainpage(self.root)

    def to_login_page(self):
        self.page.destroy()
        loginpage(self.root)
#----------------------------------Register pages-----------------------------------------------------------

class mainpage(object):
    def __init__(self, master=None):
        self.root = master 
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Register',bg='LightCyan',pady=10,font=f2)
        self.header.grid(row = 0,columnspan=3)

        self.user_Button = tk.Button(self.page, text='Register User',command=self.to_user_page,font=f1) 
        self.user_Button.grid(column=0,row=1,pady=30,padx=5) 
        self.bike_Button = tk.Button(self.page, text='Register Bike',command=self.to_bike_page,font=f1) 
        self.bike_Button.grid(column=1,row=1,padx=5) 
        self.employee_Button = tk.Button(self.page, text='Register Employee',command=self.to_employee_page,font=f1) 
        self.employee_Button.grid(column=2,row=1,sticky='e') 
        self.return_button = tk.Button(self.page, text = 'Back', command = self.back_to_top,width=10,font=f1)
        self.return_button.grid(column=1,pady=20)


    def to_user_page(self):
        self.page.destroy()
        Userpage(self.root)

    def to_bike_page(self):
        self.page.destroy()
        Bikepage(self.root)

    def to_employee_page(self):
        self.page.destroy()
        Employeepage(self.root)

    def back_to_top(self):
        self.page.destroy()
        frontpage(self.root)
    
  
class Userpage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Register User',bg='LightCyan',pady=10,font=f2)
        self.header.grid(row = 0,columnspan=2)

        self.name_frame = tk.Label(self.page, text='Name: ',bg='LightCyan',font=f1)
        self.name_frame.grid(row = 1, column = 0,pady=10)
        self.name_entry = tk.Entry(self.page)
        self.name_entry.grid(row = 1, column = 1,pady=10)
        self.id_frame = tk.Label(self.page, text='Student ID: ',bg='LightCyan',font=f1)
        self.id_frame.grid(row = 2, column = 0)
        self.id_entry = tk.Entry(self.page)
        self.id_entry.grid(row = 2, column = 1)

        self.register_button = tk.Button(self.page, text = 'register', command = self.get_info,font=f1)
        self.register_button.grid(row = 3, column = 1,pady=40)
        self.Button = tk.Button(self.page, text='Go Back',command=self.mainpage,font=f1) 
        self.Button.grid(row = 3, column = 0,pady=40)

    def user_reg(self, name, ID):
        sql = "INSERT INTO _User (StudentID, StudentName) VALUES ('%s', '%s')"%(ID, name)
        print("sql:", sql)#
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("error")
            db.rollback()

    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)

    def get_info(self):
        if not self.id_entry.get():
            message=messagebox.showwarning("Warning",'Student ID missed!')
        else:
            name = self.name_entry.get()
            studentid = self.id_entry.get()
            ####user_create(name, studentid)
            self.name_entry.delete(0, 'end')
            self.id_entry.delete(0, 'end')
            message=messagebox.showwarning("Warning",'Student ' + name + ' successfully registered!')
            self.user_reg(name, studentid)


class Bikepage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Register Bike',bg='LightCyan',pady=10,font=f2)
        self.header.grid(row = 0,columnspan=2)

        self.bike_id_frame = tk.Label(self.page, text='Bike ID: ',bg='LightCyan',font=f1)
        self.bike_id_frame.grid(row = 1, column = 0)
        self.bike_id_entry = tk.Entry(self.page)
        self.bike_id_entry.grid(row = 1, column = 1)
        self.lock_id_frame = tk.Label(self.page, text='Lock ID: ',bg='LightCyan',font=f1)
        self.lock_id_frame.grid(row = 2, column = 0)
        self.lock_id_entry = tk.Entry(self.page)
        self.lock_id_entry.grid(row = 2, column = 1)
        self.lock_passwd_frame = tk.Label(self.page, text='Lock Password: ',bg='LightCyan',font=f1)
        self.lock_passwd_frame.grid(row = 3, column = 0)
        self.lock_passwd_entry = tk.Entry(self.page)
        self.lock_passwd_entry.grid(row = 3, column = 1)
        self.student_id_frame = tk.Label(self.page, text='Student ID: ',bg='LightCyan',font=f1)
        self.student_id_frame.grid(row = 4, column = 0)
        self.student_id_entry = tk.Entry(self.page)
        self.student_id_entry.grid(row = 4, column = 1)

        self.register_button = tk.Button(self.page, text = 'register', command = self.get_info,font=f1)
        self.register_button.grid(row = 5, column = 1,pady=10)
        self.Button = tk.Button(self.page, text='Go Back',command=self.mainpage,font=f1) 
        self.Button.grid(row = 5, column = 0,pady=10) 


    def bike_reg(self, bikeID, lockpswd, studentID):
        sql = "INSERT INTO Bike (BikeID, Lock_Password, Renting, OwnerID) VALUES ('%s', '%s', 0, '%s')" % (bikeID, lockpswd, studentID)
        print("sql:", sql)
        #try:
        cursor.execute(sql)
        db.commit()
        # except:
        #     print("error")
        #     db.rollback()


    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)  

    def get_info(self):
        if not self.student_id_entry.get():
            message=messagebox.showwarning("Warning",'Student ID missed!')
        elif not self.bike_id_entry.get():
            message=messagebox.showwarning("Warning",'Bike ID missed!')
        else:
            bike_id = self.bike_id_entry.get()
            lock_id = self.lock_id_entry.get()
            lock_passwd = self.lock_passwd_entry.get()
            student_id = self.student_id_entry.get()
            self.bike_id_entry.delete(0, 'end')
            self.lock_id_entry.delete(0, 'end')
            self.lock_passwd_entry.delete(0, 'end')
            self.student_id_entry.delete(0, 'end')
            message=messagebox.showwarning("Warning",'Bike ' + bike_id + ' of ' + student_id + ' successfully registered!')
            self.bike_reg(bike_id, lock_passwd, student_id)


class Employeepage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Register Employee',bg='LightCyan',font=f2)
        self.header.grid(row = 0,columnspan=2)

        self.name_frame = tk.Label(self.page, text='Name: ',bg='LightCyan',font=f1)
        self.name_frame.grid(row = 1, column = 0,pady=30)
        self.name_entry = tk.Entry(self.page)
        self.name_entry.grid(row = 1, column = 1)
        self.ssn_frame = tk.Label(self.page, text='SSN: ',bg='LightCyan',font=f1)
        self.ssn_frame.grid(row = 2, column = 0)
        self.ssn_entry = tk.Entry(self.page)
        self.ssn_entry.grid(row = 2, column = 1)

        self.register_button = tk.Button(self.page, text = 'register', command = self.get_info,font=f1)
        self.register_button.grid(row = 3, column = 1,pady=40)
        self.Button = tk.Button(self.page, text='Go Back',command=self.mainpage,font=f1) 
        self.Button.grid(row = 3, column = 0) 


    def employee_reg(self, name, SSN):
        sql = "INSERT INTO Employee (EmployeeSSN, EmployeeName) VALUES ('%s', '%s')" % (SSN, name)
        print("sql:", sql)#
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("error")
            db.rollback()

    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)   

    def get_info(self):
        if not self.ssn_entry.get():
            message=messagebox.showwarning("Warning",'Employee SSN missed!')
        else:
            name = self.name_entry.get()
            SSN = self.ssn_entry.get()
            ####empolyee_create(name, SSN)
            self.name_entry.delete(0, 'end')
            self.ssn_entry.delete(0, 'end')
            message=messagebox.showwarning("Warning",'Employee ' + name + ' successfully registered!')
            self.employee_reg(name, SSN)


#--------------------------------Login pages-------------------------------------------------------------

class loginpage(object):
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Login',bg='LightCyan',font=f2)
        self.header.grid(row = 0,columnspan=2)

        self.user_login_button = tk.Button(self.page, text = 'User Login', command = self.to_login_user,font=f1)
        self.user_login_button.grid(column=0,row=1,pady=40,padx=10,sticky='e')
        self.employee_login_button = tk.Button(self.page, text = 'Employee Login', command = self.to_login_employee,font=f1)
        self.employee_login_button.grid(column=1,row=1,padx=10,sticky='e')
        self.back_button = tk.Button(self.page, text = 'Go Back', command = self.go_to_top,font=f1)
        self.back_button.grid(columnspan=2)

    def to_login_user(self):
        self.page.destroy()
        userloginpage(self.root)

    def to_login_employee(self):
        self.page.destroy()
        employeeloginpage(self.root)

    def go_to_top(self):
        self.page.destroy()
        frontpage(self.root)

class userloginpage(object):
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Login',bg='LightCyan',font=f2)
        self.header.grid(row = 0,columnspan=2)

        self.name_frame = tk.Label(self.page, text='Name: ',bg='LightCyan',font=f1)
        self.name_frame.grid(row = 1, column = 0,pady=20)
        self.name_entry = tk.Entry(self.page)
        self.name_entry.grid(row = 1, column = 1)
        self.id_frame = tk.Label(self.page, text='Student ID: ',bg='LightCyan',font=f1)
        self.id_frame.grid(row = 2, column = 0)
        self.id_entry = tk.Entry(self.page)
        self.id_entry.grid(row = 2, column = 1)

        self.login_button = tk.Button(self.page, text = 'Login', command = self.login,font=f1)
        self.login_button.grid(row = 3,column=1,pady=40)
        self.back_button = tk.Button(self.page, text = 'Go Back', command = self.to_login_page,font=f1)
        self.back_button.grid(row = 3,column=0)


    def searchDBforUser(self, name, ID): #todo
        cursor.execute("SELECT * FROM _User WHERE StudentName ='%s' AND StudentID = '%s'" % (name,ID))
        data = cursor.fetchall()
        if data:
            return True
        else:
            return False


    def to_login_page(self):
        self.page.destroy()
        loginpage(self.root)

    def login(self):        # either to user operating page or show error pswd
        if not self.id_entry.get():
            message=messagebox.showwarning("Warning",'Student ID missed!')
        elif not self.name_entry.get():
            message=messagebox.showwarning("Warning",'Student name missed!')
        else:
            name = self.name_entry.get()
            studentid = self.id_entry.get()
            ####SEARCH FOR ID IN DB AND LOGIN
            found = self.searchDBforUser(name, studentid)
            if found:#found target
                message=messagebox.showwarning("Login success",'Wellcome!')
                self.page.destroy()
                useroperatingpage(self.root)
            else:#do sth. (todo)
                message=messagebox.showwarning("Warning",'User not found!')

class employeeloginpage(object):
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Login',bg='LightCyan',font=f2)
        self.header.grid(row = 0,columnspan=2)

        self.name_frame = tk.Label(self.page, text='Name: ',font=f1)
        self.name_frame.grid(row = 1, column = 0,pady=20)
        self.name_entry = tk.Entry(self.page)
        self.name_entry.grid(row = 1, column = 1)
        self.SSN_frame = tk.Label(self.page, text='SSN: ',font=f1)
        self.SSN_frame.grid(row = 2, column = 0)
        self.SSN_entry = tk.Entry(self.page)
        self.SSN_entry.grid(row = 2, column = 1)

        self.login_button = tk.Button(self.page, text = 'Login', command = self.login,font=f1)
        self.login_button.grid(row = 3,column=1,pady=40)
        self.back_button = tk.Button(self.page, text = 'Go Back', command = self.to_login_page,font=f1)
        self.back_button.grid(row = 3,column=0)

    def to_login_page(self):
        self.page.destroy()
        loginpage(self.root)

    def searchDBforEmployee(self, name, ID): #todo
        cursor.execute("SELECT * FROM Employee WHERE EmployeeName ='%s' AND EmployeeSSN = '%s'" % (name,ID))
        data = cursor.fetchall()
        if data:
            return True
        else:
            return False

    def login(self):
        if not self.SSN_entry.get():
            message=messagebox.showwarning("Warning",'SSN missed!')
        elif not self.name_entry.get():
            message=messagebox.showwarning("Warning",'Name missed!')
        else:
            name = self.name_entry.get()
            SSN = self.SSN_entry.get()
            ####SEARCH FOR SSN IN DATA AND LOGIN
            found = self.searchDBforEmployee(name, SSN)
            if found:#found target
                message=messagebox.showwarning("success",'Employee Login!')
                self.page.destroy()
                employeeoperatingpage(self.root)
            else:#do sth. (todo)
                message=messagebox.showwarning("Warning",'Employee not found!')


#---------------------------------User operating pages-----------------------------------------------
class useroperatingpage(object):
    """docstring for useroperatingpage"""
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Wellcome',bg='LightCyan',font=f2)
        self.header.grid(row = 0,columnspan=2)

        self.Rent_button = tk.Button(self.page, text = 'Rent', command = self.rentbike,font=f1)
        self.Rent_button.grid(row = 1,column=0,pady=40)
        self.reserve_button = tk.Button(self.page, text = 'Reserve', command = self.reservebike,font=f1)
        self.reserve_button.grid(row = 1,column=1)


    def rentbike(self):
        self.page.destroy()
        rentbikepage(self.root)

    def reservebike(self):
        #print("haha")
        self.page.destroy()
        reservepage(self.root)

class rentbikepage(object):
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Rent Bike',bg='LightCyan',pady=10,font=f2)
        self.header.grid(row = 0,columnspan=3)

        self.SID_frame = tk.Label(self.page, text='StudentID: ',font=f1)
        self.SID_frame.grid(row = 2, column = 0,pady=5)
        self.SID_entry = tk.Entry(self.page)
        self.SID_entry.grid(row = 2, column = 1)
        self.BID_frame = tk.Label(self.page, text='BikeID: ',font=f1)
        self.BID_frame.grid(row = 3, column = 0,pady=2)
        self.BID_entry = tk.Entry(self.page)
        self.BID_entry.grid(row = 3, column = 1)

        self.doRent_button = tk.Button(self.page, text = 'confirm Rent', command = self.Rent,font=f1)
        self.doRent_button.grid(row = 4,columnspan=2,pady=5)

    def Rent(self):
        if not self.SID_entry.get():
            message=messagebox.showwarning("Warning",'Student ID missed!')
        elif not self.BID_entry.get():
            message=messagebox.showwarning("Warning",'Bike ID missed!')
        else:
            S_ID = self.SID_entry.get()
            B_ID = self.BID_entry.get()
            now = datetime.datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")
            date = year + month + day
            time = now.strftime("%H:%M:%S")
            print(type(date), type(time))
            message=messagebox.showwarning("success",S_ID + ' borrow ' + B_ID + ' at ' + month + '/' + day +" "+ time)
            #todo: some sql instruction to add (1)insert into Rent record (2)update bike status
            sql = "UPDATE Bike SET Renting = 1 WHERE BikeID = '%s'" % B_ID
           # try:
            cursor.execute(sql)
            db.commit()
            # except:
            #     print("error")
            #     db.rollback()


            sql = "INSERT INTO Lend_Record (StudentID, BikeID, L_Date, Start_Time) VALUES ('%s', '%s', '%s', '%s')"%(S_ID, B_ID, date, time)
          #  try:
            cursor.execute(sql)
            db.commit()
            # except:
            #     print("error")
            #     db.rollback()


class reservepage(object):
    """docstring for reservepage"""
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root,bg='LightCyan')
        self.page.pack()

        self.header = tk.Label(self.page, text='Reserve Bike',bg='LightCyan',pady=10,font=f2)
        self.header.grid(row = 0,columnspan=2)


        self.id_frame = tk.Label(self.page, text='Student ID: ',font=f1)
        self.id_frame.grid(row = 1, column = 0)
        self.id_entry = tk.Entry(self.page)
        self.id_entry.grid(row = 1, column = 1)

        self.bike_id_frame = tk.Label(self.page, text='Bike ID: ',font=f1)
        self.bike_id_frame.grid(row = 2, column = 0)
        self.bike_id_entry = tk.Entry(self.page)
        self.bike_id_entry.grid(row = 2, column = 1)


        self.back_button = tk.Button(self.page, text = 'Back',font=f1, command = self.go_back)
        self.back_button.grid(row = 3, column = 0,pady=20)

        self.reserve_button = tk.Button(self.page, text = 'Reserve',font=f1, command = self.reserve)
        self.reserve_button.grid(row = 3, column = 1)

    def go_back(self):
        self.page.destroy()
        useroperatingpage(self.root)

    def reserve(self):
        if not self.id_entry.get():
            message=messagebox.showwarning("Warning",'Student ID missed!')
        elif not self.bike_id_entry.get():
            message=messagebox.showwarning("Warning",'Bike ID missed!')
        else:
            S_ID = self.id_entry.get()
            B_ID = self.bike_id_entry.get()
            now = datetime.datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")
            date = year + month + day
            time = now.strftime("%H:%M:%S")
            print(type(date), type(time))
            message=messagebox.showwarning("success",S_ID + ' reserved ' + B_ID + ' at ' + month + '/' + day +" "+ time)
            #todo: some sql instruction to add (1)insert into Rent record (2)update bike status
            sql = "UPDATE Bike SET Renting = 1 WHERE BikeID = '%s'" % B_ID
   #         try:
            cursor.execute(sql)
            db.commit()
            # except:
            #     print("error")
            #     db.rollback()


            sql = "INSERT INTO Reservation_Record (StudentID, BikeID, R_Date, R_Time) VALUES ('%s', '%s', '%s', '%s')"%(S_ID, B_ID, date, time)
   #        try:
            cursor.execute(sql)
            db.commit()
            # except:
            #     print("error")
            #     db.rollback()

#################################EMPLOYEE OPERATING PAGE######################################
class employeeoperatingpage(object):
    """docstring for employeeoperatingpage"""
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.change_data_button = tk.Button(self.page, text = 'Change Bike Data', command = self.change_data)
        self.change_data_button.grid(row = 0)

        self.add_fix_button = tk.Button(self.page, text = 'Add fix event', command = self.add_fix)
        self.add_fix_button.grid(row = 1)

        self.add_violate_button = tk.Button(self.page, text = 'Add violate event', command = self.add_violate)
        self.add_violate_button.grid(row = 2)

    def change_data(self):
        self.page.destroy()
        changedatapage(self.root)

    def add_fix(self):
        self.page.destroy()
        addfixpage(self.root)

    def add_violate(self):
        self.page.destroy()
        addviolatepage(self.root)


class changedatapage(object):
    """docstring for changedatapage"""
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.bike_id_frame = tk.Label(self.page, text='Bike ID: ')
        self.bike_id_frame.grid(row = 1, column = 0)
        self.bike_id_entry = tk.Entry(self.page)
        self.bike_id_entry.grid(row = 1, column = 1)

        self.rate_frame = tk.Label(self.page, text = 'Earning rate to change')
        self.rate_frame.grid(row = 2, column = 0)
        self.rate_entry = tk.Entry(self.page)
        self.rate_entry.grid(row = 2, column = 1)

        self.cost_frame = tk.Label(self.page, text = 'Cost to change')
        self.cost_frame.grid(row = 3, column = 0)
        self.cost_entry = tk.Entry(self.page)
        self.cost_entry.grid(row = 3, column = 1)

        self.back_button = tk.Button(self.page, text = 'Back', command = self.go_back)
        self.back_button.grid(row = 4, column = 0)

        self.change_button = tk.Button(self.page, text = 'Change', command = self.change)
        self.change_button.grid(row = 4, column = 1)

        self.message_label = tk.Label(self.page)
        self.message_label.grid(row = 5)

    def go_back(self):
        self.page.destroy()
        employeeoperatingpage(self.root)

    def change(self):
        if not self.bike_id_entry.get():
            message = 'Bike ID Missed!'
            self.message_label.configure(text = message)

        else:
            ###change changed data###
            self.bike_id_entry.delete(0, 'end')
            self.cost_entry.delete(0, 'end')
            self.rate_entry.delete(0, 'end')
            message = 'Successfully Changed!'
            self.message_label.configure(text = message)


class addfixpage(object):
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.bike_id_frame = tk.Label(self.page, text='Bike ID: ')
        self.bike_id_frame.grid(row = 1, column = 0)
        self.bike_id_entry = tk.Entry(self.page)
        self.bike_id_entry.grid(row = 1, column = 1)

        self.date_frame = tk.Label(self.page, text='Date: ')
        self.date_frame.grid(row = 2, column = 0)
        self.date_entry = tk.Entry(self.page)
        self.date_entry.grid(row = 2, column = 1)

        self.content_frame = tk.Label(self.page, text='Content: ')
        self.content_frame.grid(row = 3, column = 0)
        self.content_entry = tk.Entry(self.page)
        self.content_entry.grid(row = 3, column = 1)

        self.back_button = tk.Button(self.page, text = 'Back', command = self.go_back)
        self.back_button.grid(row = 4, column = 0)

        self.change_button = tk.Button(self.page, text = 'Add', command = self.add)
        self.change_button.grid(row = 4, column = 1)

        self.message_label = tk.Label(self.page)
        self.message_label.grid(row = 5)

    def go_back(self):
        self.page.destroy()
        employeeoperatingpage(self.root)

    def add(self):
        if not self.bike_id_entry.get():
            message = 'Bike ID Missed!'
            self.message_label.configure(text = message)

        else:
            ###add changed data###
            self.bike_id_entry.delete(0, 'end')
            self.date_entry.delete(0, 'end')
            self.content_entry.delete(0, 'end')
            message = 'Successfully Added!'
            self.message_label.configure(text = message)


class addviolatepage(object):
    def __init__(self, master = None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.id_frame = tk.Label(self.page, text='Student ID: ')
        self.id_frame.grid(row = 1, column = 0)
        self.id_entry = tk.Entry(self.page)
        self.id_entry.grid(row = 1, column = 1)

        self.date_frame = tk.Label(self.page, text='Date: ')
        self.date_frame.grid(row = 2, column = 0)
        self.date_entry = tk.Entry(self.page)
        self.date_entry.grid(row = 2, column = 1)

        self.time_frame = tk.Label(self.page, text='Time: ')
        self.time_frame.grid(row = 3, column = 0)
        self.time_entry = tk.Entry(self.page)
        self.time_entry.grid(row = 3, column = 1)
        
        self.fine_frame = tk.Label(self.page, text='Fine: ')
        self.fine_frame.grid(row = 4, column = 0)
        self.fine_entry = tk.Entry(self.page)
        self.fine_entry.grid(row = 4, column = 1)

        self.back_button = tk.Button(self.page, text = 'Back', command = self.go_back)
        self.back_button.grid(row = 5, column = 0)

        self.change_button = tk.Button(self.page, text = 'Add', command = self.add)
        self.change_button.grid(row = 5, column = 1)

        self.message_label = tk.Label(self.page)
        self.message_label.grid(row = 6)

    def go_back(self):
        self.page.destroy()
        employeeoperatingpage(self.root)

    def add(self):
        if not self.id_entry.get():
            message = 'Student ID Missed!'
            self.message_label.configure(text = message)

        else:
            ###add changed data###
            self.id_entry.delete(0, 'end')
            self.date_entry.delete(0, 'end')
            self.time_entry.delete(0, 'end')
            self.fine_entry.delete(0, 'end')
            message = 'Successfully Added!'
            self.message_label.configure(text = message)


                                

        
frontpage(root)
root.mainloop()     