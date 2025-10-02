from fastapi import APIRouter, Depends
from ..database import get_db_conn, redis_client
from ..crud import domiciliario_crud
from typing import Dict
import json

router = APIRouter(prefix="/api/domiciliario", tags=["Domiciliario"])

def _get_conn():
    conn = get_db_conn()
    try:
        yield conn
    finally:
        conn.close()

@router.post("/")
def create_item(payload: Dict, conn=Depends(_get_conn)):
    return domiciliario_crud.create_domiciliario(conn, payload)

@router.get("/")
def list_items(conn=Depends(_get_conn)):
    cache_key = "domiciliario_list"
    if redis_client:
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
    rows = domiciliario_crud.list_domiciliario(conn)
    if redis_client:
        try:
            redis_client.setex(cache_key, 60, json.dumps(rows, default=str))
        except Exception:
            pass
    return rows

@router.get("/{item_id}")
def get_item(item_id: int, conn=Depends(_get_conn)):
    return domiciliario_crud.get_domiciliario(conn, item_id)

@router.put("/{item_id}")
def update_item(item_id: int, payload: Dict, conn=Depends(_get_conn)):
    return domiciliario_crud.update_domiciliario(conn, item_id, payload)

@router.delete("/{item_id}")
def delete_item(item_id: int, conn=Depends(_get_conn)):
    return domiciliario_crud.delete_domiciliario(conn, item_id)