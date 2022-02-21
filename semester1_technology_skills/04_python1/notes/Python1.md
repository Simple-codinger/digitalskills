> Alle Codebeispiele für diese Challenge sind auf replit.com abrufbar:
> https://replit.com/@mheckner/Digital-Skills04Python

# Python

In dieser Challenge wird eine neue Programmiersprache (**Python**) vorgestellt. Python verfügt über alle Features von Sratch (und mehr) ist aber etwas weniger nutzerfreundlich, da der gesamte Code als Text geschrieben wird. Ziel dieses Semesters ist nicht, dass sie eine spezifische Programmiersprache beherrschen, sondern lernen, *wie* man programmiert. Am Ende ist nicht die Programmiersprache entscheidend sondern das grundlegende Verständnis wie man Programme schreibt. Die Syntax eine Programmiersprache mag am Anfang verwirrend erscheinen und man versteht, besonders zu Beginn, nicht   welche Bedeutung alle Elemente des Programmcodes haben. Aber je mehr Übung man beim Programmieren hat, desto leichter fällt das Verständnis und das Schreiben von eigenem Code.

In Scratch wurden u.a. die folgenden Elemente einer Programmiersprache vorgestellt:

*  Funktionen (mit Parametern und Rückgabewerten)
* Verzweigungen
* Boolsche Ausdrücke
* Schleifen
* Variablen
* ...

Diese Konzepte werden in der heutigen Challenge in die Programmiersprache Python übertragen. Python verfügt über eine eigene Syntax, ist präziser als Scratch und beinhaltet ein Vokabular, das man als Programmierer erlernen muss (aber mit sehr viel weniger Wörtern als eine menschliche Sprache!).

Zu Beginn versteht man nicht alle Details und blendet die Details aus. Erst nach und nach versteht man den gesamten Code. Dieses Prinzip, bestimmte Dinge auszublenden und sich auf deren Funktion zu verlassen, auch wenn man nicht weiß wie diese funktionieren, wird auch als **Abstraktion** bezeichnet.

Die Qualität von Quellcode lässt sich anhand der folgenden Aspekte bewerten:

* **Korrektheit**, d.h. ob der Code die korrekte Lösung für ein Problem liefert
* **Design**, d.h. wie gut lesbar der Code ist und wie effizient er das Problem löst.
* **Stil**, d.h. ob der Code visuell ansprechend formatiert ist (d.h. Abstände, Einrückungen, etc.)

Unser erstes Python gibt einfach nur "hello world" auf der Shell in replit aus. Der Code dafür ist knapp und sieht wie folgt aus:

~~~python
print("Hello world!")
~~~

# Integrated Development Environments (IDEs), Kommandozeile und Interpreter

Das obige Programm ist für den Menschen lesbar, aber nicht direkt für den Computer ausführbar. Um das obige Programm auszuführen muss dieser Code in ein Format überführt werden, das der Computer versteht. Diese Übersetzung in die Sprache des Computers erfolgt in Python über einen **Python-Interpreter**.

**Integrated Development Environment (IDEs)** sind Werkzeuge für Entwickler, die Entwickler dabei unterstützen Code zu schreiben, in die Sprache des Computers zu übersetzen und auszuführen.

In diesem Kurs verwenden wir die IDE replit.com, die u.a. einen Dateiexplorer und einen Texteditor bietet, in dem sich der Code ausführen lässt.

![04_replit_editor](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_replit_editor.png)

Auf der linken Seite befindet sich ein Dateiexplorer in dem sich (wie unter Windows) neue Ordner und Dateien anlegen lassen und Dateien kopieren lassen. Aktuell ist die Datei ```hello.py``` ausgewählt und im Texteditor rechts daneben geöffnet. Dort kann die Datei bearbeitet, erweitert und gespeichert werden. Der Code im Texteditor kann von Menschen gelesen werden, wird aber nicht direkt vom Computer verstanden und muss erst in die Sprache des Computers übersetzt werden, bevor er ausgeführt werden kann. Diese Übersetzung und anschließende Ausführung erfolgt in Python mit einem einzigen Befehl.

Dieser und andere Befehle lassen sich in replit (und auch auf allen anderen Computern) durch Eintippen in eine Shell auführen. Die folgende Abbildung zeigt die Shell in replit:

