import requests
import tkinter as tk
import threading
import os
import requests, json, re, base64, uuid, random, os
from urllib.parse import (parse_qsl, urlsplit)
from codecs import unicode_escape_decode
from bs4 import BeautifulSoup as bs
from time import sleep
class tool:
    def __init__(self) -> None:
        self.lckie = []
        self.cookieprof = []
        self.idp = []
        self.stt = 0
        with open(f'cookiepage.txt', 'r') as f:
            for line in f.readlines():
                self.lckie.append(line.strip().split()[1])
        with open(f'cookiepage.txt', 'r') as f:
            self.ff = f.readlines()
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
        # cookie get id link
        self.get_cookies = {
            'cf_clearance': 'LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
        }

        self.get_headers = {
            'authority': 'id.traodoisub.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'cf_clearance=LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
            'origin': 'https://id.traodoisub.com',
            'pragma': 'no-cache',
            'referer': 'https://id.traodoisub.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest',
        }
    def bufflike(self,tree,link,soview,dlay):
        if len(self.lckie) >= int(soview):
        
            data = {
                    'link': f'{link}',
                }
            # lấy id bài viết
            response = requests.post('https://id.traodoisub.com/api.php', cookies=self.get_cookies, headers=self.get_headers, data=data)
            
            response_json = response.json()
            try:
                self.getid = response_json['id']
            except:
                print('Link sai hoặc bài viết chưa công khai')
            for i in range(int(soview)):
                try:
                    self.cookieprofile = {
                        'sb': self.lckie[i].split('sb=')[1].split(';')[0],
                        'datr': self.lckie[i].split('datr=')[1].split(';')[0],
                        'c_user': self.lckie[i].split('c_user=')[1].split(';')[0],
                        'xs': self.lckie[i].split('xs=')[1].split(';')[0],
                        'fr': self.lckie[i].split('fr=')[1].split(';')[0],
                        'm_page_voice': self.lckie[i].split('m_page_voice=')[1].split(';')[0],
                        'i_user': self.lckie[i].split('i_user=')[1].split(';')[0],
                    }
                    print(self.cookieprofile)
                    url = requests.get(f'https://mbasic.facebook.com/{self.getid}',headers=self.headers,cookies=self.cookieprofile).text

                    Like = '/a/like.php?'+url.split('/a/like.php?')[1].split('"')[0].replace("amp;", '')
                    re = requests.get('https://mbasic.facebook.com/'+Like, headers=self.headers, cookies=self.cookieprofile)
                    tree.insert("", "end", values=(i,self.ff[i].split()[0],self.ff[i].split()[1],self.getid,f'{i+1}/{soview}','Buff Success'))
                    delay = tree.insert("", "end", values=('','','','','','',int(dlay)))

                    for ii in range(int(dlay)):
                        tree.item(delay, values=(i+1,'','','','','',int(dlay)-ii))
                        sleep(1)
                    tree.delete(delay)
                except:
                    tree.insert("", "end", values=(i,self.ff[i].split()[0],self.ff[i].split()[1],self.getid,f'{i+1}/{soview}','Buff That Bai'))
        else:
            tk.messagebox.showinfo(title='Lỗi', message=f'Số Like Buff Phải Nhỏ Hơn Số Page Có',)
