import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk 
from tkinter import font as tkfont
import pyperclip  # Module để truy cập clipboard
import os,json
import threading
from manager import manager
import api
from api import facebook
class giaodien():
    def __init__(self) -> None:
        self.nameacc = []
        self.tokenacc = []
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Tool Gộp By VoLeTrieuLan")
        self.root.geometry("1100x750")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tab3 = ttk.Frame(self.notebook)
        # self.tab8 = ttk.Frame(self.notebook)

        # self.notebook.add(self.tab8, text='Quản Lí Tool')
        self.notebook.add(self.tab3, text='Cookie Acc')
    
    def tab(self):
        self.showdevice = tk.Frame(self.tab3,bg='white')
        self.showdevice.pack(side=tk.LEFT)
        self.showdevice.pack_propagate(False)
        self.showdevice.configure(width = 1100, height = 850  )
        self.showdevice.place(x=0,y=0)

        self.cookie()
        self.button()
        self.openapp()
        self.root.mainloop()

    def show_context_menu(self,event):
        context_menu.post(event.x_root, event.y_root)

    def paste(self):
        self.len_codeacc = len(self.thongtinacc.get_children())
        manager().account(self.ck,self.thongtinacc,self.len_codeacc)

    def threadpaste(self):
        copied_text = pyperclip.paste()
        self.ck = copied_text.split()
        print(copied_text)
        try:
            with open('code.txt','a') as f:
                f.write(f'{copied_text}\n')
                f.close()
        except:
            with open('code.txt','w') as f:
                f.write(f'{copied_text}\n')
                f.close()
        for _ in range(1):
            thread = threading.Thread(target=self.paste)
            thread.start()

    def run(self):
        api.thread(self.thongtinacc)
        
    def threadrun(self):
        for _ in range(1):
            thread = threading.Thread(target=self.run)
            thread.start()

    def openapp(self):
        with open('code.txt','r') as f:
            f = f.readlines()
            for i in range(len(f)):
                try:
                    tk , mk , check = f[i].split('|')
                    self.thongtinacc.insert("", "end", values=(i, tk,mk,check))
                except:
                    tk , mk = f[i].split('|')
                    self.thongtinacc.insert("", "end", values=(i, tk,mk))
            
    def closechrome(self):
        for _ in range(1):
            thread = threading.Thread(target=facebook.close)
            thread.start()

    def contine(self):
        for _ in range(1):
            thread = threading.Thread(target=facebook.contineu)
            thread.start()

    def cookie(self):

        global context_menu
        self.thongtincookie = tk.Frame(self.showdevice, background='white', highlightbackground='black', highlightthickness=1)
        self.thongtincookie.place(x=0, y=125, width=1100, height=610)

        scrollbar = tk.Scrollbar(self.thongtincookie, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure("Treeview", rowheight=25)

        self.thongtinacc = ttk.Treeview(self.thongtincookie, yscrollcommand=scrollbar.set)
        self.thongtinacc.pack(expand=True, fill="both")
        scrollbar.config(command=self.thongtinacc.yview)

        self.thongtinacc["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight")
        self.thongtinacc.column("one", width=50)
        self.thongtinacc.column("two", width=200)
        self.thongtinacc.column("three", width=100)
        self.thongtinacc.column("four", width=200)

        self.thongtinacc.heading("one", text="Index", anchor=tk.W)
        self.thongtinacc.heading("two", text="ID ACC", anchor=tk.W)
        self.thongtinacc.heading("three", text="PASSWORD", anchor=tk.W)
        self.thongtinacc.heading("four", text="STATUS", anchor=tk.W)

        self.thongtinacc['show'] = 'headings'

        context_menu = tk.Menu(self.thongtinacc, tearoff=0)
        context_menu.add_command(label="Paste", command=self.threadpaste)
        # context_menu.add_command(label="Delete", command=self.deletecookie)
        # context_menu.add_command(label="Reset", command=self.reset)
        # context_menu.add_command(label="Getnewtoken", command=self.threadnewtoken)
        # context_menu.add_command(label="Proxy", command=self.proxy)
        self.thongtinacc.bind("<Button-3>", self.show_context_menu)

    def button(self):

        frame = tk.Frame(self.showdevice, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd=0)
        frame.configure(width = 100, height = 50  )
        frame.place(x=10,y=10)

        frame1 = tk.Frame(self.showdevice, highlightbackground="red", highlightcolor="red", highlightthickness=2, bd=0)
        frame1.configure(width = 100, height = 50  )
        frame1.place(x=120,y=10)

        frame2 = tk.Frame(self.showdevice, highlightbackground="orange", highlightcolor="orange", highlightthickness=2, bd=0)
        frame2.configure(width = 120, height = 50  )
        frame2.place(x=230,y=10)

        frame3 = tk.Frame(self.showdevice, highlightbackground="purple", highlightcolor="purple", highlightthickness=2, bd=0)
        frame3.configure(width = 130, height = 50  )
        frame3.place(x=10,y=60)

        frame4 = tk.Frame(self.showdevice, highlightbackground="brown", highlightcolor="brown", highlightthickness=2, bd=0)
        frame4.configure(width = 130, height = 50  )
        frame4.place(x=135,y=60)

        frame5 = tk.Frame(self.showdevice, highlightbackground="brown", highlightcolor="brown", highlightthickness=2, bd=0)
        frame5.configure(width = 130, height = 50  )
        frame5.place(x=260,y=60)

        custom_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        button = tk.Button(frame, text="Bắt Đầu", bg="white", fg="green", width=12, height=2,bd=0, font=custom_font,relief="solid",
                           command=self.threadrun)
        button.pack()

        button = tk.Button(frame1, text="Dừng lại", bg="white", fg="red", width=12, height=2,bd=0, font=custom_font,relief="solid",)
        button.pack()

        button = tk.Button(frame2, text="Cài đặt nâng cao", bg="white", fg="orange", width=15, height=2,bd=0, font=custom_font,relief="solid"
                           ,command=self.button_setting)
        button.pack()

        button = tk.Button(frame3, text="Output Acc Live", bg="white", fg="purple", width=14, height=2,bd=0, font=custom_font,relief="solid",
                           )
        button.pack()

        button = tk.Button(frame4, text="Output Acc Die", bg="white", fg="brown", width=14, height=2,bd=0, font=custom_font,relief="solid",
                           )
        button.pack()

        button = tk.Button(frame5, text="Continue", bg="white", fg="brown", width=14, height=2,bd=0, font=custom_font,relief="solid",
                           command=self.contine)
        button.pack()
    
    def button_setting(self):
        toplevel = tk.Toplevel(self.root)
        toplevel.title("Cài đặt nâng cao")
        toplevel.geometry('450x250')

        self.toplevel = tk.Frame(toplevel,background='white')
        self.toplevel.pack(side=tk.LEFT,fill="both", expand=True)
        self.toplevel.pack_propagate(False)
        self.toplevel.configure(width = 450, height = 250  )
        self.toplevel.place(x=0,y=0)

        

        #-------------------------------------------------Cài đặt nâng cao-----------------------------------------------
        
        self.WIDTH = tk.StringVar()
        self.HEIGHT = tk.StringVar()
        self.CHECKCLONE = tk.StringVar()
        self.LUONG = tk.StringVar()
        self.DELAY = tk.StringVar()

        self.len_codeacc = len(self.thongtinacc.get_children())
        
        self.create_ld = tk.Frame(self.toplevel,background='white',highlightbackground='black',
                    highlightthickness=1)
        self.create_ld.pack(side=tk.LEFT,fill="both", expand=True)
        self.create_ld.pack_propagate(False)
        self.create_ld.configure(width = 450, height = 250  )
        self.create_ld.place(x=0,y=17)

        frame = tk.Frame(self.toplevel, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd=0)
        frame.configure(width = 300, height = 50  )
        frame.place(x=0,y=207)

        label = tk.Label(self.create_ld, text="SIZE: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=16)

        label = tk.Label(self.create_ld, text="X ",fg='black',bg='white', font=("Airbnb Cereal", 15, "bold"))
        label.place(x=246,y=16)

        label = tk.Label(self.toplevel, text="Setting Chrome",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=0,y=0)

        label = tk.Label(self.create_ld, text="Số Clone Check: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=56)

        label = tk.Label(self.create_ld, text=f"( Đang có [{self.len_codeacc}] Clone )",fg='red',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=280,y=56)

        label = tk.Label(self.create_ld, text="Luồng: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=86)

        label = tk.Label(self.create_ld, text="Delay mỗi luồng: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=116)

        try:
            with open('Advanced_settings.json', 'r') as configfile:
                config_data = json.load(configfile)
                soclone = config_data["soclone"]
                luong = config_data["luong"]
                delay = config_data["delay"]

                spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                        textvariable = self.WIDTH, font=("Arial", 10, "bold")).place(x=150,y=19)
                self.WIDTH.set(400)

                spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                        textvariable = self.HEIGHT, font=("Arial", 10, "bold")).place(x=280,y=19)
                self.HEIGHT.set(500)

                spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                        textvariable = self.CHECKCLONE, font=("Arial", 10, "bold")).place(x=150,y=56)
                self.CHECKCLONE.set(soclone)

                spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                        textvariable = self.LUONG, font=("Arial", 10, "bold")).place(x=150,y=86)
                self.LUONG.set(luong)

                spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                        textvariable = self.DELAY, font=("Arial", 10, "bold")).place(x=150,y=116)
                self.DELAY.set(delay)
    
        except:
            spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                    textvariable = self.WIDTH, font=("Arial", 10, "bold")).place(x=150,y=19)

            spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                    textvariable = self.HEIGHT, font=("Arial", 10, "bold")).place(x=280,y=19)

            spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                    textvariable = self.CHECKCLONE, font=("Arial", 10, "bold")).place(x=150,y=56)

            spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                    textvariable = self.LUONG, font=("Arial", 10, "bold")).place(x=150,y=86)

            spinbox = tk.Spinbox(self.create_ld, from_=0, to=10000000000000,width=10,
                                    textvariable = self.DELAY, font=("Arial", 10, "bold")).place(x=150,y=116)

        custom_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        button = tk.Button(frame, text="Lưu cấu hình", bg="green", fg="black", width=55, height=2,bd=0, font=custom_font,relief="solid",
                           command=self.save_setting)
        button.pack()

    def save_setting(self):

        WIDTH = self.WIDTH.get()
        HEIGHT = self.HEIGHT.get()
        CHECKCLONE = self.CHECKCLONE.get()
        LUONG = self.LUONG.get()
        DELAY = self.DELAY.get()

        manager().setting(WIDTH,HEIGHT,CHECKCLONE,LUONG,DELAY)



giaodien().tab()