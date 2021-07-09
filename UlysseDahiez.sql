-- tp bdd 
--Ulysse Dahiez
--///////////////////création des tables/////////////////

CREATE TABLE Utilisateur (
	usr_id integer PRIMARY KEY,
	usr_nom varchar(20),
	usr_prenom varchar(20),
	usr_login varchar(20),
	usr_mdpmd5 password,
	log_id integer references Logement(user_id));

CREATE TABLE Logement (log_id integer PRIMARY KEY,
					  log_adresse varchar(100),
					  log_cp varchar(100),
					  log_ville varchar(100),
					  log_pays varchar(100),
					  log_surface integer,
					  usr_id integer references Utilisateur(usr_id));

CREATE TABLE PeriodePossible (
	pp_id integer PRIMARY KEY,
	pp_dateDebut date,
	pp_dateFin date,
	pp_prix_nuit float,
	log_id integer references Logement(user_id)
);


CREATE TABLE PeriodeReservee (
	pr_id integer PRIMARY KEY,
	pp_dateDebut date,
	pp_dateFin date,
	log_id integer references Logement(user_id),
	usr_id integer references Utilisateur(user_id));

--///////////////Insertion des données utilisateur///////////////////////////

--Question 1

INSERT INTO Utilisateur (usr_nom, usr_prenom, usr_login, usr_mdpmd5, usr_salt)
VALUES
    	('Oswald', 'clara', 'coswald', md5('mdpclara'||'salt0'), 'salt0'),
    	('Khan', 'Yasmin', 'ykhan', md5('mdpyasmin'||'salt1'), 'salt1'),
    	('sinclair', 'Ryan', 'rsinclair', md5('mdpryan'||'salt2'), 'salt2'),
    	('OBlien', 'Graham', 'goblien', md5('mdpgraham'||'salt3'), 'salt3');

-- Question 2
SELECT * from Utilisateur WHERE usr_login = $login AND usr_mdp = md5($mdp||usr);
-- Question 3

SELECT * from Utilisateur WHERE usr_login = 'coswald' AND usr_mdpmd5 = md5('BonjourBon'||usr_salt);

--Question 4 

SELECT * from Utilisateur WHERE usr_login = 'coswald' AND usr_mdpmd5 = md5('WrongPassword'||usr_salt);

--Question 5

INSERT INTO Logement (log_adresse, log_cp, log_ville, log_pays, log_surface, usr_id)
VALUES
    ('150 London Wall', 'EC2Y5HN', 'LONDON', 'United Kingdom', 52, (SELECT usr_id FROM Utilisateur WHERE usr_prenom = 'Graham')),
    ('Cromwell Rd, South Kensington', 'SW15BD', 'London', 'United Kingdom', 150, (SELECT usr_id FROM Utilisateur WHERE usr_prenom = 'Clara')),
    ('Rue de Rivaldi', '75001', 'Paris', 'France', 35, (SELECT usr_id FROM Utilisateur WHERE usr_prenom = 'Graham')),
    ('19 Rue de Bruxelles', '59000', 'Lille', 'france', 110, (SELECT usr_id FROM Utilisateur WHERE usr_prenom = 'Ryan'));



--/////////Partie 2 ///////////////////////////


--Question a

CREATE FUNCTION genereLogin(user_nom VARCHAR(20), user_prenom VARCHAR(20)) RETURNS varchar(21)
AS $$
    
     Select (substring(user_prenom, 0, 1) || LOWER(user_nom))AS user_login;
    
    
result user_login;
$$ LANGUAGE SQL;


--Question b

CREATE FUNCTION logementsDispo(pays varchar(150), dateDebut date, dateFin date) RETURNS TABLE(log_id int, log_adresse varchar, log_cp varchar, log_ville varchar, log_pays varchar, pp_prix_nuit int, pp_dateDebut date, pp_dateFin date)
AS $$
    select Logement.log_id, log_adresse, log_cp, log_ville, log_pays, pp_prix_nuit, pp_dateDebut, pp_dateFin
    from Logement
    inner join PeriodePossible
    on Logement.log_id = PeriodePossible.log_id
    AND PeriodePossible.pp_dateDebut <= dateDebut
    AND PeriodePossible.pp_dateFin >= dateFin
    AND Logement.log_pays = pays;
$$ LANGUAGE SQL;

-- Question c

-- Question d



