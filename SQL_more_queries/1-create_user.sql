-- script pour créé l'utilisateur user_0d_1
-- user_0d_1 devrait avoir tous les privilèges plus mdp 
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
