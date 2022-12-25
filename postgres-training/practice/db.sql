
Create sequence serial;
CREATE TABLE rides (
    id          integer PRIMARY KEY DEFAULT nextval('serial'),
    distance    double precision NOT NULL,
    company     varchar(40) NOT NULL,
    time_stamp  timestamp NOT NULL,
    destination varchar(40) NOT NULL,
    source      varchar(40) NOT NULL,
    price       double precision NULL,
    category    varchar(40) NOT NULL
);
