
/* change this name to place before launch */
CREATE TABLE Pizza (
    id SERIAL,
    name varchar(32) NOT NULL,
    grade NUMERIC,
    details VARCHAR(1024),
    PRIMARY KEY(id)
);