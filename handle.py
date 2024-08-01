import requests

class handle:
    def thaymail(mail,passw):
        re = requests.get(fr'https://tools.dongvanfb.net/api/get_code?mail={mail}&pass={passw}&type=facebook')
        return re.json()['code']
    def doipass(mail,passw):
        re = requests.get(fr'https://tools.dongvanfb.net/api/get_code?mail={mail}&pass={passw}&type=facebook')
        return re.json()['code']