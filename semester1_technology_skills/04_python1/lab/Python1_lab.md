# Lab Challenge 4

> Arbeiten Sie alleine an den Challenges. Sie können sich mit ihrem Coach oder anderen Studierenden austauschen, aber arbeiten Sie nicht zusammen mit anderen Studierenden an einer Challenge und geben Sie auch nicht denselben Code ab.

## Was es zu tun gibt

1. **Replit konfigurieren** (einmalig für alle Challenges)
1. Programmieren Sie **Hello**
1. Progammieren Sie **Mario**
1. Programmieren Sie **Cash** (optional)

## Replit konfigurieren

Führen Sie die folgenden Schritte einmalig durch, um die browserbasierte IDE replit einzurichten:

1. Registrieren Sie sich mit Ihrer studentischen E-Mail-Adresse bei https://replit.com/
2. Registrieren Sie sich Ihrer studentischen E-Mail-Adresse bei https://github.com/
3. Öffnen Sie https://replit.com/ und klicken Sie auf das **+**-Symbol oben rechts auf der Webseite
4. Klicken Sie in dem Fenster, das jetzt erschienen ist auf "Import from Github" 
5. Kopieren Sie den folgenden Link in das Eingabefeld unter "GitHub URL": https://github.com/ndhbr-classroom/replit-template
6. Klicken Sie auf den Schieberegler neben dem Text "Repli is public", um ihr repl vor unbefugtem Zugriff zu schützen
7. Klicken Sie auf "+ Import from Github"
8. Klicken Sie den Button "Run", um ihr replit zu konfigurieren
9. Um die Labs herunterzuladen, müssen Sie Ihr repl mit GitHub authentifizieren: Klicken Sie auf den Tab "Console" und tippen dort den Befehl ```github```, gefolgt von der Taste Enter ein.
10. Kopieren Sie die Ausgabe des Programms nach dem Doppelpunkt, d.h. ab ```sss-rsa ...``` bis zum Ende der Zeichenkette durch Markieren, Rechtsklick mit der Maus und Wählen von Kopieren aus dem Kontextmenü (alternativ ```Strg+C``` unter Windows und ```Cmd+C``` unter Mac OS)
11. Klicken Sie auf den Link https://github.com/settings/keys und auf der dortigen Seite auf "New SSH Key"
12. Fügen Sie den zuvor kopierten Text in das Feld "Key" ein und vergeben einen "Title" z.B. replit, Klicken Sie anschließend auf "Add SSH key"
13. Wechseln Sie zu replit geben Sie auf der Console hinter "Enter your name: " ihren echten Namen ein und bestätigen Sie die Eingabe mit Enter
14. Geben Sie auf der Console hinter "Enter your email: " ihre studentische Mailadresse ein, mit der Sie sich bei GitHub authentifiziert haben.
15. Die Meldung "GitHub Setup completed" erscheint und die Einrichtung von replit ist abgeschlossen

Replit sollte sich jetzt selbständig konfigurieren und Sie können starten.

Replit ist eine webbasierte IDE, mit der Sie Code schreiben, ausführen und debuggen können. Replit ist in die folgenden drei Bereiche unterteilt:

1. **Files** (auf der linken Seite) - Zeigt Ordner und Dateien an. Klickt man auf eine Datei wird diese im **Texteditor** geöffnet.
2. **Texteditor** (mittig) - Hier schreiben Sie Ihren Code
3. **Console** (auf der rechten Seite) - Hier geben Sie die Befehle zum Ausführen Ihrer Programme und zum wechseln von Ordnern ein.

Tippen Sie in der Console den folgenden Befehl ein, gefolgt von Enter, um einen neuen Ordner zu erstellen:

~~~shell
mkdir hello_world
~~~

Vergessen Sie nicht das Leerzeichen zwischen ```mkdir``` und ```hello_world```. Auf diese Art und Weise (d.h. eine Zeile, gefolgt von der Taste Enter) geben Sie alle Befehle in die Console ein. Alle Befehle sind "case-sensitive", d.h. die Groß- und Kleinschreibung muss genau so sein wie in den Beispielen angegeben.

Geben Sie jetzt den folgenden Befehl ein (wieder gefolgt von Enter), um in den neu erstellten Ordner zu wechseln:

~~~shell
cd hello_world
~~~

