import tkinter
import os 
from tkinter import messagebox
#from tkinter.ttk import * 
y = 0
Appointments_list1 = ["","1)8 to 8:30 AM","2)8:30 to 9 AM","3)9 to 9:30 AM","4)9:30 to 10 AM","5)10 to 10:30 AM","6)10:30 to 11 AM","7)11 to 11:30 AM","8)11:30 to 12 PM","9)12 to 12:30 PM","10)12:30 to 1 PM","11)1 to 1:30 PM","12)1:30 to 2 AM"]



def CancelAppointmentFunc() :
	f13 = E59.get()
	if os.path.exists("Book"+str(f13)+".txt"):
		os.remove("Book"+str(f13)+".txt")
		file77 = open("Appointments2.txt","r")
		x12 =0 
		ALLBAW = ""
		while x12 < 12 :
			ALLBAR = file77.readline()
			if str(ALLBAR) == (Appointments_list1[int(E60.get())]+"\n") :
				pass 
			elif str(ALLBAR) == "\n" :
				pass
			elif str(ALLBAR) == " " :
				pass
			else : 
				if ALLBAW == "" :
					ALLBAW = str(ALLBAR)
				else :	
					ALLBAW = ALLBAW + str(ALLBAR)
			x12+=1	
		file77.close()
		os.remove("Appointments2.txt")
		file77 = open("Appointments2.txt","w")
		file77.write(ALLBAW)
		file77.close()	
		messagebox.showinfo("Congratulation","Done")
	else :
		messagebox.showinfo("Warning","Not Exist ID")
	

def CancelAppointmentFile():
	global E59
	global E60
	L58 = tkinter.Label(page7, text = "Enter ID" , bg="blue",width=5)
	L59 = tkinter.Label(page7, text = "Enter Appointment" , bg="blue",width=30)
	E59 = tkinter.Entry(page7,width = 5)
	E60 = tkinter.Entry(page7,width = 5)
	btn29 = tkinter.Button(page7,text="Enter",bg="dodgerblue",width=21,command = CancelAppointmentFunc)
	L58.pack(fill="y",expand="true") 
	E59.pack(fill="y",expand="true")
	L59.pack(fill="y",expand="true") 
	E60.pack(fill="y",expand="true")
	btn29.pack(fill="y",expand="true") 

def EditAppointmentFunc2():
	f12 = E56.get()
	if os.path.exists("Book"+str(f12)+".txt"):
		file = open("Book"+str(f12)+".txt","w")
		file.write(str(E48.get())+"\n")
		file.write(str(E49.get())+"\n")
		file.write(str(E50.get())+"\n")
		file.write(str(E51.get())+"\n")
		file.write(str(E52.get())+"\n")
		file.write(str(E53.get())+"\n")
		file.write(str(E54.get())+"\n")
		file.write(str(E55.get())+"\n")
		file.write(str(E56.get())+"\n")
		file.write(Appointments_list1[int(E58.get())]+"\n")
		file.close() 
		file77 = open("Appointments2.txt","r")
		y12 = 0
		ALLBAW = ""
		while y12 < 12 :
			ALLBAR = file77.readline()
			if str(ALLBAR) == (Appointments_list1[int(E57.get())]+"\n") :
				pass
			elif str(ALLBAR) == "\n" :
				pass
			elif str(ALLBAR) == " " :
				pass		
			else : 
				if ALLBAW == "" :
					ALLBAW = str(ALLBAR)
				else :	
					ALLBAW = ALLBAW + str(ALLBAR)
			y12+=1		
		ALLBAW = ALLBAW + (Appointments_list1[int(E58.get())]+"\n")	
		file77.close()
		os.remove("Appointments2.txt")
		file77 = open("Appointments2.txt","w")
		file77.write(ALLBAW)
		file77.close()
		messagebox.showinfo("Congratulation","Done")
	else :
		#print("Not Exist")
		messagebox.showinfo("Warning","Not Exist ID")

