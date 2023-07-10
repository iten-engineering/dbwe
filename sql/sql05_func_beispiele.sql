/* ========================================================================= */
/* Datenbanken und SQL - Kapitel 5 Funktionen und Gruppierung                */
/* ========================================================================= */

use beispiele;

/* ------------------------------------------------------------------------- */
/* Aggregatfunktionen */
/* ------------------------------------------------------------------------- */

select count(*) from student;

select avg(note), min(note), max(note) from pruefung;

/* Wie ist der Notendurchschnitt der Prüfungen im Fach Systems Engineering 
 * für die Klasse HFWI.BE.H22? */

select avg(note)
FROM pruefung p JOIN student s ON p.student = s.student_id
JOIN klasse k ON s.klasse = k.klasse_id
JOIN fach f ON p.fach = f.fach_id
WHERE k.bezeichnung = 'HFWI.BE.H22' AND f.titel = 'Systems Engineering';


/* ------------------------------------------------------------------------- */
/* Gruppierung */
/* ------------------------------------------------------------------------- */

SELECT k.bezeichnung Klasse, count(*) Anzahl
FROM klasse k JOIN student s ON s.klasse = k.klasse_id
WHERE k.semester = 5
GROUP BY k.bezeichnung;


SELECT k.bezeichnung Klasse, count(*) Anzahl
FROM klasse k JOIN student s ON s.klasse = k.klasse_id
WHERE k.semester = 5
GROUP BY k.bezeichnung
HAVING k.bezeichnung LIKE 'HFSNT%'
ORDER BY count(*);

/* ------------------------------------------------------------------------- */
/* Funktionen */
/* ------------------------------------------------------------------------- */

SELECT ROUND(3.3567, 2);

SELECT CEIL(25.2)

SELECT FLOOR(25.2);

SELECT CURDATE();

SELECT DATE_FORMAT('2021-11-18', '%d.%m.%y');

SELECT DATE_FORMAT('2021-11-18', '%d.%m.%Y');

SELECT DATE_ADD("2017-06-15", INTERVAL 10 DAY);

SELECT CONCAT( 'Die Klasse heisst ', bezeichnung ) FROM klasse;

SELECT DATE_FORMAT(CURDATE(), '%d.%m.%y');

SELECT ROUND(AVG(note), 1) from pruefung;

/* ========================================================================= */
/* The end. */