![04_shell](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_shell.png)

Sowohl IDE als auch eine Shell sind im Prinzip auf jedem Computer installierbar (IDE) bzw. bereits verfügbar (Shell). Um dieses Setup nicht selbst durchführen zu müssen, bündelt replit beide Komponenten in einer jederzeit verfügbaren (sofern natürlich eine Internetverbindung besteht) browserbasierten Anwendung, die immer unabhängig vom eigenen Rechner funktioniert. Replit bietet also einen **virtuellen Rechner in der Cloud** und alle Kommandos, die in den Browser getippt werden, werden an diesen Rechner geschickt und dort ausgeführt.

Die Shell bietet eine **Komandozeile** die Zugrifff auf das Betriebssystem Linux bietet, das jedem virtullen Rechner in replit zugrundeliegt.

Die folgende Zeile bedeutet, dass der aktuelle Ordner in der Kommandozeile "geöffnet" ist und die Kommandozeile auf Eingaben wartet:

```shell
~/Digital-Skills04Python$ 
```

Auch wenn der Dateiexplorer dies nicht anzeigt, ist dies der selbe Ordner, in dem auch die Datei ```hello.py``` liegt. Um die Datei ```hello.py``` in Maschinencode zu übersetzen, muss man auf der Kommandozeile den Befehl ```python3 hello.py``` eingeben:

![04_python3_hello](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_python3_hello.png)

Der obige Befehl übersetzt also das Programm ```hello.py``` führt es aus und gibt die Kommandozeile danach wieder frei (symbolisiert durch den Ordnernamen in blau und das weiße Rechteck am Ende der Zeile).

Mithilfe der Kommandozeile lässt sich mit dem Befehl ```ls``` anzeigen, welche Dateien sich im aktuellen Ordner befinden:

![04_ls](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_ls.png)

Um Dateien in replit zu löschen klickt man im Dateiexplorer auf die drei vertikalen Punkte (oder klickt mit der rechten Maustaste und wählt dort Delete). Alternativ lässt sich eine Datei aber auch auf der Shell mit dem Befehl ```rm``` löschen:

```shell 
rm hello.py
```

Nach Eintippen des Kommandos (und Bestätigung mit der Enter Taste) wird die Datei gelöscht und verschwindet aus dem Datei-Explorer.

# Funktionen, Parameter, Rückgabewerte (return) und Variablen

In der letzten Challenge zu Scratch wurden Funktionen und Parameter (= Eingaben) zu diesen Funktionen vorgestellt, die beeinflußen, was diese Funktionen tun.

Beispielsweise ist der Block "say" konzeptuell sehr nahe an ```print``` in Python:

![04_scratch_say](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_say.png)

```python
print("Hello world!")
```

Die Funktion ```print``` erhält als Parameter den **String** "Hello world!". Strings sind mehrere Zeichen, die in Python als Text interpretiert werden sollen und müssen in ```"```  eingeschlossen werden.

Die Klammern ```()``` kennzeichnen ```print``` als Funktion und ermöglichen es Parameter an die Funktion zu übergeben (in diesem Fall den String "hello world").

Die Funktion ```print``` erzeugt eine sichtbare **Ausgabe** auf der Shell:

![04_funktionen_ausgabe](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_funktionen_ausgabe.png)

Mögliche Ausgaben sind (wie hier) die Ausgabe von Text auf der Shell oder das Abspielen einer Sounddatei).

Auch in Scratch gibt es Ausgaben, wie z.B. die des Blocks "say":

![04_funktionen_scratch_ausgabe](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_funktionen_scratch_ausgabe.png)

Neben Ausgaben, gibt es in Scratch auch Blöcke mit **Rückgabewerten**, die in Programmen weiterverwendet werden können (im Gegensatz zu einer Ausgabe, die einmal erscheint und dann "verschwindet"). Die Rückgabewerte können in **Variablen** gespeichert werden. 

Beispielsweise speichert der Block "ask" in Scratch ein Ergebnis im Block "answer":

![04_funktionen_scratch_return](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_funktionen_scratch_return.png)

Das Äquivalent in Python sieht wie folgt aus:

```python
answer = get_string("Whats your name?")
```

