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

    def close(self):
        self.driver.close()

    def contineu(self):
        try:
            self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div').click()
            sleep(5)
            self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div').click()
            sleep(5)
            self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div').click()
            sleep(5)
            try:
                self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div').click()
                sleep(1)
                self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div').click()
                sleep(1)
                self.driver.find_element("xpath",' /html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div').click()
                sleep(1)
            except:pass
            cookies = self.driver.get_cookies()
            ck = ''
            for cookie in cookies:
                ck += f'{cookie['name']}={cookie['value']};'
            print(ck)
            try:
                with open('acclive.txt','a') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{ck}\n')
                    f.close()
            except:
                with open('acclive.txt','w') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{ck}\n')
                    f.close()
        except:
            cookies = self.driver.get_cookies()
            ck = ''
            for cookie in cookies:
                ck += f'{cookie['name']}={cookie['value']};'
            print(ck)
            try:
                with open('acclive.txt','a') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{ck}\n')
                    f.close()
            except:
                with open('acclive.txt','w') as f:
                    f.write(f'{self.values[1]}|{self.values[2]}|{ck}\n')
                    f.close()


    def checkdie(self,tree,i):
        try:
            check = self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/h2/span').text
            if check == 'Zaloguj się na innym urządzeniu, aby kontynuować':
            #   
                check = 'Checkpoint_681'
                tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}','Checkpoint 681'))
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
                tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}',check))
            except:
                try:
                    check = self.driver.find_element("xpath",'/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div[1]/div[2]').text
                    tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}',check))
                except:
                    try:
                        check = self.driver.find_element("xpath",'/html/body/div[1]/div[1]/div[1]/div/div/form/div/div[1]/div/div[2]/h2').text
                        check = 'Sai PASS'
                        tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}',check))
                    except:
                        try:
                            check = self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/h2/span').text
                            check = '2FA'
                            tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}',check))
                        except:
                            tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}','Acc Live'))
                            messagebox.showinfo("Thông báo", "Hãy Ấn all cookie và nhấn oke để lấy cookie")
                            self.contineu()
                         
        clonenew = ''
        with open('code.txt','r') as f:
            f = f.readlines()
        
        for j in range(len(f)):
            if f[j].split('|')[0] == self.values[1]:
                try:
                    clonenew += f'{f[j].split('\n')[0]}|{check}\n'
                except:
                    clonenew += f'{f[j].split('\n')[0]}|live\n'
            else:
                clonenew += f'{f[j]}'
        with open('code.txt','w') as f:
            f.write(clonenew)
            f.close()
    def run(self,tree,i,j):
        self.item_id = tree.get_children()
        self.values = tree.item(self.item_id[i], "values")
        tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}','Đang mở Chrome'))
        self.driver.get(self.url)
        self.driver.set_window_size(int(self.width),int(self.height))
        print(i)
        stt = 1
        if j > 5:
            self.driver.set_window_position(int(self.width)*stt,500)
            stt += 1
        else:
            self.driver.set_window_position(int(self.width)*j,0)
        sleep(2)
        try:
            self.driver.find_element("xpath",' /html/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div').click()
        except:pass
        sleep(5)
        self.driver.find_element("xpath",' /html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/input').send_keys(self.values[1])
        tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}','Đang Nhập ID'))
        sleep(1)
        self.driver.find_element("xpath",' /html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[2]/div/div/input').send_keys(self.values[2].split('\n')[0])
        tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}','Đang Nhập Pass'))
        sleep(1)
        self.driver.find_element("xpath",' /html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[3]/button').click()
        tree.item(self.item_id[i], values=(i, f'{self.values[1]}', f'{self.values[2]}','Đang Click Đăng Nhập'))
        sleep(5)
        
        print(self.checkdie(tree,i))
def thread(tree):
    with open('Advanced_settings.json', 'r') as configfile:
        config_data = json.load(configfile)
        soclone = config_data["soclone"]
        luong = config_data["luong"]
        delay = config_data["delay"]
    soreg = 0
    item_id = tree.get_children()
    for i in range(0, int(soclone), int(luong)):
        for j in range(int(luong)):
            while True:
                values = tree.item(item_id[soreg], "values")
                if len(values) == 3:
                    break
                else:
                    soreg += 1

            threads = []
            if i + j < int(soclone):
                thread =threading.Thread(target=partial(facebook().run, tree,soreg,j))
                threads.append(thread)
                soreg += 1
                thread.start()
        
        # Chờ tất cả các luồng trong batch này hoàn thành
        for thread in threads:
            thread.join()
        sleep(int(delay))