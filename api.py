from selenium import webdriver
from time import sleep
import json
import threading
from functools import partial
from tkinter import messagebox


class facebook:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

        # URL của trang web bạn muốn truy cập
        self.url = fr"https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F"
        with open('Advanced_settings.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.width = config_data["width"]
            self.height = config_data["height"]
            self.delay = config_data["delay"]
            self.thaymaill = config_data["thaymail"]
            self.doipass = config_data["doipass"]
            self.logclonep = config_data["logclonep"]
            self.logclone = config_data["logclone"]
            self.doitt = config_data["doitt"]

    def close(self):
        self.driver.close()

    def contineu(self):
        try:
            self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div').click()
            sleep(5)
            self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div').click()
            sleep(5)
            self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div').click()
            sleep(5)
            try:
                self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div').click()
                sleep(1)
                self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div').click()
                sleep(1)
                self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div').click()
                sleep(1)
            except:pass
            cookies = self.driver.get_cookies()
            self.ck = ''
            for cookie in cookies:
                self.ck += f'{cookie['name']}={cookie['value']};'
            print(self.ck)
            try:
                with open('acclive.txt','a') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{self.ck}\n')
                    f.close()
            except:
                with open('acclive.txt','w') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{self.ck}\n')
                    f.close()
        except:
            cookies = self.driver.get_cookies()
            self.ck = ''
            for cookie in cookies:
                self.ck += f'{cookie['name']}={cookie['value']};'
            print(self.ck)
            try:
                with open('acclive.txt','a') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{self.ck}\n')
                    f.close()
            except:
                with open('acclive.txt','w') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{self.ck}\n')
                    f.close()

    def matkhau(self,tree,i,treemail,mail):
        self.item_id_cookie = tree.get_children()
        self.values_cookie = tree.item(self.item_id_cookie[i], "values")

        self.item_id_mail = treemail.get_children()

        self.values_mail = treemail.item(self.item_id_mail[mail], "values")
        if (self.doipass == 1 or self.logclonep == 1 ) and (self.thaymaill == 0 or self.logclonep == 1):
        # if self.doipass == 1 or self.logclonep == 1:
            

            cookies = self.values_cookie[4].split(';')

            # Xóa các khoảng trắng đầu và cuối
            cookies = [cookie.strip() for cookie in cookies]

            # Tách từng cặp key-value thành dict
            cookie_dict = {}
            for cookie in cookies:
                if '=' in cookie:
                    key, value = cookie.split('=', 1)
                    cookie_dict[key] = value
            cookies_list = [{'name': key, 'value': value} for key, value in cookie_dict.items()]
            for cookie in cookies_list:
                self.driver.add_cookie(cookie)
    
        # print(cookies_list)

        
        sleep(5)

        self.driver.get('https://accountscenter.facebook.com/password_and_security')
            
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/main/div/div/div[2]/div[1]/div[2]/div/div/div[1]/a/div[1]').click()
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div/div/div[2]/div/div/div[1]').click()
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[5]/div[2]/div[1]/div/div/div[6]/a/span').click()
        sleep(5)
        messagebox.showinfo("Thông báo", "bỏ qua allow")
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/div/div[2]/div/div[2]/div[1]/div').click()
        sleep(5)
        code = self.getcode()
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div/label/input').send_keys(code)
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div').click()
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[3]/div/div[1]/div/div/div/div/label/input').send_keys('lan123@@@')
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/div/div[2]/div[1]/div').click()
        # pass moi
        sleep(5)
        tree.item(self.item_id_cookie[i], values=(i, f'{self.values_cookie[1]}',f'{self.values_mail[1]}', f'lan123@@@', f'','Pass Success'))
        
        clonenew = ''
        with open('code.txt','r') as f:
            f = f.readlines()
        
        for j in range(len(f)):
            if f[j].split('|')[0] == self.values_cookie[1]:
                try:
                    clonenew += f'{self.values_cookie[1]}|{self.values_mail[1]}|lan123@@@|Pass Success\n'
                except:
                    clonenew += f'{self.values_cookie[1]}|{self.values_mail[1]}|lan123@@@|Pass Success\n'

            else:
                clonenew += f'{f[j]}'
        with open('code.txt','w') as f:
            f.write(clonenew)
            f.close()
    def thaymail(self,tree,i,treemail,mail):
        self.item_id_cookie = tree.get_children()
        self.values_cookie = tree.item(self.item_id_cookie[i], "values")

        self.item_id_mail = treemail.get_children()

        self.values_mail = treemail.item(self.item_id_mail[mail], "values")

        if self.thaymaill == 1 or self.logclonep == 1:

            cookies = self.values_cookie[4].split(';')

            # Xóa các khoảng trắng đầu và cuối
            cookies = [cookie.strip() for cookie in cookies]

            # Tách từng cặp key-value thành dict
            cookie_dict = {}
            for cookie in cookies:
                if '=' in cookie:
                    key, value = cookie.split('=', 1)
                    cookie_dict[key] = value
            cookies_list = [{'name': key, 'value': value} for key, value in cookie_dict.items()]
            for cookie in cookies_list:
                self.driver.add_cookie(cookie)
        print(cookies_list)

        
        sleep(5)
        self.driver.get('https://accountscenter.facebook.com/personal_info')
        
        sleep(10)
        treemail.item(self.item_id_mail[mail], values=(mail, f'{self.values_mail[1]}', f'{self.values_mail[2]}', f'Checkinggg'))
        tree.item(self.item_id_cookie[i], values=(i, f'{self.values_cookie[1]}', f'{self.values_mail[1]}', f'{self.values_cookie[3]}', f'{self.values_cookie[4]}','Thay Mail'))
        try:
            self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/main/div/div/div[3]/div/div[1]/div/div/div[1]/a/div[1]').click()
        except:
            tree.item(self.item_id_cookie[i], values=(i, f'{self.values_cookie[1]}', f'{self.values_mail[1]}', f'{self.values_cookie[3]}', f'{self.values_cookie[4]}','Thay Mail Error'))
            self.driver.close()
        sleep(5)

        try:
            self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[3]/div[1]').click()
        except:
            self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/div[1]').click()
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]').click()
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(f'{self.values_mail[1]}')
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div[3]/div/div[2]/div/div/div/div/label/div[1]').click()
        sleep(5)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[6]/div[3]/div/div/div/div/div/div/div/div').click()
        sleep(5)
        try:
            text = self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/span').text
            print(text)
            if text == 'Ten adres e-mail jest już w użyciu: Podany adres e-mail jest już używany przez inne konto na Facebooku.':
                tree.item(self.item_id_cookie[i], values=(i, f'{self.values_cookie[1]}', f'{self.values_mail[1]}', f'{self.values_mail[1]}', f'{self.values_cookie[3]}', f'{self.values_cookie[4]}','Mail Error'))
                treemail.item(self.item_id_mail[mail], values=(mail, f'{self.values_mail[1]}', f'{self.values_mail[1]}', f'{self.values_mail[2]}',  f'Mail Lặp'))
        except:
            
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
            code = self.getcode()
            # code = handle.thaymail(f'{self.values_mail[1]}',f'{self.values_mail[2]}')
            if code == '':
                status = 'Active ERROR'
            else:
                status = 'Success Acctive Mail'
            self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[5]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/input').send_keys(code)
            sleep(5)
            
            self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[6]/div[3]/div/div/div/div/div/div/div/div').click()
            sleep(4)
            try:

                tree.item(self.item_id_cookie[i], values=(i, f'{self.values_cookie[1]}', f'{self.values_mail[1]}', f'{self.values_cookie[3]}', f'{self.ck}','Success Active Mail'))
            except:
                tree.item(self.item_id_cookie[i], values=(i, f'{self.values_cookie[1]}', f'{self.values_mail[1]}', f'{self.values_cookie[3]}', f'{self.values_cookie[4]}','Success Active Mail'))
            treemail.item(self.item_id_mail[mail], values=(mail, f'{self.values_mail[1]}',  f'{self.values_mail[2]}',  f'Active'))
            clonenew = ''
            with open('code.txt','r') as f:
                f = f.readlines()
            
            for j in range(len(f)):
                if f[j].split('|')[0] == self.values_cookie[1]:
                    try:
                        clonenew += f'{self.values_cookie[1]}|{self.values_mail[1]}|{self.values_cookie[3].split('\n')[0]}|{self.ck}|{status}\n'
                    except:
                        clonenew += f'{self.values_cookie[1]}|{self.values_mail[1]}|{self.values_cookie[3].split('\n')[0]}|{self.values_cookie[4]}|{status}\n'

                else:
                    clonenew += f'{f[j]}'
            with open('code.txt','w') as f:
                f.write(clonenew)
                f.close()

            clonenew = ''
            with open('mail.txt','r') as f:
                f = f.readlines()
            
            for j in range(len(f)):
                if f[j].split('|')[0] == self.values_mail[1]:
                    clonenew += f'{self.values_mail[1]}|{self.values_mail[2].split('\n')[0]}|Active\n'
                    

                else:
                    clonenew += f'{f[j]}'
            with open('mail.txt','w') as f:
                f.write(clonenew)
                f.close()
        print('đã đổi xong')
            
        

    def getcode(self):

        # self.driver.get("https://www.facebook.com/")
        sleep(2)
        if len(self.driver.window_handles) == 1:
            self.driver.execute_script("window.open('');")
            # Chuyển sang tab mới mở (tab cuối cùng)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get("https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=1&msaredir=1&client-request-id=14e919c9-31e4-4f14-7bf7-3c8caa547c53&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&nonce=638574000277108412.3457696c-6582-4e2d-9037-d373e3cf8289&state=Dcu7DoIwFIDhou_iVjmcXk47EAeNYcAFTTRs9GIikWCAYHx7O3z_9meMsW2ySTJIYaSFUSQBAIkKMLLAvZCKtNWea2WQy4iBWxDEgyARhX8aNDZL7ykfv11-mJduiWWxm2J4TdEvt7HsqgZ8ddH1z67h0cwO7VQPdmiHd99eVe8QVnc_f9zR_AE")
            self.driver.set_window_size(400,900)

            sleep(5)
            self.driver.find_element("xpath",' /html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(f'{self.values_mail[1]}')
            sleep(5)
            self.driver.find_element("xpath",' /html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input').click()
            sleep(5)
            self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/input').send_keys(f'{self.values_mail[2]}')
            sleep(5)
            # self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div/button').click()
            # sleep(5)
            #click vo mail
            # sleep(5)
            # self.driver.find_element("xpath",' /html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/button').click()
            # input('')
            self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[1]/button').click()
            sleep(5)
        else:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        
        messagebox.showinfo("Thông báo", "Nhấn Banner")
        sleep(2)
        self.driver.find_element("xpath",' /html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]').click()
        code = ''
        while True:
             
            try:
                code1 = self.driver.find_element("xpath",' /html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[3]/div[1]/div/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[8]/td/span/center').text
                code += code1
            except:
                try:
                    code1 = self.driver.find_element("xpath",' /html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[3]/div[1]/div/div/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/span/span/table[1]/tbody/tr/td/span/span').text
                    code += code1
                except:pass
            if len(code) > 1:
                # self.driver.close()
                self.driver.back()
                sleep(2)
        # Chuyển về tab trước đó (tab đầu tiên)
                self.driver.switch_to.window(self.driver.window_handles[0])

                # input('')
                break
        return code

    def checkdie(self,tree,i):
        try:
            new_url = self.driver.current_url
            
            if new_url == r'https://www.facebook.com/checkpoint/828281030927956/?next=https%3A%2F%2Fwww.facebook.com%2F':
                tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'','Checkpoint 956'))

            check = self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/h2/span').text
            
            if check == 'Zaloguj się na innym urządzeniu, aby kontynuować':
            #   
                check = 'Checkpoint_681'
                tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'','Checkpoint 681'))
        # except:
        #     tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}','Live'))

        # try:
        #     check = self.driver.find_element("xpath",'/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div[1]/div[2]').text
        #     return check #Nieprawidłowa nazwa użytkownika lub hasło
        except:
            try:
                check = self.driver.find_element("xpath",'/html/body/div[1]/div[1]/div[1]/div/div/form/div/div[1]').text 
                #
                check = 'Sai Pass'
                tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'',check))
            except:
                try:
                    check = self.driver.find_element("xpath",'/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div[1]/div[2]').text
                    tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'',check))
                except:
                    try:
                        check = self.driver.find_element("xpath",'/html/body/div[1]/div[1]/div[1]/div/div/form/div/div[1]/div/div[2]/h2').text
                        check = 'Sai PASS'
                        tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'',check))
                    except:
                        try:
                            check = self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/h2/span').text
                            check = '2FA'
                            tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'',check))
                        except:
                            try:
                                check = self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div[3]/span').text
                                check = '282'
                                tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'',check))
                            except:
                                tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'','Acc Live'))
                                messagebox.showinfo("Thông báo", "Hãy Ấn all cookie và nhấn oke để lấy cookie")
                                self.contineu()
                            
        self.ck = ''
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            self.ck += f'{cookie['name']}={cookie['value']};'
        print(self.ck)
        clonenew = ''
        with open('code.txt','r') as f:
            f = f.readlines()
        
        for j in range(len(f)):
            if f[j].split('|')[0] == self.values[1]:
                try:
                    clonenew += f'{self.values[1]}|{self.values[3].split('\n')[0]}|{check}\n'
                except:
                    clonenew += f'{self.values[1]}|{self.values[3].split('\n')[0]}|{self.ck}|live\n'
                    tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', self.ck,'Acc Live'))
            else:
                clonenew += f'{f[j]}'
        with open('code.txt','w',encoding='utf-8') as f:
            f.write(clonenew)
            f.close()
    
    def run(self,tree,i,j,treemail,mail):
        self.driver.get(self.url)
        # self.getcode()
        sleep(2)

        self.driver.set_window_size(int(self.width),int(self.height))
        print(i)
        stt = 1
        if j > 5:
            self.driver.set_window_position(int(self.width)*stt,900)
            stt += 1
        else:
            self.driver.set_window_position(int(self.width)*j,0)
        sleep(2)
        try:
            self.driver.find_element("xpath",' /html/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div').click()
        except:pass
        sleep(5)
        if self.doitt == 2:
            
            self.item_id = tree.get_children()
            self.values = tree.item(self.item_id[i], "values")
            tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'','Đang mở Chrome'))
            
            self.driver.find_element("xpath",' /html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/input').send_keys(self.values[1])
            tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'','Đang Nhập ID'))
            sleep(1)
            self.driver.find_element("xpath",' /html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[2]/div/div/input').send_keys(self.values[3].split('\n')[0])
            tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'','Đang Nhập Pass'))
            sleep(1)
            self.driver.find_element("xpath",' /html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[3]/button').click()
            tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}', f'{self.values[3]}', f'','Đang Click Đăng Nhập'))
            sleep(5)
            

            self.checkdie(tree,i)
        

        if self.thaymaill == 1 or self.logclonep == 1:
            self.thaymail(tree,i,treemail,mail)
        print('đã đổi xong')
        if self.doipass == 1 or self.logclonep == 1:
            print('đổi mk')
            self.matkhau(tree,i,treemail,mail)
