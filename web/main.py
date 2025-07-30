from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()

@app.get("/")
def read_root():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpass",
            database="mydb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        return {"message": f"Database connected! Current time: {result[0]}"}
    except Error as e:
        return {"error": str(e)}

