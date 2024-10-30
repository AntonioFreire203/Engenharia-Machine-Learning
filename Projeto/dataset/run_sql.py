import os
import psycopg2
import psycopg2.extras as ext
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

def run_sql(sql, values=None):
    # Variáveis de controle
    conn = None
    results = []

    # Conexão ao banco de dados
    try:
        
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return results