def EditAppointmentFunc():
	global E56
	global E48
	global E49
	global E50
	global E51
	global E52
	global E53
	global E54
	global E55
	global E57
	global E58
	f11 = E47.get()
	if os.path.exists("Book"+str(f11)+".txt"):
		global page13 
		page13=tkinter.Toplevel(page7)
		page13.title("Edit an Appointment")
		page13.geometry("500x500+500+150")
		page13.configure(bg="blue")
		L47 = tkinter.Label(page13, text = "Department" , bg="blue",width=25)
		L48 = tkinter.Label(page13, text = "Name of Doctor" , bg="blue",width=25)
		L49= tkinter.Label(page13, text = "Name" , bg="blue",width=25)
		L50 = tkinter.Label(page13, text = "Age" , bg="blue",width=25)
		L51 = tkinter.Label(page13, text = "Gender" , bg="blue",width=25)
		L52 = tkinter.Label(page13, text = "Address" , bg="blue",width=25)
		L53 = tkinter.Label(page13, text = "Phone Number" , bg="blue",width=25)
		L54 = tkinter.Label(page13, text = "Condition" , bg="blue",width=25)
		L55 = tkinter.Label(page13, text = "ID" , bg="blue",width=25)
		L56 = tkinter.Label(page13, text = "Old Appointment" , bg="blue",width=25)
		L57 = tkinter.Label(page13, text = "New Appointment" , bg="blue",width=25)
		E48 = tkinter.Entry(page13,width = 15)
		E49 = tkinter.Entry(page13,width = 15)
		E50 = tkinter.Entry(page13,width = 15)
		E51 = tkinter.Entry(page13,width = 15)
		E52 = tkinter.Entry(page13,width = 15)
		E53 = tkinter.Entry(page13,width = 15)
		E54 = tkinter.Entry(page13,width = 15)
		E55 = tkinter.Entry(page13,width = 30)
		E56 = tkinter.Entry(page13,width = 5)
		E57 = tkinter.Entry(page13,width = 30)
		E58 = tkinter.Entry(page13,width = 30)
		btn28 = tkinter.Button(page13,text="Enter",bg="dodgerblue",width=21,command = EditAppointmentFunc2)
		L47.grid(row=0,column=0)
		L48.grid(row=1,column=0)
		L49.grid(row=2,column=0)
		L50.grid(row=3,column=0)
		L51.grid(row=4,column=0)
		L52.grid(row=5,column=0)
		L53.grid(row=6,column=0)
		L54.grid(row=7,column=0)
		L55.grid(row=8,column=0)
		L56.grid(row=9,column=0)
		L57.grid(row=10,column=0)
		E48.grid(row=0,column=1)
		E49.grid(row=1,column=1)
		E50.grid(row=2,column=1)
		E51.grid(row=3,column=1)
		E52.grid(row=4,column=1)
		E53.grid(row=5,column=1)
		E54.grid(row=6,column=1)
		E55.grid(row=7,column=1)
		E56.grid(row=8,column=1)
		E57.grid(row=9,column=1)
		E58.grid(row=10,column=1)
		btn28.grid(row=11,column=1)
		file55 = open("Appointments.txt","r")
		BA55 = str(file55.read())
		#messagebox.showinfo("Appointments", BA55)
		file55.close()
		if os.path.exists("Appointments2.txt"): 
			file66 = open("Appointments2.txt","r")
			BA66 = str(file66.read())
			messagebox.showinfo("Appointments",BA55+"\n"+"----------\n"+"Booked Appointments"+"\n"+BA66)
			file66.close()
		else :
			messagebox.showinfo("Appointments", BA55)
	else :
		messagebox.showinfo("Warning","Not Exist ID")
		
def EditAppointmentFile():
	global E47 
	L46 = tkinter.Label(page7, text = "Enter ID" , bg="blue",width=25)
	E47 = tkinter.Entry(page7,width = 5)
	btn27 = tkinter.Button(page7,text="Enter",bg="dodgerblue",width=21,command = EditAppointmentFunc)
	L46.pack(fill="y",expand="true") 
	E47.pack(fill="y",expand="true")
	btn27.pack(fill="y",expand="true") 

def AddAppointmentFunc():
	f10 = E45.get()
	if os.path.exists("Book"+str(f10)+".txt"):
		#print("Error Repeat")
		messagebox.showinfo("Warning","Exist ID")
	else :		
		file = open("Book"+str(f10)+".txt","w")
		file.write(str(E37.get())+"\n")
		file.write(str(E38.get())+"\n")
		file.write(str(E39.get())+"\n")
		file.write(str(E40.get())+"\n")
		file.write(str(E41.get())+"\n")
		file.write(str(E42.get())+"\n")
		file.write(str(E43.get())+"\n")
		file.write(str(E44.get())+"\n")
		file.write(str(E45.get())+"\n")
		file.write(str(Appointments_list1[int(E46.get())])+"\n")
		#DD = Appointments_list1.index(str(E46.get()))
		file.close()
		if os.path.exists("Appointments2.txt"): 
			file44 = open("Appointments2.txt","a")
			file44.write(str(Appointments_list1[int(E46.get())])+"\n")
		else : 	
			file44 = open("Appointments2.txt","w")
			file44.write(str(Appointments_list1[int(E46.get())])+"\n")
				
		#print("Done")
		messagebox.showinfo("Congratulation","Done")
	

