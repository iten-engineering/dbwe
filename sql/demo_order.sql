create TABLE article (
	nr VARCHAR(255)	PRIMARY KEY, 
	description VARCHAR(255) NOT NULL,
	quantity INTEGER NOT NULL,
    creation_ts TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    update_ts   TIMESTAMP    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)

insert into article (nr, description, quantity) values ('HP-5712', 'HP Laptop', 100);
insert into article (nr, description, quantity) values ('PM-4711', 'Logitec Mouse', 5000);
insert into article (nr, description, quantity) values ('PT-1122', 'Cherry CH Tastatur', 1500);

select * from article;


CREATE TABLE  `order` (
	id          INTEGER      PRIMARY KEY AUTO_INCREMENT,
	customer    VARCHAR(255) NOT NULL,
    creation_ts TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    update_ts   TIMESTAMP    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

insert into `order` (customer) values ('Peter Meier');
insert into `order` (customer) values ('Anna Keller');
insert into `order` (customer) values ('Natascha Müller');

select * from `order`;
update `order` set customer = "Mia Tschanz" where id = 1;
select * from `order`;


CREATE TABLE order_item (
	id	     	INTEGER PRIMARY KEY AUTO_INCREMENT,
	quantity 	INTEGER NOT NULL,
	article_nr	VARCHAR(255) NOT NULL,
	order_id    INTEGER NOT NULL,
	FOREIGN KEY (article_nr) REFERENCES article(nr) 
		ON DELETE RESTRICT 
		ON UPDATE CASCADE,
	FOREIGN KEY (order_id) REFERENCES `order`(id) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE
);

insert into order_item (quantity, article_nr, order_id) values (1, 'HP-5712', 1);
insert into order_item (quantity, article_nr, order_id) values (1, 'PM-4711', 1);
insert into order_item (quantity, article_nr, order_id) values (1, 'PT-1122', 1);
insert into order_item (quantity, article_nr, order_id) values (2, 'HP-5712', 2);
insert into order_item (quantity, article_nr, order_id) values (2, 'PM-4711', 2);
insert into order_item (quantity, article_nr, order_id) values (2, 'PT-1122', 2);

select * from order_item;

DELETE from `order` WHERE id = 1;
DELETE from article WHERE nr = 'PT-1122'

insert into article (nr, description, quantity) values ('PT-3344', 'Cherry US Tastatur', 1500);
DELETE from article WHERE nr = 'PT-3344'

select * from article;

