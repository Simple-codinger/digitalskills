# Das Internet

In dieser Challenge geht es um Webentwicklung. Es werden neue Sprachen und Technologien vorgestellt, mit deren Hilfe sich **serverseitige** Anwendungen, d.h. Anwendungen die auf einem Server oder einem Cloudservice laufen und  *clientseitige* Anwendungen entwickeln lassen, die im Browser der Nutzer laufen.

Das **Internet** ist ein Netzwerk aus Netzwerken Rechnern (bzw. Servern), die miteinenander kommunizieren, indem sie Daten senden und empfangen. Das erste Internet war das ARPANET, dass die Rechner verschiedener amerikanischer Universitäten miteinander verbunden hat (vgl. https://de.wikipedia.org/wiki/Arpanet). Das heutige Internet verbindet alle per Kabel oder WiFi *angeschlossenen* Rechner der Welt miteinander. 

**Router** sind spezielle Rechner (mit CPU und Speicher), die Daten von einem Punkt zu einem anderen Punkt weiterleiten (d.h. von einem an das Internet angeschlossenen Rechner zu einem anderen Rechner). Router erhalten die Daten von einem Rechner und entscheiden selbst, wie sie diese Daten weitergeben. Die Daten, die von einem Rechner zu einem anderen Rechner über das Internet geschickt werden passieren also mehrere Router.

**Protokolle** sind Regelwerke, die festlegen, wie Computer miteinander kommunizieren. Wie die Kommunikation zwischen Menschen mit einer Begrüßung beginnt und einer Verabschiedung endet, regelt ein Protokoll exakt, wie Daten zwischen Rechnern ausgetauscht werden.

**TCP/IP** sind zwei Protokolle, um Daten zwischen zwei Rechnern auszutauschen. In der realen Welt schreiben wir den Empfänger auf einen Brief und den Sender, damit der Empfänger auf den Brief antworten kann.

**IP** (Internet Protocol) beinhaltet einen standardisierten Weg, wie Computer sich identifizieren können. **IP-Adressen** sind eindeutige Adressen für Rechner, die mit dem Internet verbunden sind. Ein Paket von Daten, das von einem Rechner an einen anderen gesendet wird passiert mehrere Router auf dem Weg zum Ziel. Eine IP-Adresse hat typischerweise das Format ```#.#.#.#```, wobei jedes ```#``` für eine Zahl zwischen 0 und 255 steht. Jede Zahl hat dabei die Größe ein Byte, d.h. eine IP-Adresse besteht aus 4 Bytes oder 32 Bits. Somit kann die aktuelle Version 4 des IP Protokolls nur 256<sup>2</sup>, d.h. ca. 4 Milliarden unterscheiden. Eine neuere Version 6 des IP-Protokolls unterstützt 128 Bits, um deutlich mehr Adressen unterscheiden zu können.

**TCP** (Transmission Control Protocol) ist ein Protokoll, um Daten zu senden und zu empfangen. TCP erlaubt es einem einzelnen Rechner unter der selben IP-Adresse mehrere Dienste anzubieten. Dies wird durch einen **Port**, d.h. eine Zahl unterstützt, die mit ```:``` an die IP-Adresse angehängt wird. Beispielsweise werden Anfragen für Webseiten meist an den Port 80 gesendet und verschlüsselte Webseiten am Port 443 angefragt. 

TCP ermöglicht es große Dateien (wie z.B. Bilder) in kleineren Teilstücken zu senden. Jedes dieser Teilstücke kann mit einer Nummer versehen werden (z.B. "Teil 1 von 4" oder "Teil 2 von 4"). Somit kann der Empfänger ein Teilstück erneut anfragen, falls dieses nicht angekommen sein sollte. Protokolle wie UDP erlauben den Versand von Daten, garantieren die Lieferung aber nicht. Dies kann beispielsweise für Videokonferenzen sinnvoll sein, bei denen die Nutzer nicht warten wollen, bis alle Daten angekommen sind, weil sie ansonsten nicht mehr synchron mit den anderen Teilnehmern der Videokonferenz kommunizieren können.

**DNS** (Domain Name System) übersetzt für Menschen lesbare Domain-Namen (wie z.B. www.oth-regensburg.de) in IP-Adressen. DNS-Server verfügen über große Tabellen, um zwischen lesbaren Domain-Namen und IP-Adressen übersetzen zu können.

# Das Web

Das Internet mit Routern, TCP/IP und DNS-Servern bildet die Grundlage, um Daten von einem Rechner zu einem anderen zu schicken. Das Web ist eine Applikation, die auf dieser Grundlage aufbaut.

Das Protokoll **HTTP** standardisiert, wie Webbrowser und Webserver auf Basis von TCP/IP miteinander kommunizieren. **HTTPS** ist die sichere Variante von HTTP, indem es sicherstellt, dass die zu versendenden Daten verschlüsselt sind.

Eine URL ist eine Adresse die beispielsweise in die Adresszeile des Browsers eingegben werden kann und kann wie folgt aussehen: ```https://www.example.com/```

* ```https://``` ist das verwendete Protkoll
* Das ```/``` am Ende der URL fragt die Standarddatei bzw. Startseite des Webservers an. ```/file.html``` fragt eine spezifische Datei vom Webserver an.
* ```example.com``` ist der Domain-Name. ```.com``` ist der Name der Top-Level-Domain und zeigt an, welche Art von Website sich hinter der URL verbergen könnte. Andere Top-Level-Domains sind beispielsweise ```.de```, ```.edu``` oder ```.io```.
* ```www``` ist der Hostname (oder Subdomain), der sich auf einen oder mehrere Server des Domain-Names bezieht. Ein Domain-Name kann einen Webserver (```www```) oder einen Mailserver (```mail```) anbieten, d.h. mithilfe der Subdomain lassen sich diese Server gezielt adressieren.
* ```www.example.com``` ist ein *fully qualified domainname*, um einen Server eindeutig zu identifizieren.

HTTP unterstützt die beiden Methoden **GET** und **POST**. GET ermöglicht es einem Browser eine Datei von einem Webserver als Teil der URL abzufragen und POST erlaubt es dem Browser zusätzliche Informationen zu senden, die aber nicht Teil der URL sind. Besonders sensitive Daten wie Passwörter oder Kreditkarteninformationen sollten niemals per GET als Teil der URL übermittelt werden. Beide Methoden erzeugen immer einen **request** an einen Webserver, der vom Server immer mit einer **response** beantwortet wird.

Ein GET-request beginnt wie folgt:

~~~http
GET / HTTP/1.1
Host: www.example.com
~~~

```GET``` fragt mit ```/```die Startseite des Servers an. ```HTTP/1.1``` legt fest, dass der Browser die Version 1.1 des HTTP-Protokolls verwendet. ```Host: www.example.com``` fragt ```www.example.com```vom Webserver an, da der Webserver mehrere Webseiten und Domains anbieten könnte.

Eine response auf eine erfolgreiche Anfrage könnte wie folgt aussehen:

~~~http
HTTP/1.1 200 OK
Content-Type: text/html
...
~~~

Der Webserver antwortet zunächst mit der Version des HTTP-Protokolls (```HTTP/1.1```), gefolgt von einem Statuscode. Der Statuscode ```200 OK``` bedeutet, dass der request des Browsers valide war. Anschließend teilt der Webserver mit, welche Art von Inhalten verschickt werden (in diesem Fall ```text/html``` ). Ander Inhalte können Bilder oder weitere Datentypen sein. Der restliche Teil der HTTP-response (symbolisiert durch ```...```) sind die eigentlichen Daten bzw. Inhalte, die verschickt werden. 

Die Schlüssel und Wertpaare (```Host: www.example.com``` und ```Content-Type: text/html```) werden als **HTTP-Header** bezeichnet.

Tippt man ```http://www.oth-regensburg.de/``` in die Adresszeile des Browsers und klickt dann, nachdem die Website geladen wurde erneut in die Adresszeile, hat sich die URL in ```https://www.oth-regensburg.de/``` verändert.

Mithilfe der Chrome Developer Tools, einem Werkzeug für Webentwickler, lässt sich nachvollziehen, was passiert ist. Dazu öffnet man ein neues Incognito-Browserfenster, um die bisherige History an Webseitenaufrufen auszublenden. Die Developer Tools lassen sich durch Rechtsklick auf eine beliebige Stelle auf der Webseite aufrufen (Rechtsklick => Inspect).

Im Tab Network lässt sich erkennen, dass der Aufruf der URL zu insgesamt 46 requests an den Webserver geführt hat. Der Webserver hat dem Browser als response mitgeteilt, dass er weitere Bilder, Texte und andere Daten vom Server anfragen muss, um die Seite korrekt darzustellen:

![08_requests](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_requests.png)

Scrollt man in der Liste der requests ganz nach oben, kann man sich die Header des ersten Requests an ```http://www.oth-regensburg.de/```ansehen:

![08_request_response_headers](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_request_response_headers.png)

Der Server schickt den Statuscode ```301 Moved Permanently``` an den Browser zurück, und leitet den Browser somit an eine neue Seite weiter. Der Header ```Location: https://www.oth-regensburg.de/```zeigt dem Browser die neue Seite mit, die er anschließend in einem neuen request aufruft. Durch den redirect können die Nutzer die Webseite mit http aufrufen, jede weitere Kommunikation mit dem Webserver kann dann aber über eine verschlüsselte Kommunikation über https erfolgen.

Auch in replit lassen sich die Header einer response auf der Shell mithilfe des Kommandozeilenprogramms curl anzeigen:

~~~shell
curl -I -X GET http://www.oth-regensburg.de
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.oth-regensburg.de/
~~~

Ruft man mit curl jetzt die neue *Location* auf, wird der Statuscode ```200```angezeigt (und eine neuere Version des http-Prokolls):

~~~shell
curl -I -X GET https://www.oth-regensburg.de
HTTP/2 200
server: nginx/1.14.2
date: Wed, 16 Feb 2022 15:47:29 GMT
content-type: text/html; charset=utf-8
...
~~~

Versucht man mit curl eine URL aufzurufen, erhält man den Statuscode ```400```:

~~~shell
curl -I -X GET https://www.oth-regensburg.de/doesnotexit
HTTP/2 404
server: nginx/1.14.2
date: Wed, 16 Feb 2022 15:49:02 GMT
content-type: text/html; charset=UTF-8
...
~~~

Die folgende Liste enthält beispielhafte **HTTP status Codes**:

* ```200 OK```

* ```301 Moved Permanently```

* ```302 Found```

* ```304 Not Modified```

* ```307 Temporary Redirect```

* ```401 Unauthorized```

* ```403 Forbidden```

* ```404 Not Found``` - Ein Klassiker

* ```418 I'm a Teapot``` - Aprilscherz

* ```500 Internal Server Error``` - Ausgelöst durch einen Bug im serverseitigen Code

* ```503 Service Unavailable```

* ...


# HTML

Das Internet und HTTP erlauben es Nachrichten zwischen Browser und Server auszutauschen spezifizieren aber nicht den Inhalt dieser Nachrichten (nur die Header). Der Inhalt von Webseiten wird in der Sprache **HTML** (Hypertext Markup Language) geschrieben und kann vom Browser interpretiert und dargestellt werden. HTML ist keine Programmiersprache, sondern wird dazu verwendet Texte so zu strukturieren, damit sie korrekt auf einer Webseite dargestellt werden.

Eine einfache HTML-Seite (```hello_0.html```) sieht wie folgt aus:

~~~html
<!DOCTYPE html>

<!-- Demonstrates HTML -->

<html lang="en">
    <head>
        <title>hello, title</title>
    </head>
    <body>
        hello, body
    </body>
</html>
~~~

Um diese in replit anzuzeigen auf den Button Run klicken. Das Preview-Fenster auf der rechten Seite in replit zeigt die Meldung "Not Found", da dort nur eine Datei ```index.html``` angezeigt wird. Durch Klick auf den Button "Open in a new tab" rechts oben im Preview-Fenster lässt sich ein neuer Browser-Tab öffnen. Fügt man dort den Dateinamen ```/hello_0.html``` an die URL an, wird die Seite korrekt angezeigt.

Die Bestandteile der HTML-Seite im Detail:

* Die erste Zeile ```<!DOCTYPE html>``` legt fest, dass die Datei dem Standard HTML folgt
* ```<!-- Demonstrates HTML -->``` ist ein Kommentar für Entwickler der Website, der nicht auf der Webseite angezeigt wird.
*  ```<html>``` und ```</html>``` sind HTML-**Tags**, d.h. Wörter in spitzen Klammern. ```<html>``` ist ein öffnender und ```</html>``` ein schließender Tag. Beide Tags zusammen ergeben ein HTML-**Element**. Die beiden ```html ```Tags markieren den Start und das Ende der HTML-Seite. Tags können auch **Attribute** enthalten, das Attribut ```lang="en"``` legt deutsch als die Sprache für die Webseite fest. Die Festlegung der Sprache hilft dem Browser die Webseite bei Bedarf zu übersetzen. Attribute sind Schlüssel-Wert-Paare.
* Innerhalb des ```html```-Elements sind zwei weitere Elemente ```head``` und ```body``` verschachtelt. beide sind Kindelemente des Elternelements ```html```. Innerhalb des Elements ```body``` befindet mit dem Text ```hello body```, ein weiteres Kindelement.

Die Webseite wird im Speicher des Browsers als baumartige Datenstruktur angelegt:

![08_html_structure](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_html_structure.png)

Die Elemente sind dabei in einer Hierarchie verschachtelt. Rechteckige Knoten repräsentieren Tags, ovale Knoten sind Texte.

HTML ermöglicht es die Struktur von Webseiten festzulegen. Im Web lassen zahlreiche Quellen mit Dokumentationen für alle Tags und Attribute finden, die sich als Bausteine verwenden lassen.

Mithilfe des W3C Validierers lässt sich überprüfen, ob der HTML-Code valide ist: https://validator.w3.org/#validate_by_input

Die HTML-Datei ```paragraphs_0.html```zeigt, wie sich Textabsätze mit HTML formatieren lassen:

~~~html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>paragraphs</title>
    </head>
    <body>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        </p>
        <p>
            Mauris ut dui in eros semper hendrerit.
        </p>
        <p>
            Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula 								tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet.
        </p>
    </body>
</html>
~~~

Der Tag ```<p>``` kennzeichnet den Text bis zum schließenden Tag ```</p>``` als Textabsatz.

Überschriften lassen sich mit den Tags ```<h1>```, ```<h2>``` oder ```<h3>``` ergänzen (vgl. ```headings.html```):

~~~html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>headings</title>
    </head>
    <body>
      	<h2>One</h2>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        </p>
      	<h2>Two</h2>
        <p>
            Mauris ut dui in eros semper hendrerit.
        </p>
      	<h2>Three</h2>
        <p>
            Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula 								tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet.
        </p>
    </body>
</html>
~~~

Jede Nummer einer Überschrift entspricht einer bestimmten Größe, ```<h6>``` ist die kleinste Überschrift.

Das Beispiel ```list_0.html``` zeigt, wie sich mithilfe der Elemente ```ul``` und ```li``` Listen erstellen lassen:

~~~html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>list</title>
    </head>
    <body>
        <ul>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ul>
    </body>
</html>
~~~

Ändert man ```ul``` in ```ol``` lassen sich nummerierte Listen darstellen.

Tabellen beginnen mit dem Tag ```<table>```, die Tags ```<tr>```repräsentieren Zeilen, die Tags ```<td>```die einzelnen Zellen der Tabellen (```table.html```):

~~~html
<!DOCTYPE html>

<!-- Demonstrates table -->

<html lang="en">
    <head>
        <title>table</title>
    </head>
    <body>
        <table>
            <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
            </tr>
            <tr>
                <td>4</td>
                <td>5</td>
                <td>6</td>
            </tr>
            <tr>
                <td>7</td>
                <td>8</td>
                <td>9</td>
            </tr>
            <tr>
                <td>*</td>
                <td>0</td>
                <td>#</td>
            </tr>
        </table>
    </body>
</html>

~~~



Das Beispiel ```image.html``` zeigt wie sich Bilder in Webseiten einbinden lassen:

~~~html
<!DOCTYPE html>

<!-- Demonstrates image -->

<html lang="en">
    <head>
        <title>image</title>
    </head>
    <body>
        <!-- https://www.harvard.edu/ -->
        <img alt="Regensburg" src="regensburg.jpg">
    </body>
</html>
~~~

Auch Videos sind möglich (```video.html```):

~~~html
<!DOCTYPE html>

<!-- Demonstrates video -->

<html lang="en">
    <head>
        <title>video</title>
    </head>
    <body>
        <!-- https://www.harvard.edu/ -->
        <video autoplay loop muted width="1280">
            <source src="halloween.mp4" type="video/mp4">
        </video>
    </body>
</html>
~~~

Die Attribute des Tags ```<video>``` steuern die Darstellung des Videos, manche Attribute haben keine Werte.

Links auf andere Webseiten lassen sich mithilfe des Elements ```a``` erstellen (```link_1.html```):

~~~html
<!DOCTYPE html>

<!-- Demonstrates link -->

<html lang="en">
    <head>
        <title>link</title>
    </head>
    <body>
       Visit <a href="https://www.oth-regensburg.de/">OTH Regensburg</a>.
    </body>
</html>
~~~

Der Wert des Attributs ```href``` bestimmt das Ziel des Links, der Inhalt des Elements ```a``` bestimmt den Text, den die Nutzer auf der Homepage sehen. Fährt man mit der Maus über den Link ohne zu klickern (*hovern*), sieht man das Ziel des Links. Man kann Nutzer täuschen, indem man den Wert des Attributs ```href``` auf den Wert ```http://www.uni-regensburg.de``` setzt. Derartige Aktivitäten, die das Ziel haben die Nutzer zu täuschen, lassen sich mit dem Oberbegriff **Phishing** bezeichnen. Links auf die eigene Seite lassen sich durch die alleinige Eingabe des Dateinamens (z.B. ```image.html```) als Ziel für den Link erstellen.

# URL-Parameter mit GET

Mit einer URL lassen sich nicht nur Dateien von einem Webserver abrufen, sondern auch Informationen an den Webserver übertragen.

Sucht man man mit Google nach einem Begriff, ändert sich die URL im Browser wie folgt:

```https://www.google.de/search?q=robot&...``` 

 Der Key ```q``` (= *query* oder Suchbegriff) hat in obiger URL den Wert ```robot```, nach dem Zeichen ```&```, folgen weitere Variablen.

Diese Variablen sind Teil des GET requests und lassen sich im Network-Tab der Chrome Developer Tools anzeigen:

![08_get_params](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_get_params.png)

Alle vom Browser aufgerufenen URLs werden in der History des Browsers gespeichert, d.h. sensitive Daten sollten nicht per GET übergeben werden.

Das folgende Beispiel ```search_0.html``` zeigt, wie es mithilfe eines Formulars möglich ist, einen GET request an einen Webserver (in diesem Fall Google) zu schicken.

~~~html
<!DOCTYPE html>

<!-- Demonstrates form -->

<html lang="en">
    <head>
        <title>search</title>
    </head>
    <body>
        <form action="https://www.google.com/search" method="get">
            <input name="q" type="search">
            <input type="submit">
        </form>
    </body>
</html>
~~~

Das Element ```form``` erlaubt es mehrere Eingaben des Nutzers zu erfassen und an einen Server zu senden. Das Attribut ```action``` legt fest, dass die Such-URL von Google aufgerufen werden soll, wenn das Formular abgeschickt wird. Das Element ```input``` ermöglicht die Eingabe eines Suchbegriffs, das Attribut ```name``` legt den Schlüssel der Variable für die URL fest, die Eingabe des Nutzers ist der Wert. Gibt der Nutzer *robot* ein und klickt auf den Absendebutton (```<input type="submit">```) erzeugt der Browser die URL ```https://www.google.de/search?q=robot``` und versendet damit eine Suchanfrage an Google.

# CSS

Mithilfe von HTML lässt sich die Struktur und der Inhalt einer Webseite festlegen, das Aussehen wird aber nur durch den Browser bestimmt. Mithilfe von CSS (Cascading Style Sheets) lassen sich Webseiten optisch gestalten.

Das folgende Beispiel ```home_0.html``` zeigt den Code für eine einfache Homepage:

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <title>home</title>
    </head>
    <body>
        <p>
            John Harvard
        </p>
        <p>
            Welcome to my home page!
        </p>
        <p>
            Copyright (c) John Harvard
        </p>
    </body>
</html>
~~~

Die Seite lässt sich mit dem Element ```div``` in mehrere Bereiche teilen (```home_1.html```):

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <title>home</title>
    </head>
    <body>
        <div>
            John Harvard
        </div>
        <div>
            Welcome to my home page!
        </div>
        <div>
            Copyright (c) John Harvard
        </div>
    </body>
</html>
~~~

Das Element ```div``` ist ein leerer Container, der weder für Menschen noch für Computer eine Bedeutung hat. In HTML gibt es daher vordefinierte Elemente, die ebenfalls dazu dienen eine Webseite in mehrere Bereich zu unterteilen, die aber zusätzlich eine Bedeutung haben (semantisches HTML):

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <title>home</title>
        <style>
          header {
            font-size: large;
            text-align: center;
          }

          main {
            font-size: medium;
            text-align: center;
          }

          footer {
            font-size: small;
            text-align: center;
          }
        </style>
    </head>
    <body>
        <header>
            Donald Duck
        </header>
        <main>
            Welcome to my home page!
        </main>
        <footer>
            Copyright (c) Donald Duck
        </footer>
    </body>
</html>
~~~

Im ```head``` wurde ein neues HTML-Element ```style``` ergänzt. Dieses Element enthält CSS-Anweisungen, die aus einem Selektor (d.h. das oder die Elemente die gestaltet werden sollen) wie beispielsweise ```header``` und Schlüssel-Wert Paaren (oder CSS-Anweisungen) bestehen, die das Aussehen für den durch den Selektor ausgewählten Elementen festlegen: ``` font-size: large;``` legt beispielsweise eine Schriftgröße fest. Der obige Code wiederholt aber dreimal die Anweisung zum Zentrieren des Texts, das Beispiel nutzt Vererbung oder Kaskadierung (**Cascading** Style Sheets) indem die Anweisungen sich vom ```body```auf die Kindelemente übertragen:

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <title>home</title>
        <style>
          body {
            text-align: center;
          }

          header {
            font-size: large;
          }

          main {
            font-size: medium;
          }

          footer {
            font-size: small;
          }
        </style>
    </head>
    <body>
        <header>
            Donald Duck
        </header>
        <main>
            Welcome to my home page!
        </main>
        <footer>
            Copyright (c) Donald Duck
        </footer>
    </body>
</html>
~~~

Die obigen Beispiele haben HTML-Elemente direkt über den Namen des Elements selektiert (z.B. ```header``` und ```main```). Eine flexiblere Möglichkeit, um Elemente auszuwählen bieten **CSS-Klassen** in dem folgenden Beispiel ```home_5.html```:

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <title>home</title>
        <style>
          .centered {
            text-align: center;
          }

          .large {
            font-size: large;
          }

          .medium {
            font-size: medium;
          }

          .small {
            font-size: small;

          }
        </style>
    </head>
    <body>
        <header class="centered large">
            Donald Duck
        </header>
        <main class="centered medium">
            Welcome to my home page!
        </main>
        <footer class="centered small">
            Copyright (c) Donald Duck
        </footer>
    </body>
</html>
~~~

Eine Klasse lässt sich mit CSS durch ergänzen eines ```.``` vor den Selektor. Der Name des Selektors ist jetzt kein Name eines Elements mehr sondern eine selbstgewählte Bezeichnung. Im obigen Beispiel wurden die Klassen ```.centered```,  ```.large```, ```.medium``` und ```.small``` erstellt.

Soll ein HTML-Element mit den erstellten Klassen formatiert werden, kann diesem Element das Attribut ```class``` mit den gewünschten Klassen als Werte übergeben werden (Achtung: Klassen durch Leerzeichen, nicht durch Komma trennen).

Im letzten Schritt wird das CSS in eine separate Datei ausgelagert, damit sich das CSS für eine Website mit mehreren Seiten auf jeder Seite einbinden lässt und so mehrfach verwendet werden kann (```home_6,html```:

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <title>home</title>
        <link href="home.css" rel="stylesheet">
    </head>
    <body>
        <header class="centered large">
            Donald Duck
        </header>
        <main class="centered medium">
            Welcome to my home page!
        </main>
        <footer class="centered small">
            Copyright (c) Donald Duck
        </footer>
    </body>
</html>
~~~

Das dazugehörige CSS steht in ```home.css```:

~~~css
.centered {
  text-align: center;
}

.large {
  font-size: large;
}

.medium {
  font-size: medium;
}

.small {
  font-size: small;
}
~~~

Das HTML-Dokument enthält eine neue Zeile ```link...``` zur Einbindung der CSS-Anweisungen aus einer weiteren Datei vom Server. ```home.css``` enthält alle CSS-Anweisungen, die vorher im Element ```style``` im ```head``` der HTML-Datei waren.

Das Auslagern in eine separate CSS-Datei ist ein Grund, warum einb Browser mehrere requests an einen Webserver sendet, bis eine Webseite vollständig auf dem Browser dargestellt werden kann.

CSS ermöglicht zusätzlich eine Selektion von Elementen über das Attribut ```id```. Die HTML-Elemente erhalten das Attribut ```id```, um die CSS Formatierung mit ```#``` zu erhalten (```paragraphs_1.html```):

~~~html
<!DOCTYPE html>

<!-- Demonstrates ID selector -->

<html lang="en">
    <head>
        <style>

            #first
            {
                font-size: larger;
            }

        </style>
        <title>paragraphs</title>
    </head>
    <body>
        <p id="first">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        </p>
        <p>
            Mauris ut dui in eros semper hendrerit. Morbi vel elit mi.
        </p>
    </body>
</html>
~~~

Im obigen Beispiel erscheint nur der erste Textabsatz in einer größeren Schriftart. Im Gegensatz zu Klassen  dürfen ```ids``` nur einem Element auf der HTML-Seite zugewiesen werden. D.h. ers darf kein zweites  HTML-Element mit dem Attribut ```id="first"``` auf der gleichen Seite geben.

In Chrome lassen sich nach Rechtsklick auf den Inhalt der Website und Auswahl von Inspect aus dem Kontextmenü die CSS-Anweisungen im Tab Elements ansehen und manipulieren. Dies ändert nicht den Quellcode der Seite ermöglicht aber ein Experimentieren mit Live-Ansicht.

Für CSS gibt es zahlreiche Quellen im Netz auf denen sich CSS-Eigenschaften und mögliche Werte nachlesen lassen. Sie müssen und können diese als Entwickler nicht alle auswendig kennen.

Zum Schluss zeigt das Beispiel wie sich die Darstellung einer Webseite interaktiv anpassen lässt am Beispiel eines Link der seine Darstellung anpasst, wenn Nutzer mit der Maus über den Link fahren (```link_3.html```):

~~~html
<!DOCTYPE html>

<!-- Demonstrates pseudo attribute selectors -->

<html lang="en">
    <head>
        <style>

            a {
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }
        </style>
        <title>link</title>
    </head>
    <body>
        Besuchen Sie die <a href="https://www.oth-regensburg.de/">OTH Regensburg</a>.
    </body>
</html>
~~~

# Frameworks - Bootstrap

Die Darstellung von Webseiten für größere Webprojekte lässt sich mit den vorgestellten Technologien HTML und CSS "from scratch", d.h. von Grund auf umsetzen. Allerdings erfordert dies viel Handarbeit, da beispielsweise Schriftart, Farben und Abstände alle in eigenen CSS-Anweisungen erstellt werden müssen.

Damit Entwickler das Rad nicht immer neu erfinden müssen gibt es **Frameworks**. Diese stellen häufig benötigten Code bereit, auf dem Entwickler aufsetzen können und den sie mit eigenem Code ergänzen können. Frameworks können so die Entwicklung von Anwendungen beschleunigen. **Bootstrap** ist ein Framework das die Entwicklung von HTML-Seiten erleichtert, indem es den Entwicklern CSS-Klassen anbietet, welche diese HTML-Elementen zuweisen können. Mit Bootstrap können Entwickler, wenn sie wollen, auf das Schreiben eigener CSS-Anweisungen verzichten. Beispielsweise lässt sich eine farbige Box mit einer Infomeldung wie folgt in Bootstrap umsetzen (vgl. https://getbootstrap.com/docs/5.1/components/alerts/):

~~~html
<div class="alert alert-info" role="alert">
  A simple info alert—check it out!
</div>
~~~

Die Klassen ```alert``` und ```alert-warning``` stammen aus dem Bootstrap Framework und bestimmen das Aussehen des HTML-Elements.

Das folgende Beispiel zeigt die Funktionsweise von Bootstrap anhand einer Tabelle.

```table_no_bootstrap.html``` ist eine Standardtabelle in HTML, ohne CSS:

~~~html
<!DOCTYPE html>

<!-- Demonstrates table -->

<html lang="en">
    <head>
        <title>table</title>
    </head>
    <body>
        <table>
            <thead>
              <th>Titel</th>
              <th>Erscheinungsjahr
            </thead>
            <tbody>
              <tr>
                  <td>Jäger des verlorenen Schatzes</td>
                  <td>1981</td>
              </tr>
              <tr>
                  <td>Indiana Jones und der Tempel des Todes</td>
                  <td>1984</td>
              </tr>
              <tr>
                  <td>Jäger des verlorenen Schatzes</td>
                  <td>1981</td>
              </tr>
              <tr>
                  <td>Indiana Jones und der letzte Kreuzzug</td>
                  <td>1989</td>
              </tr>
              <tr>
                  <td>Indiana Jones und das Königreich des Kristallschädels</td>
                  <td>2008</td>
              </tr>
              <tr>
                  <td>Indiana Jones 5</td>
                  <td>2023</td>
              </tr>
            </tbody>
        </table>
    </body>
</html>
~~~

Auf der Dokumentation von Bootstrap (https://getbootstrap.com/docs/5.1/getting-started/introduction/) findet man den Hinweis, dass man den folgenden Code im ```head``` des HTML-Dokuments integrieren muss, um das Framework zu verwenden:

~~~
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
~~~

Kopiert man den Code in den ```head``` sieht das Ergebnis besser aus, es fällt auf, dass die Schriftart formatiert wurde und die Einrückungen anders sind. Allerdings sieht die Tabelle nicht wie eine Tabelle aus. Dazu bietet Bootstrap eine Dokumentation der einzelnen Komponenten. Auf der Seite https://getbootstrap.com/docs/4.0/content/tables/ kann man nachlesen, dass eine Tabelle die CSS-Klasse ```table``` aus dem Bootstrap Framework benötigt.

Das Beispiel ```table_bootstrap.html``` zeigt den um die Klasse ergänzten Code:

~~~html
<!DOCTYPE html>

<!-- Demonstrates table -->

<html lang="en">
    <head>
        <title>table</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
        <table class="table">
            <thead>
              <th>Titel</th>
              <th>Erscheinungsjahr
            </thead>
            <tbody>
              <tr>
                  <td>Jäger des verlorenen Schatzes</td>
                  <td>1981</td>
              </tr>
              <tr>
                  <td>Indiana Jones und der Tempel des Todes</td>
                  <td>1984</td>
              </tr>
              <tr>
                  <td>Jäger des verlorenen Schatzes</td>
                  <td>1981</td>
              </tr>
              <tr>
                  <td>Indiana Jones und der letzte Kreuzzug</td>
                  <td>1989</td>
              </tr>
              <tr>
                  <td>Indiana Jones und das Königreich des Kristallschädels</td>
                  <td>2008</td>
              </tr>
              <tr>
                  <td>Indiana Jones 5</td>
                  <td>2023</td>
              </tr>
            </tbody>
        </table>
    </body>
</html>

~~~

Öffnet man diese Seite im Browser wird die Tabelle so formatiert, wie in der Dokumentation von Bootstrap dargestellt.

Auch die Google-Suchseite lässt sich mit Bootstrap anpassen:

~~~html
<!DOCTYPE html>

<html lang="en">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>search</title>
    </head>
    <body>
        <div class="container-fluid">

            <ul class="m-3 nav">
                <li class="nav-item">
                    <a class="nav-link text-dark" href="https://about.google/">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link text-dark" href="https://store.google.com/">Store</a>
                </li>
                <li class="nav-item ms-auto">
                    <a class="nav-link text-dark" href="https://www.google.com/gmail/">Gmail</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link text-dark" href="https://www.google.com/imghp">Images</a>
                </li>
                <li class="nav-item">
                    <a class="btn btn-primary" href="https://accounts.google.com/ServiceLogin" role="button">Sign in</a>
                </li>
            </ul>

            <div class="text-center">
              <img alt="Happy Cat" class="img-fluid w-25" src="cat.gif">
              <form action="https://www.google.com/search" class="mt-4" method="get">
                  <input autocomplete="off" autofocus class="form-control form-control-lg mb-4 mx-auto w-50" name="q" placeholder="Query" type="search">
                  <button class="btn btn-light" type="submit">Google Search</button>
                  <button class="btn btn-light" name="btnI" type="submit">I'm Feeling Lucky</button>
              </form>
 
          </div>
        </div>
          
    </body>
</html>
~~~

Die Seite beginnt mit einem ```<div>``` Tag, der die Inhalte einrückt und an die Breite des Bildschirms anpasst. Anschließend folgt eine Liste Elementen und Klassen entsprechend der Bootstrap-Dokumention, um die Links und Buttons im Header anzuzeigen. Abschließend folgt das Bild einer Katze und weitere Klassen für das Suchformular.

Kleinere Anpassungen der Abstände erfolgen mit den CSS-Klassen ```w-25```, ```mt-4``` oder ```m-3```. Sie müssen Bootstrap nicht bis ins Detail beherrschen, aber erkennen, dass Frameworks helfen Entwicklungsarbeit zu beschleunigen und Anpassungen im Detail (wie die Veränderung der Abstände) dann als Finetuning erfolgen kann.

# JavaScript

Bisher haben wir HTML, CSS und Bootstrap kennengelernt. Zusammen helfen Sie die Webseiten ansprechend zu gestalten. Die Webseiten sind aber immer statisch, d.h. Nutzer können auf der Seite zwar auf Links klicken, sie werden dann aber immer zu einer weiteren Seite weitergeleitet. Mithilfe von **JavaScript** lassen sich Webseiten interaktiver gestalten.

Die Syntax ähnelt der Syntax von Python und für alle Scratch Elemente gibt es Entsprechungen in JavaScript:

![08_scratch_set](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_scratch_set.png)

~~~javascript
let counter = 0;
~~~

![08_scratch_increment](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_scratch_increment.png)

~~~javascript
counter = counter + 1;
counter += 1;
counter++;
~~~

![08_scratch_if_else](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_scratch_if.png)

~~~javascript
if (x < y) {

}
~~~

![08_scratch_if_else](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_scratch_if_else.png)

~~~javascript
if (x < y) {

} else {

}
~~~

![08_scratch_if_else_else](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_scratch_if_else_else.png)

~~~javascript
if (x < y) {

} else if (x > y) {

} else {

}
~~~

![08_scratch_while](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_scratch_while.png)

~~~javascript
while (true) {

}
~~~

![08_scratch_for](/Users/markus/Dropbox/_additional shares/_be_disc/semester1_technology_skills/08_web/notes/img/08_scratch_for.png)

~~~javascript
for (let i = 0; i < 3; i++) {

}
~~~

```let``` wird in JavaScript verwendet, um Variablen zu deklarieren.

Mithilfe von JavaScript lässt sich die Darstellung im Browser durch Manipulation der HTML-Elemente nahezu in Echtzeit anpassen. JavaScript lässt sich in einem HTML-Tag Skript in eine HTML-Datei einfügen oder kann (wie CSSS) aus einer externen Datei geladen werden.

JavaScript kann zusammen mit einem Formular verwendet werden (```hello_js_0.html```):

~~~html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>hello</title>
    </head>
    <body>
        <form onsubmit="greet(); return false;">
            <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
        <script>

            function greet() {
                alert("Hallo Du!");
            }

        </script>
    </body>
</html>
~~~

Das Formular verfügt über kein Attribut ```action```, da das Formular keine Daten an weitere Seiten senden soll, sondern eine JavaScript Funktion auf der selben Seite. Stattdessen verfügt das Formular über ein Attribut ```onsubmit```, in dem eine Funktion aufgerufen wird, sobald die Nutzer auf den Submit Button klicken abgeschickt wird. ```return: false``` verhindert, dass das Formular abgeschickt wird. Lädt man die Seite im Browser und klickt auf Submit, erscheint der Text "Hallo Du!".

Im ```head``` der HTML-Datei befindet sich ein Element ```script```, in welchem die JavaScript-Funktion ```greet()```  definiert ist. 

Bis jetzt ist die Begrüßung aber immer die selbe. Um persönlich begrüßt zu werden lässt sich das Attribut ```id=name``` des Eingabefelds für den Namen der Nutzer verwenden (```hello_js_1.html```):

~~~html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>hello</title>
    </head>
    <body>
        <form onsubmit="greet(); return false;">
            <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
    <script>

            function greet() {
                let name = document.querySelector("#name").value;
                alert("Hallo " + name + "!");
            }

        </script>
    </body>
</html>
~~~

```document``` ist eine globale Variable, die von JavaScript im Browser bereitgestellt wird und repräsentiert das gesamte HTML-Dokument mit all seinen Elementen. ```document``` bietet die Methode ```querySelector```, mit der Elemente aus dem **DOM** (d.h. der internen JavaScript-Baumstruktur aller HTML-Elemente) abfragen lassen.

Mithilfe von JavaScript kann man auf **Events** reagieren, d.h. ganz allgemein Dinge die auf der Seite passieren, wie beispielsweise das Absenden eines Fomulars (``` onsubmit```).

Mit anonymen Funktionen (d.h. Funktionen ohne Namen) lassen sich diese Events auch im Code abfangen und nicht über Attribute von HTML-Elementen definieren (```hello_js_2.html```):

~~~html
<!DOCTYPE html>

<!-- Demonstrates addEventListener -->

<html lang="en">
    <head>
        <title>hello</title>
    </head>
    <body>
        <form>
            <input autocomplete="off" autofocus id="name" placeholder="Name" type="text">
            <input type="submit">
        </form>
        <script>

            document.querySelector('form').addEventListener('submit', function(event) {
                alert('hello, ' + document.querySelector('#name').value);
                event.preventDefault();
            });

        </script>
    </body>
</html>
~~~

Der Funktion ```addEventListener``` wird als zweiter Parameter eine Funktion ohne Namen ```function(event)``` übergeben. Diese Funktion erhält automatisch, wenn sie aufgerufen wird, einen Parameter ```event```. Dieser kann dann mittels ```event.preventDefault()``` verhindern, dass das Formular Daten an eine andere Webseite übermittelt (vgl. ```return false;```) aus dem obigen Beispiel.

Mittels JavaScript lässt sich auch das Aussehen der Seite verändern (```hello_js_3.html```):

~~~html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>background</title>
    </head>
    <body>
        <button id="red">R</button>
        <button id="green">G</button>
        <button id="blue">B</button>
        <script>

            let body = document.querySelector('body');
            document.querySelector('#red').addEventListener('click', function()
            {
                body.style.backgroundColor = 'red';
            });

            document.querySelector('#green').addEventListener('click', function() {
                body.style.backgroundColor = 'green';
            });

            document.querySelector('#blue').addEventListener('click', function() {
                body.style.backgroundColor = 'blue';
            });

        </script>
    </body>
</html>
~~~

Bei jedem, Klick (= event ```click```) auf einen Button wird jeweils eine anonyme Funktion aufgerufen. Diese verändert dann die Farbe des Elements ```body``` der Webseite.

JavaScript kann auch dazu verwendet werden ein HTML-Element blinken zu lassen:

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <script>

            // Toggles visibility of greeting
            function blink()
            {
                let body = document.querySelector('body');
                if (body.style.visibility == 'hidden')
                {
                    body.style.visibility = 'visible';
                }
                else
                {
                    body.style.visibility = 'hidden';
                }
            }
  
            // Blink every 500ms
            window.setInterval(blink, 500);
  
        </script>
        <title>blink</title>
    </head>
    <body>
        hello, world
    </body>
</html>
~~~

Das folgende Beispiel implementiert ein Formular mit Autocomplete unter Verwendung eines Arrays in JavaScript:

~~~html
<!DOCTYPE html>
  
<html lang="en">
  
    <head>
        <title>autocomplete</title>
    </head>
  
    <body>
  
        <input autocomplete="off" autofocus placeholder="Query" type="text">
  
        <ul></ul>
  
        <script src="large.js"></script>
        <script>
      
            let input = document.querySelector('input');
            input.addEventListener('keyup', function(event) {
                let html = '';
                if (input.value) {
                    for (word of WORDS) {
                        if (word.startsWith(input.value)) {
                            html += `<li>${word}</li>`;
                        }
                    }
                }
                document.querySelector('ul').innerHTML = html;
            });
  
        </script>
  
    </body>
</html>
~~~

In ```large.js``` wird ein Array aus Wörtern definiert. Mithilfe des Events ```keyup``` wird jedesmal eine anonyme Funktiopn aufgerufen, wenn die Nutzer eine Eingabe in dem Eingabefeld machen, d.h. eine Taste loslassen. 

Sieht man sich die Seite im Browser an, entsteht während des Tippens eine Liste von Suchbegriffen unter dem Eingabefeld.

Das Beispiel ```geolocation.html```zeigt, wie sich die Koordinaten des Nutzers ermitteln lassen:

~~~html
<!DOCTYPE html>
  
<html lang="en">
    <head>
        <title>geolocation</title>
    </head>
    <body>
        <script>
            navigator.geolocation.getCurrentPosition(function(position) {
                document.write(position.coords.latitude + ", " + position.coords.longitude);
            });
  
        </script>
    </body>
</html>
~~~

Diese Koordinaten könnten jetzt verwendet werden, um die Position der Nutzer auf einer Karte anzuzeigen.

Quelle: Angepasst und ergänzt von CS50, Harvard University, 2022 - https://cs50.harvard.edu/x/2022/

