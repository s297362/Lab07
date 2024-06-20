import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        mese = self._view.dd_mese.value
        situazioni = self._model.umiditaMedia(mese)
        self._view.lst_result.controls.append(ft.Text(f"L'umidità media del mese selezionato è:"))
        for i in situazioni:
            self._view.lst_result.controls.append(ft.Text(f'{i.Localita}: {i.UmiditaMedia}'))
        self._view.update_page()



    def handle_sequenza(self, e):
        mese = self._view.dd_mese.value
        percorso, costo = self._model.gestisciPercorso(mese)
        self._view.lst_result.controls.append(ft.Text(f'Il percorso costa: {costo}'))
        for i in percorso:
            self._view.controls.append(ft.Text(f'Città: {i.Localita} '))
        self._view.update_page()

    def read_mese(self, e):
        self._mese = int(e.control.value)