class buffcmt:
    def __init__(self) -> None:
        self.buffsuccess = 0
        self.bufferror = 0
        self.stt = 0
        self.doic = 0
        self.print_count = 0
        self.doicmt = 0
        self.cmt =[]
        self.doick = 1
        # Đọc danh sách cookie từ file
        self.lckie = []
        with open(f'acc.txt', 'r') as f:
            for line in f.readlines():
                self.lckie.append(line.strip().split()[1])
        self.ck = self.lckie[0]
        # cookie đăng nhập facbook
    
        with open(rf'cmt.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self.cmt.append(line.strip())

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
        # cookie get id link
        self.get_cookies = {
            'cf_clearance': 'LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
        }

        self.get_headers = {
            'authority': 'id.traodoisub.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'cf_clearance=LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
            'origin': 'https://id.traodoisub.com',
            'pragma': 'no-cache',
            'referer': 'https://id.traodoisub.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest',
        }
    # phần chính
    def main(self,tree,thongtin,link,socmt,dlay):
        data = {
                'link': link,
            }
        # lấy id bài viết
        response = requests.post('https://id.traodoisub.com/api.php', cookies=self.get_cookies, headers=self.get_headers, data=data)
        sleep(2)
        
        response_json = response.json()
        try:
            self.getid = response_json['id']
        except:
            print('Link sai hoặc bài viết chưa công khai')
        def cmt():

            try:
            #cmt bài viết cố định
                id = self.getid
                r = requests.get(f'https://mbasic.facebook.com/{id}', cookies=self.cookies, headers=self.headers).url

                accest = requests.get(r, cookies=self.cookies, headers=self.headers).text
                nodecmt = 'https://mbasic.facebook.com/a/comment.php?fs='+accest.split('/a/comment.php?fs=')[1].split('"')[0].replace("amp;", '')
                fb_dtsg = accest.split('name="fb_dtsg" value="')[1].split('"')[0]
                jazoest = accest.split('name="jazoest" value="')[1].split('"')[0]
                data = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'comment_text': f'{self.cmt[self.doicmt]}',
                }
                
                requests.post(nodecmt, data=data,cookies=self.cookies, headers=self.headers)
                c_user=  self.ck.split('c_user=')[1].split(';')[0]
                
                tree.insert("", "end", values=(self.stt+1,c_user,self.ck,id,self.cmt[self.doicmt],f'{i+1}/{socmt}','Buff Success'))
                
                self.buffsuccess += 1
                label1 = tk.Label(thongtin, text=f"{self.buffsuccess}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                label1.place(x=85,y=35)
                
                delay = tree.insert("", "end", values=('','','','','','',int(dlay)))

                for ii in range(int(dlay)):
                    tree.item(delay, values=(self.stt+2,'','','','','',int(dlay)-ii))
                    sleep(1)
                tree.delete(delay)
                self.doicmt += 1
    
                self.stt = self.stt + 1
                
                # ngược lại khi không chọn chức năng cmt bài viết cố định
            
                self.print_count += 1
                if self.print_count % self.doick  == 0:
                    self.doic = (self.doic + 1) % len(self.lckie)
                    self.ck = self.lckie[self.doic]
                    self.update_cookies()
            except:
                self.bufferror += 1
                tree.insert("", "end", values=(self.stt+1,c_user,self.ck,id,'',f'{i+1}/{socmt}','Buff Error'))
                label1 = tk.Label(thongtin, text=f"{self.bufferror}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                label1.place(x=285,y=35)
                self.print_count += 1
                if self.print_count % self.doick == 0:
                    self.doic = (self.doic + 1) % len(self.lckie)
                    self.ck = self.lckie[self.doic]
                    self.update_cookies()
        print(socmt)
        for i in range(int(socmt)):
            cmt()
        print('buff xong')

    def update_cookies(self):
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
class buffshare:
    def __init__(self) -> None:
        self.idpage = []
        self.tokenpage = []
        self.doic = 0
        self.stt = 0
        self.doick = 1
        self.print_count = 0
        self.buffsuccess = 0
        self.bufferror = 0
        with open('tokenpage.txt','r') as f:
            token = f.readlines()
            for i in range(len(token)):
                self.tokenpage.append(token[i])
        with open('cookiepage.txt','r') as f:
            id = f.readlines()
            for i in range(len(id)):
                self.idpage.append(id[i].split()[0])
        self.get_cookies = {
            'cf_clearance': 'LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
        }

        self.get_headers = {
            'authority': 'id.traodoisub.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'cf_clearance=LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
            'origin': 'https://id.traodoisub.com',
            'pragma': 'no-cache',
            'referer': 'https://id.traodoisub.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest',
        }
        
    def run(self,token,stt):
            response = requests.post(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{self.getid}&published=0&access_token={token}').json()
            
            try:
                stt1 = response['id']
                self.tree.insert("", "end", values=(stt,'',token,self.getid,f'{stt}/{self.soshare}',f'{stt1}'))
                # ngược lại khi không chọn chức năng cmt bài viết cố định
                self.buffsuccess += 1
                label1 = tk.Label(self.thongtin, text=f"{self.buffsuccess}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                label1.place(x=85,y=35)
            except:
                self.bufferror += 1
                self.tree.insert("", "end", values=(stt,'',token,self.getid,f'{stt}/{self.soshare}',f'BLOCK'))
                label1 = tk.Label(self.thongtin, text=f"{self.bufferror}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                label1.place(x=285,y=35)
            
            
        
        
        
    def run_threads(self,tree,thongtin,link,soshare,threadd,dlay):
        self.tree = tree
        self.thongtin =thongtin
        self.soshare = soshare
        data = {
                'link': f'{link}',
            }
        # lấy id bài viết
        response = requests.post('https://id.traodoisub.com/api.php', cookies=self.get_cookies, headers=self.get_headers, data=data)
        sleep(2)
        response_json = response.json()
        try:
            self.getid = response_json['id']
        except:
            print('Link sai hoặc bài viết chưa công khai')
        stt = 0
        while True:
            threads = []
            for i in range(0, len(self.tokenpage), int(threadd)):
                batch_urls = self.tokenpage[i:i+int(threadd)]
                for token in batch_urls:
                    stt += 1
                    thread = threading.Thread(target=self.run, args=(token,stt))
                    thread.start()
                    threads.append(thread)
                for thread in threads:
                    thread.join()
            delay = tree.insert("", "end", values=('','','','','','',int(dlay)))

            for ii in range(int(dlay)):
                tree.item(delay, values=(self.stt+2,'','','','','',int(dlay)-ii))
                sleep(1)
            tree.delete(delay)
            if stt >= int(self.soshare):
                break

shinsad = 0
class FacebookMain:

    def __init__(self,stt, proxy: str = None) -> None:
        self.buffsuccess = 0
        self.bufferror = 0
        self.stt = stt
        self.__client           = requests.Session()
        if proxy != None and ':' in proxy:
            proxies = {
                'http': '',
                'https': ''
            }
            proxy = proxy.strip().split(':')
            if len(proxy) > 2: proxynew = f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
            else: proxynew = f"http://{proxy[0]}:{proxy[1]}"
            for x in proxies:
                proxies[x] = proxynew
            self.__client.proxies = proxies
        self.__client.headers       = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'referer': 'https://www.facebook.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }
        self.__client.headers ={
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.109", "Google Chrome";v="120.0.6099.109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'viewport-width': '2814',
        }
    def addCookie(self, cookie: str = ''):
        try:
            self.__client.headers['cookie'] = cookie
            self.cookie = cookie
            return self.infoAccount()
        except Exception as e: print(e)
        return False, "Cookie die"

    def check_url(self):
        send = self.__client.get('https://www.facebook.com/')
        print(send.status_code)
        open('a.html', 'w+', encoding='utf-8').write(send.text)
        url = send.url
        if '/login' in url: return False, "Cookie die"
        elif '/checkpoint' in url: 
            type_cp = None
            for pt in url.split('/'):
                try:
                    int(pt)
                    if pt[-3:] in ['282', '956']:
                        type_cp = pt[-3:]
                except: pass
            return False, "Tài khoản bị checkpoint" + ("|"+type_cp if type_cp != None else '')
        else: 
            return True, True
    
    def check_login_is_run(self):
        try:
            check_status = self.check_url()
            if check_status[0] == True: 
                return True, ''
            else: return check_status
        except: pass    
        return False, ''
    
    def infoAccount(self):
        try:
            send = self.__client.get('https://www.facebook.com/').text
            DTSG__INIT__ = re.findall('DTSGInitialData",\[\],{"token":"(.*?)"}', send)[0]
            if DTSG__INIT__:
                self.fb_dtsg = DTSG__INIT__
                self.jazoest = re.findall('&jazoest=(.*?)"', send)[0]
                self.idFacebook = str(re.findall('"USER_ID":"(.*?)"', send)[0])
                self.lsdFacebook = re.findall('\["LSD",\[\],{"token":"(.*?)"}', send)[0]
                self.nameFacebook = unicode_escape_decode(re.findall('"NAME":"(.*?)"', send)[0])[0]
                self.__client.headers['sec-fetch-site'] = 'same-origin'
                return True, {'idFacebook': self.idFacebook, 'nameFacebook': self.nameFacebook}
        except Exception as e:
            pass
        return False, "Cookie die"

    def view_live(self,id,cookie,tree,thongtin,link: str,soview,delay,status):
        try:
            data = {    
                'd': '{"pps":{"m":true,"pf":3368,"s":"playing","sa":2757389},"ps":{"m":true,"pf":13608,"s":"playing","sa":2757389},"si":"f15a9d1e26e924","so":"tahoe::topic_live","vi":"' + link + '","tk":"8Qv0Li7gMFJ5BBFyb1m6yBHLCpEUYQ1eOTCdZrxLR1Y1myQk+aSMWGOI+1BZoJCHIcDB2DEdv0JISR+KBV034w==","ls":true}',
                '__user': self.idFacebook,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'lsd': self.lsdFacebook,
            }
            response = self.__client.post('https://www.facebook.com/video/unified_cvc/', data).text
            print(response)
            if "LIVE" in response: 
                
                with open('statusview.txt','a') as f:
                    f.write(f'{id} {cookie} success\n')
                    f.close()
                return True, 'done'

        except:pass
        return False,'die'
stt = 0
def main(id,cookie, tree,thongtin,link,soview,delay,status):
    global stt
    fb = FacebookMain(stt)
    if fb.addCookie(cookie)[0] == True:
        stt = fb.view_live(id,cookie,tree,thongtin,link,soview,delay,status)
        print(stt)
def threadviewlive(tree,thongtin,link,soview,timeview,delay):
    stt = 0
    import time
    start_time = time.time()
    with open("cookiepage.txt", 'r', encoding='utf-8') as ff:
        cookie_liness = ff.readlines()
    idacc = []
    while True:
        idpage = []
        status = open('statusview.txt','w') 
        with open("cookiepage.txt", 'r', encoding='utf-8') as f:
            cookie_lines = f.readlines()
            for i in range(int(soview)):
                cookie = cookie_lines[i].strip().split()[1]
                id =  cookie_lines[i].strip().split()[0]
                idacc.append(id)
                stt += 1
                threading.Thread(target=main, args=(id,cookie, tree,thongtin,link,soview,delay,status),).start()
        sleep(5)
        with open('statusview.txt','r') as f:
            status = f.readlines()
        success = 0
        errorr = 0
        for i in range( len(status)):
            if 'success' in status[i].split():
                success += 1
                idpage.append(status[i].split()[0])
                tree.insert("", "end", values=(i+1,status[i].split()[0],status[i].split()[1],link,f'{i+1}/{soview}',f'Buff Thành Công'))

        set_bien1 = set(idacc)
        set_bien2 = set(idpage)
        error = set_bien1 - set_bien2
        error = list(error)
    
        for j in range(len(error)):
            for k in range(len(cookie_lines)):
                if (error[j] in cookie_lines[k].split()) == True:
                    tree.insert("", "end", values=(i+j+2,error[j],cookie_lines[k].split()[1],link,f'{i+j+2}/{soview}',f'Buff Thất Bại'))
                    errorr += 1
        label1 = tk.Label(thongtin, text=f"{success}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=85,y=35)
        label1 = tk.Label(thongtin, text=f"{errorr}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=285,y=35)
        elapsed_time = time.time() - start_time
        if elapsed_time >= int(timeview) * 60:
            msg_box = tk.messagebox.showinfo(
                "Thông Báo",
                f"Đã buff xong {soview} view thời gian {timeview} phút",
            )
            break
        
        delay1 = tree.insert("", "end", values=('','','','','','',int(delay)))

        for ii in range(int(delay)):
            tree.item(delay1, values=(i+j+3,'','','','','',int(delay)-ii))
            sleep(1)
        tree.delete(delay1)
        for item_id in tree.get_children():
            tree.delete(item_id)


