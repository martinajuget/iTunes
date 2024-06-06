import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.txt_soglia = None
        self.btn_percorso = None
        self.ddAlbum1 = None
        self.btn_adiacenze = None
        self.ddAlbum2 = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_n = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 29-6-22", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW with some controls
        # text field for the name
        self.txt_n = ft.TextField(
            label="Canzoni (n)",
            width=200,
            hint_text="Insert n"
        )

        # button for the "hello" reply
        self.btn_creaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_creaGrafo)
        row1 = ft.Row([self.txt_n, self.btn_creaGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.ddAlbum1= ft.Dropdown(label="Album 1")
        self.btn_adiacenze = ft.ElevatedButton(text="Stampa adiacenze", on_click=self._controller.handle_stampaAdiacenze)
        row2 = ft.Row([self.ddAlbum1, self.btn_adiacenze],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.ddAlbum2 = ft.Dropdown(label="Album 2")
        self.btn_percorso = ft.ElevatedButton(text="Calcola percorso",
                                               on_click=self._controller.handle_percorso)

        row3 = ft.Row([self.ddAlbum2, self.btn_percorso],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self.txt_soglia = ft.TextField(
            label="Soglia x",
            width=200,
            hint_text="Insert x"
        )
        row4 = ft.Row([self.txt_soglia],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
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
