import Tkinter
from Tkinter import *
import tkMessageBox
class App:
	def __init__(self,parent):
		self.parent = parent
		self.frame_1 = Frame(parent)
		self.frame_1.pack()
		
		self.lbl_1 = Label(self.frame_1,text="Current CGPA :")
		self.lbl_1.grid(row=0,column=0)
		self.entry_1 = Entry(self.frame_1)
		self.entry_1.grid(row=0,column=1)

		self.lbl_2 = Label(self.frame_1,text="Units Completed :")
		self.lbl_2.grid(row=1,column=0)
		self.entry_2 = Entry(self.frame_1)
		self.entry_2.grid(row=1,column=1)

		self.lbl_3 = Label(self.frame_1,text="Number of Courses to add :")
		self.lbl_3.grid(row=2,column=0)
		self.entry_3 = Entry(self.frame_1)
		self.entry_3.grid(row=2,column=1)		
		
		self.btn_1 = Button(parent,text="Add Courses !",command=self.add_courses)
		self.btn_1.pack(pady=8)

		self.frame_2 = Frame(parent)
		self.frame_2.pack()
		
	def add_courses(self):
		if ((self.entry_3.get() != '') & (self.entry_3.get().isdigit())):
			self.num_courses = int(self.entry_3.get())
			self.grades_list = []
			self.units_list = []
			self.lbl_units = Label(self.frame_2,text="Units :")
			self.lbl_units.grid(row=0,column=0)
			self.lbl_grades = Label(self.frame_2,text="Grades :")
			self.lbl_grades.grid(row = 0,column=1)
			for i in range (0, self.num_courses):				
				self.units_list.append(Spinbox(self.frame_2,values=(1,2,3,4,5,20)))
				self.units_list[i].grid(row = i+1,column = 0,padx=10,pady=10)
				
				self.grades_list.append(Spinbox(self.frame_2,values = ("A","A-","B","B-","C","C-","D","E")))
				self.grades_list[i].grid(row = i+1,column=1,padx=10,pady=10)
			self.btn_calcCG = Button(self.parent,text="Calculate CGPA",command = self.calc_CG)
			self.btn_calcCG.pack(pady=8)
			self.btn_1.config(state = DISABLED)
		else:
			tkMessageBox.showinfo("Hey ! ", "Enter a Valid Value")

	def calc_CG(self):
		print "Calculating !"
		credits_this_sem = 0
		units_this_sem = 0
		for j in range (0,self.num_courses):
			credits_this_sem = credits_this_sem + int(self.units_list[j].get())*(self.grade(self.grades_list[j].get()))
			units_this_sem = units_this_sem + int(self.units_list[j].get())
		final_cgpa = (credits_this_sem + float(self.entry_1.get())*int(self.entry_2.get())) / (units_this_sem+int(self.entry_2.get()))
		tkMessageBox.showinfo("Predicted CGPA ", str(final_cgpa))	
		

	def grade(self,grd):
    		dict_ = {'A':10,'A-':9,'B':8,'B-':7,'C':6,'C-':5,'D':4,'E':2}
		return dict_[grd]
root=Tk()
app = App(root)
print('*** Welcome to CGPA calculator ***')
print('-----------------------------------')
print('Note: This CGPA calculator calculates the GPA out of 10 scale as used in various indian colleges. Please enter your details below to continue : \n')

root.mainloop()
