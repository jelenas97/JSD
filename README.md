# JSD za kreiranje HTML stranica
Jezik bi kreirao HTML stranice koje bi kasnije mogle da se koriste u web projektu ili za vizuelizaciju dizajn ideja. Pored osnovnih HTML elemenata kao što su tagovi, koristili bi se i  inline stilovi kao i razne prečice za generisanje često korišćenih složenijih struktura. 

## Generisanje
Struktura JSD bi se ugledala na strukturu YAML-a. Kao izvori podataka mogu se direktno navesti neki fajlovi poput CSV-a za tabele ili tekstualni fajlovi za paragrafe. U nastavku je dat primer jezika i njegove sintakse.
~~~
html:
	head:
		title(color: red, size: 12): TITLE_TEXT
	body:
		- titlebar : TITLE_TEXT
		- div(align: center):
			- p: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ultrices."
			- p(source: "path/to/file.txt")
			- table:
				header(columns: 4): asdf||qwer||1234||uiop
				rows:
					- data1||data2||data3||data4
			- table(csv: "path/to/file.csv")
		- footer(color: green, borders: black):
			- table:
				header(columns: 4): asdf||qwer||1234||uiop
				rows:
					- data1||data2||data3||data4
		
~~~
