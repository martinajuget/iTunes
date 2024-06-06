import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def handle_creaGrafo(self,e):
        try:
            intN=int(self._view.txt_n.value)
        except ValueError:
            self._view.create_alert("Inserire numero canzoni")
            return
        self._model.creaGrafo(intN)
        self._view.txt_result.controls.clear()
        numNodi=self._model.getNumNodes()
        numArchi=self._model.getNumEdges()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente."))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi:{numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi:{numArchi}"))
        self.fillAlbum1()
        self._view.update_page()

    def fillAlbum1(self):
        album=list(self._model.grafo.nodes)
        album.sort(key=lambda x:x.Title)
        for a in album:
            self._view.ddAlbum1.options.append(ft.dropdown.Option(data=a,
                                                                  key=a.AlbumId,
                                                                  text=a.Title,
                                                                  on_click=self.leggiAlbum))
        self._view.update_page()
    def handle_stampaAdiacenze(self,e):
        if self._view.ddAlbum1.value is None:
            self._view.create_alert("Seleziona un album1")
            return
        nodi=self._model.getSuccessori(int(self._view.ddAlbum1.value))
        self._view.txt_result.controls.append(ft.Text(f"Numero successori:{len(nodi)}"))
        for n in nodi:
            self._view.txt_result.controls.append(ft.Text(f"{n}"))
        self._view.update_page()

    def leggiAlbum(self,e):
        if e.control.data is None:
            self.Album=None
        else:
            self.Album=e.control.data


    def handle_percorso(self,e):
        pass