# -----------------------------------------------------------------------------------------
# -----------------------( Student Registration System Desktop App )-----------------------
# -----------------------------------------------------------------------------------------
# ---( Import Library )---
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

# ---()---
class StudentRegistrationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration System")  # Title
        self.root.geometry("1530x800+0+0")  # Width and Height
        self.root.configure(background='silver')  # Background Color

        app_title = Label(self.root, text="Student Registration System", bd=15, relief=RIDGE,
                          bg='white', fg='#C21E56', font=("Poppins", 40, "bold"),
                          pady=4)
        app_title.pack(side=TOP, fill=X)

        # ---( Logo )---
        img1 = Image.open("N:\Student Registration System\college.png")
        img1 = img1.resize((60, 60), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Label(self.root, image=self.photoimg1, borderwidth=0, bg='white')
        b1.place(x=320, y=20)
        # ---( Icon Frame )---
        root.iconbitmap("college.ico")

        # ----( Variable )---
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.grade_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.dell_var = StringVar()
        self.se_by = StringVar()    # Combobox Data
        self.se_txt = StringVar()   # Entry Data

        # ---------------------------------------------------------------------
        # ---( Data Frame Section )---
        manage_frame = Frame(self.root, bg='#E5E4E2', bd=12, relief=RIDGE, padx=20)
        manage_frame.place(x=0, y=100, width=1535, height=400)

        # ---( Data Frame Left )---
        manage_frame_left = LabelFrame(manage_frame, bd=10, relief=RIDGE, padx=20, text="Fill Information",
                                       fg='#C21E56', font=("Poppins", 15, "bold"))
        manage_frame_left.place(x=0, y=10, width=1150, height=350)
        # ---------
        # ---( Serial Number )---
        lbl_id = Label(manage_frame, text="Student ID", bg='#5F9EA0', font=("Poppins", 15, "bold"),
                       padx=2, pady=6)
        lbl_id.place(x=50, y=70, width=250, height=40)

        id_entry = Entry(manage_frame, bd=2, justify='left', font=("Poppins", 15, "bold"),
                         bg='white', width=29, relief=RIDGE, textvariable=self.id_var)
        id_entry.place(x=320, y=70, width=250, height=40)

        # ---( Student Name )---
        lbl_name = Label(manage_frame, text="Student Name", bg='#96DED1', font=("Poppins", 15, "bold"),
                         padx=2, pady=6)
        lbl_name.place(x=50, y=140, width=250, height=40)
        name_entry = Entry(manage_frame, bd=2, justify='left', font=("Poppins", 15, "bold"),
                           width=29, relief=RIDGE, bg='white', textvariable=self.name_var)
        name_entry.place(x=320, y=140, width=250, height=40)

        # ---( Student Email )---
        lbl_email = Label(manage_frame, text="Student Email", bg='#CCCCFF', font=("Poppins", 15, "bold"),
                          padx=2, pady=6)
        lbl_email.place(x=50, y=205, width=250, height=40)
        email_entry = Entry(manage_frame, bd=2, justify='left', textvariable=self.email_var,
                            font=("Poppins", 15, "bold"), width=29, relief=RIDGE)
        email_entry.place(x=320, y=205, width=250, height=40)

        # ---( Mobile Phone )---
        lbl_phone = Label(manage_frame, text="Mobile Phone", bg='#A9A9A9', font=("Poppins", 15, "bold"),
                          padx=2, pady=6)
        lbl_phone.place(x=50, y=280, width=250, height=40)
        phone_entry = Entry(manage_frame, bd=2, justify='left', textvariable=self.phone_var,
                            font=("Poppins", 15, "bold"), width=29, relief=RIDGE)
        phone_entry.place(x=320, y=280, width=250, height=40)

        # ---( Student grades )---
        lbl_student_grades = Label(manage_frame, text="Student Grades", bg='#A95C68',
                                   font=("Poppins", 15, "bold"), padx=2, pady=6)
        lbl_student_grades.place(x=580, y=70, width=250, height=40)
        student_grade_entry = Entry(manage_frame, bd=2, justify='left', textvariable=self.grade_var,
                                    font=("Poppins", 15, "bold"), width=29, relief=RIDGE, bg='white')
        student_grade_entry.place(x=850, y=70, width=250, height=40)

        # ---( Gender )---
        lbl_gender = Label(manage_frame, text="Select Student Gender", bg='#E97451', font=("Poppins", 15, "bold"),
                           padx=2, pady=6)
        lbl_gender.place(x=580, y=140, width=250, height=40)
        combo_gender = ttk.Combobox(manage_frame, font=("Poppins", 15, "bold"), width=27,
                                    textvariable=self.gender_var)
        combo_gender['value'] = ('Male', 'Female')
        combo_gender.place(x=850, y=140, width=250, height=40)

        # ---( Address )---
        lbl_address = Label(manage_frame, text="Student Address", bg='#8A9A5B', font=("Poppins", 15, "bold"),
                            padx=2, pady=6, justify=LEFT)
        lbl_address.place(x=580, y=205, width=250, height=40)
        address_entry = Entry(manage_frame, bd=2, justify='left', font=("Poppins", 15, "bold"),
                              width=29, relief=RIDGE, textvariable=self.address_var)
        address_entry.place(x=850, y=205, width=250, height=40)

        # ---( Delete )---
        lbl_delete = Label(manage_frame, text="Delete Student By Name", bg='#E1C16E',
                           font=("Poppins", 15, "bold"), padx=2, pady=6)
        lbl_delete.place(x=580, y=280, width=250, height=40)
        delete_entry = Entry(manage_frame, bd=2, justify='left', font=("Poppins", 15, "bold"),
                             width=29, relief=RIDGE, textvariable=self.dell_var)
        delete_entry.place(x=850, y=280, width=250, height=40)
        delete_icon = Button(manage_frame, text='X', fg='red', font=("Poppins", 15, "bold"),
                             command=self.clear_del)
        delete_icon.place(x=1068, y=280, height=40)

        # -----------------------------------------
        # ---( Data Frame Right )---
        manage_frame_right = LabelFrame(manage_frame, bd=10, relief=RIDGE, padx=20, text="Search",
                                        fg='#C21E56', font=("Poppins", 15, "bold"))
        manage_frame_right.place(x=1160, y=10, width=320, height=350)

        lbl_search = Label(manage_frame_right, text="Search By", bg='#CCCCFF',
                           font=("Poppins", 15, "bold"), padx=2, pady=6)
        lbl_search.place(x=10, y=20, width=250, height=40)
        combo_search = ttk.Combobox(manage_frame_right, font=("Poppins", 15, "bold"), width=27,
                                    textvariable=self.se_by)
        combo_search['value'] = ('ID', 'Name', 'Email', 'Phone')
        combo_search.place(x=10, y=70, width=250, height=40)
        combo_search.current(0)

        search_entry = Entry(manage_frame_right, bd=3, relief=RIDGE, width=250, font=("Poppins", 15, "bold"),
                             textvariable=self.se_txt)
        search_entry.place(x=10, y=190, width=250, height=40)

        search_btn = Button(manage_frame_right, text="Search", bg='#5F9EA0', font=("Poppins", 15, "bold"),
                            command=self.search)
        search_btn.place(x=10, y=240, width=250)
        search_icon = Button(manage_frame_right, text='X', fg='red', font=("Poppins", 15, "bold"),
                             command=self.clear_search)
        search_icon.place(x=229, y=190, height=40)

        # -----------------------------------------
        # ---( Button Frame Section )---
        button_frame = LabelFrame(self.root, bd=12, relief=RIDGE, padx=20, fg='#C21E56',
                                  font=("Poppins", 15, "bold"), bg='white')
        button_frame.place(x=0, y=500, width=1535, height=90)

        add_btn = Button(button_frame, text="Add Student", bg='#6E082C', font=("Poppins", 13, "bold"),
                         fg='white', width=20, height=2, command=self.add_student)
        add_btn.place(x=0, y=8)

        del_btn = Button(button_frame, text="Delete Student", bg='#6C082B', font=("Poppins", 13, "bold"),
                         fg='white', width=20, height=2, command=self.delete)
        del_btn.place(x=250, y=8)

        update_btn = Button(button_frame, text="Update", bg='#97012F', font=("Poppins", 13, "bold"),
                            fg='white', width=20, height=2, command=self.update)
        update_btn.place(x=500, y=8)

        clear_btn = Button(button_frame, text="Clear", bg='#B50033', font=("Poppins", 13, "bold"),
                           fg='white', width=20, height=2, command=self.clear)
        clear_btn.place(x=750, y=8)

        about_btn = Button(button_frame, text="About US", bg='#DB1536', font=("Poppins", 13, "bold"),
                           fg='white', width=20, height=2, command=self.about)
        about_btn.place(x=1000, y=8)

        exit_btn = Button(button_frame, text="Exit Program", bg='#F1373B', font=("Poppins", 13, "bold"),
                          fg='white', width=20, height=2, command=self.exit_program)
        exit_btn.place(x=1250, y=8)

        # ---------------------------------------------------------------------
        # ---( Data Base Frame Section )---
        data_base_frame = LabelFrame(self.root, bd=12, relief=RIDGE, padx=10, pady=5, fg='#C21E56',
                                     font=("Poppins", 15, "bold"), bg='#E5E4E2')
        data_base_frame.place(x=0, y=590, width=1535, height=210)

        # ---( Main Table & Scrollbar )---
        scroll_x = ttk.Scrollbar(data_base_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(data_base_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_table = ttk.Treeview(data_base_frame, columns=('id', 'name', 'email', 'phone',
                                                                    'grade', 'gender', 'address'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        self.student_table.place(x=5, y=2, width=1430, height=100)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        # Heading Table
        self.student_table["show"] = "headings"

        self.student_table.heading('id', text='Student ID')
        self.student_table.heading('name', text='Student Name')
        self.student_table.heading('email', text='Student Email')
        self.student_table.heading('phone', text='Student Phone')
        self.student_table.heading('grade', text='Student Grade')
        self.student_table.heading('gender', text='Student Gender')
        self.student_table.heading('address', text='Student Address')
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.column('id', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('email', width=100)
        self.student_table.column('phone', width=100)
        self.student_table.column('grade', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('address', width=100)
        # To Show Data
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)  # Private Cursor
        self.fetch_all()  # Show data from data base

    # =============================================================
    # Functions + Database
    # ---( Add Student Function )---
    def add_student(self):
        if self.id_var.get() == '' or self.name_var.get() == '' or self.email_var. get() == '' or self.phone_var.get() == '' or self.grade_var.get() == '' or self.gender_var.get() == '' or self.address_var.get() == '':
            messagebox.showinfo('Warning', 'Please, Fill All Data Required For Student')
        else:
            con = pymysql.connect(
                host='localhost', user='root', password='root', database='student')
            cur = con.cursor()  # Connect To Data Base
            # Insert In DB
            cur.execute('insert into student_information values(%s, %s, %s, %s, %s, %s, %s)',
                        (
                            self.id_var.get(), self.name_var.get(), self.email_var.get(),
                            self.phone_var.get(), self.grade_var.get(), self.gender_var.get(),
                            self.address_var.get()
                        ))
            con.commit()  # Execute above command.
            self.fetch_all()  # when i add new student connect to data base and show data in table immediately.
            self.clear()  # when i add new student in table them remove data from fields.
            messagebox.showinfo('Student Registration System', 'Successfully Add Student')
            con.close()

    # --------------------------------------------------
    # Show Data From Database into Project
    def fetch_all(self):
        con = pymysql.connect(
            host='localhost', user='root', password='root', database='student')
        cur = con.cursor()
        #
        cur.execute('select * from student_information')
        rows = cur.fetchall()  # To Take All Data From DB
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())  # Remove tree view from other display
            for i in rows:
                self.student_table.insert('', END, value=i)  # add data at the end of data base
            con.commit()  # execute
        con.close()

    # --------------------------------------------------
    # ---( Clear Input Data From Field )---
    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.grade_var.set('')
        self.gender_var.set('')
        self.address_var.set('')

    def clear_del(self):
        self.dell_var.set('')

    def clear_search(self):
        self.se_txt.set('')

    # --------------------------------------------------
    # ---( delete student by name )---
    def delete(self):
        student_name = self.dell_var.get()
        if len(student_name) != 0:
            con = pymysql.connect(
                host='localhost', user='root', password='root', database='student')
            cur = con.cursor()
            cur.execute('delete from student_information where name=%s',  self.dell_var.get())
            con.commit()
            self.fetch_all()
            self.clear_del()
            con.close()
        else:
            messagebox.showinfo('Warning', 'You Must Enter Student Name First?')

    # --------------------------------------------------
    # When I Click on Data  In table show it in field
    def get_cursor(self, ev):  # ev => event
        curses_row = self.student_table.focus()  # When I click on data
        contents = self.student_table.item(curses_row)  # when i focus save it in contents
        columns = contents['values']  # student data i click such as id, name, ....
        self.id_var.set(columns[0])
        self.name_var.set(columns[1])
        self.email_var.set(columns[2])
        self.phone_var.set(columns[3])
        self.grade_var.set(columns[4])
        self.gender_var.set(columns[5])
        self.address_var.set(columns[6])

    # --------------------------------------------------
    # Update Student Data
    def update(self):
        if self.id_var.get() == '' or self.name_var.get() == '' or self.email_var.get() == '' or self.phone_var.get() == '' or self.grade_var.get() == '' or self.gender_var.get() == '' or self.address_var.get() == '':
            messagebox.showinfo('Warning', 'Please, Select Data For Student Table And Update It')
        else:
            con = pymysql.connect(
                host='localhost', user='root', password='root', database='student')
            cur = con.cursor()
            cur.execute('update student_information set name=%s, email=%s, phone=%s, grade=%s, gender=%s, address=%s where id=%s',
                        (
                            self.name_var.get(), self.email_var.get(),
                            self.phone_var.get(), self.grade_var.get(), self.gender_var.get(),
                            self.address_var.get(), self.id_var.get()
                        ))
            con.commit()  # Execute above command.
            self.fetch_all()  # when i add new student connect to data base and show data in table immediately.
            # self.clear()  # when i add new student in table them remove data from fields.
            messagebox.showinfo('Student Registration System', 'Successfully Update Student')
            con.close()

    # --------------------------------------------------
    # Search By (ID - Name - Email - Phone)
    def search(self):
        search_ent = self.se_txt.get()
        if len(search_ent) != 0:
            con = pymysql.connect(
                host='localhost', user='root', password='root', database='student')
            cur = con.cursor()
            # Search By Student Id LIKE I Input in Entry
            cur.execute("select * from student_information where " +
                        str(self.se_by.get()) + " LIKE '%" + str(self.se_txt.get()) + "%'")
            rows = cur.fetchall()  # To Take All Data From DB
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())  # all data
                for i in rows:
                    self.student_table.insert('', END, value=i)  # add data at the end of data base
                con.commit()
            self.clear_search()
            con.close()
        else:
            messagebox.showinfo('Warning', 'You Must Enter Value Above To Search')

    # --------------------------------------------------
    # ---( About us Function )---
    def about(self):
        messagebox.showinfo('Student Registration System',
                            """Team Members:\n[1] Mohamed Ayman Said (Leader)\n[2] Eslam Ashram Mohamed\n[3] Eslam Ashraf Gaber\n[4] Yousef Ali Sayed\n[5] Michelle Nady Fayez""")

    # -----------------------------------------------
    # ---( Exit Function )---
    def exit_program(self):
        clear = messagebox.askyesno('Confirm Exit', 'Are you sure you want exit?')
        if clear > 0:
            root.destroy()
            return

# -----------------------------------------------
# Main Function
if __name__ == "__main__":
    root = Tk()
    obj = StudentRegistrationSystem(root)
    root.mainloop()

# pyinstaller.exe --onefile -windowed -i college.ico main.py
