# JSD za brzo generisanje "kostura" web aplikacije
Jezik bi kreirao kostur web aplikacije koja se zasniva na spring boot-u i jsp stranicama.

## Generisanje
Struktura JSD bi se ugledala na strukturu YAML-a. Kao izvori podataka mogu se direktno navesti neki fajlovi poput CSV-a za tabele ili tekstualni fajlovi za paragrafe. U nastavku je opisana ideja i dat je primer jezika sa njegovom sintaksom.


## Ideja

Upotrebom kljucne reci entity formiraju se jpa entiteti, odgovarajuci repozitorijumi i crud operacije unutar servisa.

Stranice se mogu formirati na osnovu entiteta, csv fajlova ili tekstualnih fajlova. 
Ako se kao content type u okviru stranice nadje csv fajl, na osnovu njega i njegovog headera kreiramo entitet. Naziv entiteta ce biti preuzet od samog naziva csv fajla. Sadrzaj csv fajla ce se iskoristiti za formiranje sql skripte koju korisnik moze da iskoristi za insertovanje podatka iz csv fajla u bazu. 

Ukoliko je vrednost content type-a entity, atribut source ce predstavljati entitet na koji "mapiramo" stranicu.

Ukoliko je vrednost content type-a txt, atribut source predstavlja txt fajl iz kog se preuzima tekst koji ce biti nalepljen kao tekstualni sadrzaj u okviru odgovarajuce stranice.


~~~		

entity ClassName1:
	properties:
		property1 : type1 {id}
		property2 : type2 {column}
	operations:
		(cr)       //kada zelimo samo create i read operacije, mogucnost i update i delete operacija
			   //kreiraju se metode u servisu, kontroleru i repozitorijumu

entity ClassName2:
	properties:
		property1 : type1 {id} 
		property2 : (ClassName1) {column}	//tip property-ja je jedan objekat
		property3 : [ClassName1]		//tip property-ja je lista objekata; dodatno, upotrebom {} moguce definisati anotacije 
	operations:
		(cru)

page PageName1: 
	navbar(name : "Navbar1 name")
		- linkName1 : "link1"
		- linkName2 : "link2"
	content(type : csv, source : "path/to/file.csv")	//Moze biti csv, entity ili txt
	
	
page PageName2: 
	content(type : entity, source : "ClassName1")
	
page PageName3: 
	content(type : txt, source : "path/to/file.txt")	
			
~~~


### Napomena

Traziti sugestiju za definisanje crud operacija.
Oznacavanje liste objekata i singl objekata.
