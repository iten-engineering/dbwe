/* ========================================================================= */
/* Datenbanken und SQL - Kapitel 4.1 und 4.2 Daten verknüpfen                */
/* ========================================================================= */

use course;

/* ------------------------------------------------------------------------- */
/* FOREIGN KEY */
/* ------------------------------------------------------------------------- */

/* Anlegen der Tabelle Pruefung mit Fremdschlüsselspalten */
CREATE TABLE pruefung (
  teilnehmer    INTEGER NOT NULL,
  pruefungsfach INTEGER NOT NULL,
  note          DECIMAL(2,1) NOT NULL,
  pruefung_am   DATE NOT NULL,
  FOREIGN KEY (teilnehmer) REFERENCES student(student_id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (pruefungsfach) REFERENCES fach(fach_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

/* Einfügen von zwei Zeilen */
INSERT INTO pruefung 
  (teilnehmer, pruefungsfach, pruefung_am, note)
VALUES
  (1,1,'2021-09-27', 4.5),
  (5,1,'2021-09-27', 4.0)
;

/* Überprüfung */
SELECT * FROM pruefung;

/* Einfügen einer Zeile mit ungültigem Fach */
INSERT INTO pruefung
  (teilnehmer, pruefungsfach, pruefung_am, note)
VALUES
  (1,7777, '2021-09-27', 4.5)
;

/* Versuch, die Studentin mit der id 1 zu löschen */
DELETE from student WHERE student_id = 1;

/* Ändern einer Fach-ID von 1 auf 9 */
UPDATE fach SET fach_id = 9 WHERE fach_id = 1;

/* Prüfung, ob ON UPDATE CASCADE funktioniert hat */
SELECT * FROM pruefung;

/* Kap  4.3.1 SELECT mit JOIN */
SELECT student.vorname, 
       student.name, 
       pruefung.pruefung_am, 
       fach.name,
       pruefung.note
FROM   pruefung 
       JOIN student ON pruefung.teilnehmer = student.student_id
       JOIN fach ON pruefung.pruefungsfach = fach.fach_id;
     

/* ========================================================================= */
/* The end. */
