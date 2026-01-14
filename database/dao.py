from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_album_per_durata(durata: int):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.id 
                    FROM album a, track t
                    WHERE a.id= t.album_id
                    group by a.id
                    having SUM(t.milliseconds)/60000 > %s 
                     """

        cursor.execute(query, (durata,))

        for row in cursor:
            result.append(row["id"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_album_per_playlist():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """  with playlist_album as(select distinct pt.playlist_id, t.album_id
		                                    from playlist_track pt, track t
		                                    where t.id=pt.track_id)
                SELECT DISTINCT (pa1.album_id) AS a1, pa2.album_id AS a2
                FROM playlist_album pa1, playlist_album pa2
                WHERE pa1.playlist_id = pa2.playlist_id
                AND pa1.album_id < pa2.album_id
                     """

        cursor.execute(query)

        for row in cursor:
            result.append((row["a1"], row["a2"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def read_durata(a:int):
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT SUM(t.milliseconds)/60000 as durata
                            FROM album a, track t
                            WHERE a.id= t.album_id
                            and a.id= %s
                             """

        cursor.execute(query, (a,))

        for row in cursor:
            result=(row["durata"])

        cursor.close()
        conn.close()
        return result