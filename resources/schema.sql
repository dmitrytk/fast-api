DROP TABLE IF EXISTS fields CASCADE;
CREATE TABLE fields
(
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR(100) UNIQUE NOT NULL,
    type        VARCHAR(50),
    location    VARCHAR(100),
    description TEXT
);


DROP TABLE IF EXISTS field_coordinates;
CREATE TABLE field_coordinates
(
    id       BIGSERIAL PRIMARY KEY,
    x        NUMERIC(20, 2),
    y        NUMERIC(20, 2),
    lat      NUMERIC(10, 7),
    lng      NUMERIC(10, 7),
    field_id INTEGER,
    FOREIGN KEY (field_id) REFERENCES fields (id) ON DELETE CASCADE
);


DROP TABLE IF EXISTS wells CASCADE;
CREATE TABLE wells
(
    id       BIGSERIAL PRIMARY KEY,
    name     VARCHAR(255) NOT NULL,
    pad      VARCHAR(100),
    type     VARCHAR(100),
    status   VARCHAR(100),
    lat      NUMERIC(10, 6),
    lng      NUMERIC(10, 6),
    x        NUMERIC(20, 2),
    y        NUMERIC(20, 2),
    alt      NUMERIC(6, 2),
    bottom   NUMERIC(7, 2),
    field_id INTEGER      NOT NULL,
    UNIQUE (name, field_id),
    FOREIGN KEY (field_id) REFERENCES fields (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS zones;
CREATE TABLE zones
(
    id      BIGSERIAL PRIMARY KEY,
    well_id BIGINT NOT NULL,
    name    VARCHAR(100),
    top_md  NUMERIC(7, 2),
    bot_md  NUMERIC(7, 2),
    top_tvd NUMERIC(7, 2),
    bot_tvd NUMERIC(7, 2),
    h       NUMERIC(7, 2),
    UNIQUE (well_id, name),
    FOREIGN KEY (well_id) REFERENCES wells (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS inclinometry;
CREATE TABLE inclinometry
(
    id      BIGSERIAL PRIMARY KEY,
    well_id BIGINT        NOT NULL,
    md      NUMERIC(7, 2) NOT NULL CHECK ( md >= 0 ),
    inc     NUMERIC(5, 2),
    azi     NUMERIC(5, 2),
    FOREIGN KEY (well_id) REFERENCES wells (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS rates;
CREATE TABLE rates
(
    id       BIGSERIAL PRIMARY KEY,
    well_id  BIGINT NOT NULL,
    date     DATE,
    rate     NUMERIC(10, 2),
    dynamic  NUMERIC(6, 2),
    static   NUMERIC(6, 2),
    pressure NUMERIC(6, 2),
    FOREIGN KEY (well_id) REFERENCES wells (id) ON DELETE CASCADE
);
DROP TABLE IF EXISTS mer;
CREATE TABLE mer
(
    id         BIGSERIAL PRIMARY KEY,
    well_id    BIGINT NOT NULL,
    date       DATE,
    status     VARCHAR(100),
    rate       NUMERIC(10, 2),
    production NUMERIC(20, 2),
    work_days  INTEGER,
    UNIQUE (well_id, date),
    FOREIGN KEY (well_id) REFERENCES wells (id) ON DELETE CASCADE
);

-- VIEWS
DROP VIEW IF EXISTS inclinometry_view;
CREATE VIEW inclinometry_view as
SELECT i.id,
       w.name as well,
       i.md,
       i.inc,
       i.azi
FROM inclinometry i
         JOIN wells w on w.id = i.well_id;

DROP VIEW IF EXISTS mer_view;
CREATE VIEW mer_view as
SELECT m.id,
       w.name as well,
       m.date,
       m.rate,
       m.status,
       m.production,
       m.work_days
FROM mer m
         JOIN wells w on w.id = m.well_id;

DROP VIEW IF EXISTS rates_view;
CREATE VIEW rates_view as
SELECT r.id,
       w.name as well,
       r.date,
       r.rate,
       r.dynamic,
       r.static,
       r.pressure
FROM rates r
         JOIN wells w on w.id = r.well_id;


DROP VIEW IF EXISTS zones_view;
CREATE VIEW zones_view AS
SELECT z.id,
       w.name AS well,
       z.name,
       z,
       top_md,
       z.bot_md,
       z.top_tvd,
       z.bot_tvd,
       z.h
FROM zones z
         JOIN wells w ON w.id = z.well_id;

DROP VIEW IF EXISTS field_data;
CREATE VIEW field_data AS
SELECT f.id, f.name, count(w.name) as wells_count
FROM fields f
         JOIN wells w ON f.id = w.field_id
GROUP BY 1;