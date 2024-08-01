import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import font as tkfont
import pyperclip  # Module để truy cập clipboard
import os,json
import threading
from manager import manager
from api import facebook
class giaodien():
    def __init__(self) -> None:
        self.nameacc = []
        self.tokenacc = []
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Tool Gộp By VoLeTrieuLan")
        self.root.geometry("1600x800")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tab3 = ttk.Frame(self.notebook)
        # self.tab8 = ttk.Frame(self.notebook)

        # self.notebook.add(self.tab8, text='Quản Lí Tool')
        self.notebook.add(self.tab3, text='Cookie Acc')

        icon = tk.PhotoImage(file='image/facebook.png')

        # Đặt ảnh làm biểu tượng cho cửa sổ
        self.root.iconphoto(False, icon)
    
    def tab(self):
        self.showdevice = tk.Frame(self.tab3,bg='white')
        self.showdevice.pack(side=tk.LEFT)
        self.showdevice.pack_propagate(False)
        self.showdevice.configure(width = 1600, height = 800  )
        self.showdevice.place(x=0,y=0)

        self.cookie()
        self.mail()
        self.button()
        self.openapp()
        self.root.mainloop()

    def show_context_menu(self,event):
        context_menu.post(event.x_root, event.y_root)

    def show_context_menu1(self,event):
        context_menu.post(event.x_root, event.y_root)

    def delete(self):
        selected_items = self.thongtinacc.selection()
        with open('code.txt','r') as f:
            xetacc = f.readlines()
        with open('code.txt','w') as f:
            f.close()
        iddetele = []
        for item in selected_items:
            # Lưu giá trị của các mục đã chọn
            current_values = self.thongtinacc.item(item, 'values')
            self.thongtinacc.delete(item)
            iddetele.append(current_values[1])
        for i in range(len(xetacc)):
            print(iddetele,xetacc[i].split('|')[0])

            if (xetacc[i].split('|')[0] in iddetele) == False:
                with open('code.txt','a') as f:
                    f.write(fr'{xetacc[i]}')
                    f.close()
    def paste(self):
        self.len_codeacc = len(self.thongtinacc.get_children())
        manager().account(self.ck,self.thongtinacc,self.len_codeacc)
    
    def passemail(self):
        self.len_codeacc = len(self.thongtinm.get_children())
        manager().mail(self.maill,self.thongtinm,self.len_codeacc)

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

    def threadpastemail(self):
        copied_text = pyperclip.paste()
        self.maill = copied_text.split()
        print(copied_text)
        try:
            with open('mail.txt','a') as f:
                f.write(f'{copied_text}\n')
                f.close()
        except:
            with open('mail.txt','w') as f:
                f.write(f'{copied_text}\n')
                f.close()
        for _ in range(1):
            thread = threading.Thread(target=self.passemail)
            thread.start()

    def run(self):
        api.thread(self.thongtinacc,self.thongtinm)
        
    def threadrun(self):
        for _ in range(1):
            thread = threading.Thread(target=self.run)
            thread.start()

    def openapp(self):
        with open('code.txt','r') as f:
            f = f.readlines()
            for i in range(len(f)):
                print(f[i].split('|'))
                try:
                    tk ,mail, mk ,cookie, check = f[i].split('|')
                    self.thongtinacc.insert("", "end", values=(i, tk,mail,mk,cookie,check))
                except:
                    try:
                            
                        tk , mk ,cookie, check = f[i].split('|')
                        if check == 'Pass Success':
                            self.thongtinacc.insert("", "end", values=(i, tk,mk,cookie,'',check))
                        else:
                            self.thongtinacc.insert("", "end", values=(i, tk,'',mk,cookie,check))
                    except:
                        try:
                            tk , mk ,check= f[i].split('|')
                            self.thongtinacc.insert("", "end", values=(i, tk,'',mk,'',check))
                        except:
                            tk , mk = f[i].split('|')
                            self.thongtinacc.insert("", "end", values=(i, tk,'',mk,'',''))

        with open('mail.txt','r') as f:
            f = f.readlines()
            for i in range(len(f)):
                try:
                    mail, mk = f[i].split('|')
                    self.thongtinm.insert("", "end", values=(i, mail,mk))
                except:
                    mail, mk ,stt = f[i].split('|')
                    self.thongtinm.insert("", "end", values=(i, mail,mk,stt))
            
    def closechrome(self):
        for _ in range(1):
            thread = threading.Thread(target=facebook.close)
            thread.start()

    def contine(self):
        for _ in range(1):
            thread = threading.Thread(target=facebook.contineu)
            thread.start()

    def mail(self):
        global context_menu
        self.thongtinmail = tk.Frame(self.showdevice, background='white', highlightbackground='black', highlightthickness=1)
        self.thongtinmail.place(x=1110, y=125, width=490, height=610)

        scrollbar = tk.Scrollbar(self.thongtinmail, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure("Treeview", rowheight=25)

        self.thongtinm = ttk.Treeview(self.thongtinmail, yscrollcommand=scrollbar.set)
        self.thongtinm.pack(expand=True, fill="both")
        scrollbar.config(command=self.thongtinm.yview)

        self.thongtinm["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight")
        self.thongtinm.column("one", width=50)
        self.thongtinm.column("two", width=200)
        self.thongtinm.column("three", width=100)
        self.thongtinm.column("four", width=200)


        self.thongtinm.heading("one", text="Index", anchor=tk.W)
        self.thongtinm.heading("two", text="Mail", anchor=tk.W)
        self.thongtinm.heading("three", text="Password", anchor=tk.W)
        self.thongtinm.heading("four", text="Status", anchor=tk.W)

        self.thongtinm['show'] = 'headings'



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
        self.thongtinacc.column("two", width=100)
        self.thongtinacc.column("three", width=200)
        self.thongtinacc.column("four", width=100)
        self.thongtinacc.column("five", width=450)
        self.thongtinacc.column("six", width=200)

        self.thongtinacc.heading("one", text="Index", anchor=tk.W)
        self.thongtinacc.heading("two", text="ID ACC", anchor=tk.W)
        self.thongtinacc.heading("three", text="Mail", anchor=tk.W)
        self.thongtinacc.heading("four", text="Password", anchor=tk.W)
        self.thongtinacc.heading("five", text="Cookie", anchor=tk.W)
        self.thongtinacc.heading("six", text="STATUS", anchor=tk.W)

        self.thongtinacc['show'] = 'headings'

        context_menu = tk.Menu(self.thongtinacc, tearoff=0)
        context_menu.add_command(label="Paste", command=self.threadpaste)
        context_menu.add_command(label="Delete", command=self.delete)
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
    
    def button_setting(self):
        toplevel = tk.Toplevel(self.root)
        toplevel.title("Cài đặt nâng cao")
        toplevel.geometry('450x400')

        self.toplevel = tk.Frame(toplevel,background='white')
        self.toplevel.pack(side=tk.LEFT,fill="both", expand=True)
        self.toplevel.pack_propagate(False)
        self.toplevel.configure(width = 450, height = 400  )
        self.toplevel.place(x=0,y=0)

        def toggle_checkbutton():
            if self.DOITT.get() == 2:
                self.chk_btn1.config(state=tk.DISABLED)
            else:
                self.chk_btn1.config(state=tk.NORMAL)

            if self.DOITT.get() == 2:
                self.chk_btn2.config(state=tk.DISABLED)
            else:
                self.chk_btn2.config(state=tk.NORMAL)

            if self.DOITT.get() == 1:
                self.chk_btn3.config(state=tk.DISABLED)
            else:
                self.chk_btn3.config(state=tk.NORMAL)

            if self.DOITT.get() == 1:
                self.chk_btn4.config(state=tk.DISABLED)
            else:
                self.chk_btn4.config(state=tk.NORMAL)

        

        #-------------------------------------------------Cài đặt nâng cao-----------------------------------------------
        
        self.WIDTH = tk.StringVar()
        self.HEIGHT = tk.StringVar()
        self.CHECKCLONE = tk.StringVar()
        self.LUONG = tk.StringVar()
        self.DELAY = tk.StringVar()
        self.THAYMAIL = tk.IntVar()
        self.DOIPASS = tk.IntVar()
        self.LOGCLONEP = tk.IntVar()
        self.LOGCLONE = tk.IntVar()
        self.DOITT = tk.IntVar()
        self.DOITT.set(0)

        soacc = 0
        soacctrang = 0
        somail = 0
        somailactive = 0


        for acc in self.thongtinacc.get_children():
            print(len(self.thongtinacc.item(acc, "values")))

            if len(self.thongtinacc.item(acc, "values")) < 6:
                soacc += 1
                soacctrang += 1
            else:
                soacctrang += 1

        for acc in self.thongtinm.get_children():
            if len(self.thongtinm.item(acc, "values")) < 4:
                somail += 1
            elif len(self.thongtinm.item(acc, "values")) == 4:
                somailactive += 1
            else:pass

        
        
        self.create_ld = tk.Frame(self.toplevel,background='white',highlightbackground='black',
                    highlightthickness=1)
        self.create_ld.pack(side=tk.LEFT,fill="both", expand=True)
        self.create_ld.pack_propagate(False)
        self.create_ld.configure(width = 450, height = 400  )
        self.create_ld.place(x=0,y=17)

        frame = tk.Frame(self.toplevel, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd=0)
        frame.configure(width = 300, height = 50  )
        frame.place(x=0,y=360)

        label = tk.Label(self.create_ld, text="SIZE: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=16)

        label = tk.Label(self.create_ld, text="X ",fg='black',bg='white', font=("Airbnb Cereal", 15, "bold"))
        label.place(x=246,y=16)

        label = tk.Label(self.toplevel, text="Setting Chrome",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=0,y=0)

        label = tk.Label(self.create_ld, text="Số Clone Check: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=56)

        label = tk.Label(self.create_ld, text=f"( Đang có [{soacc}] Clone )",fg='red',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=280,y=56)

        label = tk.Label(self.create_ld, text=f"( Đang có [{soacctrang - somailactive}] Acc và [{somail}] Mail )",fg='red',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=225,y=145)

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

        rad_btn = tk.Radiobutton(self.create_ld, text="Thanh Đổi Thông Tin",bg='white', variable=self.DOITT, font=("Times New Roman", 12, "normal"), value=1,command=toggle_checkbutton)
        rad_btn.place(x=10,y=145)

        rad_btn = tk.Radiobutton(self.create_ld, text="Log Clone",bg='white', variable=self.DOITT, font=("Times New Roman", 12, "normal"), value=2,command=toggle_checkbutton)
        rad_btn.place(x=10,y=235)

        self.chk_btn1 = tk.Checkbutton(self.create_ld, text="Thay Mail",bg='white', variable=self.THAYMAIL, font=("Times New Roman", 12, "normal"))
        self.chk_btn1.place(x=50,y=175)

        self.chk_btn2 = tk.Checkbutton(self.create_ld, text="Đổi Pass",bg='white', variable=self.DOIPASS, font=("Times New Roman", 12, "normal"))
        self.chk_btn2.place(x=50,y=205)

        self.chk_btn3 = tk.Checkbutton(self.create_ld, text="Log clone(Đổi Thông Tin)",bg='white', variable=self.LOGCLONEP, font=("Times New Roman", 12, "normal"))
        self.chk_btn3.place(x=50,y=265)

        self.chk_btn4 = tk.Checkbutton(self.create_ld, text="Log clone(Cookie)",bg='white', variable=self.LOGCLONE, font=("Times New Roman", 12, "normal"))
        self.chk_btn4.place(x=50,y=295)

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
        THAYMAIL = self.THAYMAIL.get()
        DOIPASS = self.DOIPASS.get()
        LOGCLONEP = self.LOGCLONEP.get()
        LOGCLONE = self.LOGCLONE.get()
        DOITT = self.DOITT.get()
    
        if int(THAYMAIL) == 1:
            if int(THAYMAIL) > int(CHECKCLONE):
                messagebox.showerror("ERROR", "Vui lòng đổi số acc check lớn hơn số mail hoặc bằng")
            else:
                manager().setting(WIDTH,HEIGHT,CHECKCLONE,LUONG,DELAY,THAYMAIL,DOIPASS,LOGCLONEP,LOGCLONE,DOITT)
        else:
            manager().setting(WIDTH,HEIGHT,CHECKCLONE,LUONG,DELAY,THAYMAIL,DOIPASS,LOGCLONEP,LOGCLONE,DOITT)



giaodien().tab()
