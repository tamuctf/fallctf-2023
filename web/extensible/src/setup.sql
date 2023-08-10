PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS users;
CREATE TABLE users (username varchar(16), password varchar(32), session varchar(32));
COMMIT;
