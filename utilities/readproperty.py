import configparser
import os

file_location = "C:\\Users\\sulta\\PycharmProjects\\OpenCart_V1\\configurations\\config.ini"
config = configparser.RawConfigParser()
config.read(file_location)

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username=(config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password=(config.get('commonInfo', 'password'))
        return password


# Testing above methods - optional Code
print(ReadConfig.getApplicationURL())
print(ReadConfig.getUseremail())

