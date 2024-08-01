import json

class manager:
    def account(self,ck,tree,acc):
        for i in range(len(ck)):
            tk , mk = ck[i].split('|')
            tree.insert("", "end", values=(acc+i, tk,mk,))

    def mail(self,mail,tree,somail):
        for i in range(len(mail)):
            tk , mk = mail[i].split('|')
            tree.insert("", "end", values=(somail+i, tk,mk,))
        
    def setting(self,width,height,soclone,luong,delay,thaymail,doipass,logclonep,logclone,doitt):
        config_data = {
            'width': width,
            'height': height,
            'soclone': soclone,
            'luong': luong,
            'delay': delay,
            'thaymail': thaymail,
            'doipass': doipass,
            'logclonep': logclonep,
            'logclone': logclone,
            'doitt': doitt,
        }

        with open('Advanced_settings.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
