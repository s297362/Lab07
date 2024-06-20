import copy

import database.meteo_dao


class Model:
    def __init__(self):
        self.bestPath = None
        self.bestCost = -1

    def umiditaMedia(self, mese):
        risultati = database.meteo_dao.MeteoDao().get_situazione_media(mese)
        return risultati

    def gestisciPercorso(self, mese):
        situazioni = database.meteo_dao.MeteoDao().get_all_situzioni(mese)
        parziale = []
        costo = 0
        print(len(situazioni))
        self.ricorsione(parziale, situazioni, costo)
        return self.bestPath

    def ricorsione(self, parziale, situazioni, costo):
        # Soluzione valida?
        print(self.bestCost)
        print(len(parziale))
        if not self.validita(parziale):
            if parziale == self.bestPath:
                return
        # Condizione terminale
        if len(parziale) == 15:
            if costo < self.bestCost or self.bestCost == -1:
                self.bestPath = copy.deepcopy(parziale)
                self.bestCost = costo
                costo = 0

        # Ciclo sulle situazioni

        day = len(parziale)+1
        for s in situazioni[(day - 1)*3:day*3]:
            if self.vincoli(parziale, s):
                parziale.append(s)
            if parziale[-1].Localita != s.Localita:
                costo += s.Umidita + 100
            else:
                costo += s.Umidita
            self.ricorsione(parziale, situazioni, costo)
            parziale.pop()


    def validita(self, parziale):
        if len(parziale) <= 6:
            return True
        if len(parziale) > 15:
            return False
        for i in parziale:
            if parziale.count(i) > 6:
                return False

    def vincoli(self, parziale, situazione):
        # check che il tecnico non si sposti prima di aver trascorso 3 giorni consecutivi nella stessa
        # citta
        if len(parziale) >= 3:
            last_stop = parziale[-1].Localita
            permanenza = 0
            for stop in parziale[-3:]:
                if stop.Localita == last_stop:
                    permanenza += 1
            if permanenza < 3 and situazione.Localita != last_stop:
                return False
            else:
                return True
        else:
            for stop in parziale:
                if stop.Localita != situazione.Localita:
                    return False
            return True


