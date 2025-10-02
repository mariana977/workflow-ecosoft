CREATE DATABASE IF NOT EXISTS Ecosoft;
USE Ecosoft;

-- TABLA CLIENTE
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(30),
    direccion VARCHAR(100),
    correo VARCHAR(100),
    contraseña_c VARCHAR(255) NOT NULL
);

-- TABLA EMPLEADOS
CREATE TABLE IF NOT EXISTS empleados (
    id_empleados INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(30),
    direccion VARCHAR(100),
    correo VARCHAR(100),
    contraseña_e VARCHAR(255) NOT NULL
);

-- TABLA DOMICILIARIO
CREATE TABLE IF NOT EXISTS domiciliario (
    id_domiciliario INT PRIMARY KEY AUTO_INCREMENT,
    id_factura INT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    tipo_vehiculo VARCHAR(30),
    capacidad_carga DECIMAL(10,2),
    contacto VARCHAR(30),
    correo VARCHAR(40)
);

-- TABLA PEDIDO
CREATE TABLE IF NOT EXISTS pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    fecha_pedido DATE,
    estado VARCHAR(20),
    tipo_mt VARCHAR(30),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- TABLA FACTURA
CREATE TABLE IF NOT EXISTS factura (
    id_factura INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    fecha DATE,
    precio_por_kg DECIMAL(10,2),
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- TABLA PROVEEDOR
CREATE TABLE IF NOT EXISTS proveedor (
    id_proveedor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(30),
    correo VARCHAR(100),
    contraseña_p VARCHAR(255) NOT NULL
);

-- TABLA RECEPCION DE MATERIAL
CREATE TABLE IF NOT EXISTS recepcion_material (
    id_recepcion INT PRIMARY KEY AUTO_INCREMENT,
    id_proveedor INT,
    fecha_recepcion DATE,
    precio_por_kg DECIMAL(10,2),
    FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor)
);

-- TABLA MATERIAL
CREATE TABLE IF NOT EXISTS material (
    id_material INT PRIMARY KEY AUTO_INCREMENT,
    tipo_mt VARCHAR(30),
    cantidad_mt DECIMAL(10,2),
    descripcion VARCHAR(100)
);

-- TABLA INVENTARIO
CREATE TABLE IF NOT EXISTS inventario (
    id_inventario INT PRIMARY KEY AUTO_INCREMENT,
    id_material INT,
    id_pedido INT,
    fecha DATE,
    cantidad DECIMAL(10,2),
    FOREIGN KEY (id_material) REFERENCES material(id_material),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
);

-- TABLA PAGO A PROVEEDOR
CREATE TABLE IF NOT EXISTS pago_proveedor (
    id_pago INT PRIMARY KEY AUTO_INCREMENT,
    id_proveedor INT,
    total_pago DECIMAL(10,2),
    fecha_pago DATE,
    estado VARCHAR(20),
    FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor)
);