Die Funktion ```get_string()``` erhält einen Parameter ```"Whats your name?"``` als Aufforderung an die Nutzer den eigenen Namen anzugeben (dieser Parameter erzeugt eine Ausgabe auf der Shell).

Anschließend wird mittels ```answer = ``` der Rückgabewert in die Variable ```answer``` gespeichert.

Das folgende Programm fragt zuerst nach einem Nutzernamen und versucht diesen anschließend auf der Kommandozeile auszugeben:

~~~python
answer = get_string("What's your name?")
print("Hello answer")
~~~

Versucht man dieses Programm auf der Shell auszuführen, erhält man die folgende Fehlerausgabe des Python-Interpreters:

~~~shell
python3 hello1.py 
Traceback (most recent call last):
  File "hello1.py", line 1, in <module>
    answer = get_string("What's your name?")
NameError: name 'get_string' is not defined
~~~

Der Interpreter produziert nicht immer besonders einsteiger- bzw. nutzerfreundliche Ausgaben, aber wenn man diese genauer ansieht, gibt diese Tipps, wo die Fehler liegen können: In dieser Ausgabe liegt der Fehler direkt in der Datei ```hello1.py``` (der einzigen Datei des Programms) und dort in der ersten Zeile (```line 1```). Es lässt sich erahnen, dass der Interpreter die Funktion ```get_string``` nicht kennt.

Standard-Python enthält nur eine Reihe von Funktionen (wie z.B. ```print```) die sich direkt nutzen lassen. Will man diesen Funktionsumfang erweitern, müssen **Bibliotheken** geladen werden. Eine Bibliothek ist eine zusammengehörige Sammlung von Code, die von vielen Programmierern verwendet werden kann. Der Code ```get_string``` ist in der Bibliothek ```cs50``` enthalten. Diese soll den Einstieg in die Programmierung erleichtern und enthält dazu einige Funktionen wie ```get_string```.

Das Beispiel kann wie folgt erweitert werden, um die Funktion ```get_string``` aus der Bibliothek ```cs50``` zu importieren:

~~~python
from cs50 import get_string

answer = get_string("What's your name?")
print("Hello answer")
~~~

Wenn man das Programm jetzt ausführt, stoppt das Programm, damit Nutzer ihren Nutzernamen eingeben können zwar wie erwartet, aber die Ausgabe ist immer ```"hello answer```":

~~~shell
python3 hello1.py 
What's your name? Markus
Hello answer
~~~

Um dieses Problem zu lösen muss der Code wie folgt angepasst werden (```hello1.py```):

~~~python
from cs50 import get_string

answer = get_string("What's your name?")
print(f"Hello {answer}")
~~~

Das Voranstellen von ```f``` vor den String bedeutet, dass der nachfolgende String einen Platzhalter enthält. Der Platzhalter ```{answer}``` wird in den String mit den Klammern ```{}``` integriert und beim Aufruf von print wird dort der korrekte Wert von ``` answer``` eingesetzt und das Programm funktioniert.

Der Parameter ```"What's your name?"``` lässt sich in ```What's your name? " ``` mit einem Leerzeichen am Ende umschreiben, damit die Abfrage des Namens nicht direkt am Fragezeichen "klebt".

Replit (und viele andere IDEs) unterstützen Entwickler dabei Strukturen im Code zu erkennen. Beispielsweise wird ```answer```, wenn es von ```{}``` umgeben wird in weißer Farbe (d.h. als Variable) gekennzeichnet:

![04_replit_highlighting](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_replit_highlighting.png)

Auch beim Klick auf die öffnende Klammer in Zeile 3 gibt replit einen Hinweis durch das automatische markieren der schließenden Klammer in der selben Zeile.

Die Funktion ```get_string``` und der Block "ask" in Scratch liefern einen Rückgabewert als Ergebnis:

![04_funktionen_rückgabe](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_funktionen_rückgabe.png) 

Weiterhin ähnelt ```print(f"Hello {answer}")``` der Kombination der folgenden Blöcke in Scratch:

![04_scratch_format_string](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_format_string.png)

In beiden Fällen wird eine Variable in einen String eingefügt und direkt angezeigt.

# main-Funktion