Die Console sollte in etwas so aussehen und somit anzeigen, dass Sie den Ordner erfolgreich gewechselt haben:

~~~shell
OTH-Console:~/.../hello_world> 
~~~

Erstellen Sie mit dem folgenden Befehl Ihr erstes Programm:

~~~python
touch hello_world.py	
~~~

Im Bereich Files (auf der linken Seite) können Sie jetzt sehen, dass eine neue leere Datei erstellt wird. Klicken Sie auf diese Datei, um diese im Texteditor zu öffnen.

Tippen Sie auf der Console den folgenden Befehl ein, um sich alle Dateien im Ordner ```hello_world``` anzeigen zu lassen:

~~~shell
ls
~~~

Die Ausgabe sollte wie folgt sein (die Datei ```hello_world.py``` haben Sie zuvor mit ```touch hello_world.py``` angelegt):

~~~shell
ls
hello_world.py
OTH-Console:~/.../hello_world> 
~~~

Erstellen Sie jetzt Ihr erstes Programm: Tippen Sie dazu den folgenden Code in den Texteditor, exakt so, wie hier dargestellt:

~~~python
def main():
  print("hello world!")

main()
~~~

Tippen Sie den folgenden Befehl in der Console, um zu Testen, ob alles wie erwartet funktioniert:

~~~shell
python hello_world.py 
~~~

Ihr Programm sollte die folgende Ausgabe erzeugen:

~~~shell
hello world!
~~~

Glückwunsch! Sie haben replit erfolgreich eingerichtet und ihr erstes Python-Programm geschrieben!

## Hello

### Vorbereitung

Klicken Sie auf den folgenden Link, um die Aufgabe zu beginnen:

https://classroom.github.com/assignment-invitations/3393be936636f2d6916b7a643a2dc599/status

Auf der Seite erscheint ein Link unter dem Text "Your assignment repository has been created" wie der Folgende:

~~~shell
https://github.com/ndhbr-classroom/01-intro-mheckner
~~~

