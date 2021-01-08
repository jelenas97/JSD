# JSD za brzo generisanje "kostura" web aplikacije
Jezik bi kreirao kostur web aplikacije koja se zasniva na spring boot-u i jsp stranicama.

## Generisanje
Struktura JSD bi se ugledala na strukturu YAML-a. Kao izvori podataka mogu se direktno navesti neki fajlovi poput CSV-a za tabele ili tekstualni fajlovi za paragrafe. U nastavku je opisana ideja i dat je primer jezika sa njegovom sintakse.


## Ideja

Upotrebom kljucne reci entity formiraju se jpa entiteti, odgovarajuci repozitorijumi i crud operacije unutar serivsa.

Stranice se mogu formirati na osnovu entiteta, csv fajlova ili tekstualnih fajlova. 
Ako se kao content type u okviru stranice nadje csv fajl, na osnovu njega i njegovog headera kreiramo entitet. Naziv entiteta ce biti preuzet od samog naziva csv fajla. Sadrzaj csv fajla ce se iskoristiti za formiranje sql skripte koju korisnik moze da iskoristi za insertovanje podatka iz csv fajla u bazu. 

Ukoliko je vrednost content type-a entity, atribut source ce predstavljati entitet na koji "mapiramo" stranicu.



~~~		

entity ClassName1:
	property1 : type1
	property2 : type2
		

entity ClassName2:
	property1 : [ClassName1]
	property2 : type1


page PageName1: 
	navbar(name : "Navbar1 name")
		- linkName1 : "link1"
		- linkName2 : "link2"
	content(type : csv, source : "path/to/file.csv")	//Moze biti csv, entity ili txt
	
	
page PageName2: 
	content(type : entity, source : "ClassName1")
			
~~~