Die bisherigen Python-Codebeispiele integrieren Variablen und Funktionen direkt in das Python-Programm.  Häufig soll aber ein definierter Startpunkt beim Ausführen eines Python-Programms definiert werden. In Scratch ist der definierte Startpunkt eines Programms durch den Block "when green flag clicked" gekennzeichnet:

![04_scratch_green_flag](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_green_flag.png)

Das Äquivalent von "when green flag clicked" sieht in Python wie folgt aus:

~~~python
from cs50 import get_string

def main():
  answer = get_string("What's your name?")
  print(f"Hello {answer}")
~~~

```def main():``` erstellt eine Funktion ```main()```, d.h. einen Block von zusammengehörigen Anweisungen. Die beiden folgenden Zeilen sind Teil dieser Funktion, gekennzeichnet durch eine Einrückung. Nicht eingerückte Zeilen gehören nicht zur Funktion.

Startet man das Programm von der Shell passiert aber erstmal garnichts. Erst das Ergänzen des Codes um zwei weitere Zeilen bringt das Programm wie erwartet zum Laufen (```hello2.py```):

~~~python
from cs50 import get_string

def main():
  answer = get_string("What's your name?")
  print(f"Hello {answer}")

if __name__ == "__main__":
    main()
~~~

Die beiden ergänzten Zeilen sorgen dafür, dass die Funktion ```main()``` dann aufgerufen wird, wenn das Programm von der Shell mit ```python3 hello2.py``` ausgeführt wird.

# Shell-Befehle

Linux bietet weitere Befehle, die auf der Shell ausgeführt werden können:

* ```cd``` (*change directory*) - wechselt das aktuelle Verzeichnis (= Ordner)
* ```cp``` (*copy*) - kopiert Dateien und Ordner
* ```ls``` (*list*) - zeigt die Dateien in einem Ordner an
* ```mkdir``` (*make directory*) - erstellt einen Ordner
* ```mv``` (*move*) - verschiebt Dateien und Ordner
* ```rm``` (*remove*) - löscht Dateien
* ```rmdir``` (*remove directory*) - löscht Ordner
* ...

Neue Dateien und Ordner lassen sich in replit über den Dateiexplorer anlegen (+-Symbole):

![04_replit_file_folder](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_replit_file_folder.png)

Alternativ geht dies auch über die Shell:

~~~shell
$ mkdir lab1
$ mkdir lab2
$ ls
$ hello0.py  hello1.py  hello2.py  lab1  lab2
~~~

Hinweis: Das ```$```-Zeichen steht für eine Zeile in der Kommandozeile. Ggf. steht in replit davor bereits der Ordner des aktuellen Verzeichnisses (wie z.B. ```~/Digital-Skills04Python$```).

```mkdir``` erstellt jeweils einen Ordner. Anschließend zeigt ```ls``` an, welche Dateien und Ordner sich im aktuellen Ordner befinden: Die beiden neuen Ordner ```lab1``` und ```lab2``` werden angezeigt. Mithilfe von ```cd``` kann man den aktuellen Ordner wechseln:

~~~shell
$ cd lab1
/lab1$ ls
/lab1$ 
~~~

Der Beginn der Zeile ändert sich zu ```/lab1$``` und zeigt an, dass sich das aktuelle Verzeichnis geändert hat. ```ls``` zeigt, dass der neue Ordner leer ist.

Mit den folgenden Befehlen wird ein weiterer Ordner erstellt und in diesen gewechselt:

~~~shell
/lab1$ mkdir mario
/lab1$ ls
mario
/lab1$ cd mario/
/lab1/mario$ 
~~~

In diesem neuen Ordner ```mario``` lässt sich mit dem folgenden Befehl eine neue Datei anlegen:

~~~shell
touch mario.py
~~~

Die angelegten Ordner und die Datei ```mario.py``` erscheinen in replit auch im Datei-Explorer:

![04_replit_files_touch](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_replit_files_touch.png)

Mit zweimaliger Eingabe des Befehls ```cd ..``` gelangt man wieder zum Ausgangsordner:

~~~shell
/lab1/mario$ cd ..
/lab1$ cd ..
$ 
~~~

# Datentypen, Operatoren

In Python können Variablen unterschiedliche Arten von Werten (d.h. *Datentypen*) annehmen. Die folgende Liste zeigt typische Datentypen in Python:

