import tkinter as tk  
from functools import partial  
import os
   
   

def createFile():
    start1 = start.get()
    end1 = end.get()
    path = link.get()
    for i in range(int(start1),(int(end1)+1)):
        file_name =  name.get()+ str(i) + ext.get()
        i = i+1
        complete = os.path.join(path,file_name)
        
        file1 = open(complete, "w")
        file1.close()
    
   
root = tk.Tk()  
root.geometry('500x400')  
  
root.title('Create new file')  
   
link = tk.StringVar()  
name = tk.StringVar()  
start = tk.StringVar()  
end = tk.StringVar()  
ext = tk.StringVar()
labelLink = tk.Label(root, text="Nhap link").grid(row=1, column=0)  
  
labelName = tk.Label(root, text="Name").grid(row=2, column=0)  
  
labelStart = tk.Label(root,text="Start").grid(row=3,column=0)

labelEnd = tk.Label(root,text="End").grid(row=4,column=0)  

labelExt = tk.Label(root,text="Extension").grid(row=5,column=0)  

entryLink = tk.Entry(root, textvariable=link).grid(row=1, column=1)  
  
entryName = tk.Entry(root, textvariable=name).grid(row=2, column=1)  

entryStart = tk.Entry(root, textvariable=start).grid(row=3, column=1)  

entryEnd = tk.Entry(root, textvariable=end).grid(row=4, column=1)  

entryExt = tk.Entry(root, textvariable=ext).grid(row=5, column=1)  

labelLink = tk.Label(root, text="(C://user//foldername)").grid(row=1, column=3)  
  
labelName = tk.Label(root, text="Name").grid(row=2, column=3)

labelStart = tk.Label(root,text="Nhap so").grid(row=3,column=3)

labelEnd = tk.Label(root,text="Nhap so").grid(row=4,column=3)  

labelExt = tk.Label(root,text="(.txt, .csv, .xlsx...)").grid(row=5,column=3)  
  
btn1 = tk.Button(root, text="Create", command=createFile).grid(row=6, column=0)  
  
root.mainloop()  