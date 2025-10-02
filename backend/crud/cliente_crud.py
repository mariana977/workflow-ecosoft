from fastapi import HTTPException
from mysql.connector import MySQLConnection
from typing import List, Dict

def create_cliente(db: MySQLConnection, data: Dict):
    cursor = db.cursor()
    # build insert dynamically
    cols = ", ".join(data.keys())
    vals = ", ".join(["%s"] * len(data))
    sql = f"INSERT INTO cliente ({cols}) VALUES ({vals})"
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    return {"message": "cliente creado"}

def list_cliente(db: MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente")
    return cursor.fetchall()

def get_cliente(db: MySQLConnection, id_val: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente WHERE id_cliente=%s", (id_val,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="cliente no encontrado")
    return row

def update_cliente(db: MySQLConnection, id_val: int, data: Dict):
    cursor = db.cursor()
    set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
    sql = f"UPDATE cliente SET {set_clause} WHERE id_cliente=%s"
    params = list(data.values()) + [id_val]
    cursor.execute(sql, tuple(params))
    db.commit()
    return {"message": "cliente actualizado"}

def delete_cliente(db: MySQLConnection, id_val: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM cliente WHERE id_cliente=%s", (id_val,))
    db.commit()
    return {"message": "cliente eliminado"}