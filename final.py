from Tkinter import *
import time


#main class
class Main(object):
    def __init__(self):
        self.root=Tk()
        self.root.title("Main")
        self.root.geometry("640x480")
        
        self.btnStaff=Button(self.root,text="STAFF")
        self.btnAdmin=Button(self.root,text="ADMIN")
        self.btnManager=Button(self.root,text="MANAGER")
        self.root.bind("<Button-1>",self.actionPerformed)
        self.btnStaff.place(x=320,y=240)
        self.btnAdmin.place(x=320,y=270)
        self.btnManager.place(x=320,y=300)
        
        self.root.mainloop()


    def actionPerformed(self,e):
        if(e.widget==self.btnStaff):
            obj=Staff(self.root)
        elif(e.widget==self.btnAdmin):
            obj=AdminLogin(self.root)
        elif(e.widget==self.btnManager):
            obj=ManagementLogin(self.root)

class DlgBox(Toplevel):
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("OK")
        self.geometry("160x120")
        self.parent=par

        btn=Button(self,text="Done",command=self.ok)
        btn.pack()

        self.wait_window(self)

    def ok(self):
        self.destroy()
        



#staff selection class
class Staff(Toplevel):
    stfName=""
    lbx=None
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Staff")
        self.geometry("640x480")
        self.parent=par
        
        lblStf=Label(self,text="STAFF")
        localtime=time.asctime(time.localtime(time.time()))
        lblTime=Label(self,text=localtime)

        slctStf=None
        Staff.lbx=Listbox(self)
        Staff.lbx.insert(1,"Jason Dennis")
        Staff.lbx.insert(2,"Mohd Arif")
        Staff.lbx.insert(3,"John Lai")
        Staff.lbx.bind("<<ListboxSelect>>",self._set)

        btnIn=Button(self,text="CLOCK-IN", command=self.ok)
        btnOut=Button(self,text="CLOCK-OUT", command=self.ok)
        btnView=Button(self,text="VIEW-RECORDS",command=self.view)


        lblStf.place(x=5,y=5)
        lblTime.place(x=480,y=5)
        Staff.lbx.place(x=5,y=100)
        btnIn.place(x=530,y=100)
        btnOut.place(x=530,y=150)
        btnView.place(x=530,y=200)
        self.wait_window(self)

    def _set(self,x):
        
        Staff.stfName=Staff.lbx.get(Staff.lbx.curselection()[0])

    def ok(self):
        obj=DlgBox(self)

    def view(self):
        obj=StaffRec(self)


#Staff record view class
class StaffRec(Toplevel):
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Record")
        self.geometry("640x480")
        self.parent=par

        lbl1=Label(self,text=Staff.stfName)
        lbl2=Label(self,text="11/02 (Monday) : 0655 - 1710")
        lbl3=Label(self,text="12/02 (Tuesday) : 0620 - 1720")
        lbl4=Label(self,text="13/02 (Wednesday) : 0645 - 1715")

        lbl1.pack()
        lbl2.pack()
        lbl3.pack()
        lbl4.pack()

        self.wait_window(self)

#Admin class
class Admin(Toplevel):
    lbxMnth=None
    slctMnth=""
    def __init__(self, par):
        Toplevel.__init__(self,par)
        self.title("Admin")
        self.geometry("640x480")
        self.parent=par

        lbl=Label(self,text="ADMIN")
        
        lbxStf=Listbox(self)
        lbxStf.insert(1,"Jason Dennis")
        lbxStf.insert(2,"Mohd Arif")
        lbxStf.insert(3,"John Lai")

        Admin.lbxMnth=Listbox(self)
        Admin.lbxMnth.insert(1,"Jan")
        Admin.lbxMnth.insert(2,"Feb")
        Admin.lbxMnth.bind("<<ListboxSelect>>",self._set)

        btnGenPay=Button(self,text="GENERATE PAYSLIP",command=self.actionPerformed)


        lbl.place(x=5,y=5)
        lbxStf.place(x=5,y=20)
        Admin.lbxMnth.place(x=100,y=20)
        btnGenPay.place(x=100,y=200)

        self.wait_window(self)

    def _set(self,x):
        Admin.slctMnth=Admin.lbxMnth.get(Admin.lbxMnth.curselection()[0])

    def actionPerformed(self):
        obj=AdminPayslip(self)

