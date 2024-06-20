from database.DB_connect import DBConnect
from model.situazione import Situazione
from model.umiditaMedia import UmiditaMedia


class MeteoDao():

    @staticmethod
    def get_situazione_media(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, sum(s.Umidita)/COUNT(*) as UmiditaMedia
FROM situazione s 
WHERE month(s.`Data`) = %s
GROUP BY s.Localita"""
            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(UmiditaMedia(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_situzioni(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
            FROM situazione s
            WHERE month(s.`Data`) = %s
            AND day(s.`Data`) <= 15"""
            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(Situazione(**row))
            cursor.close()
            cnx.close()
        return result



