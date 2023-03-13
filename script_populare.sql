insert into roluri(denumire_rol) values ('Presedinte');
insert into roluri(denumire_rol) values ('Vicepresedinte');
insert into roluri(denumire_rol) values ('Secretar General');
insert into roluri(denumire_rol) values ('Voluntar');
insert into roluri(denumire_rol) values ('Voluntar 2');

select * from roluri;

insert into departamente(nume_departament) values ('Resurse Umane');
insert into departamente(nume_departament) values ('Multimedia');
insert into departamente(nume_departament) values ('Relatii Externe');
insert into departamente(nume_departament) values ('IT');
insert into departamente(nume_departament) values ('PR');
insert into departamente(nume_departament) values ('PR12');

select * from departamente;

-- presedinte
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Cat Ovidiu', '14-MAR-2021', (select id_rol from roluri where denumire_rol = 'Presedinte'), NULL); 
-- vicepresedinte
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Must Denisa', '14-MAR-2021', 20, NULL); 
-- secretar general
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Apo Roxana', '14-MAR-2021', 30, NULL); 

-- voluntari
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Ioan Andrei', '19-FEB-2021', 40, 40);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Popa Andrei','19-FEB-2020', 40, 10);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Popa Dragos', '13-JAN-2021', 40, 10);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Alex Andrei', '16-FEB-2021', 40, 20);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Androne Sebastian', '26-FEB-2021', 40, 30);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Chiriac Iulia', '16-FEB-2020', 40, 30);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Cristian Andrei', '16-FEB-2020', 40, 50);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Costache Ionut', '16-FEB-2022', 40, 50);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Vieru Tudor', '19-FEB-2021', 40, 30);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Anton Ioana', '19-FEB-2021', 40, 20);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Avram Oana', '19-FEB-2021', 50, 20);
insert into voluntari(nume, data_aderare, id_rol, id_departament) 
values ('Enescu Cristina22', '19-FEB-2021', 40, 20);

select * from voluntari;

select * from voluntari
where id_departament = 10;

select * from voluntari
where id_rol = 40;

--Detalii voluntari
insert into Detalii_Vol values(100, '+40742309898', 'ovidiu.cat@lsaciasi.com', '04-Sep-2001'); 
insert into Detalii_Vol values(101, '+40742309825', 'denisa.must@lsaciasi.com', '01-Jul-2001'); 
insert into Detalii_Vol values(102, '+40742357898', 'roxana.apo@lsaciasi.com', '14-May-2001'); 
insert into Detalii_Vol values(103, '+40745709898', 'andrei.ioan@lsaciasi.com', '26-Sep-2001'); 
insert into Detalii_Vol values(104, '+407457067898', 'andrei.popa@lsaciasi.com', '26-MAR-2001'); 
insert into Detalii_Vol values(104, '+40745706898', 'andrei.popa@lsaciasi.com', '26-MAR-2001'); 
insert into Detalii_Vol values(105, '+40742303298', 'dragos.popa@lsaciasi.com', '01-Aug-2000'); 
insert into Detalii_Vol values(106, '+40742302991', 'andrei.alex@lsaciasi.com', '04-Sep-2002'); 
insert into Detalii_Vol values(107, '+40747509898', 'sebastian.androne@lsaciasi.com', '02-Oct-2002'); 
insert into Detalii_Vol values(108, '+40763543698', 'iulia.chiriac@lsaciasi.com', '08-FEB-2000'); 
insert into Detalii_Vol values(109, '+40743469898', 'andrei.cristian@lsaciasi.com', '05-NOV-2002'); 
insert into Detalii_Vol values(110, '0712853412', 'ionu5.costache@lsaciasi.com', '04-Sep-2001'); 
insert into Detalii_Vol values(111, '+42321489898', 'tudor.vieru@lsaciasi.com', '15-JUN-1999'); 
insert into Detalii_Vol values(112, '+40742893498', 'ioana.anton@lsaciasi', '08-APR-2001'); 
insert into Detalii_Vol values(112, '+40742893498', 'ioana.anton@lsaciasi.com', '08-APR-2001'); 

select * from detalii_vol;

--Evenimente
insert into evenimente(nume_event, data_start, data_stop, locatie_event, buget_event)
    values('IT Marathon', SYSDATE, SYSDATE, 'Iasi', 10000);
insert into evenimente(nume_event, data_start, data_stop, locatie_event, buget_event)
    values('DevMe', '08-JUL-2023', '16-JUL-2023', 'CAMPUS TUIASI', 20000);
insert into evenimente(nume_event, data_start, data_stop, locatie_event, buget_event)
    values('LSAC INTERNSHIP MONTH', '01-NOV-2023', '30-NOV-2023', 'online', 4000);
insert into evenimente(nume_event, data_start, data_stop, locatie_event, buget_event)
    values('LAN Party', '12-MAR-2023', '13-MAR-2023', 'online', 3000);
insert into evenimente(nume_event, data_start, data_stop, locatie_event, buget_event)
    values('Cyber Security', '21-NOV-2023', '21-NOV-2023', 'Sediu LSAC, Iasi', 2000);
insert into evenimente(nume_event, data_start, data_stop, locatie_event, buget_event)
    values('Cyber Security', '21-NOV-2023', '20-NOV-2023', 'Sediu LSAC, Iasi', 2000);
	
select * from evenimente;

--Parteneri
insert into parteneri(nume_partener) values('Continental');
insert into parteneri(nume_partener) values('Allied Testing');
insert into parteneri(nume_partener) values('Vitesco');
insert into parteneri(nume_partener) values('CGM');
insert into parteneri(nume_partener) values('Amazon');
insert into parteneri(nume_partener) values('Amazon2');

select * from parteneri;

--inserare in table parteneri_evenimente
insert into parteneri_evenimente values(10, 10);
insert into parteneri_evenimente values(10, 12);
insert into parteneri_evenimente values(11, 10);
insert into parteneri_evenimente values(11, 11);
insert into parteneri_evenimente values(11, 14);
insert into parteneri_evenimente values(12, 13);
insert into parteneri_evenimente values(13, 11);
insert into parteneri_evenimente values(14, 12);
insert into parteneri_evenimente values(14, 10);
insert into parteneri_evenimente values(12, 11);
insert into parteneri_evenimente values(12, 11);

select * from parteneri_evenimente;

--alumnizare

/* ALUMNIZARE SECRETAR GENERAL CU ID = 102 */
insert into voluntari_alumni values(
    102,
    (select nume from voluntari where id_voluntar = 102),
    (select data_aderare from voluntari where id_voluntar = 102),
    SYSDATE,
    (select id_rol from voluntari where id_voluntar = 102),
    (select numar_telefon from detalii_vol where id_voluntar = 102),
    (select email from detalii_vol where id_voluntar = 102),
    (select data_nastere from detalii_vol where id_voluntar = 102)
);


delete detalii_vol
where id_voluntar = 102;
delete voluntari
where id_voluntar = 102;
/

select * from voluntari_alumni;