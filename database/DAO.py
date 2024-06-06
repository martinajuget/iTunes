from database.DB_connect import DBConnect
from model.album import Album

class DAO():

    @staticmethod
    def getAlbums(canzoni):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.* ,count(distinct T.TrackId) as numCanzoni
            from album a, track t 
            where t.AlbumId=a.AlbumId 
            group by a.AlbumId 
            having numCanzoni>%s"""

        cursor.execute(query, (canzoni,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAlbums():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.* ,count(distinct T.TrackId) as numCanzoni
                from album a, track t 
                where t.AlbumId=a.AlbumId 
                group by a.AlbumId 
                """

        cursor.execute(query)

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result