def AddAppointmentFile():
	global E37
	global E38
	global E39
	global E40
	global E41
	global E42
	global E43
	global E44
	global E45
	global page12
	global E46
	page12=tkinter.Toplevel(page7)
	page12.title("Add an Appointment")
	page12.geometry("500x500+500+150")
	page12.configure(bg="blue")
	L36 = tkinter.Label(page12, text = "Department" , bg="blue",width=25)
	L37 = tkinter.Label(page12, text = "Name of Doctor" , bg="blue",width=25)
	L38 = tkinter.Label(page12, text = "Name" , bg="blue",width=25)
	L39 = tkinter.Label(page12, text = "Age" , bg="blue",width=25)
	L40 = tkinter.Label(page12, text = "Gender" , bg="blue",width=25)
	L41 = tkinter.Label(page12, text = "Address" , bg="blue",width=25)
	L42 = tkinter.Label(page12, text = "Phone Number" , bg="blue",width=25)
	L43 = tkinter.Label(page12, text = "Condition" , bg="blue",width=25)
	L44 = tkinter.Label(page12, text = "ID" , bg="blue",width=25)
	L45 = tkinter.Label(page12, text = "Appointment" , bg="blue",width=25)
	E37 = tkinter.Entry(page12,width = 15)
	E38 = tkinter.Entry(page12,width = 15)
	E39 = tkinter.Entry(page12,width = 15)
	E40 = tkinter.Entry(page12,width = 15)
	E41 = tkinter.Entry(page12,width = 15)
	E42 = tkinter.Entry(page12,width = 15)
	E43 = tkinter.Entry(page12,width = 15)
	E44 = tkinter.Entry(page12,width = 15)
	E45 = tkinter.Entry(page12,width = 15)
	E46 = tkinter.Entry(page12,width = 15)
	L36.grid(row=0,column=0)
	L37.grid(row=1,column=0)
	L38.grid(row=2,column=0)
	L39.grid(row=3,column=0)
	L40.grid(row=4,column=0)
	L41.grid(row=5,column=0)
	L42.grid(row=6,column=0)
	L43.grid(row=7,column=0)
	L44.grid(row=8,column=0)
	L45.grid(row=9,column=0)
	E37.grid(row=0,column=1)
	E38.grid(row=1,column=1)
	E39.grid(row=2,column=1)
	E40.grid(row=3,column=1)
	E41.grid(row=4,column=1)
	E42.grid(row=5,column=1)
	E43.grid(row=6,column=1)
	E44.grid(row=7,column=1)
	E45.grid(row=8,column=1)
	E46.grid(row=9,column=1)
	btn26 = tkinter.Button(page12,text="Enter",bg="dodgerblue",width=21,command = AddAppointmentFunc).grid(row=10,column=1)
	file33 = open("Appointments.txt","r")
	BA33 = str(file33.read())
	#messagebox.showinfo("Appointments", BA33)
	if os.path.exists("Appointments2.txt"): 
			file333 = open("Appointments2.txt","r")
			BA333 = str(file333.read())
			messagebox.showinfo("Appointments",BA33+"\n"+"----------\n"+"Booked Appointments"+"\n"+BA333)
			file333.close()
	else :
			messagebox.showinfo("Appointments", BA33)
	file33.close()
	
	'''Counter = 1
	iterator = 0
	while iterator <12 :
		if Appointments_list2 != 1 :
			Label_list.append(tkinter.Label(page12 ,text =str(Appointments_list1[iterator]),width=30))
			Label_list[Counter].grid(row=(Counter+10),column =0)
			Counter+=1
		iterator+=1	'''
	

''' Book an Appointment '''
'''
	*
	*
	*
	*
	*
	*
	'''
''' Manage a Doctor '''
def ReadDocFunc():
	f9 = E36.get()
	if os.path.exists("Doc"+str(f9)+".txt"):
		file=open("Doc"+str(f9)+".txt","r")
		read = file.read()
		#print(str(read))
		messagebox.showinfo("Read a Doctor", str(read))
	else :
		messagebox.showinfo("Warning","Not Exist ID")
def ReadDocFile():
	global E36
	L35 = tkinter.Label(page6, text = "Enter ID" , bg="blue",width=25)
	E36 = tkinter.Entry(page6,width = 5)
	btn25 = tkinter.Button(page6,text="Enter",bg="dodgerblue",width=21,command = ReadDocFunc)
	L35.pack(fill="y",expand="true") 
	E36.pack(fill="y",expand="true")
	btn25.pack(fill="y",expand="true") 