class AdminLogin(Toplevel):
    btnSub=None
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Admin Login")
        self.geometry("320x240")
        self.parent=par

        lbl=Label(self,text="Admin Login\nPlease Enter Password\n")
        pword=Entry(self,show="*")
        AdminLogin.btnSub=Button(self,text="Submit")
        AdminLogin.btnSub.bind("<Button-1>",self.actionPerformed)

        lbl.pack()
        pword.pack()
        AdminLogin.btnSub.pack()

    def actionPerformed(self,e):
        if(e.widget==AdminLogin.btnSub):
            obj=Admin(self)


class AdminPayslip(Toplevel):
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Admin Payslip")
        self.geometry("640x480")
        self.parent=par

        lbl1=Label(self,text="Constance University")
        lbl2=Label(self,text="Payslip")
        lbl3=Label(self,text="Month: ")
        lbl4=Label(self,text=Admin.slctMnth)#Admin.slctMnth)
        lbl5=Label(self,text="Hours worked: 50")
        lbl6=Label(self,text="hours")
        lbl7=Label(self,text="Total")
        lbl8=Label(self,text="RM500")
        btn=Button(self,text="PRINT & EMAIL")

        lbl1.place(x=5,y=5)
        lbl2.place(x=5,y=50)
        lbl3.place(x=5,y=240)
        lbl4.place(x=100,y=240)
        lbl5.place(x=5,y=260)
        lbl6.place(x=100,y=260)
        lbl7.place(x=5,y=280)
        lbl8.place(x=100,y=280)
        btn.place(x=500,y=400)

        self.wait_window(self)




#Management class
class Management(Toplevel):
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Management")
        self.geometry("640x480")
        self.parent=par

        btnWkHrs=Button(self,text="Staff Working Hours",command=self.actionPerformed)
        btnYrPay=Button(self,text="Yearly Staff Pay",command=self.actionPerformed2)
        btnWkTdy=Button(self,text="Staff Working Today",command=self.actionPerformed3)

        btnWkHrs.place(x=320,y=240)
        btnYrPay.place(x=320,y=270)
        btnWkTdy.place(x=320,y=300)

        self.wait_window(self)
    def actionPerformed(self):
        obj=WorkingHours(self)
    def actionPerformed2(self):
        obj=YearlyPay(self)
    def actionPerformed3(self):
        obj=StfWrkToday()

class ManagementLogin(Toplevel):
    btnSub=None
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Admin Login")
        self.geometry("320x240")
        self.parent=par

        lbl=Label(self,text="Admin Login\nPlease Enter Password\n")
        pword=Entry(self,show="*")
        ManagementLogin.btnSub=Button(self,text="Submit",command=self.actionPerformed)
        

        lbl.pack()
        pword.pack()
        ManagementLogin.btnSub.pack()
    def actionPerformed(self):
        obj=Management(self)

class WorkingHours(Toplevel):
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Working Hours")
        self.geometry("640x480")
        self.parent=par

        lbl1=Label(self,text="Staff Working Hours")
        lbl2=Label(self,text="January\n1.Jason - 40\n2.Arif - 50\n3.John - 60\n\n\n")
        lbl3=Label(self,text="February\n1.Jason - 20\n2.Arif - 30\n3.John - 70\n\n\n")

        lbl1.pack()
        lbl2.pack()
        lbl3.pack()

        self.wait_window(self)

class YearlyPay(Toplevel):
    def __init__(self,par):
        Toplevel.__init__(self,par)
        self.title("Yearly Pay")
        self.geometry("640x480")
        self.parent=par

        lbl1=Label(self,text="Yearly Pay")
        lbl2=Label(self,text="\n\n\nJason - RM5000\nArif - RM4500\nJohn - RM3000\n\n\n")

        lbl1.pack()
        lbl2.pack()

        self.wait_window(self)

class StfWrkToday(object):
    def __init__(self):
        self.root=Tk()
        self.root.title("Staff Working Today")
        self.root.geometry("640x480")

        lbl1=Label(self.root,text="Staff Working Today\n\n\n")
        lbl2=Label(self.root,text="Jason\n\n\nJohn\n\n\n")
        lbl1.pack()
        lbl2.pack()

        self.root.mainloop()

cInTime={}

obj1=Main()
                   
