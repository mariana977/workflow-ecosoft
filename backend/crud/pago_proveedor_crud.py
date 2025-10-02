from fastapi import HTTPException
from mysql.connector import MySQLConnection
from typing import List, Dict

def create_pago_proveedor(db: MySQLConnection, data: Dict):
    cursor = db.cursor()
    # build insert dynamically
    cols = ", ".join(data.keys())
    vals = ", ".join(["%s"] * len(data))
    sql = f"INSERT INTO pago_proveedor ({cols}) VALUES ({vals})"
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    return {"message": "pago_proveedor creado"}

def list_pago_proveedor(db: MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pago_proveedor")
    return cursor.fetchall()

def get_pago_proveedor(db: MySQLConnection, id_val: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pago_proveedor WHERE id_pago=%s", (id_val,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="pago_proveedor no encontrado")
    return row

def update_pago_proveedor(db: MySQLConnection, id_val: int, data: Dict):
    cursor = db.cursor()
    set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
    sql = f"UPDATE pago_proveedor SET {set_clause} WHERE id_pago=%s"
    params = list(data.values()) + [id_val]
    cursor.execute(sql, tuple(params))
    db.commit()
    return {"message": "pago_proveedor actualizado"}

def delete_pago_proveedor(db: MySQLConnection, id_val: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM pago_proveedor WHERE id_pago=%s", (id_val,))
    db.commit()
    return {"message": "pago_proveedor eliminado"}