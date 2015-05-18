__author__ = 'MaxTechTV'

import requests

class ytstats:


    html_string = ""

    def __init__(self,userID):

        url = "http://youtube.de/user/"+userID+"/about"
        html = requests.get(url)
        self.html_string = html.text

    def getSubscribers(self):

        abo = self.html_string.find("Abonnenten")
        raw = self.html_string[(abo-10):abo]
        abonnenten = ""
        for x in raw:
           if(x.isdigit()):
               abonnenten += x
        return int(abonnenten)

    def getViews(self):

        abo =   self.html_string.find("Aufrufe")
        raw = self.html_string[(abo-15):abo]
        aufrufe = ""
        for x in raw:
           if(x.isdigit()):
               aufrufe += x
        return int(aufrufe)
