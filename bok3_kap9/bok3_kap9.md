**MODBUS** er ein seriekommunikasjonsprotokoll utvikla av Modicon (no Schneider Electric) på slutten av 1970-talet, primært for kommunikasjon med **PLC-ar** (Programmerbare Logiske Kontrollar). MODBUS opererer på **applikasjonslaget** i OSI-modellen og brukar ein **klient-server-arkitektur** for å tillate kommunikasjon mellom einingar i eit nettverk.

### Hovudtrekk:
- **Kommunikasjonsmodell**: Brukar ein *master-slave*-modell, der masteren startar alle transaksjonar. Ein master kan kommunisere med opptil 247 slaver.
- **Val av fysiske medium**: MODBUS støttar fleire fysiske medium, som RS-422, RS-485, og 20 mA strømsløyfer. Dette gir fleksibilitet for ulike installasjonar.
- **Protokollens stabilitet og utbreiing**: Sidan 1979 har MODBUS blitt ein industristandard for seriell kommunikasjon, spesielt innan automatisering, sjølv om den er noko seinare enn andre bussar.

### Teknisk oppbygging:
- MODBUS bruker eit **fast rammeformat** for meldingar, som inkluderer funksjonskode, datafelt og kontrollsum for feilsjekking.
- Protokollen er relativt enkel og lett å implementere, noko som har bidratt til at den har fått brei aksept.
  
MODBUS si popularitet kjem av den enkle strukturen og fleksibiliteten, sjølv om den manglar sertifisering for kompatibilitet og kan vere litt seint samanlikna med nyare protokollar.


### 1. Communication Stack
MODBUS kan bli implementert ved hjelp av ulike fysiske medium og protokollar:
- **TCP/IP over Ethernet**: Brukar Ethernet som transportlag, som gir høgare overføringshastigheit og enklare integrasjon i moderne nettverk.
- **Asynkron seriell overføring**: Kan bruke medium som RS-232, RS-422, RS-485, fiber, og radio. Dette er den tradisjonelle MODBUS-protokollen, spesielt for industrielle miljø med låg bandbreidde.
- **MODBUS Plus**: Ein høghastigheits token-passing metode som støtter meir avansert kommunikasjon mellom einingar.

### 2. Network Architecture
MODBUS støttar ein hierarkisk nettverksstruktur der forskjellige typar einingar (som PLC-ar, HMI, og I/O-einingar) kan koplast til MODBUS-nettverket via gatewayar. Dette gjer det mogleg å bruke fleire MODBUS-variantar (som MODBUS TCP/IP og MODBUS RS-485) i same nettverk.

### 3. Communication Transactions
MODBUS brukar ein **master-slave** kommunikasjonsmodell, der masteren startar alle kommunikasjonar og slavane berre responderer:
- **Svar frå slaven**: Slavane kan respondere ved å utføre handlingar, gi tilbake nødvendig informasjon, eller gi beskjed dersom ei handling ikkje kan utførast.
- **Exception Response**: Dersom slaven ikkje kan utføre den ønskte handlinga, sender den ein *exception response* til masteren med informasjon om feilen. Denne meldinga inneheld:
  - Adressa til slaven.
  - Handlinga slaven vart bedt om å utføre.
  - Ei indikering på kvifor handlinga ikkje kunne utførast.

MODBUS sin enkle struktur og fleksibilitet gjer protokollen spesielt populær i automatiseringsmiljø der stabilitet og kompatibilitet er viktig.

### 9.4.1 Master–Slave and Broadcast Communication
I MODBUS kan masteren kommunisere individuelt med ein bestemt slave ved hjelp av *unicast mode*, der meldinga er adressert til éin slave. Alternativt kan den sende ei melding til alle slavane samtidig i *broadcast mode*. Slavane responderer berre på unicast-meldingar og ignorerer broadcast-meldingar.

### 9.4.2 Query–Response Cycle
I MODBUS blir alle transaksjonar starta av masteren gjennom ein *query–response cycle*. Ein førespurnad frå masteren inneheld fire felt:
- **Address Field**: Spesifiserer adressa til slaven meldinga er retta mot. Adressa varierer frå 1 til 247, medan adressa "0" er reservert for broadcast.
- **Function Field**: Inneheld funksjonskoden (1–255) som indikerer handlinga slaven skal utføre. Eksempel på handlingar inkluderer lesing av status eller innhald i register.
- **Data Field**: Inneheld registerverdiar eller adresser som trengs for oppdraget. Dette feltet kan variere avhengig av funksjonen.
- **Error Check Field**: Brukast for å verifisere integriteten til meldinga, vanlegvis gjennom **CRC** (Cyclic Redundancy Check) i RTU-modus eller **LRC** (Longitudinal Redundancy Check) i ASCII-modus.

Når slaven responderer, returnerer den meldinga til masteren med same struktur, inkludert adressa og funksjonskoden.

### 9.5 Protocol Description: PDU and ADU
I MODBUS-protokollen er **Protocol Data Unit (PDU)** kjernen av meldinga og inneheld funksjonskoden og dataen. For at PDU skal kunne sendast over ulike nettverk, vert den kombinert med andre komponentar, som adressering og feilsjekking, for å danne ein **Application Data Unit (ADU)**.

- **ADU**: Inneheld adresse, funksjonskode, data og eit feilsjekkfelt.
- **PDU**: Er ein del av ADU-en og inneheld funksjonskode og data.

I MODBUS TCP/IP vert feilsjekkinga handtert av TCP-protokollen, og difor er feilsjekkfeltet ikkje inkludert i ADU-en ved bruk av TCP.

