**Spørsmål og Svar fra Kapittel 1: Datanettverk og Internett**

**1. Hva er forskjellen mellom en vert (host) og et endesystem i datanettverk? Er en webserver et endesystem?**

**Svar:**
I datanettverk brukes begrepene vert (host) og endesystem ofte om hverandre. Et endesystem er enhver enhet som er koblet til et nettverk og kan sende eller motta data. Dette inkluderer datamaskiner, mobiltelefoner, servere, IoT-enheter, osv. En webserver er et eksempel på et endesystem fordi den er en enhet i nettverket som gir tjenester (f.eks. levering av websider) til andre endesystemer.

**2. Hvorfor er protokoller viktige i datanettverk?**

**Svar:**
Protokoller er sett av regler og standarder som tillater kommunikasjon mellom enheter i et nettverk. De definerer hvordan data formateres, overføres og mottas, slik at forskjellige systemer kan forstå hverandre. Uten protokoller ville det være umulig å sikre pålitelig og konsistent kommunikasjon mellom ulike enheter og systemer.

**3. Beskriv de ulike typene tilgangsnettverk og deres egenskaper.**

**Svar:**
Tilgangsnettverk forbinder endesystemer til den første ruter i nettverket. Hovedtyper inkluderer:

- **Hjemmetilgang (Home Access):**
  - *Digital Subscriber Line (DSL)*: Bruker eksisterende telefonlinjer for høyhastighets Internett-tilgang.
  - *Kabelmodem*: Bruker kabel-TV-nettverket for å gi Internett-tilgang.
  - *Fiber til hjemmet (FTTH)*: Tilbyr svært høyhastighetsforbindelser direkte via fiberoptiske kabler.

- **Bedriftstilgang (Enterprise Access):**
  - *Ethernet*: Vanlig i bedriftsnettverk, tilbyr høye hastigheter over kobber- eller fiberkabler.
  - *WiFi*: Trådløse lokale nettverk som gir mobilitet innenfor et begrenset område.

- **Mobiltilgang (Wide-Area Wireless Access):**
  - *3G/4G/5G mobilnettverk*: Gir trådløs Internett-tilgang over store geografiske områder.

**4. Forklar forskjellen mellom transmisjonsforsinkelse, propageringsforsinkelse, køforsinkelse og prosesseringsforsinkelse.**

**Svar:**
- **Transmisjonsforsinkelse** er tiden det tar å sende alle bits i en pakke inn i lenken og er gitt ved $d_{\text{trans}} = \frac{L}{R}$, der $L$ er pakkelengden og $R$ er overføringsraten.
- **Propageringsforsinkelse** er tiden det tar for signalet å reise gjennom mediet fra sender til mottaker og er gitt ved $d_{\text{prop}} = \frac{d}{s}$, der $d$ er avstanden og $s$ er signalets hastighet.
- **Køforsinkelse** er tiden en pakke venter i køen på en ruter før den kan overføres. Dette avhenger av nettverkstrafikken.
- **Prosesseringsforsinkelse** er tiden det tar for ruteren å behandle pakkenes header og bestemme hvor de skal sendes videre.

**5. Diskuter fordeler og ulemper med pakkesvitsjing sammenlignet med krets-svitsjing.**

**Svar:**
*Fordeler med pakkesvitsjing:*
- Effektiv utnyttelse av nettverksressurser ved å dele båndbredde dynamisk.
- Kan håndtere bursty trafikk effektivt.
- Mindre kostnad og kompleksitet i infrastruktur.

*Ulemper med pakkesvitsjing:*
- Variabel forsinkelse og potensiell pakkeloss.
- Ikke ideell for applikasjoner som krever konstant båndbredde eller forsinkelse (f.eks. tradisjonell taletelefoni).

*Fordeler med krets-svitsjing:*
- Garantert båndbredde og forsinkelse under hele kommunikasjonen.
- Ingen pakkeloss etter at forbindelsen er etablert.

*Ulemper med krets-svitsjing:*
- Ineffektiv bruk av ressurser når forbindelsen ikke utnyttes fullt ut.
- Overhead og forsinkelse ved etablering og nedkobling av forbindelser.

**6. Hva er protokollagdeling, og hvorfor brukes det i nettverksdesign?**

**Svar:**
Protokollagdeling er praksisen med å dele nettverksfunksjonalitet inn i separate lag, der hvert lag tilbyr spesifikke tjenester til laget over og bruker tjenester fra laget under. Dette brukes fordi:

- Det gir en modulær design som er lettere å forstå og vedlikeholde.
- Det tillater uavhengig utvikling og oppdatering av hvert lag.
- Det fremmer standardisering, slik at produkter fra forskjellige leverandører kan fungere sammen.

**7. Forklar konseptet innkapsling i lagdelte protokoller.**

**Svar:**
Innkapsling er prosessen der data fra et lag pakkes inn med headerinformasjon når de sendes nedover protokollstakken. Hvert lag legger til sin egen header til dataene fra laget over, som gir nødvendig informasjon for at dataene skal behandles korrekt på mottakersiden. Ved mottak fjernes headerne i omvendt rekkefølge når dataene beveger seg oppover stakken.

**8. Beskriv hovedkomponentene i Internett-protokollstakken.**

**Svar:**
Internett-protokollstakken består av fem lag:

1. **Applikasjonslaget**: Inneholder applikasjoner og protokoller som HTTP, FTP, SMTP.
2. **Transportlaget**: Gir prosess-til-prosess dataoverføring (f.eks. TCP, UDP).
3. **Nettverkslaget**: Ansvarlig for ruting av datagrammer fra kilde til destinasjon (f.eks. IP).
4. **Lenkelaget**: Håndterer dataoverføring mellom nærliggende nettverksenheter (f.eks. Ethernet, WiFi).
5. **Fysisk lag**: Overfører rå bitstrømmer over et fysisk medium.

**9. Diskuter noen av sikkerhetstruslene som datanettverk står overfor i dag.**

**Svar:**
- **Malware**: Skadelig programvare som virus, ormer og trojanere som kan skade systemer eller stjele data.
- **Denial-of-Service (DoS) angrep**: Forsøk på å gjøre en tjeneste utilgjengelig ved å overvelde den med trafikk.
- **Distributed Denial-of-Service (DDoS) angrep**: Lignende som DoS, men trafikken kommer fra mange kompromitterte systemer (botnets).
- **Pakkesniffing**: Avlytting av nettverkstrafikk for å fange opp sensitive data.
- **IP-spoofing**: Forfalskning av IP-adresser for å skjule identiteten eller utgi seg for en annen enhet.

**10. Oppsummer den historiske utviklingen av Internett fra de tidlige begynnelser til i dag.**

**Svar:**
- **1960-tallet**: Konseptet pakke-svitsjing ble introdusert. ARPAnet, forgjengeren til Internett, ble opprettet.
- **1970-tallet**: Utviklingen av TCP/IP-protokollen, som ble standarden for dataoverføring.
- **1980-tallet**: Vekst av nettverk og standardisering av protokoller som DNS.
- **1990-tallet**: Fremveksten av World Wide Web, som gjorde Internett tilgjengelig for allmennheten.
- **2000-tallet og fremover**: Eksplosiv vekst i bredbåndstilgang, mobil Internett, sosiale medier, cloud computing, og IoT (Internet of Things), som har forvandlet måten vi kommuniserer og bruker teknologi på.

