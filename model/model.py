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

    def getTopVendite(self, anno, brand, retailer):
        return self.dao.getRicavi(anno, brand, retailer)

    def getAnalisiVendite(self, anno, brand, retailer):
        return self.dao.AnalisiVendite(anno, brand, retailer)

if __name__ == "__main__":
    m = Model()
    print(m.getTopVendite(2017, "Star", "Connor Department Store"))