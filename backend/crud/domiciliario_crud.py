from fastapi import HTTPException
from mysql.connector import MySQLConnection
from typing import List, Dict

def create_domiciliario(db: MySQLConnection, data: Dict):
    cursor = db.cursor()
    # build insert dynamically
    cols = ", ".join(data.keys())
    vals = ", ".join(["%s"] * len(data))
    sql = f"INSERT INTO domiciliario ({cols}) VALUES ({vals})"
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    return {"message": "domiciliario creado"}

def list_domiciliario(db: MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM domiciliario")
    return cursor.fetchall()

def get_domiciliario(db: MySQLConnection, id_val: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM domiciliario WHERE id_domiciliario=%s", (id_val,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="domiciliario no encontrado")
    return row

def update_domiciliario(db: MySQLConnection, id_val: int, data: Dict):
    cursor = db.cursor()
    set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
    sql = f"UPDATE domiciliario SET {set_clause} WHERE id_domiciliario=%s"
    params = list(data.values()) + [id_val]
    cursor.execute(sql, tuple(params))
    db.commit()
    return {"message": "domiciliario actualizado"}

def delete_domiciliario(db: MySQLConnection, id_val: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM domiciliario WHERE id_domiciliario=%s", (id_val,))
    db.commit()
    return {"message": "domiciliario eliminado"}