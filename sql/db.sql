CREATE SEQUENCE cliente_id_seq START 1;
-- Crear la tabla utilizando la secuencia
CREATE TABLE "uees"."cliente" (
  "id" int4 NOT NULL DEFAULT nextval('"uees".cliente_id_seq1'::regclass),
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


--- tabla de articulo
CREATE SEQUENCE articulo_id_seq START 1;
-- Crear la tabla de Articulos
CREATE TABLE "uees"."articulo" (
  "id" int4 NOT NULL DEFAULT nextval('"uees".articulo_id_seq1'::regclass),
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