# JSD za brzo generisanje "kostura" web aplikacije
Jezik bi kreirao kostur web aplikacije koja se zasniva na spring boot-u i jsp stranicama.

## Ideja

Struktura JSD bi se ugledala na strukturu YAML-a.

Upotrebom ključne reči `entity` formiraju se JPA entiteti i odgovarajući repozitorijumi.

Funkcije kontrolera i servisa mogu se specificirati u sekciji `operations` u okviru `entity`. A polja entiteta se specificiraju u `properties` sekciji. Ukoliko su neka polja ili operacije sadržane u više entiteta mogu se smestiti u odgovarajućoj sekciji `shared`.

Stranice se mogu formirati na osnovu entiteta i ključnih reči funkcije stranica u okviru sekcije `pages`.


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
		updateValidity(id : long) bool
		addMedication(medication : Medication) bool
		removeMedication(id : long) bool

entity Patient:
	properties:
		{Column}
		name > string

		{OneToOne}
		prescription > Prescription

shared[Medication, Prescription, Patient]:
  	properties:
		{Id}
		id > long
  
  	operations:
		getById
		getAll
		save
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
- entity : ključna reč za klase modela
- properties : ključna reč za atribute
- operations : funkcije koje se nalaze unutar kontrolera i servisa za određene entitete
- shared : sekcija gde se navode zajednički atributi i operacije koje poseduju određeni entiteti
- pages : sekcija gde se navode vrste stranica koje će se generisati za određene entitete

Atributi mogu biti sledećeg tipa:
- `long`
- `int`
- `string`
- `bool`
- `date`

Moguće vrednosti anotacija nad atributima su:
- `Column`
- `ManyToMany`
- `OneToMany`
- `OneToOne`
- `Id`

Moguće vrednosti za tipove stranica:
- add
- edit
- view
- viewDelete

# Pokretanje

Instalirati sve dependency-je navedene u `requirements.txt` pokretanjem komande:

```bash
pipenv install
```

```bash
```
