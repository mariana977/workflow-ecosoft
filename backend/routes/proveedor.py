from fastapi import APIRouter, Depends
from ..database import get_db_conn, redis_client
from ..crud import proveedor_crud
from typing import Dict
import json

router = APIRouter(prefix="/api/proveedor", tags=["Proveedor"])

def _get_conn():
    conn = get_db_conn()
    try:
        yield conn
    finally:
        conn.close()

@router.post("/")
def create_item(payload: Dict, conn=Depends(_get_conn)):
    return proveedor_crud.create_proveedor(conn, payload)

@router.get("/")
def list_items(conn=Depends(_get_conn)):
    cache_key = "proveedor_list"
    if redis_client:
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
    rows = proveedor_crud.list_proveedor(conn)
    if redis_client:
        try:
            redis_client.setex(cache_key, 60, json.dumps(rows, default=str))
        except Exception:
            pass
    return rows

@router.get("/{item_id}")
def get_item(item_id: int, conn=Depends(_get_conn)):
    return proveedor_crud.get_proveedor(conn, item_id)

@router.put("/{item_id}")
def update_item(item_id: int, payload: Dict, conn=Depends(_get_conn)):
    return proveedor_crud.update_proveedor(conn, item_id, payload)

@router.delete("/{item_id}")
def delete_item(item_id: int, conn=Depends(_get_conn)):
    return proveedor_crud.delete_proveedor(conn, item_id)