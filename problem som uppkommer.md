# Problem & Lösningar

1. Textfilen öppnades inte, vilket ledde till att programmet skapade fler och fler rum.

    Lösning: Specifierade filsökvägen till filen, och rensade den


2. Rummen som visades duplicerades över varandra.

    Lösning: Vi ändrade från grid till pack, för att pack_forget skulle fungera


3. Bakgrundsbild visades inte korrekt.

    Lösning: Satte en label över hela siden, och lade en bild över hela labelen
    

4. Om man klickade exit så spelades inte "hejdå" animationen.

    Lösning: Vi gjorde programmet till helskärm, och skapade en egen exit knapp

5. Om man i menyn där man kan välja rumstyp klickar på samma typ två gånger
så läggs det till kopior av samma rum över, vilket inte ska ske. 

    Lösning: Problemet uppstod pågrund av att man inte tog bort rumsalternativen från
    den menyn man varit i om man klickar på samma meny. Vi fixade problemet genom
    att göra det (ta bort dessa menyalternativ)

6. Om användaren registrerar sig igen med samma namn och mail så kommer det bli duplikaner

    Lösning: Vi valde att inte åtgärda problemet eftersom resultatet blir detsamma, d.v.s. att
    alla rummen visas för personen. 

7. Väder-appen behövde pip. Efter att vi hade lagt till väderappen i main-programmet krashade programmet ifall man ville starta det och inte hade pip

    Lösning: Vi lade till en try-accept sats. Om det inte går att importera väder-appen så hoppar programmet över det. Vilket stoppade programmet för att få error ifall pip saknades. 

8. Rum som bokats togs inte bort från listorna över de lediga rummen, och visades därmed igen om 
man klickade tillbaks till samma meny. 

    Lösning: Köra en check på de olika textfilerna för att se vilka rum som var och inte var bokade varje gång
    man klickade på ett menyval, och fixade till listorna utefter den informationen. 