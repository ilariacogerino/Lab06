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
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._view._ddRetailer.value
        topVendite = self._model.getTopVendite(anno, brand, retailer)
        #print(anno, brand, retailer)
        #print(topVendite)
        for vendita in topVendite:
            self._view._lv.controls.append(ft.Text(vendita))
        self._view._page.update()


    def handleAnalizzaVendite(self, e):
        self._view._lv.controls.clear()
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._view._ddRetailer.value
        self._view._lv.controls.append(ft.Text(f"Statistiche vendite: "))
        dati = self._model.getAnalisiVendite(anno, brand, retailer)
        self._view._lv.controls.append(ft.Text(f"Giro d'affari: {dati[0]} "))
        self._view._lv.controls.append(ft.Text(f"Numero vendite: {dati[1]} "))
        self._view._lv.controls.append(ft.Text(f"Numero retailers coinvolti: {dati[2]} "))
        self._view._lv.controls.append(ft.Text(f"Numero prodotti coinvolti: {dati[3]} "))

        self._view._page.update()

