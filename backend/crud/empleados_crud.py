from fastapi import HTTPException
from mysql.connector import MySQLConnection
from typing import List, Dict

def create_empleados(db: MySQLConnection, data: Dict):
    cursor = db.cursor()
    # build insert dynamically
    cols = ", ".join(data.keys())
    vals = ", ".join(["%s"] * len(data))
    sql = f"INSERT INTO empleados ({cols}) VALUES ({vals})"
    cursor.execute(sql, tuple(data.values()))
    db.commit()
    return {"message": "empleados creado"}

def list_empleados(db: MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados")
    return cursor.fetchall()

def get_empleados(db: MySQLConnection, id_val: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados WHERE id_empleados=%s", (id_val,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="empleados no encontrado")
    return row

def update_empleados(db: MySQLConnection, id_val: int, data: Dict):
    cursor = db.cursor()
    set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
    sql = f"UPDATE empleados SET {set_clause} WHERE id_empleados=%s"
    params = list(data.values()) + [id_val]
    cursor.execute(sql, tuple(params))
    db.commit()
    return {"message": "empleados actualizado"}

def delete_empleados(db: MySQLConnection, id_val: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM empleados WHERE id_empleados=%s", (id_val,))
    db.commit()
    return {"message": "empleados eliminado"}