from fastapi import FastAPI
from backend.routes import cliente, empleados, proveedor, pedido, factura, material, inventario, domiciliario, pago_proveedor

app = FastAPI(title="Ecosoft API")

app.include_router(cliente.router)
app.include_router(empleados.router)
app.include_router(proveedor.router)
app.include_router(pedido.router)
app.include_router(factura.router)
app.include_router(material.router)
app.include_router(inventario.router)
app.include_router(domiciliario.router)
app.include_router(pago_proveedor.router)

@app.get("/")
def root():
    return {"message": "API Ecosoft funcionando"}