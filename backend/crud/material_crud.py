from fastapi import HTTPException
from mysql.connector import MySQLConnection
from typing import List, Dict

def create_material(db: MySQLConnection, data: Dict):
    cursor = db.cursor()
    # build insert dynamically
    cols = ", ".join(data.keys())
    vals = ", ".join(["%s"] * len(data))
    sql = f"INSERT INTO material ({cols}) VALUES ({vals})"
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    return {"message": "material creado"}

def list_material(db: MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM material")
    return cursor.fetchall()

def get_material(db: MySQLConnection, id_val: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM material WHERE id_material=%s", (id_val,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="material no encontrado")
    return row

def update_material(db: MySQLConnection, id_val: int, data: Dict):
    cursor = db.cursor()
    set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
    sql = f"UPDATE material SET {set_clause} WHERE id_material=%s"
    params = list(data.values()) + [id_val]
    cursor.execute(sql, tuple(params))
    db.commit()
    return {"message": "material actualizado"}

def delete_material(db: MySQLConnection, id_val: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM material WHERE id_material=%s", (id_val,))
    db.commit()
    return {"message": "material eliminado"}