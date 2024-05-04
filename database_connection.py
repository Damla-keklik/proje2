import pyodbc
def connect_to_database():

    try:
        # Veritabanı bağlantı dizesi
        server = 'DAMLA'  # Sunucu adı veya IP adresi
        database = 'GEZGIN_GEMI'  # Veritabanı adı
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        # Veritabanına bağlan
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Bağlantıyı döndür
        return conn, cursor

    except Exception as e:
        # Bağlantı hatası
        print("Veritabanına bağlanırken bir hata oluştu:", e)
        return None, None