* ```bool``` - Kann entweder ```true``` (wahr) oder ```false``` (falsch) sein
* ```str``` - Zeichenketten
* ```float``` - Fließkommazahlen
* ```int``` - Ganzzahlen

Die Bibliothek ```cs50``` bietet die entsprechenden Funktionen, um diese Werte einzulesen:

* ```get_string```
* ```get_float```
* ```get_int```

Mithilfe der Funktion ```type()``` lassen sich die Datentypen von Variablen anzeigen:

Die Ausgabe ist wie folgt:

~~~python
from cs50 import get_string, get_float, get_int

def main():
  player_name = get_string("Enter player name: ")
  total_goals = get_int("Enter total goals scored: ")
  goals_per_match = get_float("Enter average goals per match: ")

  print(f"Type of player_name: {player_name} is {type(player_name)}")
  print(f"Type of total_goals: {total_goals} is {type(total_goals)}")
  print(f"Type of goals_per_match: {goals_per_match} is {type(goals_per_match)}")
  

if __name__ == "__main__":
    main()
~~~

~~~shell
$ python3 hello3.py 
Enter player name: Lewandowski
Enter total goals scored: 28
Enter average goals per match: 1.1
Type of player_name: Lewandowski is <class 'str'>
Type of total_goals: 28 is <class 'int'>
Type of goals_per_match: 1.1 is <class 'float'>
~~~

In Python lassen sich unterschiedliche mathematische Operatoren verwenden:

* ```+``` für Addition
* ```-``` für Subtraktion
* ```*``` für Multiplikation
* ```/``` für Division
* ```%``` für Ermittlung des Rests bei ganzzahliger Division

# Variablen, *syntactic sugar*

In Scratch lässt sich eine Variable ```counter``` anlegen und deren Wert auf ```0``` wie folgt setzen:

![04_scratch_define_var](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_define_var.png)

Der Code in Python sieht dazu wie folgt aus:

~~~python
counter = 0
~~~

Der Wert von ```counter``` lässt sich wie folgt um 1 erhöhen:

![04_scratch_change_var](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_change_var.png)

In Python geht dies wie folgt:

~~~python
counter = counter + 1
~~~

Der obige Code liest zuerst auf der rechten Seite des ```=``` den Wert von ```counter``` aus, erhöht den Wert um 1 und weist das neue Ergebnis wieder ```counter``` zu. 

Python erlaubt auch die Kurzschreibweise ```counter += 1```, welche die Variable um den Wert rechts des ```=``` erhöht. Derartige Kurzschreibweisen werden häufig ***syntactic sugar*** genannt.

# Berechnungen

Mit dem Befehl ```touch calculator0.py``` lässt sich die Datei ```calclulator0.py``` anlegen und anschließend in replit wie folgt ergänzen:

~~~python
from cs50 import get_int

def main():
  x = get_int("x: ")
  y = get_int("y: ")
  print(f"{x + y}")

if __name__ == "__main__":
    main()
~~~

Zuerst werden die Nutzer aufgefordert Werte für die beiden Variablen ```x``` und ```y``` einzugeben. Anschließend wird mithilfe eines Platzhalters in ```print``` der Wert der Summe ausgegeben. 

Achtung: Normalerweise sind Variablennamen wie ```x``` und ```y``` schlecht gewählt, da sich ihre Bedeutung beim Lesen des Codes nicht erschließt. Ein Variablenname sollte immer anzeigen, welche Art von Informationen sich in der Variable befinden (vgl. ```player_name``` oder ```total_goals```). Für die folgenden Beispiele ist das aber ausnahmsweise in Ordnung.

Führt man das Programm auf der Shell aus, ist die Ausgabe wie folgt:

~~~shell
$ python3 calculator0.py 
x: 3
y: 8
11
~~~

Das Programm lässt sich um eine dritte Variable ```z``` wie folgt erweitern, um das Ergebnis der Berechnung zu speicher, bevor dieses ausgegeben wird (```calculator1.py```):

~~~python
from cs50 import get_int

def main():
  x = get_int("x: ")
  y = get_int("y: ")
  z = x + y
  print(z)

if __name__ == "__main__":
    main()
~~~