Kopieren Sie den Teil nach ```-classroom``` (hier: ```01-intro-mheckner``` mit Rechtsklick und Kopieren Sie diesen mit Rechtsklick mit der Maus und Wählen von Kopieren aus dem Kontextmenü (alternativ ```Strg+C``` unter Windows und ```Cmd+C``` unter Mac OS). Dieser Teil ist der Name Ihrer Aufgabe (```EXERCISE_NAME```)

Laden Sie sich den Startecode für die Aufgabe mit dem folgenden Befehl auf der Console in replit herunter:

~~~shell
get EXERCISE_NAME
~~~

Achtung: Ersetzen Sie ```EXERCISE_NAME``` durch den Text aus Ihrem Link von oben!

Tippen Sie anschließend den folgenden Befehl ein, um in den soeben erstellten Ordner zu gelangen:

~~~shell
cd ~/replit-template-1/EXERCISE_NAME/
~~~

Der Ordner ```EXERCISE_NAME``` enthält eine Reihe von Ordnern und Dateien - Ignorieren Sie alle Dateien und konzentrieren Sie sich auf die Datei ```hello.py``` - Dort schreiben Sie ihr Programm.

### Specs

Schreiben Sie ein Programm ```hello.py```, das die Nutzer auffordert ihren Namen einzugeben und anschließend ```Hallo soundso```, wobei ```soundso``` der Name ist, den die Nutzer zuvor eingegeben haben:

~~~shell
$ python hello.py 
Wie ist dein Name? Markus
Hallo Markus
~~~

### Testen

Testen Sie Ihr Programm mit den folgenden Eingaben, bevor Sie es abgeben.

* Führen Sie Ihr Programm auf der Kommandozeile wie folgt aus ```python hello.py```, warten Sie bis das Programm zu einer Eingabe auffordert und tippen ```Markus``` gefolgt von der ```Enter```-Taste ein. Das Programm sollte ```Hallo Markus``` ausgeben.
* Führen Sie Ihr Programm auf der Kommandozeile wie folgt aus ```python hello.py```, warten Sie bis das Programm zu einer Eingabe auffordert und tippen ```Ulrike``` gefolgt von der ```Enter```-Taste ein. Das Programm sollte ```Hallo Ulrike``` ausgeben.
* Führen Sie Ihr Programm auf der Kommandozeile wie folgt aus ```python hello.py```, warten Sie bis das Programm zu einer Eingabe auffordert und tippen ```Johannes``` gefolgt von der ```Enter```-Taste ein. Das Programm sollte ```Hallo Johannes``` ausgeben.

Wenn alle manuellen Tests erfolgreich waren, können Sie Ihr Programm auch wie folgt automatisch auf der Console testen:

~~~shell 
test EXERCISE_NAME
~~~

Tipp: Der ```EXERCISE_NAME``` beginnt mit ```01-intro-``` und endet mit Ihrem GitHub Usernamen.

TODO: Wie kann man das besser erklären?!

### Abgabe

Geben Sie Ihr Programm mit dem folgenden Befehl auf der Console ab:

~~~shell
submit EXERCISE_NAME
~~~

Hinweis: Sie können den obigen Befehl so oft ausführen wie Sie wollen. Bewertet wird immer der mit dem letzten Befehl hochgeladene Code.

## Mario

### Vorbereitung

TODO - Anpassen von Hello

### Specs

Am Ende eines Levels in Super Mario Brothers, muss Mario über einen Pyramide wie die Folgende springen:

![04_lab_pyramid](img/04_lab_pyramid.png)

Ihre Aufgabe ist es diese Pyramide in Python nachzubauen, woebei jedes Element der Pyramide aus einem ```#```-Zeichen besteht. Jedes ```#```-Zeichen ist etwas höher als breit, daher ist die daraus bestehende Pyramide auch etwas höher als breit:

~~~
  		 #
      ##
     ###
    ####
   #####
  ######
 #######
########
~~~

Sie schreiben das Programm ```mario.py```. Das Programm soll die Nutzer zunächst nach der Höhe der Pyramide fragen (beispielsweise eine Ganzzahl zwischen 1 und 8 (beide inklusive)).

Das Programm soll wie folgt funktionieren, wenn die Nutzer ```8``` eingeben, nachdem sie dazu aufgefordert wurden:

~~~shell
$ python mario.py
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
~~~

Wenn die Nutzer ```4``` eingeben, nachdem sie dazu aufgefordert wurden soll das Programm wie folgt funktionieren:

```shell
$ python mario
Height: 4
   #
  ##
 ###
####
```

Und wie folgt bei einer Eingabe von ```2```:

~~~shell
$ ./mario
Height: 2
 #
##
~~~

Und bei einer Eingabe von ```1``` wie folgt:

~~~shell
$ ./mario
Height: 1
#
~~~

Falls die Nutzer keine gültige Zahl zwischen 1 und 8 eingeben, soll das Programm die Nutzer immer weiter zur Eingabe einer Zahl auffordern, bis eine korrekte Zahl eingegeben wird:

~~~shell
$ python mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
####
~~~

Wie beginnt man diese Aufgabe am Besten? Versuchen Sie das Problem Schritt für Schritt anzugehen.

### Schritt für Schritt

#### Pseudocode

Erstellen Sie sich zuerst mit dem folgenden Befehl eine Datei ```pseudocode.txt```:

~~~shell
touch pseudocode.txt
~~~

Öffnen Sie diese Datei im Texteditor von replit. Schreiben Sie in diese Datei einen Pseudocode, d.h. eine Abfolge von Schritten, die das Programm durchführen muss, auch wenn Sie noch nicht genau wissen, wie der exakte Python Code dafür lauten soll. Ein paar knappe Sätze reichen. In den Slides zur ersten Python-Sitzung finden Sie ein Beispiel für Pseudocode. Ihr Pseucode wird wahrscheinlich Funktionen, Schleifen und Verzweigungen enthalten.

Spoiler - Lesen Sie nicht weiter, wenn Sie den Pseudocode selbst schreiben wollen!

Es gibt viele Varianten den Pseudocode zu schreiben, die ist nur eine Variante:

~~~
1 User nach Höhe fragen
2 Wenn Höhe weniger als 1 oder mehr als 8 (oder garkeine Ganzzahl ist) wieder bei 1 anfangen
3 Iteriere von 1 bis 8 und
	Gebe in Iteration i, i-#-Zeichen aus und anschließend eine neue Zeile
~~~

#### User nach Input fragen

Beginnen Sie damit (egal, wie Ihr Pseudocode aussieht) den Code zu schreiben, der die Nutzer (wiederholt) dazu auffordert eine Höhe einzugeben. Öffnen Sie dazu die Datei ```mario.py``` in replit. 

Passen Sie ```mario.py``` jetzt so an, dass das Programm die Benutzer immer wieder auffordert eine zulässige Zahl zwischen 1 und 8 einzugeben und speichern Sie dieses Ergebnis in einer Variable ab. Geben Sie dann die gespeicherte Höhe wie folgt aus:

~~~shell
$ python mario
Höhe: -1
Höhe: 0
Höhe: 42
Höhe: 50
Höhe: 4
Gespeichert: 4
~~~

Tipps:

* Sie können einen formatierten String mit ```print(f"Höhe: {height}")``` ausgeben, wobei ```height```eine Variable ist.
* Ganzzahlen lassen sich von den Nutzern mit der Funktion ```get_int``` einlesen. Dazu müssen Sie die Funktion aus der Bibliothek ```cs50``` importieren.
* Eine ```while``` Schleife führt Code wiederholt aus

#### Bauen Sie das Gegenteil

Nachdem das Programm die Eingabe der Nutzer akzeptiert, geht es an die Ausgabe der Pyramide. Eine links-ausgerichtete Pyramide lässt sich leichter ausgeben:

~~~shell
#
##
###
####
#####
######
#######
########
~~~

Beginnen Sie mit der links ausgerichteten Pyramide und richten diese erst dann rechts aus.

Tipps:

* Das ```#```-Zeichen ist ein Zeichen wie jeder Buchstabe, das Sie einfach ausgeben können

* Scratch bietet den Block "repeat" - In Python können Sie eine for-Schleife verwenden, um die Pyramide auszugeben. 

* Sie können Variablen auch mit zwei Zählvariablen verschachteln. Beispielsweise gibt das folgende Beispiel ein Rechteck mit der Höhe ```n```  aus ```#```-Zeichen aus (was natürlich nicht ganz das ist, was Sie wollen)

  ~~~shell
  for i in range(n):
    for i in range(n):
        print("#", end="")
    print()
  ~~~

#### Pyramide rechts ausrichten

Richten Sie jetzt die Pyramide dadurch rechts aus, dass Sie die Lücken mit Punkten (```.```) füllen:

~~~shell
.......#
......##
.....###
....####
...#####
..######
.#######
########
~~~

Tipp: Die Anzahl der Punkte ist das "Gegenteil" der Anzahl an ```#```-Zeichen in der jeweiligen Zeile. Für eine Pyramide mit der Höhe 8 hat die erste Zeile 1 ```#```-Zeichen und 7 Punkte. Die Basis der Pyramide hat 8 ```#```-Zeichen und keine Punkte. Mit Welcher Rechnung könnten Sie dieses Ergebnis erzielen?

#### Testen

Testen Sie Ihren Code manuell mit den folgenden Eingaben. Funktioniert das Programm wie erwartet?

* ```-1``` - Oder andere negative Zahlen
* ```0```
* ```1``` bis ```8```
* ```9``` oder andere positive Ganzzahlen
* Buchstaben oder Wörter
* Keine Eingabe, wenn Die Nutzer sofort Enter drücken

#### Punkte entfernen

Passen Sie Ihr Programm am Ende so an, dass anstelle der Punkte Leerzeichen ausgegeben werden.

#### Automatisierte Tests

Wenn alle manuellen Tests erfolgreich waren, können Sie Ihr Programm auch wie folgt automatisch auf der Console testen:

~~~shell 
test EXERCISE_NAME
~~~

Tipp: Der ```EXERCISE_NAME``` beginnt mit ```01-intro-``` und endet mit Ihrem GitHub Usernamen.

TODO: Wie kann man das besser erklären?!

### Abgabe

Geben Sie Ihr Programm mit dem folgenden Befehl auf der Console ab:

~~~shell
submit EXERCISE_NAME
~~~

Hinweis: Sie können den obigen Befehl so oft ausführen wie Sie wollen. Bewertet wird immer der mit dem letzten Befehl hochgeladene Code.

# Cash (optional)

Diese Aufgabe ist optional und bietet Ihnen noch mehr Übungsmöglichkeiten.

### Vorbereitung

TODO - Anpassen von Hello

### Specs

Wenn Sie Wechselgeld an einen Käufer ausgeben, versuchen Sie so wenige Münzen wie möglich zurückzugeben, damit Ihnen die Münzen nicht ausgehen, und um die Kunden nicht zu verärgern. Praktischerweise gibt es in der Informatik einen Ansatz, um dieses Problem zu lösen.

#### Greedy-Algorithmus

Laut Wikipedia (https://de.wikipedia.org/wiki/Greedy-Algorithmus) "zeichnen sich [Greedy-Algorithmen] dadurch aus, dass sie schrittweise den Folgezustand auswählen, der zum Zeitpunkt der Wahl den größten Gewinn bzw. das beste Ergebnis [...] verspricht". 

![04_lab_coins](img/04_lab_coins.jpeg)

Was bedeutet das für das oben geschilderte Problem? Angenommen eine Kassiererin möchte Kunden Wechselgeld geben und in der Schublade der Kassiererin befinden sich alle Euro Münzen: € 2, € 1, 50 Cent, 20 Cent, 10 Cent, 5 Cent, 2 Cent und 1 Cent. Das zu lösende Problem ist, welche Münzen und wie viele von jeder Münze als Wechselgeld ausgehändigt werden muss.

Eine "greedy"-Kassierin will das Problem mit jedem Griff in die Wechselgeldschublade möglichst stark verkleinern. Wenn ein Kunde 76 Cent bekommt, dann wird die Kassiererin erst ein 50 Cent-Stück nehmen, da dies das Problem bei einem Rückgabebetrag von 0 anzukommen maximal verkleinert. Das Problem hat sich dadurch von 76 Cent auf 26 Cent verkleinert, da 76 - 50 = 26. Dieses kleinere Problem kann jetzt auf die selbe Art gelöst werden. Eine 50 Cent Münze kann jetzt offensichtlich nicht mehr zurückgegeben werden, aber 26 - 25 = 1 funktioniert. Bleibt am Ende eine 1 Cent Münze und das Problem ist gelöst wenn auch diese an die Kunden zurückgegeben wurde. Der Kunde erhält demnach insgesamt 3 Münzen (1 x 50 Cent, 1 x 25 Cent und 1 x 1 Cent).

Dieser Algorithmus bietet eine optimale Lösung für das Problem und liefert immer die minimale Anzahl von Münzen zurück.

Implentieren Sie Ihr Programm in der Datei ```cash.py```. Dieses Programm fragt die Nutzer zuerst wie viel Wechselgeld sie bekommen und gibt danach die dazu notwendige Anzahl von Münzen aus:

~~~
$ python cash.py 
Cash: 76
Minimale Anzahl Münzen: 4
~~~

* Verwenden Sie ```get_int``` um den Betrag des Wechselgelds von den Nutzern einzulesen. Lesen Sie den Betrag in Cent ein, d.h. ein Wechselgeld von € 4,31 entspricht einer Eingabe von 431.
* Geben Sie das Ergebnis mit ```print``` aus.
* Lagern Sie die Berechnung der zurückzugebenden Münzen in eine Funktion ```get_coins``` aus, welche die Anzahl dieser Münzen als Ergebnis zurückgibt. In den Notes finden Sie Beispiele für solche Funktionen.
* Fordern Sie die Nutzer erneut zu einer Eingabe auf, falls diese eine negative Zahl eingeben.

### Testen

Testen Sie, ob Ihr Code wie erwartet für die folgenden Eingaben funktioniert:

* ```-1``` oder anderen negativen Eingaben
* ```0```?
* ```1``` oder anderen positiven Eingaben
* keine Eingabe, wenn die Nutzer direkt Enter drücken

Wenn alle manuellen Tests erfolgreich waren, können Sie Ihr Programm auch wie folgt automatisch auf der Console testen:

~~~shell 
test EXERCISE_NAME
~~~

Tipp: Der ```EXERCISE_NAME``` beginnt mit ```01-intro-``` und endet mit Ihrem GitHub Usernamen.

TODO: Wie kann man das besser erklären?!

### Abgabe

Geben Sie Ihr Programm mit dem folgenden Befehl auf der Console ab:

~~~shell
submit EXERCISE_NAME
~~~

Hinweis: Sie können den obigen Befehl so oft ausführen wie Sie wollen. Bewertet wird immer der mit dem letzten Befehl hochgeladene Code.
