from database.DAO import DAO

class Model:
    def __init__(self):
        self.dao = DAO()

    def getAnni(self):
        return self.dao.getAnni()

    def getBrand(self):
        return self.dao.getBrand()

    def getRetailer(self):
        return self.dao.getRetailer()

    def getVendite(self):
        return self.dao.getVendite()

    def getAnalisiVendite(self):
        return self.dao.AnalisiVendite()