### 9.6 Transmission Modes
MODBUS støttar to overføringsmodusar for seriell dataoverføring:
- **RTU Mode**: Hovudmodus som bruker binærkoding og har ein kompakt datalengde, noko som gjer den rask og påliteleg.
- **ASCII Mode**: Bruker ASCII-teikn for datarepresentasjon og er enklare å lese manuelt, men er mindre effektiv og brukar lengre meldingar.

#### 9.6.1 ASCII Mode
I ASCII-modus vert kvar byte representert av to ASCII-teikn. Feilsjekk skjer med **LRC (Longitudinal Redundancy Check)**, og den typiske strukturen har start- og sluttfelt for kvar melding. ASCII-modus gjer meldinga meir lesbar, men nyttar dobbelt så mykje plass som RTU.

#### 9.6.2 RTU Mode
RTU-modus sender data som to heksadesimale teikn per byte og brukar **CRC (Cyclic Redundancy Check)** for feilsjekk. Denne modusen er meir effektiv og brukar færre byte enn ASCII-modus, og den har difor auka bruk i industrielle miljø.

### 9.7 Message Framing
For å sikre korrekt overføring av meldingar er MODBUS-meldingar ramma inn:
- **Start og sluttteikn**: Definerer byrjinga og slutten på meldinga.
- **Adressefelt**: Identifiserer den aktuelle slaven i unicast-meldingar eller spesifiserer broadcast.
- **Funksjonskode og datafelt**: Inneheld informasjon om ønskte handlingar og eventuelle data for utføring av desse.
- **Feilsjekkfelt**: Sikrar integriteten til meldinga.

#### 9.7.1 ASCII Framing
I ASCII-framing består kvar melding av seks felt: start, adresse, funksjonskode, data, LRC og slutt. Meldinga startar med ein kolon og sluttar med ein carriage return (CR) og line feed (LF).

#### 9.7.2 RTU Framing
RTU-framing krev ein stille periode på minst 3,5 teiknlengder for å markere starten og slutten av meldinga. Det er krav om at meldinga må sendast i ein samanhengande straum utan opphald; elles vil ein feil oppstå.

**9.8 MODBUS TCP/IP**

MODBUS TCP/IP blei introdusert i 1999 og gjev fleire fordelar. Den baserer seg på Ethernet og er open, enkel og rask, med moglegheit for overføringsfartar over 1 kB/s på ein enkel stasjon. Teknisk sett er MODBUS TCP/IP berre MODBUS med ein TCP-wrapper, noko som betyr at MODBUS-einingar kan kommunisere direkte over TCP/IP. Ein gateway er nødvendig for å omforme mellom fysiske MODBUS-linjer som RS-232, RS-485 osv., og Ethernet. MODBUS-ramma pakkast då inn i MODBUS TCP/IP-ramma for overføring over Ethernet.

MODBUS TCP/IP brukar vanlege IP-adresser og ein einingsidentifikator for å identifisere einingar i nettverket, og nyttar TCP sin 32-bits CRC-sjekksum i staden for MODBUS sin vanlege 16-bits sjekksum. Den tradisjonelle master-slave-arkitekturen er endra til ein klient-server-modell i MODBUS TCP/IP, der kvar førespurnad må ha ei tilhøyrande respons.

**9.9 INTRODUCTION TO MODBUS PLUS**

MODBUS Plus er ein utvida variant av den opprinnelege MODBUS-protokollen, utvikla for å overkomme einskildmaster-begrensinga i vanleg MODBUS. MODBUS Plus brukar eit LAN-baserte token-passing-protokoll som kan knytte ulike MODBUS-segment til ei større, geografisk distribuert eining. Kvar eining i nettverket kan kommunisere med inntil 64 einingar ved hjelp av adresser frå 01 til 64, med meldingar som kan ruterast opptil fem lag djup.

**9.10 MESSAGE FRAME**

MODBUS Plus-meldingsramma består av fleire felt: preamble, åpningsflagg, broadcast-adresse, MAC/LLC-data, ein feilsjekk (error check), og eit avsluttingsflagg. Dei variable datafelta inkluderer mellom anna destinasjonsadresse, MAC-funksjon og routing-path.

### 9.11 Networking MODBUS Plus
**MODBUS Plus** kan støtte opptil 64 noder i eitt nettverk. På éin seksjon kan opptil 32 noder koblast til med ei maksimal kabellengd på 450 meter mellom dei to nærmaste nodene. For å auke nodetalet, kan repeaters brukast, noko som aukar kabelgrensa til 1800 meter. Fiberkabel kan også brukast for lengre avstandar. Repeaterar forlengjer lengda på éitt nettverk, mens bruer koblar saman fleire nettverk.

### Adressering og kommunikasjon
Kvar node får ei unik adresse, og det kan ikkje vere like adresser i same nettverk. Nettverket fungerer med ein token-passing-metode, der ein token blir sendt mellom nodene for å gi tilgang til å sende data. Denne tokenen blir aldri delt mellom ulike nettverk, men berre mellom noder innanfor eit nettverk.

### Token-passing-mekanismen
Token-passing-mekanismen byrjar frå den noden med lavast adresse, og roterer progressivt til høgast adresserte node. Når det blir lagt til eller fjerna noder frå nettverket, blir den nye token-passing-sekvensen oppdatert automatisk: det tar 100 ms for ei node å bli fjerna og 5 sekund for ei ny node å bli lagt til.