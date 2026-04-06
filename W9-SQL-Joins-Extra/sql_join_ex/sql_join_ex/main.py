from db import DB
from tilaus import Tilaus
from asiakas import Asiakas
import menu_strings as ms
class Main:
    def __init__(self, dbname: str):
        self.db = DB(dbname)
        self.db.create_tables()
        self.run()
        self.db.conn.close()
    def run(self):
        while True:
            print(ms.M_NAYTA_TILAUKSET)
            print(ms.M_NAYTA_ASIAKKAAT)
            print(ms.M_NAYTA_TIL_AS)
            print(ms.M_NAYTA_TIL_AS_LJ)
            print(ms.M_NAYTA_TIL_AS_RJ)
            print(ms.M_NAYTA_TIL_AS_FOJ)
            print(ms.M_NAYTA_TIL_AS_WS)
            print(ms.M_NAYTA_TIL_AS_OD)
            print(ms.M_NAYTA_TIL_AS_SG)
            print(ms.M_LISAA_TILAUS)
            print(ms.M_LISAA_ASIAKAS)
            print(ms.M_POISTA_TILAUS)
            print(ms.M_POISTA_ASIAKAS)
            print(ms.M_LOPETA)
            valinta = input(ms.M_VALITSE)
            if valinta == "1":
                tilaukset = self.db.get_tilaukset()
                for tilaus in tilaukset:
                    print(Tilaus(*tilaus))
                
            elif valinta == "2":
                asiakkaat = self.db.get_asiakkaat()
                for asiakas in asiakkaat:
                    print(Asiakas(*asiakas))
                
            elif valinta == "3":
                tilaukset_asiakkaat = self.db.get_tilaukset_asiakkaat()
                for tilaus_asiakas in tilaukset_asiakkaat:
                    print(tilaus_asiakas)
            
            elif valinta == "a":
                tilaukset_asiakkaat = self.db.get_tilaukset_asiakkaat_left()
                for tilaus_asiakas in tilaukset_asiakkaat:
                    print(tilaus_asiakas)
            
            elif valinta == "b":
                tilaukset_asiakkaat = self.db.get_tilaukset_asiakkaat_right()
                for tilaus_asiakas in tilaukset_asiakkaat:
                    print(tilaus_asiakas)
            
            elif valinta == "c":
                tilaukset_asiakkaat = self.db.get_tilaukset_asiakkaat_full()
                for tilaus_asiakas in tilaukset_asiakkaat:
                    print(tilaus_asiakas)
            
            elif valinta == "d":
                summa = 0.0
                try:
                    summa = float(input(ms.MSG_ANNA_SUMMA))
                except ValueError:
                    
                    print(ms.MSG_ERR_SUMMA.format(summa))
                tilaukset_asiakkaat = self.db.get_tilaukset_asiakkaat_where(summa)
                for tilaus_asiakas in tilaukset_asiakkaat:
                    print(tilaus_asiakas)
            
            elif valinta == "e":
                tilaukset_asiakkaat = self.db.get_tilaukset_asiakkaat_order()
                for tilaus_asiakas in tilaukset_asiakkaat:
                    print(tilaus_asiakas)
            
            elif valinta == "f":
                tilaukset_asiakkaat = self.db.get_tilaukset_asiakkaat_group()
                for tilaus_asiakas in tilaukset_asiakkaat:
                    print(tilaus_asiakas)
            
            elif valinta == "4":
                id = 0
                try:
                    id = int(input(ms.MSG_ANNA_AS_ID))
                except ValueError:
                    print(ms.MSG_VIRHE_ID)
                    continue
                if not self.db.check_asiakas_exists(id):
                    print(ms.MSG_ASIAKAS_EI_OLEMASSA.format(id) )
                    continue
                summa = 0.0
                try:
                    summa = float(input(ms.MSG_ANNA_TIL_SUM))
                except ValueError:
                    print(ms.MSG_VIRHE_SUM)
                    continue
                if not self.db.insert_tilaus(id, summa):
                    print(ms.MSG_TIL_LISAYS_EPAONNISTUI)
            
            elif valinta == "5":
                nimi = input(ms.MSG_ANNA_AS_NIMI).strip()
                sahkoposti = input(ms.MSG_ANNA_AS_SPOSTI).strip()
                self.db.insert_asiakas(nimi, sahkoposti)
            elif valinta == "6":
                id = 0
                try:
                    id = int(input(ms.MSG_ANNA_TIL_ID))
                except ValueError:
                    print(ms.MSG_VIRHE_ID)
                    continue
                    
                if not self.db.delete_tilaus(id):
                    print(ms.MSG_TIL_POISTO_EPAONNISTUI)
            elif valinta == "7":
                id = 0
                try:
                    id = int(input(ms.MSG_ANNA_AS_ID))
                except ValueError:
                    print(ms.MSG_VIRHE_ID)
                    continue
                    
                if not self.db.delete_asiakas(id):
                    print(ms.MSG_AS_POISTO_EPAONNISTUI)
            elif valinta == "0":
                break
            else:
                print(ms.MSG_VIRHE_VALINTA)
            print()
if __name__ == "__main__":
    main = Main("tilaukset.db")
