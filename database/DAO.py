from database.DB_connect import DBConnect
from model.sales import Sales


class DAO():

    def getAnni(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """select year(Date) from go_daily_sales"""
        cursor.execute(query)

        date = []
        for row in cursor:
            if row[0] not in date:
                date.append(row[0])
        cursor.close()
        cnx.close()
        return date

    def getBrand(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """select Product_brand from go_products"""
        cursor.execute(query)

        brand = []
        for row in cursor:
            if row[0] not in brand:
                brand.append(row[0])
        cursor.close()
        cnx.close()
        return brand

    def getRetailer(self):
        from model.retailer import Retailer
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from go_retailers"""
        cursor.execute(query)
        retailers = []
        for row in cursor:
            retailers.append(Retailer(**row))
        cursor.close()
        cnx.close()
        return retailers

    def getRicavi(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select Date, Unit_sale_price * Quantity as Ricavo, gds.Retailer_code, gds.Product_number  
                    from go_daily_sales gds, go_products gp, go_retailers gr 
                    where gds.Retailer_code = gr.Retailer_code and gds.Product_number = gp.Product_number
                         and year(Date)= %s and gp.Product_brand =  %s and gr.Retailer_code = %s
                    order by -ricavo"""
        cursor.execute(query, (anno, brand, retailer))
        ricavi = []
        for row in cursor:
            ricavi.append(Sales(row["Date"], row["Ricavo"], row["Retailer_code"], row["Product_number"]))
        cursor.close()
        cnx.close()
        return ricavi

    def AnalisiVendite(self, anno, brand, retailer):
        vendite = self.getRicavi(anno, brand, retailer)
        ricaviTot = 0
        countVendite = 0
        RetailerCoinvolti = []
        ProductCoinvolti = []
        for vendita in vendite:
            ricaviTot += vendita.Ricavo
            countVendite += 1
            if vendita.Retailer_code not in RetailerCoinvolti:
                RetailerCoinvolti.append(vendita.Retailer_code)
            if vendita.Product_number not in ProductCoinvolti:
                ProductCoinvolti.append(vendita.Product_number)
        return ricaviTot, countVendite, len(RetailerCoinvolti), len(ProductCoinvolti)



        pass

if __name__ == '__main__':
    dao = DAO()
    print(dao.getRicavi(2017, "Star", "1216"))

