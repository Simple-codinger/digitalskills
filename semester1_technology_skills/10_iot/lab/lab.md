# Lab Challenge 10

> Arbeiten Sie alleine an den Challenges. Sie können sich mit ihrem Coach oder anderen Studierenden austauschen, aber arbeiten Sie nicht zusammen mit anderen Studierenden an einer Challenge und geben Sie auch nicht denselben Code ab.

## Was es zu tun gibt

1. Umschalten zwischen Ansichten mit den Buttons
2. Abfragen und Darstellen der Sensoren Daten
3. Senden von Daten vom der Arduino Cloud an den Arduino
4. Anfragen und Darstellen der Daten der Wetter API

## Ziel Challenge
Das Ziel dieser Challenge ist Ihre bestehende Wetteranwendung zu einer internationalen Wetterstation umzubauen. Diese Anwendung soll es dann ermöglichen sowohl die Sensordaten anzuzeigen, als auch von anderen Städten weltweit z.B. die aktuelle Temperatur anzuzeigen. Gesteuert wird das Ganze über die Web GUI.

Am Ende soll Ihr Dashboard in etwa so aussehen. 
![10_lab_finalDashboard](img/10_lab_finalDashboard.jpg)

## Umschalten zwischen Ansichten mit den Buttons
Um verschiedene Werte auf dem Display des Arduinos anzuzeigen soll es im Ersten Schritt ermöglicht werden mit den Buttons zwischen mehreren Texten umzuschalten. 

Folgenden Aufrufe sind dafür notwendig:
Dieser Befehl muss in der Loop Methode aufgerufen werden. Er bewirkt das die Werte gesetzt werden welcher Button gedrückt wurde.
~~~
carrier.Buttons.update();
~~~

Dieser Aufruf gibt zurück, ob der Button 0 gedrückt wurde. (Analog Button 1-4)
~~~
carrier.Buttons.onTouchDown(TOUCH0)
~~~

Ihre Aufgabe ist es zu überprüfen welcher der eizelnen Buttons gedrückt wurden und am Display den Text "Button x" wurde gedrückt auszugeben.


## Abfragen und Darstellen der Sensoren Daten

Im Note wurde bereits genau erklärt wie man die aktuelle Temperatur abfragen und darstellen kann. Ihre Aufgabe ist es jetzt zusätzlich die Luftfeuchtigkeit anzuzeigen.
Folgender Aufruf gibt Ihnen die aktuelle Luftfeuchtigkeit zurück.
~~~
  carrier.Env.readHumidity();
~~~

Anschließend sollte Ihr Dashboard in etwa so aussehen:
![10_lab_dashboardHumidityAdded](img/10_lab_dashboardHumidityAdded.jpg)
  
## Senden von Daten vom der Arduino Cloud an den Arduino


## Anfragen und Darstellen der Daten der Wetter API

### Abgabe