def thread(tree,treemail):
    with open('Advanced_settings.json', 'r') as configfile:
        config_data = json.load(configfile)
        soclone = config_data["soclone"]
        luong = config_data["luong"]
        delay = config_data["delay"]
        thaymaill = config_data["thaymail"]
        doipass = config_data["doipass"]
        logclonep = config_data["logclonep"]
        logclone = config_data["logclone"]
        doitt = config_data["doitt"]
    soreg = 0
    mail = 0
    item_id = tree.get_children()
    item_id_mail = treemail.get_children()
    print(item_id_mail)
    for i in range(0, int(soclone), int(luong)):
        for j in range(int(luong)):
            if doitt == 2:
                while True:
                    values = tree.item(item_id[soreg], "values")
                    print(values)
                    if values[2] == '' and values[4] == '':
                        break
                    else:
                        soreg += 1
            else:
                if  thaymaill == 1:
                    while True:
                        values = tree.item(item_id[soreg], "values")
                        
                        if values[2] == '':
                            break
                        else:
                            soreg += 1
            while True:
                values_mail = treemail.item(item_id_mail[mail], "values")
                if ((values_mail[3].split('\n')[0] == 'Checking') or (values_mail[3].split('\n')[0] == 'Active')) == False:
                    treemail.item(item_id_mail[mail], values=(mail, f'{values_mail[1]}', f'{values_mail[2]}', f'Checking'))
                    break
                else:
                    mail += 1

            threads = []
            if i + j < int(soclone):
                thread =threading.Thread(target=partial(facebook().run, tree,soreg,j,treemail,mail,))
                threads.append(thread)
                soreg += 1
                thread.start()
        
        # Chờ tất cả các luồng trong batch này hoàn thành
        for thread in threads:
            thread.join()
        sleep(int(delay))
# print(handle.thaymail('dishayzakhar1@hotmail.com','b1sAEAx5huACQ'))