Da die Variable jetzt direkt ausgegeben wird, steht diese direkt (d.h. ohne Anführungszeichen) als Parameter in den Klammern für ```print```.

Tipp: Auf der Shell lassen sich Befehler mit der Taste ```Tabulator``` vervollständigen, d.h. aus ```python3 cal``` und Druck auf die Taste ```Tabulator``` wird ```python3 calculator```. Mit den Pfeiltasten oben und unten lassen sich frühere Befehle wiederherstellen, dies beschleunigt die Verwendung der Shell. 

Die Lesbarkeit des Programms lässt sich mit **Kommentaren** wie folgt verbessern (auch wenn diese in diesem Fall lediglich offensichtliche Dinge wiederholen):

~~~python
from cs50 import get_int

def main():
  # prompt user for x
  x = get_int("x: ")

  # prompt user for x
  y = get_int("y: ")

  # perform addition and output sum to users
  z = x + y
  print(z)

if __name__ == "__main__":
    main()
~~~

Kommentare helfen bei komplexeren Codebeispielen nachzuvollziehen, was der Code tun soll.

Code und Kommentare sollten immer auf englisch geschrieben werden, um Programme für möglichst viele Nutzer lesbar zu gestalten. V.a. in internationalen Projekten wäre es fatal, wenn Entwickler demn Code in ihren jeweils eigenen Sprachen schreiben würden.

# Verzweigungen und boolesche Ausdrücke

In Scratch kann ein Block zwei Variablen vergleichen:

![04_scratch_if](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_if.png)

In Python sieht der dazugehörige Code wie folgt aus:

~~~python
if x < y:
    print("x ist kleiner als y")
~~~

Achtung: Die Zeile ```print``` mus eingerückt sein, um nur dann ausgeführt zu werden, falls die Bedingung ```x<y``` zutrifft. Ist die Zeile nicht eingerückt, wird immer ```"x ist kleiner als y"``` ausgegeben.

If und else in Scratch...

![04_scratch_if_else](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_if_else.png)

... können in Python wie folgt umgesetzt werden:

~~~python
if x < y:
  print("x ist kleiner als y")
else:
  print("x ist nicht kleiner als y")
~~~

Ein "else if" lässt sich wie folgt in Scratch...

![04_scratch_if_else](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_if_else.png)

... und in Python umsetzen:

~~~python
if x < y:
  print("x ist kleiner als y")
elif x > y:
  print("x ist größer als y")
elif x == y:
	print("x ist gleich y")
~~~

Zwei Werte werden in Python mit ```==``` verglichen, nicht mit nur einem ```=```. Die letzte Prüfung ```elif x == y:``` ist eigentlich unnötig, da dies der einzig verbleibende Fall ist, wenn keiner der Werte der beiden Variablen größer oder kleiner als der andere Wert ist, d.h. der Code lässt sich wie folgt umschreiben:

~~~python
if x < y:
	print("x ist kleiner als y")
elif x > y:
	print("x ist größer als y")
else:
	print("x ist gleich y")
~~~

Das Beispiel ```points0.py``` zeigt die Verwendung von Verzweigungen an einem konkreten Beispiel:

~~~python
from cs50 import get_int

def main():
  # Prompt user for points
  points = get_int("Wie viele Punkte hast Du verloren? ")

  # Compare points against mine
  if points < 2:
      print("Du hast weniger Punkte verloren als ich.")
  elif points > 2:
      print("Du hast mehr Punkte verloren als ich")
  else:
      print("Du hast gleiche viele Punkte wie ich verloren.")

if __name__ == "__main__":
    main()
~~~

Das Programm enthält an zwei Stellen **Magic Numbers**, d.h. Zahlen, die sich nicht ohne den Kontext erschließen lassen. Statt die Variable ```points``` zweimal gegen die Magic Number 2 zu vergleichen, lässt sich die 2 als Konstante an einer Stelle des Programms definieren:

~~~python
from cs50 import get_int

def main():
  # Prompt user for points
  points = get_int("Wie viele Punkte hast Du verloren? ")

  MY_POINTS = 2

  # Compare points against mine
  if points < MY_POINTS:
      print("Du hast weniger Punkte verloren als ich.")
  elif points > MY_POINTS:
      print("Du hast mehr Punkte verloren als ich")
  else:
      print("Du hast gleiche viele Punkte wie ich verloren.")

