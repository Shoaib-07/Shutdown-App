from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st=Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="Black")

restart_button = Button(st, text="Restart", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart)
restart_button.place(x=150, y=60, height=50, width=200)

restart_time_button = Button(st, text="Restart in 20s", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart_time)
restart_time_button.place(x=150, y=170, height=50, width=200)

logout_button = Button(st, text="Log Out", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=logout)
logout_button.place(x=150, y=270, height=50, width=200)

shutdown_button = Button(st, text="Shutdown", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=shutdown)
shutdown_button.place(x=150, y=370, height=50, width=200)

st.mainloop()