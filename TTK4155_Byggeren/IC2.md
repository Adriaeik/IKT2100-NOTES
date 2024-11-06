I2C, eller *Inter-Integrated Circuit* bus, er eit kommunikasjonssystem utvikla for å gjere det enkelt for integrerte krinsar (IC-er) å utveksle data med kvarandre via ei to-leidnings bussforbindelse. Bussystemet krev berre to leidningar: ei seriell datalinje (SDA) og ei seriell klokkeline (SCL) for å kunne sende data mellom ein "master"- og ein "slave"-enhet. Dette designet reduserer talet på naudsynt kabling og kompliserte grensesnitt mellom ulike komponentar i eit system, noko som gjer det ideelt for bruksområde der ein treng enkel og effektiv kommunikasjon mellom einingar i t.d. konsumelektronikk og industriell elektronikk【9†source】.

Nokre av hovudtrekka ved I2C inkluderer:

1. **Fleksibilitet i busshastigheit**: I2C tilbyr fleire modusar:
   - *Standard Mode*: opptil 100 kbit/s,
   - *Fast Mode*: opptil 400 kbit/s,
   - *Fast Mode Plus (Fm+)*: opptil 1 Mbit/s, og
   - *High-Speed Mode (Hs)*: opptil 3,4 Mbit/s.
   Det finst også ein *Ultra-Fast Mode* som gir hastigheiter opptil 5 Mbit/s, men denne modusen er retningsbestemt (unidireksjonal)【9†source】.

2. **Adressebasert kommunikasjon**: Alle einingar på I2C-bussen har unike adresser, slik at "master"-enheten kan sende og motta data med spesifikke "slave"-einingar utan interferens frå andre einingar.

3. **Multi-master funksjon**: I2C støttar multi-master-arkitektur, som betyr at fleire master-enheter kan vere tilkopla same bus, og det finst mekanismer for kollisjonsdeteksjon og prioritert tilgang til bussen for å unngå datafeil【10†source】.

4. **Støtte for mange einingar**: Teoretisk sett er det ingen grenser for talet på einingar som kan tilkoplast bussen, men den totale kapasiteten til bussen kan vere avgrensa av den samla buskapasiteten. Høgare kapasitet kan tillatast under spesielle tilhøve, noko som gjer I2C-bussen skalerbar til ulike behov【9†source】.

Denne bus-arkitekturen er mykje brukt i ulike tekniske applikasjonar som LCD-drivarar, sanntidsklokker, EEPROM-minne, temperatursensorar og andre integrerte krinsar der ein treng ein effektiv og enkel metode for kommunikasjon mellom einingar【10†source】.