def EditDocFunc2():
	f9 = E36.get()
	if os.path.exists("Doc"+str(f9)+".txt"):
		file = open("Doc"+str(f9)+".txt","w")
		file.write(str(E31.get())+"\n")
		file.write(str(E32.get())+"\n")
		file.write(str(E33.get())+"\n")
		file.write(str(E34.get())+"\n")
		file.write(str(E35.get())+"\n")
		file.write(str(E36.get())+"\n")
		#print("Done")
		messagebox.showinfo("Congratulation","Done")
	else :
		#print("Not Exist")
		messagebox.showinfo("Warning","Not Exist ID")

def EditDocFunc():
	f8 = E30.get()
	if os.path.exists("Doc"+str(f8)+".txt"):
		global page11
		global E36
		global E31
		global E32
		global E33
		global E34
		global E35
		page11=tkinter.Toplevel(page6)
		page11.title("Edit a Doctor")
		page11.geometry("500x500+500+150")
		page11.configure(bg="blue")
		L30 = tkinter.Label(page11, text = "Department" , bg="blue",width=25)
		L31 = tkinter.Label(page11, text = "Name of Doctor" , bg="blue",width=25)
		L32 = tkinter.Label(page11, text = "Address" , bg="blue",width=25)
		L33 = tkinter.Label(page11, text = "Phone Number" , bg="blue",width=25)
		L34 = tkinter.Label(page11, text = "Condition" , bg="blue",width=25)
		L35 = tkinter.Label(page11, text = "ID" , bg="blue",width=25)
		E31 = tkinter.Entry(page11,width = 15)
		E32 = tkinter.Entry(page11,width = 15)
		E33 = tkinter.Entry(page11,width = 15)
		E34 = tkinter.Entry(page11,width = 15)
		E35 = tkinter.Entry(page11,width = 15)
		E36 = tkinter.Entry(page11,width = 15)
		btn24 = tkinter.Button(page11,text="Enter",bg="dodgerblue",width=21,command = EditDocFunc2)
		L30.grid(row=0,column=0)
		L31.grid(row=1,column=0)
		L32.grid(row=2,column=0)
		L33.grid(row=3,column=0)
		L34.grid(row=4,column=0)
		L35.grid(row=5,column=0)
		E31.grid(row=0,column=1)
		E32.grid(row=1,column=1)
		E33.grid(row=2,column=1)
		E34.grid(row=3,column=1)
		E35.grid(row=4,column=1)
		E36.grid(row=5,column=1)
		btn24.grid(row=6,column=1)
		
def EditDocFile():
	global E30 
	L29 = tkinter.Label(page6, text = "Enter ID" , bg="blue",width=25)
	E30 = tkinter.Entry(page6,width = 5)
	btn23 = tkinter.Button(page6,text="Enter",bg="dodgerblue",width=21,command = EditDocFunc)
	L29.pack(fill="y",expand="true") 
	E30.pack(fill="y",expand="true")
	btn23.pack(fill="y",expand="true")

def DeleteDocFunc(): 
	f7 = E29.get()
	if os.path.exists("Doc"+str(f7)+".txt"):
		os.remove("Doc"+str(f7)+".txt")
		#print("Done")
		messagebox.showinfo("Congratulation","Done")
	else :
		messagebox.showinfo("Warning","Not Exist ID")
def DeleteDocFile():
	global E29
	L28 = tkinter.Label(page6, text = "Enter ID" , bg="blue",width=25)
	E29 = tkinter.Entry(page6,width = 5)
	btn22 = tkinter.Button(page6,text="Enter",bg="dodgerblue",width=21,command = DeleteDocFunc)
	L28.pack(fill="y",expand="true")
	E29.pack(fill="y",expand="true")
	btn22.pack(fill="y",expand="true")

def AddDocFunc():
	f6 = E28.get()
	if os.path.exists("Doc"+str(f6)+".txt"):
		#print("Error Repeat")
		messagebox.showinfo("Warning","Exist ID")
	else :
		file = open("Doc"+str(f6)+".txt","w")
		file.write(str(E23.get())+"\n")
		file.write(str(E24.get())+"\n")
		file.write(str(E25.get())+"\n")
		file.write(str(E26.get())+"\n")
		file.write(str(E27.get())+"\n")
		file.write(str(E28.get())+"\n")
		#print("Done")
		messagebox.showinfo("Congratulation","Done")
	

