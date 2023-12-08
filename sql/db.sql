CREATE SEQUENCE cliente_id_seq START 1;
-- Crear la tabla utilizando la secuencia
CREATE TABLE cliente (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(255),
  cedula VARCHAR(20),
  address VARCHAR(255),
  phone VARCHAR(20),
  email VARCHAR(255) NOT NULL UNIQUE
);


--- tabla de articulo
CREATE SEQUENCE articulo_id_seq START 1;
-- Crear la tabla de Articulos
CREATE TABLE uees.articulo (
  id SERIAL PRIMARY KEY,
  codigo   Varchar(10),
  nombre  VARCHAR(255),
  fecha_empaque timestamp(6),
  fecha_vencimiento timestamp(6),
  lote VARCHAR(20),
  descripcion VARCHAR(255),
  precio numeric(10,2),
  stock  int4   -- Afectar el stock en la venta 
);
