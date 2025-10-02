from fastapi import HTTPException
from mysql.connector import MySQLConnection
from typing import List, Dict

def create_pedido(db: MySQLConnection, data: Dict):
    cursor = db.cursor()
    # build insert dynamically
    cols = ", ".join(data.keys())
    vals = ", ".join(["%s"] * len(data))
    sql = f"INSERT INTO pedido ({cols}) VALUES ({vals})"
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    return {"message": "pedido creado"}

def list_pedido(db: MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pedido")
    return cursor.fetchall()

def get_pedido(db: MySQLConnection, id_val: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pedido WHERE id_pedido=%s", (id_val,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="pedido no encontrado")
    return row

def update_pedido(db: MySQLConnection, id_val: int, data: Dict):
    cursor = db.cursor()
    set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
    sql = f"UPDATE pedido SET {set_clause} WHERE id_pedido=%s"
    params = list(data.values()) + [id_val]
    cursor.execute(sql, tuple(params))
    db.commit()
    return {"message": "pedido actualizado"}

def delete_pedido(db: MySQLConnection, id_val: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM pedido WHERE id_pedido=%s", (id_val,))
    db.commit()
    return {"message": "pedido eliminado"}