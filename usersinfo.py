import requests,json

class userInfo:

    def __init__(self):
        self.listUsers = []

    def getUser(self):
        responseUser =requests.get("https://datos.gov.co/resource/jtnk-dmga.json")
        dataJson = responseUser.json()
        for ind in range(len(dataJson)):
            self.listUsers.append(dataJson[ind]["email_address"])

    def validateUser(self):
        for ind in



prueba = userInfo()
prueba.getUser()