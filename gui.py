# import tkinter as tk					 
from tkinter import ttk 


# root = tk.Tk() 
# root.title("Tab Widget") 
# tabControl = ttk.Notebook(root) 

# tab1 = ttk.Frame(tabControl) 
# tab2 = ttk.Frame(tabControl) 

# tabControl.add(tab1, text ='Tab 1') 
# tabControl.add(tab2, text ='Tab 2') 
# tabControl.pack(expand = 1, fill ="both") 

# ttk.Label(tab1, 
# 		text ="Welcome to GeeksForGeeks").grid(column = 0, row = 0, padx = 30, pady = 30) 
# ttk.Label(tab2, 
# 		text ="Lets dive into the world of computers").grid(column = 0, row = 0,padx = 30,  	pady = 30) 


# root.mainloop() 
import tkinter as tk




master = tk.Tk()
tk.Label(master, text="Youtube Video Url").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def download_video():
    print(e1.get())
    # label = tk.Label(master, text = "Welcome to DataCamp's Tutorial on Tkinter!", fg = "red").grid(row=4)
    label.config(text="Fail!")        # op_label['fg'] = 'red'

    # ttk.Label(tab1, text =e1.get()).grid(column = 0, row = 0, padx = 30, pady = 30) 

tk.Button(master, text='Submit', command=download_video).grid(row=5, column=5, sticky=tk.W, pady=4)
label = tk.Label(master, text = "Welcome to DataCamp's Tutorial on Tkinter!", fg = "red")
label.grid(row=4)



master.mainloop()