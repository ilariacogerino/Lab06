import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDAnno(self):
        self._view._ddAnno.options.append(ft.dropdown.Option("Nessun filtro"))
        anni = self._model.getAnni()
        for anno in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(anno))
        self._view._page.update()

    def fillDDBrand(self):
        self._view._ddBrand.options.append(ft.dropdown.Option("Nessun filtro"))
        brands = self._model.getBrand()
        for brand in brands:
            self._view._ddBrand.options.append(ft.dropdown.Option(brand))
        self._view._page.update()

    def fillDDRetailer(self):
        self._view._ddRetailer.options.append(ft.dropdown.Option("Nessun filtro"))
        retailers = self._model.getRetailer()
        for retailer in retailers:
            self._view._ddRetailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code,
                                                                     text=retailer.Retailer_name,
                                                                     on_click = self.read_retailer))

    def read_retailer(self, e):
        self._ddRetailerValue = e.control.data

    def handleTopVendite(self, e):
        self._view._lv.controls.clear()
        annoStr = self._view._ddAnno.value #E' UNA STRINGA
        if annoStr != "Nessun filtro":
            anno = int(annoStr)
        else:
            anno = annoStr
        brand = self._view._ddBrand.value
        retailerStr = self._view._ddRetailer.value
        if retailerStr != "Nessun filtro":
            retailer = int(retailerStr)
        else:
            retailer = retailerStr
        vendite = []

        if (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            vendite = self._model.getVendite()

        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno and vendita.Product_brand == brand and vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Product_brand == brand and vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Product_brand == brand):
                    vendite.append(vendita)

        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno and vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno):
                    vendite.append(vendita)

        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno and vendita.Product_brand == brand):
                    vendite.append(vendita)

        if len(vendite) == 0:
            self._view._lv.controls.append(ft.Text(f"Non ci sono vendite con questi filtri!"))
        elif len(vendite)>5:
            for i in range (0,5):
                self._view._lv.controls.append(ft.Text(vendite[i]))
        else:
            for vendita in vendite:
                self._view._lv.controls.append(ft.Text(vendita))
        self._view._page.update()


    def handleAnalizzaVendite(self, e):
        self._view._lv.controls.clear()
        annoStr = self._view._ddAnno.value  # E' UNA STRINGA
        if annoStr != "Nessun filtro":
            anno = int(annoStr)
        else:
            anno = annoStr
        brand = self._view._ddBrand.value
        retailerStr = self._view._ddRetailer.value
        if retailerStr != "Nessun filtro":
            retailer = int(retailerStr)
        else:
            retailer = retailerStr
        print(anno, brand, retailer)
        self._view._lv.controls.append(ft.Text(f"Statistiche vendite: "))
        vendite = []
        ricaviTot = 0
        countVendite = 0
        RetailerCoinvolti = []
        ProductCoinvolti = []

        if (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            vendite = self._model.getVendite()

        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno and vendita.Product_brand == brand and vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Product_brand == brand and vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Product_brand == brand):
                    vendite.append(vendita)

        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno and vendita.Retailer_code == retailer):
                    vendite.append(vendita)

        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno):
                    vendite.append(vendita)

        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            topVendite = self._model.getVendite()
            for vendita in topVendite:
                if (vendita.Date.year == anno and vendita.Product_brand == brand):
                    vendite.append(vendita)

        for vendita in vendite:
            ricaviTot += vendita.Ricavo
            countVendite += 1
            if vendita.Retailer_code not in RetailerCoinvolti:
                RetailerCoinvolti.append(vendita.Retailer_code)
            if vendita.Product_number not in ProductCoinvolti:
                ProductCoinvolti.append(vendita.Product_number)

        self._view._lv.controls.append(ft.Text(f"Giro d'affari: {ricaviTot}"))
        self._view._lv.controls.append(ft.Text(f"Numero vendite: {countVendite}"))
        self._view._lv.controls.append(ft.Text(f"Numero retailers coinvolti: {len(RetailerCoinvolti)}"))
        self._view._lv.controls.append(ft.Text(f"Numero prodotti coinvolti: {len(ProductCoinvolti)}"))

        self._view._page.update()


