# Lab Challenge 10

> Arbeiten Sie alleine an den Challenges. Sie können sich mit ihrem Coach oder anderen Studierenden austauschen, aber arbeiten Sie nicht zusammen mit anderen Studierenden an einer Challenge und geben Sie auch nicht denselben Code ab.

## Was es zu tun gibt

1. Arduino einrichten
1. Programmieren Sie **Wetterstation**

## Arduino einrichten

Führen Sie die folgenden Schritte durch, um auf dem Arudino programmieren zu können:

1. Registrieren Sie sich mit Ihrer studentischen E-Mail-Adresse bei https://classroom.arduino.cc/ ?????
2. Nutzen Sie den Code "JkqKcqUT" um den Aruino Klassenraum beizutreten
3. Registrieren Sie das Arudino IoT Kit 


Mit der Arduino Cloud lässt sich einfach der Arduino programmieren und Dashboards erstellen auf denen Ihr Daten abrufen oder sie an den Arduino senden könnt.
Dafür muss zu erst die das Dashboard konfiguriert werden.

## Dashboard einrichten
### Arduino aufbauen

Den Arduino und das Shield auspacken und richtig herum zusammenstecken. **Umbedingt auf die Beschriftung der PINS achten!**
Anschließend den Arduino mit dem beiliegenden Mikro-USB-Kabel an deinen PC anschließen.

### Thing erstellen

Ein Thing ist die Repräsentation eines physisches Geräts, in unserem Fall der Arduino. Dieses muss zuerst online definiert werden damit die Website die Daten entsprechend zuordnen kann.
Klicke auf der Startseite https://classroom.arduino.cc/ auf "IoT Cloud". Klicke dann auf "Create Thing".

1. Im angezeigten Bildschirm vergeben wir zuerst einen passenden Namen, dazu einfach oben auf "Untitled" klicken und einen Namen wie z.B. "Wetterstation" vergeben.
2. Als nächstes verbinden wir unseren Arduino mit dem Thing. Dazu rechts auf Select Device klicken und den Anweisungen folgen
3. Verbindung mit dem WLAN herstellen. Rechts unten bei "Network" auf "Configure" gehen und deine WLAN Daten hinterlegen.

### Variablen konfigurieren

Die Variablen die gelesen bzw. beschrieben werden können nicht einfach im Programmcode definiert werden, da die Plattform nicht automatisch die Verbindung zu unseren definierten Variablen herstellen kann.
Deshalb müssen alle Variablen die später über das Dashboard ereichbar sein müssen mit "Add Variable" angelegt werden.

Um die Funktionsweise zu demonstrieren werden wir im folgenden die Variable für die Raumtemperatur konfigurieren. Im Anschluss wird es deine Aufgabe sein 
die anderen benötigten Variablen für das Projekt selbst zu konfigurieren.

Wir vergeben einen passenden Namen "Raumtemperatur" und wählen den Datentyp "Floating Point Number".

Bei den Berechtigungen gibt es die Optionen 
 - Read & Write
   Wird für Variablen verwendet deren Wert über das Dashboard verändert werden kann. Beispiele wären Lichtschalter, Temperatureinstellungen,... die gesteuert werden sollen.
 - Read Only
   Für Variablen die nur zur Datenübertragung vom Gerät zum Dashboard verwendet werden. Beispiele wären die aktuelle Raumtemperatur, Luftfeuchtigkeit,...

Da die Raumtemperatur nur gelesen werden soll wählen wir hier "Read Only" aus.

Bei den Update Policy gibt es die Optionen
  - On Change
  Variablen werden nur geupdated wenn sich der Wert verändert. Dies ist sinnvoll für Dinge die z.B. nur alle paar Sekunden auftreten. 
  Der genaue Zeitabstand hängt von der Anwendungssituation ab. Ist es sehr wichtig immer aktuelle Daten zu haben muss der Zeitabstand geringer sein, als z.B. bei der Raumtemperatur.
  Der Threshhold gibt an ab welcher Wertschwankung aktualisiert wird. 
  - Periodically
  Die Werte werden in einem bestimmten Zeitabstand aktualisiert. Dies ist Beispielsweise sinnvoll wenn man Diagramme die den zeitlichen Verlauf darstellen erstellen möchte.
  Im Feld wird angegeben in welchem Zeitabstand aktualisiert wird.
  
Wir wählen für die Raumtemperatur "Periodically" alle 5sec. Hier anzumerken ist, das andere Einstellungen ebenso funktionieren würden.

Abschließend bestätigen wir unsere Eingabe mit "Add variable", die Variable sollte nun angezeigt werden. 

### Sketch programmieren

Im Sketch findet das eigentliche Programmieren statt. Rechts neben "Sketch" wird jetzt auch gekennzeichnet, das das Programm durch die Erstellung der Variable
im Programmcode etwas geändert hat. Wenn wir den Code genauer ansehen sehen wir oben im Kommentar

~~~ The following variables are automatically generated and updated when changes are made to the Thing
  float raumtemperatur;
~~~
  
Andere Variablen die später angelegt werden, werden hier auch angezeigt werden. 

~~~
/*
  Since Raumtemperatur is READ_WRITE variable, onRaumtemperaturChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onRaumtemperaturChange()  {
  // Add your code here to act upon Raumtemperatur change
}
~~~
Als Beispiel, hätten wir READ_WRITE gewählt würde zusätzlich dieser Methodenrumpf generiert werden.
Dieser ist relevant für Änderungen die am Dashboard vorgenommen werden. Hier könnte definiert werden, was passieren soll 
wenn die Variable verändert wird.



 
 