def AddDocFile():
	global E23
	global E24
	global E25
	global E26
	global E27
	global E28
	page10=tkinter.Toplevel(page6)
	page10.title("Add a Doctor")
	page10.geometry("500x500+500+150")
	page10.configure(bg="blue")
	L22 = tkinter.Label(page10, text = "Department" , bg="blue",width=25)
	L23 = tkinter.Label(page10, text = "Name of Doctor" , bg="blue",width=25)
	L24 = tkinter.Label(page10, text = "Address" , bg="blue",width=25)
	L25 = tkinter.Label(page10, text = "Phone Number" , bg="blue",width=25)
	L26 = tkinter.Label(page10, text = "Condition" , bg="blue",width=25)
	L27 = tkinter.Label(page10, text = "ID" , bg="blue",width=25)
	E23 = tkinter.Entry(page10,width = 15)
	E24 = tkinter.Entry(page10,width = 15)
	E25 = tkinter.Entry(page10,width = 15)
	E26 = tkinter.Entry(page10,width = 15)
	E27 = tkinter.Entry(page10,width = 15)
	E28 = tkinter.Entry(page10,width = 15)
	L22.grid(row=0,column=0)
	L23.grid(row=1,column=0)
	L24.grid(row=2,column=0)
	L25.grid(row=3,column=0)
	L26.grid(row=4,column=0)
	L27.grid(row=5,column=0)
	E23.grid(row=0,column=1)
	E24.grid(row=1,column=1)
	E25.grid(row=2,column=1)
	E26.grid(row=3,column=1)
	E27.grid(row=4,column=1)
	E28.grid(row=5,column=1)
	btn21 = tkinter.Button(page10,text="Enter",bg="dodgerblue",width=21,command = AddDocFunc).grid(row=9,column=1)

''' Manage a Doctor ''' 
'''
    *
	*
	*
	*
	*
	*
	'''
''' Manage a Patient '''
def ReadFunc():
	f5 = E22.get()
	if os.path.exists("Pat"+str(f5)+".txt"):
		file=open("Pat"+str(f5)+".txt","r")
		read = file.read()
		messagebox.showinfo("Read a Patient", str(read))
		#print(str(read))
	else :
		messagebox.showinfo("Warning","Not Exist ID")
def ReadFile():
	global E22
	L21 = tkinter.Label(page5, text = "Enter ID" , bg="blue",width=25)
	E22 = tkinter.Entry(page5,width = 5)
	btn20 = tkinter.Button(page5,text="Enter",bg="dodgerblue",width=21,command = ReadFunc)
	L21.pack(fill="y",expand="true") 
	E22.pack(fill="y",expand="true")
	btn20.pack(fill="y",expand="true") 
def EditFunc2():
	f4 = E21.get()
	if os.path.exists("Pat"+str(f4)+".txt"):
		file = open("pat"+str(f4)+".txt","w")
		file.write(str(E13.get())+"\n")
		file.write(str(E14.get())+"\n")
		file.write(str(E15.get())+"\n")
		file.write(str(E16.get())+"\n")
		file.write(str(E17.get())+"\n")
		file.write(str(E18.get())+"\n")
		file.write(str(E19.get())+"\n")
		file.write(str(E20.get())+"\n")
		file.write(str(E21.get())+"\n")
		#print("Done")
		messagebox.showinfo("Congratulation","Done")
	else :
		#print("Not Exist")
		messagebox.showinfo("Warning","Not Exist ID")

def EditFunc():
	global E12
	f3 = E12.get()
	if os.path.exists("Pat"+str(f3)+".txt"):
		global page5
		global E21 
		page9=tkinter.Toplevel(page5)
		page9.title("Add a Patient")
		page9.geometry("500x500+500+150")
		page9.configure(bg="blue")
		L12 = tkinter.Label(page9, text = "Department" , bg="blue",width=25)
		L13 = tkinter.Label(page9, text = "Name of Doctor" , bg="blue",width=25)
		L14= tkinter.Label(page9, text = "Name" , bg="blue",width=25)
		L15 = tkinter.Label(page9, text = "Age" , bg="blue",width=25)
		L16 = tkinter.Label(page9, text = "Gender" , bg="blue",width=25)
		L17 = tkinter.Label(page9, text = "Address" , bg="blue",width=25)
		L18 = tkinter.Label(page9, text = "Phone Number" , bg="blue",width=25)
		L19 = tkinter.Label(page9, text = "Condition" , bg="blue",width=25)
		L20 = tkinter.Label(page9, text = "ID" , bg="blue",width=25)
		E13 = tkinter.Entry(page9,width = 15)
		E14 = tkinter.Entry(page9,width = 15)
		E15 = tkinter.Entry(page9,width = 15)
		E16 = tkinter.Entry(page9,width = 15)
		E17 = tkinter.Entry(page9,width = 15)
		E18 = tkinter.Entry(page9,width = 15)
		E19 = tkinter.Entry(page9,width = 15)
		E20 = tkinter.Entry(page9,width = 30)
		E21 = tkinter.Entry(page9,width = 5)
		btn19 = tkinter.Button(page9,text="Enter",bg="dodgerblue",width=21,command = EditFunc2)
		L12.grid(row=0,column=0)
		L13.grid(row=1,column=0)
		L14.grid(row=2,column=0)
		L15.grid(row=3,column=0)
		L16.grid(row=4,column=0)
		L17.grid(row=5,column=0)
		L18.grid(row=6,column=0)
		L19.grid(row=7,column=0)
		L20.grid(row=8,column=0)
		E13.grid(row=0,column=1)
		E14.grid(row=1,column=1)
		E15.grid(row=2,column=1)
		E16.grid(row=3,column=1)
		E17.grid(row=4,column=1)
		E18.grid(row=5,column=1)
		E19.grid(row=6,column=1)
		E20.grid(row=7,column=1)
		E21.grid(row=8,column=1)
		btn19.grid(row=9,column=1)
		
