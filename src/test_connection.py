from src.utils.database import get_connection

conn = get_connection()

print("Conexão realizada com sucesso!")

conn.close()