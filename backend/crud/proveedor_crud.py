from fastapi import HTTPException
from mysql.connector import MySQLConnection
from typing import List, Dict

def create_proveedor(db: MySQLConnection, data: Dict):
    cursor = db.cursor()
    # build insert dynamically
    cols = ", ".join(data.keys())
    vals = ", ".join(["%s"] * len(data))
    sql = f"INSERT INTO proveedor ({cols}) VALUES ({vals})"
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    return {"message": "proveedor creado"}

def list_proveedor(db: MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proveedor")
    return cursor.fetchall()

def get_proveedor(db: MySQLConnection, id_val: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proveedor WHERE id_proveedor=%s", (id_val,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="proveedor no encontrado")
    return row

def update_proveedor(db: MySQLConnection, id_val: int, data: Dict):
    cursor = db.cursor()
    set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
    sql = f"UPDATE proveedor SET {set_clause} WHERE id_proveedor=%s"
    params = list(data.values()) + [id_val]
    cursor.execute(sql, tuple(params))
    db.commit()
    return {"message": "proveedor actualizado"}

def delete_proveedor(db: MySQLConnection, id_val: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM proveedor WHERE id_proveedor=%s", (id_val,))
    db.commit()
    return {"message": "proveedor eliminado"}