def EditFile():
	global E12 
	L11 = tkinter.Label(page5, text = "Enter ID" , bg="blue",width=25)
	E12 = tkinter.Entry(page5,width = 5)
	btn18 = tkinter.Button(page5,text="Enter",bg="dodgerblue",width=21,command = EditFunc)
	L11.pack(fill="y",expand="true") 
	E12.pack(fill="y",expand="true")
	btn18.pack(fill="y",expand="true") 
	
def DeleteFunc():
	global E11 
	f2 = E11.get()
	if os.path.exists("Pat"+str(f2)+".txt"):
		os.remove("Pat"+str(f2)+".txt")
		#print("Done")
		messagebox.showinfo("Congratulation","Done")
	else :
		messagebox.showinfo("Warning","Not Exist ID")	
def DeleteFile():
	global page5
	global E11
	L10 = tkinter.Label(page5, text = "Enter ID" , bg="blue",width=25)
	E11 = tkinter.Entry(page5,width = 5)
	btn17 = tkinter.Button(page5,text="Enter",bg="dodgerblue",width=21,command = DeleteFunc)
	L10.pack(fill="y",expand="true")
	E11.pack(fill="y",expand="true")
	btn17.pack(fill="y",expand="true")
def AddFunc():
	f1 = E10.get()
	if os.path.exists("Pat"+str(f1)+".txt"):
		#print("Error Repeat")
		messagebox.showinfo("Warning","Exist ID")
	else :
		file = open("pat"+str(f1)+".txt","w")
		file.write(str(E2.get())+"\n")
		file.write(str(E3.get())+"\n")
		file.write(str(E4.get())+"\n")
		file.write(str(E5.get())+"\n")
		file.write(str(E6.get())+"\n")
		file.write(str(E7.get())+"\n")
		file.write(str(E8.get())+"\n")
		file.write(str(E9.get())+"\n")
		file.write(str(E10.get())+"\n")
		messagebox.showinfo("Congratulation","Done")
		#print("Done")
	

def AddFile():
	global E2
	global E3
	global E4
	global E5
	global E6
	global E7
	global E8
	global E9
	global E10
	page8=tkinter.Toplevel(page5)
	page8.title("Add a Patient")
	page8.geometry("500x500+500+150")
	page8.configure(bg="blue")
	L1 = tkinter.Label(page8, text = "Department" , bg="blue",width=25)
	L2 = tkinter.Label(page8, text = "Name of Doctor" , bg="blue",width=25)
	L3 = tkinter.Label(page8, text = "Name" , bg="blue",width=25)
	L4 = tkinter.Label(page8, text = "Age" , bg="blue",width=25)
	L5 = tkinter.Label(page8, text = "Gender" , bg="blue",width=25)
	L6 = tkinter.Label(page8, text = "Address" , bg="blue",width=25)
	L7 = tkinter.Label(page8, text = "Phone Number" , bg="blue",width=25)
	L8 = tkinter.Label(page8, text = "Condition" , bg="blue",width=25)
	L9 = tkinter.Label(page8, text = "ID" , bg="blue",width=25)
	E2 = tkinter.Entry(page8,width = 15)
	E3 = tkinter.Entry(page8,width = 15)
	E4 = tkinter.Entry(page8,width = 15)
	E5 = tkinter.Entry(page8,width = 15)
	E6 = tkinter.Entry(page8,width = 15)
	E7 = tkinter.Entry(page8,width = 15)
	E8 = tkinter.Entry(page8,width = 15)
	E9 = tkinter.Entry(page8,width = 30)
	E10 = tkinter.Entry(page8,width = 5)
	L1.grid(row=0,column=0)
	L2.grid(row=1,column=0)
	L3.grid(row=2,column=0)
	L4.grid(row=3,column=0)
	L5.grid(row=4,column=0)
	L6.grid(row=5,column=0)
	L7.grid(row=6,column=0)
	L8.grid(row=7,column=0)
	L9.grid(row=8,column=0)
	E2.grid(row=0,column=1)
	E3.grid(row=1,column=1)
	E4.grid(row=2,column=1)
	E5.grid(row=3,column=1)
	E6.grid(row=4,column=1)
	E7.grid(row=5,column=1)
	E8.grid(row=6,column=1)
	E9.grid(row=7,column=1)
	E10.grid(row=8,column=1)
	btn17 = tkinter.Button(page8,text="Enter",bg="dodgerblue",width=21,command = AddFunc).grid(row=9,column=1)
