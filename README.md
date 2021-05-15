# JSD za brzo generisanje "kostura" web aplikacije
Jezik bi kreirao kostur web aplikacije koja se zasniva na spring boot-u i jsp stranicama.

## Generisanje
Struktura JSD bi se ugledala na strukturu YAML-a. Kao izvori podataka mogu se direktno navesti neki fajlovi poput CSV-a za tabele ili tekstualni fajlovi za paragrafe. U nastavku je opisana ideja i dat je primer jezika sa njegovom sintaksom.

## Ideja

Upotrebom kljucne reci `entity` formiraju se JPA entiteti i odgovarajuci repozitorijumi.

Funkcije kontrolera i servisa mogu se specificirati u sekciji `operations` u okviru `entity`. A polja entiteta se specificiraju u `properties` sekciji. Ukoliko su neka polja, ili operacije sadržane u više entiteta, mogu se smestiti u odgovarajućoj sekciji `shared`.

Stranice se mogu formirati na osnovu entiteta i ključnih reči funkcije stranica.


## Primer

~~~		

entity Medication:
	properties:
    {Column}
		name > string

entity Prescription:
	properties:
    {Column}
		prescribedAt > date

    {Column}
    valid > bool

    {ManyToMany}
		medications > [Medication]
	
  operations:
    updateValidity > id : long < bool
    addMedication > medication : Medication < bool
    removeMedication > id : long < bool

entity Patient:
	properties:
    {Column}
		name > string

    {OneToOne}
    prescription -> Prescription

shared[Medication, Prescription, Patient]:
  properties:
    {ID}
		id : long
  
  operations:
    getById
    getAll
    create
    update
    delete

pages[Medication, Prescription]:
  view
  add
  edit

pages[Patient]:
  viewDelete
  add
			
~~~


### Elementi jezika


