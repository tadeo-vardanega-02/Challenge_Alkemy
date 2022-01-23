--Informacion obtenida del request

--Cines_df

-- Table: public.Cines_df

-- DROP TABLE IF EXISTS public."Cines_df";

CREATE TABLE IF NOT EXISTS public."Cines_df"
(
    index bigint,
    "Cod_Loc" bigint,
    "IdProvincia" bigint,
    "IdDepartamento" bigint,
    "Observaciones" double precision,
    "Categoría" text COLLATE pg_catalog."default",
    "Provincia" text COLLATE pg_catalog."default",
    "Departamento" text COLLATE pg_catalog."default",
    "Localidad" text COLLATE pg_catalog."default",
    "Nombre" text COLLATE pg_catalog."default",
    "Dirección" text COLLATE pg_catalog."default",
    "Piso" text COLLATE pg_catalog."default",
    "CP" bigint,
    cod_area text COLLATE pg_catalog."default",
    "Teléfono" text COLLATE pg_catalog."default",
    "Mail" text COLLATE pg_catalog."default",
    "Web" text COLLATE pg_catalog."default",
    "Información adicional" double precision,
    "Latitud" double precision,
    "Longitud" double precision,
    "TipoLatitudLongitud" text COLLATE pg_catalog."default",
    "Fuente" text COLLATE pg_catalog."default",
    tipo_gestion text COLLATE pg_catalog."default",
    "Pantallas" bigint,
    "Butacas" bigint,
    "espacio_INCAA" text COLLATE pg_catalog."default",
    "año_actualizacion" bigint
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Cines_df"
    OWNER to postgres;
-- Index: ix_Cines_df_index

-- DROP INDEX IF EXISTS public."ix_Cines_df_index";

CREATE INDEX IF NOT EXISTS "ix_Cines_df_index"
    ON public."Cines_df" USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;


TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Cines_df"
    OWNER to postgres;
-- Index: ix_Cines_df_index

-- DROP INDEX IF EXISTS public."ix_Cines_df_index";

CREATE INDEX IF NOT EXISTS "ix_Cines_df_index"
    ON public."Cines_df" USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;



--Museos_df

-- Table: public.Museos_df

-- DROP TABLE IF EXISTS public."Museos_df";

CREATE TABLE IF NOT EXISTS public."Museos_df"
(
    index bigint,
    "Cod_Loc" bigint,
    "IdProvincia" bigint,
    "IdDepartamento" bigint,
    "Observaciones" double precision,
    categoria text COLLATE pg_catalog."default",
    subcategoria text COLLATE pg_catalog."default",
    provincia text COLLATE pg_catalog."default",
    localidad text COLLATE pg_catalog."default",
    nombre text COLLATE pg_catalog."default",
    direccion text COLLATE pg_catalog."default",
    piso double precision,
    "CP" text COLLATE pg_catalog."default",
    cod_area double precision,
    telefono text COLLATE pg_catalog."default",
    "Mail" text COLLATE pg_catalog."default",
    "Web" text COLLATE pg_catalog."default",
    "Latitud" double precision,
    "Longitud" double precision,
    "TipoLatitudLongitud" text COLLATE pg_catalog."default",
    "Info_adicional" text COLLATE pg_catalog."default",
    fuente text COLLATE pg_catalog."default",
    jurisdiccion text COLLATE pg_catalog."default",
    "año_inauguracion" double precision,
    "IDSInCA" bigint
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Museos_df"
    OWNER to postgres;
-- Index: ix_Museos_df_index

-- DROP INDEX IF EXISTS public."ix_Museos_df_index";

CREATE INDEX IF NOT EXISTS "ix_Museos_df_index"
    ON public."Museos_df" USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;


--Bibliotecas_df

-- Table: public.Bibliotecas_df

-- DROP TABLE IF EXISTS public."Bibliotecas_df";

CREATE TABLE IF NOT EXISTS public."Bibliotecas_df"
(
    index bigint,
    "Cod_Loc" bigint,
    "IdProvincia" bigint,
    "IdDepartamento" bigint,
    "Observacion" double precision,
    "Categoría" text COLLATE pg_catalog."default",
    "Subcategoria" double precision,
    "Provincia" text COLLATE pg_catalog."default",
    "Departamento" text COLLATE pg_catalog."default",
    "Localidad" text COLLATE pg_catalog."default",
    "Nombre" text COLLATE pg_catalog."default",
    "Domicilio" text COLLATE pg_catalog."default",
    "Piso" double precision,
    "CP" text COLLATE pg_catalog."default",
    "Cod_tel" text COLLATE pg_catalog."default",
    "Teléfono" text COLLATE pg_catalog."default",
    "Mail" text COLLATE pg_catalog."default",
    "Web" double precision,
    "Información adicional" double precision,
    "Latitud" double precision,
    "Longitud" double precision,
    "TipoLatitudLongitud" text COLLATE pg_catalog."default",
    "Fuente" text COLLATE pg_catalog."default",
    "Tipo_gestion" text COLLATE pg_catalog."default",
    "año_inicio" double precision,
    "Año_actualizacion" bigint
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Bibliotecas_df"
    OWNER to postgres;
-- Index: ix_Bibliotecas_df_index

-- DROP INDEX IF EXISTS public."ix_Bibliotecas_df_index";

CREATE INDEX IF NOT EXISTS "ix_Bibliotecas_df_index"
    ON public."Bibliotecas_df" USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;



--Tabla que contiene toda la informacion normalizada 

-- Table: public.Todos_los_datos

-- DROP TABLE IF EXISTS public."Todos_los_datos";

CREATE TABLE IF NOT EXISTS public."Todos_los_datos"
(
    index bigint,
    "Cod_Loc" bigint,
    "IdProvincia" bigint,
    "IdDepartamento" bigint,
    categoria text COLLATE pg_catalog."default",
    provincia text COLLATE pg_catalog."default",
    "Departamento" text COLLATE pg_catalog."default",
    "Localidad" text COLLATE pg_catalog."default",
    "Nombre" text COLLATE pg_catalog."default",
    "Dirección" text COLLATE pg_catalog."default",
    "CP" text COLLATE pg_catalog."default",
    cod_area text COLLATE pg_catalog."default",
    "Teléfono" text COLLATE pg_catalog."default",
    "Mail" text COLLATE pg_catalog."default",
    "Web" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Todos_los_datos"
    OWNER to postgres;
-- Index: ix_Todos_los_datos_index

-- DROP INDEX IF EXISTS public."ix_Todos_los_datos_index";

CREATE INDEX IF NOT EXISTS "ix_Todos_los_datos_index"
    ON public."Todos_los_datos" USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;

--Tabla que contiene cantidad de registros totales por categoria, por fuente y por provincia y categoria

-- Table: public.Cantidad de registros totales por categoria

-- DROP TABLE IF EXISTS public."Cantidad de registros totales por categoria";

CREATE TABLE IF NOT EXISTS public."Cantidad de registros totales por categoria"
(
    provincia text COLLATE pg_catalog."default",
    categoria text COLLATE pg_catalog."default",
    "Fuente" bigint
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Cantidad de registros totales por categoria"
    OWNER to postgres;
-- Index: ix_Cantidad de registros totales por categoria_categoria

-- DROP INDEX IF EXISTS public."ix_Cantidad de registros totales por categoria_categoria";

CREATE INDEX IF NOT EXISTS "ix_Cantidad de registros totales por categoria_categoria"
    ON public."Cantidad de registros totales por categoria" USING btree
    (categoria COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: ix_Cantidad de registros totales por categoria_provincia

-- DROP INDEX IF EXISTS public."ix_Cantidad de registros totales por categoria_provincia";

CREATE INDEX IF NOT EXISTS "ix_Cantidad de registros totales por categoria_provincia"
    ON public."Cantidad de registros totales por categoria" USING btree
    (provincia COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


--Tabla de los cines (Provincia, cantidad de pantallas, de butacas, de espacios INCAA)

-- Table: public.Cantidad de pantallas, de butacas, de espacios INCAA

-- DROP TABLE IF EXISTS public."Cantidad de pantallas, de butacas, de espacios INCAA";

CREATE TABLE IF NOT EXISTS public."Cantidad de pantallas, de butacas, de espacios INCAA"
(
    "Provincia" text COLLATE pg_catalog."default",
    "Cantidad de pantallas" bigint,
    "Cantidad de butacas" bigint,
    "Cantidad de espacios INCAA" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Cantidad de pantallas, de butacas, de espacios INCAA"
    OWNER to postgres;
-- Index: ix_Cantidad de pantallas, de butacas, de espacios INCAA_24c1

-- DROP INDEX IF EXISTS public."ix_Cantidad de pantallas, de butacas, de espacios INCAA_24c1";

CREATE INDEX IF NOT EXISTS "ix_Cantidad de pantallas, de butacas, de espacios INCAA_24c1"
    ON public."Cantidad de pantallas, de butacas, de espacios INCAA" USING btree
    ("Provincia" COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;