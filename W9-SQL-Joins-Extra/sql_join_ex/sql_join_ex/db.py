from sqlite3 import Connection, connect
from typing import ClassVar
from tilaus import Tilaus
from asiakas import Asiakas
import constants as C

class DB:

    def __init__(self, dbname: str) -> None:
        self.conn = connect(dbname)
        c = self.conn.cursor()
    def create_tables(self) -> None:
        c = self.conn.cursor()
        c.execute(C.CREATE_TILAUS)
        c.execute(C.CREATE_ASIAKAS)
        self.conn.commit()

    def get_tilaukset(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET)
        return c.fetchall()
    def get_asiakkaat(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_ASIAKKAAT)
        return c.fetchall()
    def get_tilaukset_asiakkaat(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT)
        return c.fetchall()
    def get_tilaukset_asiakkaat_left(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT_LEFT)
        return c.fetchall()
    def get_tilaukset_asiakkaat_right(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT_RIGHT)
        return c.fetchall()
    def get_tilaukset_asiakkaat_full(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT_FULL)
        return c.fetchall()
    def get_tilaukset_asiakkaat_where(self, summa: float) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT_WHERE, (summa,))
        return c.fetchall()
    def get_tilaukset_asiakkaat_order(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT_ORDER)
        return c.fetchall()
    def get_tilaukset_asiakkaat_group(self) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT_GROUP)
        return c.fetchall()
    # def get_tilaukset_asiakkaat_having(self, summa: float) -> list:
    #     c = self.conn.cursor()
    #     c.execute(C.SELECT_TILAUSET_ASIAKKAAT_HAVING, (summa,))
    #     return c.fetchall()
    def get_tilaukset_asiakkaat_subquery(self, summa: float) -> list:
        c = self.conn.cursor()
        c.execute(C.SELECT_TILAUSET_ASIAKKAAT_SUBQUERY, (summa,))
        return c.fetchall()
    def insert_tilaus(self, asiakas_id: int, summa: float) -> bool:
        c = self.conn.cursor()
        if self.check_asiakas_exists(asiakas_id):
            c.execute(C.INSERT_TILAUS, (asiakas_id, summa))
            self.conn.commit()
            return True
        return False
    def insert_asiakas(self, nimi: str, sahkoposti: str) -> None:
        c = self.conn.cursor()
        c.execute(C.INSERT_ASIAKAS, (nimi, sahkoposti))
        self.conn.commit()
    def close(self) -> None:
        self.conn.close()
    def update_tilaus(self, id: int, asiakas_id: int, summa: float) -> bool:
        c = self.conn.cursor()
        if self.check_asiakas_exists(asiakas_id):
            c.execute(C.UPDATE_TILAUS, (asiakas_id, summa, id))
            self.conn.commit()
            return True
        return False
    def update_asiakas(self, id: int, nimi: str, sahkoposti: str) -> None:
        c = self.conn.cursor()
        c.execute(C.UPDATE_ASIAKAS, (nimi, sahkoposti, id))
        self.conn.commit()
    def delete_tilaus(self, id: int) -> bool:
        c = self.conn.cursor()
        c.execute(C.DELETE_TILAUS, (id,))
        self.conn.commit()
        return c.rowcount > 0
    def delete_asiakas(self, id: int, del_tilaukset: bool = True) -> bool:
        c = self.conn.cursor()
        # poistetaan asiakas ja kaikki hänen tilauksensa
        if del_tilaukset:
            c.execute(C.DELETE_TILAUS_BY_ASIAKAS, (id,))
            if not c.rowcount > 0:
                return False
        else:
            c.execute(C.UPDATE_TILAUS_SET_NULL_BY_ASIAKAS, (id,))
            if not c.rowcount > 0:
                return False            
        c.execute(C.DELETE_ASIAKAS, (id,))
        self.conn.commit()
        if not c.rowcount > 0:
            return False
        return True
    def check_asiakas_exists(self, asiakas_id: int) -> bool:
        c = self.conn.cursor()
        c.execute(C.CHECK_ASIAKAS_EXISTS, (asiakas_id,))
        return c.fetchone() is not None
