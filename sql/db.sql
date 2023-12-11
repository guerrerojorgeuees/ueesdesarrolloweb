CREATE DATABASE bd_uees WITH OWNER = postgres;
CREATE SCHEMA uees;
ALTER DATABASE bd_uees SET search_path TO uees;

CREATE SEQUENCE uees.cliente_id_seq START 1;
-- Crear la tabla utilizando la secuencia
CREATE TABLE "uees"."cliente" (
  "id" int4 NOT NULL DEFAULT nextval('"uees".cliente_id_seq'::regclass),
  "fullname" varchar(255) COLLATE "pg_catalog"."default",
  "cedula" varchar(20) COLLATE "pg_catalog"."default",
  "address" varchar(255) COLLATE "pg_catalog"."default",
  "phone" varchar(20) COLLATE "pg_catalog"."default",
  "estado" varchar(1) COLLATE "pg_catalog"."default",
  "email" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "cliente_pkey" PRIMARY KEY ("id"),
  CONSTRAINT "cliente_email_key" UNIQUE ("email")
)
;

ALTER TABLE "uees"."cliente" 
  OWNER TO "postgres";

--- Eliminar la secuencia de la BDD
--- tabla de articulo
CREATE SEQUENCE uees.articulo_id_seq START 1;

--- Eliminar la tabla y volver a crear 
CREATE TABLE "uees"."articulo" (
  "id" int4 NOT NULL DEFAULT nextval('"uees".articulo_id_seq'::regclass),
  "codigo" varchar(10) COLLATE "pg_catalog"."default",
  "nombre" varchar(255) COLLATE "pg_catalog"."default",
  "fecha_empaque" timestamp(6),
  "fecha_vencimiento" timestamp(6),
  "lote" varchar(20) COLLATE "pg_catalog"."default",
  "descripcion" varchar(255) COLLATE "pg_catalog"."default",
  "precio" numeric(10,2),
  "stock" int4,
  "imagen" varchar(255) COLLATE "pg_catalog"."default",
   "estado" varchar(1) COLLATE "pg_catalog"."default",
  CONSTRAINT "articulo_pkey" PRIMARY KEY ("id")
)
;

ALTER TABLE "uees"."articulo" 
  OWNER TO "postgres";


CREATE SEQUENCE "uees".user_id_seq START 1;
CREATE TABLE "uees"."user" (
  "id" int4 NOT NULL DEFAULT nextval('"uees".articulo_id_seq'::regclass),
  "username" varchar(50) COLLATE "pg_catalog"."default",
  "password" varchar(50) COLLATE "pg_catalog"."default",
  "role" varchar(1) COLLATE "pg_catalog"."default"
);

ALTER TABLE "uees"."user" 
  OWNER TO "postgres";