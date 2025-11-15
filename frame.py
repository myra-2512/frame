from tkinter import *

root=Tk()
root.geometry("400x400")
root.title("Number Pad")

nums=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]

for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=75)
    for j in range(0,3):
        frame=Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i,column=j)
        lbl=Label(master=frame,text=nums[i][j],bg="lightgreen")
        lbl.pack(padx=3,pady=3)

root.mainloop()