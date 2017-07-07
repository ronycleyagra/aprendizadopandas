import pymssql

class DBConnection(object):

    def __init__(self,driver, host, database, user, password):
        self.__driver = driver
        self.__host = host
        self.__database = database
        self.__user = user
        self.__password = password
        self.__con = ""

    def getconnection(self) -> pymssql.Connection:
        self.con = pymssql.connect(host=self.driver, database=self.database, user=self.user, password=self.password)
        return self.con

    def closeconnection(self):
        self.con.close


    def tostring(self) -> str:
        return "driver: "+self.__driver+", host: "+self.__host+", database: "+self.__database+", user: "+self.__user+", password: "+self.__password