''' Manage a Patient ''' 
'''
    *
	*
	*
	*
	*
	*
	'''
''' Admin Mode '''	
def Page7():
	global page7
	page7=tkinter.Toplevel(page1)
	page7.title("Admin Mode")
	page7.geometry("500x500+500+150")
	page7.configure(bg="dodgerblue")
	btn14 = tkinter.Button(page7,text="Book an Appointment",bg="dodgerblue",width=21,command=AddAppointmentFile)
	btn15 = tkinter.Button(page7,text="Edit an Appointment",bg="dodgerblue",width=21,command=EditAppointmentFile)
	btn16 = tkinter.Button(page7,text="Cancel an Appointment",bg="dodgerblue",width=21,command=CancelAppointmentFile)
	btn14.pack(fill="y",expand="true")
	btn15.pack(fill="y",expand="true")
	btn16.pack(fill="y",expand="true")
	
def Page6():
	global page6
	page6=tkinter.Toplevel(page1)
	page6.title("Admin Mode")
	page6.geometry("500x500+500+150")
	page6.configure(bg="dodgerblue")
	btn10 = tkinter.Button(page6,text="Add a Doctor",bg="dodgerblue",width=21,command = AddDocFile)
	btn11 = tkinter.Button(page6,text="Delete a Doctor",bg="dodgerblue",width=21,command = DeleteDocFile)
	btn12 = tkinter.Button(page6,text="Edit a Doctor",bg="dodgerblue",width=21,command = EditDocFile)
	btn13 = tkinter.Button(page6,text="Display a Doctor",bg="dodgerblue",width=21,command=ReadDocFile)
	btn10.pack(fill="y",expand="true")
	btn11.pack(fill="y",expand="true")
	btn12.pack(fill="y",expand="true")
	btn13.pack(fill="y",expand="true")
	
def Page5():
	global page5
	page5=tkinter.Toplevel(page1)
	page5.title("Admin Mode")
	page5.geometry("500x500+500+150")
	page5.configure(bg="dodgerblue")
	btn6 = tkinter.Button(page5,text="Add a Patient",bg="dodgerblue",width=21,command = AddFile)
	btn7 = tkinter.Button(page5,text="Delete a Patient",bg="dodgerblue",width=21,command = DeleteFile)
	btn8 = tkinter.Button(page5,text="Edit a Patient",bg="dodgerblue",width=21,command = EditFile)
	btn9 = tkinter.Button(page5,text="Display a Patient",bg="dodgerblue",width=21,command = ReadFile)
	btn6.pack(fill="y",expand="true")
	btn7.pack(fill="y",expand="true")
	btn8.pack(fill="y",expand="true")
	btn9.pack(fill="y",expand="true")
''' Admin Mode '''
'''
    *
	*
	*
	*
	*
	*
	'''
	
def Checkpass():
	global page4
	global btn3 
	global btn4
	global btn5
	global btn6
	global y
	x = E1.get() 
	z = 0
	if(str(x) == "1234"):
			page4=tkinter.Toplevel(page1)
			page4.title("Admin Mode")
			page4.geometry("500x500+500+150")
			page4.configure(bg="darkblue") 
			btn4 = tkinter.Button(page4,text="manage patients",bg="dodgerblue",width=21,command = Page5)
			btn5 = tkinter.Button(page4,text="Manage Doctors",bg="dodgerblue",width=21,command = Page6)
			btn6 = tkinter.Button(page4,text="Book an Appointment",bg="dodgerblue",width=21,command = Page7)
			btn4.pack(fill="y",expand="true")
			btn5.pack(fill="y",expand="true")
			btn6.pack(fill="y",expand="true")
	else :	
		y+=1 
	if y == 3 :
		exit()

