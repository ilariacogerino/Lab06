import flet as ft
from flet.core.types import MainAxisAlignment


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self._ddAnno = None
        self._ddBrand = None
        self._ddRetailer = None

        self._btnTopVendite = None
        self._btnAnalizzaVendite = None

        self._lv = None


    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddAnno = ft.Dropdown(label = "anno")
        self._controller.fillDDAnno()

        self._ddBrand = ft.Dropdown(label = "brand")
        self._controller.fillDDBrand()

        self._ddRetailer = ft.Dropdown(label = "retailer")
        self._controller.fillDDRetailer()

        row1 = ft.Row(controls=[self._ddAnno, self._ddBrand, self._ddRetailer], alignment=MainAxisAlignment.CENTER)

        self._btnTopVendite = ft.ElevatedButton(text = "Top vendite", on_click = self._controller.handleTopVendite)
        self._btnAnalizzaVendite = ft.ElevatedButton(text = "Analizza vendite", on_click = self._controller.handleAnalizzaVendite)

        row2 = ft.Row(controls = [self._btnTopVendite, self._btnAnalizzaVendite], alignment=MainAxisAlignment.CENTER)

        self._lv = ft.ListView(expand = 1)

        self._page.add(row1, row2, self._lv)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
