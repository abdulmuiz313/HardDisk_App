from functools import partial
from tkinter import *
import pickle
#smart_5_raw	smart_187_raw	smart_188_raw	smart_197_raw	smart_198_raw	pic
#smart_5_raw	smart_12_raw	smart_187_raw	smart_188_raw	smart_197_raw	smart_198_raw all attributes


#----------------Manual Test Frame------------------------------------
def man_ent(frame):
    for w in frame.winfo_children():
        w.destroy()
    Label(frame,text="Enter Values Manually").pack()
    s5_int=IntVar()
    s187_int=IntVar()
    s188_int=IntVar()
    s197_int=IntVar()
    s198_int=IntVar()
    Label(frame,text="Enter SMART 5").pack()
    s5=Entry(frame,textvariable=s5_int).pack()
    Label(frame,text="Enter SMART 187").pack()
    s187=Entry(frame,textvariable=s187_int).pack()
    Label(frame,text="Enter SMART 188").pack()
    s188=Entry(frame,textvariable=s188_int).pack()
    Label(frame,text="Enter SMART 197").pack()
    s197=Entry(frame,textvariable=s197_int).pack()
    Label(frame,text="Enter SMART 198").pack()
    s198=Entry(frame,textvariable=s198_int).pack()

    submit_btn=Button(frame,text="Get Result",command=partial(man_test,s5_int,s187_int,s188_int,s197_int,s198_int,frame))
    submit_btn.pack()
    previousbtn=Button(frame,text="Back",command=partial(previous_page,frame))
    previousbtn.pack()


#----------------Previous Frame------------------------------------
def previous_page(frame):
    for w in frame.winfo_children():
        w.destroy()
    Label(frame,text="Hard Disk Failure Prediction").pack()
    manualbtn=Button(frame,text="Manual Test",command=partial(man_ent,frame))
    manualbtn.pack()
    autobtn=Button(frame,text="Auto Test",command=partial(auto_test,frame))
    autobtn.pack(side=TOP)



#----------------Auto Test Frame----------------------------
def auto_test(frame):
    for w in frame.winfo_children():
        w.destroy()
    Label(frame,text="Auto test functionality not included,as this is a desktop application.").pack()
    previousbtn=Button(frame,text="Back",command=partial(previous_page,frame))
    previousbtn.pack()
    

#-------------------------Manual Test Operation Function---------------------------
def man_test(s5_int,s187_int,s188_int,s197_int,s198_int,frame):
    loaded_mmodel=pickle.load(open('bbmodel.sav','rb'))
    test=[[s5_int.get(),s187_int.get(),s188_int.get(),s197_int.get(),s198_int.get()]]
    print(test)
    result=loaded_mmodel.predict(test)
    for w in frame.winfo_children():
        w.destroy()
    Label(frame,text="Result").pack()
    if(result[0]==1):
        Label(frame,text="Your Hard Disk will Fail soon").pack()
    
    else:
        Label(frame,text="Your Hard Disk is in Good Health").pack()
    
    previousbtn=Button(frame,text="Back",command=partial(previous_page,frame))
    previousbtn.pack()



#----------------Main------------------------------------
def driver():
    win=Tk()
    win.title("Hard Disk Failure Prediction")
    win.maxsize(width=720,height=420)
    win.minsize(width=720,height=420)
    frame=Frame(win)
    frame.pack(side="top",fill="both")
    Label(frame,text="Hard Disk Failure Prediction").pack()
    manualbtn=Button(frame,text="Manual Test",command=partial(man_ent,frame))
    manualbtn.pack(side=TOP)
    autobtn=Button(frame,text="Auto Test",command=partial(auto_test,frame))
    autobtn.pack(side=TOP)
    win.mainloop()



driver()