def Page1():
	global E1
	global page1
	page1=tkinter.Toplevel(main)
	page1.title("Admin Mode")
	page1.geometry("500x500+500+150")
	page1.configure(bg="darkblue")
	Label2 = tkinter.Label(page1,text = "Enter Your Password",bg="darkblue")
	E1 = tkinter.Entry(page1,width = 8,show = "*")
	btn3 = tkinter.Button(page1,text="Enter",bg="red",width=12,command = Checkpass)
	Label2.pack(fill="y",expand="true")
	E1.pack()
	btn3.pack()
'''
    *
	*
	*
	*
	*
	*
	'''
def UserMode_Doctors() :
		UMD = 1 
		str_UMD = ""
		while UMD < 100 :
			if os.path.exists("Doc"+str(UMD)+".txt") :
				file_UMD = open("Doc"+str(UMD)+".txt","r")
				str_UMD = str_UMD + "------------\n"+str(file_UMD.read())
				file_UMD.close()
			UMD +=1
		messagebox.showinfo("Doctors", str_UMD)

def UserMode_Patients() :
		UMD2 = 1 
		str_UMD2 = ""
		while UMD2 < 100 :
			if os.path.exists("pat"+str(UMD2)+".txt") :
				file_UMD2 = open("pat"+str(UMD2)+".txt","r")
				str_UMD2 = str_UMD2 + "------------\n"+str(file_UMD2.read())
				file_UMD2.close()
			UMD2 +=1
		messagebox.showinfo("Patients", str_UMD2)
def UserMode_PatientsFunc() :
	UMD3 = Eu1.get()
	str_UMD3 = ""
	if os.path.exists("pat"+str(UMD3)+".txt"):
		file_UMD3 = open("pat"+str(UMD3)+".txt","r")
		str_UMD3=str(file_UMD3.read())
	else :
		str_UMD3 = "Error ID"	
	messagebox.showinfo("Patient", str_UMD3)

def UserMode_PatientsID() : 
	global Eu1
	Lu1 = tkinter.Label(page2,text = "Enter ID",bg="slateblue",width=20)
	btnu1 = tkinter.Button(page2,text="Enter",bg="slateblue",width=20,command = UserMode_PatientsFunc)
	Eu1 = tkinter.Entry(page2,text="ID",width=20)
	Lu1.pack(fill="y",expand="true")
	Eu1.pack(fill="y",expand="true")
	btnu1.pack(fill="y",expand="true")
	
def UserMode_Departments() :
	file99 = open("Departments.txt","r")
	BA99 = str(file99.read())
	messagebox.showinfo("Departments", BA99)
	file99.close()
	
def UserMode_Appointments() :
	file88 = open("Appointments.txt","r")
	BA88 = str(file88.read())
	messagebox.showinfo("Appointments", BA88)
	file88.close()
				
def Page2():
	global page2
	page2=tkinter.Toplevel(main)
	page2.title("User Mode")
	page2.geometry("500x500+500+150")
	page2.configure(bg="blue")
	btn1 = tkinter.Button(page2,text="Departments",bg="red",width=20,command=UserMode_Departments)
	btn2 = tkinter.Button(page2,text="Doctors",bg="red",width=20,command = UserMode_Doctors)
	btn4 = tkinter.Button(page2,text="Patients",bg="red",width=20,command = UserMode_Patients)
	btn4_2 = tkinter.Button(page2,text="Patient Details",bg="red",width=20,command = UserMode_PatientsID)
	btn4_3 = tkinter.Button(page2,text="Doctor Appointments",bg="red",width=20,command=UserMode_Appointments)
	btn1.pack(fill="y",expand="true")
	btn2.pack(fill="y",expand="true")
	btn4.pack(fill="y",expand="true")
	btn4_2.pack(fill="y",expand="true")
	btn4_3.pack(fill="y",expand="true")

	
main = tkinter.Tk()
main.title("Hospital System")
main.geometry("200x200+500+150")
main.configure(bg="slateblue")
Label = tkinter.Label(main , text = "Welcom,\nChoose Your Mode" , bg="slateblue")
Label.pack(fill="both",expand="true")
btn1 = tkinter.Button(main,text="Admin Mode",bg="dodgerblue",width=12,command=Page1)
btn2 = tkinter.Button(main,text="User Mode",bg="dodgerblue",width=12,command=Page2)
btn1.pack(fill="y",expand="true")
btn2.pack(fill="y",expand="true")


if os.path.exists("Appointments.txt"):
	pass 
else :
	BAfile = open("Appointments.txt","w")
	BAcounter = 1 
	while BAcounter < 13 :
		BAfile.write(Appointments_list1[BAcounter]+"\n")
		BAcounter +=1 
	BAfile.close()	

main.mainloop()