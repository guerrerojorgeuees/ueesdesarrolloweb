CREATE SEQUENCE contacts_id_seq START 1;
-- Crear la tabla utilizando la secuencia
CREATE TABLE contacts (
  id INTEGER DEFAULT nextval('contacts_id_seq'::regclass) PRIMARY KEY,
  fullname VARCHAR(255),
  phone VARCHAR(255),
  email VARCHAR(255) NOT NULL UNIQUE
);
