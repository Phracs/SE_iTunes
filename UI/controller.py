import flet as ft
import networkx as nx

from UI.view import View
from database.dao import DAO
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        durata=int(self._view.txt_durata.value)
        self._model.crea_grafo(durata)
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"{self._model.grafo}"))
        self._view.dd_album.options.clear()
        for a in self._model.lista_album:
            self._view.dd_album.options.append(ft.dropdown.Option(a))
        self._view.update()

    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        # TODO

    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO
        self._view.lista_visualizzazione_2.controls.clear()
        a1=int(self._view.dd_album.value)
        num_connessi=len(nx.node_connected_component(self._model.grafo, a1))
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Album connessi: {num_connessi}"))
        durata_tot=self._model.get_durata_tot(a1)
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Durata complessiva: {durata_tot}"))
        self._view.update()

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO


