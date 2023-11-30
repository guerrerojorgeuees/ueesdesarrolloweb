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
