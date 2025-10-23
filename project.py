from tkinter import *
from tkinter import ttk
import platform
import subprocess
import csv
import os
import sqlite3
from tkinter import messagebox
from fpdf import FPDF


class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Management System",bd=6,relief=GROOVE,font=("Algerian",30,'bold'),bg='#003366',fg='white' )
        title.pack(side=TOP,fill=X)


        self.sl_var = StringVar()
        self.name_var = StringVar()
        self.class_var = StringVar()
        self.section_var = StringVar()
        self.pdate_var = StringVar()
        self.mob_var = StringVar()
        self.pmob_var = StringVar()

        self.jan_var = ""
        self.feb_var = ""
        self.mar_var = ""
        self.apr_var = ""
        self.may_var = ""
        self.jun_var = ""
        self.jul_var = ""
        self.aug_var = ""
        self.sep_var = ""
        self.oct_var = ""
        self.nov_var = ""
        self.dec_var = ""


        self.pay_month_var = StringVar()
        self.pay_amount_var = StringVar()


        self.search_by = StringVar()
        self.search_txt = StringVar()


        title = Label(self.root,text="Sayon Mitra",bd=3,relief=GROOVE,font=("Brush Script MT",18),bg='#B9F6FE',fg='Black' )
        title.pack(side=BOTTOM,fill=X)

        manage_frame = Label(self.root,bd=4,relief=RIDGE,bg='#e3ebf3')
        manage_frame.place(x=15,y=80,width=480,height=580)

        m_title=Label(manage_frame,text="Manage Students",bg="#e3ebf3",fg="black",font=("times new roman",18,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)


        lbl_sl=Label(manage_frame,text="Serial No",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_sl.grid(row=1,column=0,pady=10,padx=20,sticky='w')

        txt_sl = Entry(manage_frame,textvariable= self.sl_var, font=('times new roman',14),bd=2,relief=GROOVE)
        txt_sl.grid(row=1,column=1,pady=10,padx=20,sticky='w')


        lbl_name=Label(manage_frame,text="Name",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

        txt_name = Entry(manage_frame,textvariable=self.name_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        lbl_class=Label(manage_frame,text="Class",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_class.grid(row=3,column=0,pady=10,padx=20,sticky='w')

        combo_class = ttk.Combobox(manage_frame,textvariable=self.class_var,font=("times new roman",12,'bold'),state='readonly')
        combo_class['values']=("Class 1","Class 2","Class 3","Class 4","Class 5","Class 6","Class 7","Class 8","Class 9","Class 10","Class 11","Class 12")
        combo_class.grid(row=3,column=1,pady=10,padx=20)

        lbl_section=Label(manage_frame,text="Section",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_section.grid(row=4,column=0,pady=10,padx=20,sticky='w')

        combo_section=ttk.Combobox(manage_frame,textvariable=self.section_var,font=("times new roman",12,'bold'),state='readonly')
        combo_section['values']=("A","B","C","D","E","PCM","PCB","Humanities","Commerce")
        combo_section.grid(row=4,column=1,pady=10,padx=20,sticky='w')



        lbl_pdate=Label(manage_frame,text="Date of Birth",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_pdate.grid(row=5,column=0,pady=10,padx=20,sticky='w')

        txt_pdate = Entry(manage_frame,textvariable=self.pdate_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_pdate.grid(row=5,column=1,pady=10,padx=20,sticky='w')


        lbl_mob=Label(manage_frame,text="Student's Mobile Number",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_mob.grid(row=6,column=0,pady=10,padx=20,sticky='w')

        txt_mob = Entry(manage_frame,textvariable=self.mob_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_mob.grid(row=6,column=1,pady=10,padx=20,sticky='w')

        lbl_pmob=Label(manage_frame,text="Parents Mobile Number",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_pmob.grid(row=7,column=0,pady=10,padx=20,sticky='w')

        txt_pmob = Entry(manage_frame,textvariable=self.pmob_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_pmob.grid(row=7,column=1,pady=10,padx=20,sticky='w')


        lbl_pay=Label(manage_frame,text="Payment month",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_pay.grid(row=8,column=0,pady=10,padx=20, sticky='w')

        combo_pay = ttk.Combobox(manage_frame,width=14,textvariable=self.pay_month_var,font=("times new roman",12,'bold'),state='readonly')
        combo_pay['values']=("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
        combo_pay.grid(row=8,column=1)

        lbl_amount=Label(manage_frame,text="Payment amount",bg="#e3ebf3",fg="black",font=("times new roman",14,'bold'))
        lbl_amount.grid(row=9,column=0,pady=10,padx=20, sticky='w')

        txt_pay = Entry(manage_frame,textvariable=self.pay_amount_var,width=5,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_pay.grid(row=9,column=1)

        btn_frame = Frame(manage_frame,bd=4,relief=RIDGE,bg='#f8f9fa')
        btn_frame.place(x=10,y=500,width=425)

        addbtn = Button(btn_frame,text="Add", bg="#1c4da7", fg="#FAFCFF",  width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame,text="Update", bg="#1c4da7", fg="#FAFCFF", width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame,text="Delete", bg="#1c4da7", fg="#FAFCFF", width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn = Button(btn_frame,text="Clear", bg="#1c4da7", fg="#FAFCFF", width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        detail_frame = Frame(self.root,bd=4,relief=RIDGE,bg='#e3ebf3')
        detail_frame.place(x=500,y=80,width=820,height=580)

        lbl_search = Label(detail_frame,text="Search By",bg="#e3ebf3",fg="black",font=("times new roman",16,'bold'))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')


        combo_search = ttk.Combobox(detail_frame,width=10,textvariable=self.search_by,font=("times new roman",12,'bold'),state='readonly')
        combo_search['values']=("sl","name","class")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search = Entry(detail_frame,width=30,textvariable=self.search_txt,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

        searchbtn = Button(detail_frame, bg="#484C9C", fg="#FCFCFF", text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(detail_frame, bg="#484C9C", fg="#FCFCFF", text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        csvbtn = Button(detail_frame, bg="#484C9C", fg="#FCFCFF", text="SAVE CSV",width=10,command=self.csv_save).grid(row=1,column=1,padx=5,pady=10)
        pdfbtn = Button(detail_frame, bg="#484C9C", fg="#FCFCFF", text="SAVE PDF",width=10,command=self.pdf_save).grid(row=1,column=2,padx=5,pady=10)
        pdfprintbtn = Button(detail_frame, bg="#484C9C", fg="#FCFCFF", text="PDF PRINT",width=10,command=self.print_pdf).grid(row=1,column=3,padx=5,pady=10)


        table_frame = Frame(detail_frame,bd=2,relief=RIDGE,bg='#E3EBF3')
        table_frame.place(x=10,y=80,width=785,height=480)

        scroll_x = Scrollbar(table_frame,orient="horizontal")
        scroll_y = Scrollbar(table_frame,orient="vertical")
        self.student_table = ttk.Treeview(table_frame,columns=("sl","name","class","section","pdate","mob","pmob",
                                                               "jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"),
                                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("sl", text="Sl.No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("class", text="Class")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("pdate", text="Date of Birth")
        self.student_table.heading("mob", text="Student's Mobile Number")
        self.student_table.heading("pmob", text="Parents Mobile Number")
        
        self.student_table.heading("jan", text="January")
        self.student_table.heading("feb", text="February")
        self.student_table.heading("mar", text="March")
        self.student_table.heading("apr", text="April")
        self.student_table.heading("may", text="May")
        self.student_table.heading("jun", text="June")
        self.student_table.heading("jul", text="July")
        self.student_table.heading("aug", text="August")
        self.student_table.heading("sep", text="September")
        self.student_table.heading("oct", text="October")
        self.student_table.heading("nov", text="November")
        self.student_table.heading("dec", text="December")

        self.student_table['show']='headings'

        self.student_table.column("sl",width=80)
        self.student_table.column("name",width=200)
        self.student_table.column("class",width=140)
        self.student_table.column("section",width=140)
        self.student_table.column("pdate",width=140)
        self.student_table.column("mob",width=140)
        self.student_table.column("pmob",width=140)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):

        if self.sl_var.get()=="" or self.name_var.get()=="" or self.class_var.get()=="":
            messagebox.showerror("Error","All fields are required!")
        else:
            conn=sqlite3.connect("student.db")
            cur=conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS students(sl integer,name TEXT,class TEXT, TEXT,pdate TEXT,
                            mob TEXT,pmob TEXT,jan TEXT,feb TEXT,mar TEXT,apr TEXT,may TEXT, jun TEXT,
                            jul TEXT,aug TEXT, sep TEXT,oct TEXT,nov TEXT,dec TEXT)""")

            self.set_data()
            cur.execute("insert into students values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                                                        int(self.sl_var.get()),
                                                                        self.name_var.get(),
                                                                        self.class_var.get(),
                                                                        self.section_var.get(),
                                                                        self.pdate_var.get(),
                                                                        self.mob_var.get(),
                                                                        self.pmob_var.get(),self.jan_var,self.feb_var,
                                                                        self.mar_var,self.apr_var,self.may_var,self.jun_var,
                                                                        self.jul_var,self.aug_var,self.sep_var,self.oct_var,
                                                                        self.nov_var,self.dec_var))

            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted successfully.")

    def fetch_data(self):
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            conn.commit()
        conn.close()

    def fetch_data_from_database():
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM tudents")
        columns = [description[0] for description in cursor.description]  # Fetch column names
        rows = cursor.fetchall()  # Fetch all data
        conn.close()
        return columns, rows
    

    def clear(self):
        self.sl_var.set("")
        self.name_var.set("")
        self.class_var.set("")
        self.section_var.set("")
        self.pdate_var.set("")
        self.mob_var.set("")
        self.pmob_var.set("")
        self.pay_month_var.set("")
        self.pay_amount_var.set("")

    def get_cursor(self,event):
        cursor_row =  self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.sl_var.set(row[0])
        self.name_var.set(row[1])
        self.class_var.set(row[2])
        self.section_var.set(row[3])
        self.pdate_var.set(row[4])
        self.mob_var.set(row[5])
        self.pmob_var.set(row[6])

    def update_data(self):
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        self.set_data()
        cur.execute("""update students set name=?,class=?,=?,pdate=?,mob=?,pmob=?,jan=?,
                       feb=?,mar=?,apr=?,may=?,jun=?,jul=?,aug=?,sep=?,oct=?,nov=?,dec=? where sl=?""",(
                                                                        self.name_var.get(),
                                                                        self.class_var.get(),
                                                                        self._var.get(),
                                                                        self.pdate_var.get(),
                                                                        self.mob_var.get(),
                                                                        self.pmob_var.get(),self.jan_var,self.feb_var,
                                                                        self.mar_var,self.apr_var,self.may_var,self.jun_var,
                                                                        self.jul_var,self.aug_var,self.sep_var,self.oct_var,
                                                                        self.nov_var,self.dec_var,
                                                                        int(self.sl_var.get())))

        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Record has been updated successfully.")
    def delete_data(self):
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        cur.execute("delete from students where sl=?",(int(self.sl_var.get()),))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

    def search_data(self):
        #==================================for sqlite3==================
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            conn.commit()
        else:
            messagebox.showerror("Error","Record doesn't find")
        conn.close()

    def csv_save(self):
         
       # Check if the database file exists
       if not os.path.exists("student.db"):
           messagebox.showerror("Error","Database file student.db not found.")
           return
       
       try:
           # Connect to the SQLite3 database
           conn = sqlite3.connect("student.db")
           cursor = conn.cursor()
   
           # Check if the table exists
           cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{students}'")
           
   
           # Execute the query to fetch all data from the table
           cursor.execute(f"SELECT * FROM students")
           
           # Fetch the column names
           columns = [description[0] for description in cursor.description]
           
           # Fetch all rows from the table
           rows = cursor.fetchall()
   
           # Check if the table has data
           if not rows:
               print(f"Warning: Table '{"students"}' is empty.")
           
           # Open the CSV file and write the data
           with open("data.csv", 'w', newline='') as csv_file:
               writer = csv.writer(csv_file)
               
               # Write the column headers
               writer.writerow(columns)
               
               # Write the data rows
               writer.writerows(rows)
   
           messagebox.showinfo("Done","Data from table students saved to csv_file.csv successfully.")
       
       except sqlite3.Error as e:
           print(f"SQLite error: {e}")
       
       finally:
           # Close the database connection
           if conn:
               conn.close()

    def pdf_save(self):
        # Check if the database file exists
        if not os.path.exists("student.db"):
            messagebox.showerror("Error", "Database file student.db not found.")
            return

        try:
            # Connect to the SQLite3 database
            conn = sqlite3.connect("student.db")
            cursor = conn.cursor()

            # Check if the table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
            table_exists = cursor.fetchone()
            
            if not table_exists:
                print("Warning: Table 'students' does not exist.")
                return
            # Execute the query to fetch all data from the table
            cursor.execute("SELECT * FROM students")

            # Fetch the column names
            columns = [description[0] for description in cursor.description]

            # Fetch all rows from the table
            rows = cursor.fetchall()

            # Check if the table has data
            if not rows:
                print("Warning: Table 'students' is empty.")
                return
            
             # Create PDF with A4 landscape orientation
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()

            # Header Section with School Information
            pdf.set_font("Arial", "B", 16)
            pdf.set_text_color(255, 255, 255)
            pdf.set_fill_color(70, 130, 180)  # Steel Blue color for header background
            pdf.cell(0, 10, "Greenland Public School", 0, 1, "C", fill=True)
            pdf.set_font("Arial", "", 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 10, "Address: 3, Vijayant Khand, Gomti Nagar, Lucknow", 0, 1, "C")
            pdf.cell(0, 10, "Email: responsegpslucknow@gmail.com | Phone: 9793156111, 9793243333", 0, 1, "C")
            pdf.ln(10)

             # Adding clickable payment link
            pdf.set_text_color(0, 0, 255)  # Blue color for link
            payment_url = "https://portal.eduscol.in/?sc=GPSLKO"
            pdf.cell(0, 10, "Click here for Online Payment", ln=1, align="C", link=payment_url)
            pdf.ln(10)

            # Table Header
            pdf.set_font("Arial", "B", 10)
            pdf.set_fill_color(173, 216, 230)  # Light Blue for table header
            column_widths = [25, 45, 20, 20, 30, 40, 40] + [18] * 12  # Adjusted widths for each column in landscape mode
            line_height = pdf.font_size * 1.5

            for col_name, col_width in zip(columns, column_widths):
                pdf.cell(col_width, line_height, col_name, border=1, align="C", fill=True)
            pdf.ln(line_height)
            
             # Table Rows
            pdf.set_font("Arial", "", 8)  # Reduced font size to fit more content
            for row in rows:
                for item, col_width in zip(row, column_widths):
                    pdf.cell(col_width, line_height, str(item), border=1, align="C")
                pdf.ln(line_height)
            
             # Footer
            pdf.set_y(-5)  # Position the footer at 15 mm from the bottom
            pdf.set_font("Arial", "I", 8)
            pdf.cell(0, 2, "Designed by Sayon Mitra", 0, 0, "C")

             # Save PDF
            pdf_file_name = "student_data.pdf"
            pdf.output(pdf_file_name)
            messagebox.showinfo("Done", f"Data from table students saved to {pdf_file_name} successfully.")

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

        finally:
            # Close the database connection
            if conn:
                conn.close()
    
    def print_pdf(self):
        # Define the path to the saved PDF
        pdf_path = "student_data.pdf"
        
        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            messagebox.showerror("Error", f"PDF file not found. Click on SAVE PDF")
            return
        
        try:
           # Check the operating system and use the appropriate print command
           if platform.system() == "Windows":
               # Windows print command
               os.startfile(pdf_path, "print")
           elif platform.system() == "Darwin":
               # macOS print command
               subprocess.run(["open", "-a", "Preview", pdf_path])
           else:
               # Linux/Unix print command
               subprocess.run(["lp", pdf_path])
               messagebox.showinfo("Print", "PDF sent to printer successfully.")

        except Exception as e:
            messagebox.showerror("Print Error", f"An error occurred while printing: {e}")


    def set_data(self):
        if self.pay_month_var.get()=="jan":
            self.jan_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="feb":
            self.feb_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="mar":
            self.mar_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="apr":
            self.apr_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="may":
            self.may_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="jun":
            self.jun_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="jul":
            self.jul_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="aug":
            self.aug_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="sep":
            self.sep_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="oct":
            self.oct_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="nov":
            self.nov_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="dec":
            self.dec_var = self.pay_amount_var.get()

root = Tk()
ob = Student(root)
root.mainloop()