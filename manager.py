import tkinter as tk
import json

class manager:
    def account(self,ck,tree,acc):
        for i in range(len(ck)):
            tk , mk = ck[i].split('|')
            tree.insert("", "end", values=(acc+i, tk,mk,))
        
    def setting(self,width,height,soclone,luong,delay):
        config_data = {
            'width': width,
            'height': height,
            'soclone': soclone,
            'luong': luong,
            'delay': delay,
        }

        with open('Advanced_settings.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)