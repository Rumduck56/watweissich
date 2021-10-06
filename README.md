# watweissich
Bei 'kennwort' und 'passwort' musste natürlich deine Zugangsdaten einsetzen

So bekomme ich also meine Tipps (in diesem Fall für den 7.Spieltag) ausgegeben...und wenn ich die TeilnehmerId=24378486 entsprechend ändere (ist ja anhand des Links
auf der Webseite auszulesen), könnte ich auch deine Tipps, etc. auszulesen..schon klar.

Aber 

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

funktioniert nicht, da zwar Daten ausgegeben werden, aber nicht alle (wenn ich zum Beispiel eingeloggt bin und dann auf 'inspect" gehe, mir also den Quellcode ansehe)

Liegt das daran, dass ich über requests.get(url) dann nicht eingeloggt bin...?
