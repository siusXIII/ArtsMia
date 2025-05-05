from database.DB_connect import DBConnect
from model.arco import Arco
from model.artObject import ArtObject


class DAO:

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                   FROM objects o"""

        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(v1, v2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT eo.object_id, eo2.object_id, eo.exhibition_id, count(*) as peso
                   FROM exhibition_objects eo, exhibition_objects eo2
                   WHERE eo.exhibition_id = eo2.exhibition_id AND eo.object_id < eo2.object_id
                   AND eo.object_id = %s AND eo2.object_id = %s
                   GROUP BY eo.object_id, eo2.object_id"""

        cursor.execute(query,(v1.object_id, v2.object_id))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()

        if len(result) == 0:
            return None
        return result

    @staticmethod
    def getAllArchi(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT eo.object_id as o1, eo2.object_id as o2, eo.exhibition_id, count(*) as peso
                   FROM exhibition_objects eo, exhibition_objects eo2
                   WHERE eo.exhibition_id = eo2.exhibition_id AND eo.object_id < eo2.object_id
                   GROUP BY eo.object_id, eo2.object_id
                   ORDER BY peso desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(idMap[row["o1"]], idMap[row["o2"]], row["peso"]))

        cursor.close()
        conn.close()

        if len(result) == 0:
            return None
        return result