if __name__ == "__main__":
    main()
~~~

Die Variable ```MY_POINTS``` ist groß geschrieben, um zu verdeutlichen, dass sich der Wert der Variable in diesem Programm nicht ändern sollte (auch wenn dies technisch möglich ist).

Das Programm ```parity.py``` zeigt die Verwendung des ```%``` Operators, um zu überprüfen, ob eine Zahl gerade oder ungerade ist:

~~~python
from cs50 import get_int

def main():
  # Prompt user for integer
  n = get_int("n: ")

  # Check parity of integer
  if n % 2 == 0:
      print("gerade")
  else:
      print("ungerade")

if __name__ == "__main__":
    main()
~~~

Der Operator ```%``` liefert den Rest bei einer ganzzahligen Division (im obigen Beispiel einer Division durch ```2```). Ist dieser Rest ```0```, dann ist ```n``` eine gerade Zahl.

Führt man das Programm auf der Shell aus, erhält man Ausgaben wie die Folgenden:

~~~shell
$ python3 parity.py 
n: 3
ungerade
$ python3 parity.py 
n: 4
gerade
$ python3 parity.py 
n: 8
gerade
~~~

Das Programm ```agree.py``` zeigt, wie sich einzelne Zeichen in Python von den Nutzern einlesen und sich Bedingungen verknüpfen lassen:

~~~python
from cs50 import get_string

def main():
  # Prompt user for agree
  answer = get_string("Bist Du einverstanden? ")

  if answer == "j" or answer == "J":
    print("Du bist einverstanden.")
  elif answer == "n" or answer == "N":
    print("Du bist nicht einverstanden.") 

if __name__ == "__main__":
    main()
~~~

Zuerst wird in der Variable ```answer``` eine Eingabe eingelesen. Anschließend wird geprüft, ob die Eingabe ```j``` oder ```J``` bzw. ```n``` oder ```N``` ist. Soll geprüft werden, dass beide Bedingungen wahr sind (in diesem Fall unmöglich, da die Variable ```answer``` nicht zwei Werte gleichzeitig annehmen kann), können die Bedingungen mit ```and``` verknüpft werden.

# Schleifen, Funktionen

Das folgende Programm ```miau0.py``` gibt dreimal das Wort "miau" aus:

~~~python
def main():
  print("miau")
  print("miau")
  print("miau")  

if __name__ == "__main__":
    main()
~~~

Das Programm ist korrekt, aber das Design des Programms lässt sich mit einer Schleife verbessern. In Scratch lässt sich eine Endlosschleife mit dem Block "forever" darstellen...

![04_scratch_forever](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_forever.png)

... und in Python mit dem folgenden Code:

~~~python
while True:
  print("miau")
~~~

Die while-Schleife wiederholt sich solange, wie die Bedingung in der ersten Zeile zutrifft. Da ```True``` immer ```True``` (d.h. wahr oder zutreffend ist), wiederholt sich die Schleife endlos.

Der Block "repeat" lässt sich in Scratch wie folgt darstellen...

![04_scratch_repeat](/Users/markus/Repos/digitalskills/semester1_technology_skills/04_python1/notes/img/04_scratch_repeat.png)

.. und in Python mit dem folgenden Code:

~~~python
counter = 0

while counter < 3:
    print("miau")
    counter = counter + 1
~~~

Zunächst wird eine Variable ```counter``` deklariert und ihr wird der Wert ```0``` zugwiesen.  Hier wird später gespeichert, wie oft die Schleife bereits durchlaufen wurde. Die ```while```-Schleife wiederholt sich solange ```counter``` kleiner als ```3``` ist. Bei jedem Schleifendurchlauf wird "miau" ausgegeben und anschließend ```counter``` um ```1``` erhöht. 

Die Schleife lässt sich mit "Syntactic sugar" etwas knapper darstellen:

~~~python
i = 0

while i < 3:
    print("miau")
    i += 1
~~~

Da die Variable nur zum Zählen der Schleifendurchläufe verwendet wird, kann sie den dazu häufig verwendeten Namen ```i``` erhalten. Auch der Startwert ```0 ``` ist eine häufig verwendete Konvention, damit die Zahl gegen die ```i``` verglichen wird der Anzahl der gewünschten Schleifendurchläufe entspricht.

