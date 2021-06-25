from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn    


def verifier():
    a=b=c=d=e=0
    if not student_name.get():
        t1.insert(END,"<>Student_name is required<>\n")
        a=1
    if not school_id.get():
        t1.insert(END,"<>School_Id is required<>\n")
        b=1
    if not course.get():
        t1.insert(END,"<>Course is required<>\n")
        c=1
    if not year_level.get():
        t1.insert(END,"<>Year_Level is requrired<>\n")
        d=1
    if not gender.get():
        t1.insert(END,"<>Gender is required<>\n")
        e=1
    if a==1 or b==1 or c==1 or d==1 or e==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(STUDENT_AME TEXT,SCHOOL_ID INTEGER,COURSE TEXT,YEAR_LEVEL INTEGER,GENDER TEXT)")
                cur.execute("insert into STUDENTS values(?,?,?,?,?,?)",(student_name.get(),int(school_id.get()),course.get(),int(year_level.get()),gender.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def View_Student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from STUDENTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=?",(int(school_id.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=?,ROLL_NO=?,BRANCH=?,PHONE_NO=?,FATHER=?,ADDRESS=? where ROLL_NO=?",(student_name.get(),int(school_id.get()),course.get(),int(year_level.get()),gender.get(),address.get(),int(school_id.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")


def clse():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("Event Attendance System")
     
    student_name=StringVar()
    school_id=StringVar()
    course=StringVar()
    year_level=StringVar()
    gender=StringVar()
    
    label1=Label(root,text="Student_name:")
    label1.place(x=0,y=0)

    label2=Label(root,text="School_Id:")
    label2.place(x=0,y=30)

    label3=Label(root,text="Course:")
    label3.place(x=0,y=60)

    label4=Label(root,text="Year_Level:")
    label4.place(x=0,y=90)

    label5=Label(root,text="Gender:")
    label5.place(x=0,y=120)

    e1=Entry(root,textvariable=student_name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=student_id)
    e2.place(x=100,y=30)

    e3=Entry(root,textvariable=course)
    e3.place(x=100,y=60)

    e4=Entry(root,textvariable=year_level)
    e4.place(x=100,y=90)
    
    e5=Entry(root,textvariable=gender)
    e5.place(x=100,y=120)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
   
    b1=Button(root,text="ADD STUDENT",command=add_student,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL STUDENTS",command=view_student,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE STUDENT",command=delete_student,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE INFO",command=update_student,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="CLOSE",command=clse,width=40)
    b5.grid(row=15,column=0)


    root.mainloop()