Da die Widerholung einer Schleife mit einer bekannten Anzahl von Durchgängen ein häufiges Muster darstellt, existiert dazu eine eigene Syntax:

~~~python
for i in range(3):
    print("miau")    
~~~

Die Zahl (hier: ```3```) steht dabei für die Anzahl der Wiederholungen aller eingerückten Zeilen (hier nur ```print```).

Demnach lässt sich das Programm wie folgt anpassen (```miau1.py```):

~~~python
def main():
  for i in range(3):
    print("miau")

if __name__ == "__main__":
    main()
~~~

Die Ausgabe ist wie folgt:

~~~shell
$ python3 miau1.py 
miau
miau
miau
~~~

In Scratch lassen sich eigene Blöcke erstellen, das Äquivalent dazu sind eigene Funktionen in Python (```miau2.py```):

~~~python
def main():
  for i in range(3):
    miau()

def miau():
    print("miau")
    
if __name__ == "__main__":
    main()
~~~

Die Funktion ```miau()``` lässt sich um einen Parameter erweitern (```miau3.py```):

~~~python
def main():
  miau(3)

def miau(n):
    for i in range(n):
      print("miau")
    
if __name__ == "__main__":
    main()
~~~

Durch die Änderung ```def miau(n)```, wird die Funktion so angepasst, dass sie einen Parameter (```n```) als Eingabe erwartet. Jetzt prüft die for-Schleife nicht mehr gegen eine konstante Zahl, sondern gegen den übergebenen Parameter ```n```. Ändert man jetzt die Zahl in ```main``` ab, lässt sich festlegen, wie oft "miau" ausgegeben werden soll.

# Mario

Im Folgenden wird Python dazu verwendet Blöcke (wie aus dem Spiel Super Mario Bros - https://de.wikipedia.org/wiki/Super_Mario_Bros.) auszugeben.

Der folgende Code gibt 4 Fragezeichen (jedes davon symbolisiert einen Block in dem Spiel) aus (```mario0.py```):

~~~python
def main():
  print("????")
    
if __name__ == "__main__":
    main()
~~~

 Mithilfe einer for-Schleife lässt sich der Code in ein besseres Design überführen (```mario1.py```):

~~~python
def main():
  for i in range(4):
    print("?") 
    
if __name__ == "__main__":
    main()
~~~

Das folgende Beispiel verwendet eine Schleife, um eine Ganzzahl einzulesen (```mario3.py```):

~~~python
while True:
    n = get_int("Height: ")
    if n > 0:
        break

for i in range(n):
    print("#")

~~~

Das Programm versucht solange eine Zahl einzulesen, bis die Nutzer eine positive Zahl einlesen. Dabei beendet die Anweisung ```break``` die while-Schleife und das Programm führt den Code der for-Schleife aus.

Eine zweidimensional Anordnung von Blöcken lässt sich mit ineinander verschachtelten Schleifen umsetzen (```mario4.py```):

~~~python
from cs50 import get_int

def main():
  while True:
    n = get_int("Size: ")
    if n > 0:
        break

  for i in range(n):
    for j in range(n):
        print("?", end="")
    print()
    
if __name__ == "__main__":
    main()
~~~

Die bisherige Version der Funktion ```print()``` hat jede Zeile mit einem Zeilenumbruch beendet. Da das Codebeispiel mehrere ```?``` hintereinander auf einer Zeile ausgeben soll, wird hier eine andere Version dieser Funktion verwendet: ```print("?", end="")``` endet jede Zeile mit einem leeren String, beginnt also keine neue Zeile.

Die äußere Schleife steht für eine Zeile aus ```?```-Symbolen. In jeder Zeile wird in der zweiten Schleife ```n```-mal das Symbol ```?``` Fragezeichen ausgegeben, bevor 1 mal die Funktion ```print()``` aufgerufen wird, um einen Zeilenumbruch zu erzeugen. Eine Ausgabe des Programms sieht wie folgt aus:

~~~shell
$ python3 mario3.py 
Size: 4
????
????
????
????
~~~

Quelle: Angepasst und ergänzt von CS50, Harvard University, 2022 - https://cs50.harvard.edu/x/2022/
