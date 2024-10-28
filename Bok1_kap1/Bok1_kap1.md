For å forstå korleis datamaskiner kommuniserer over nettverket, er det viktig å kjenne til dei grunnleggjande nettverksprotokollane. Her er ei forklaring på nokre av dei mest sentrale:

### 1. **IP (Internet Protocol)**
IP er den grunnleggjande protokollen for å sende data mellom datamaskiner over internett. IP-adresser identifiserer kvar enkelt enhet (til dømes ein datamaskin eller ein ruter) på nettet. Det finst to versjonar av IP: IPv4 og IPv6. IPv4 bruker 32-bit adresser, noko som gir om lag 4,3 milliardar unike adresser. IPv6 bruker 128-bit adresser og har eit mykje større adresserom.

### 2. **TCP (Transmission Control Protocol)**
TCP er ein av hovudprotokollane som brukar IP for å levere data. TCP sørgjer for at data vert sendt på ein påliteleg måte ved å dele opp informasjonen i mindre pakker, sende dei, og deretter sørgje for at alle pakkane kjem fram og vert sette saman i riktig rekkefølge. Om ein pakke ikkje kjem fram, sender TCP den på nytt. Dette sikrar at mottakaren får alle dataene korrekt.

### 3. **HTTP (HyperText Transfer Protocol)**
HTTP er protokollen som vert brukt for å overføre websider frå ein webserver til ein nettlesar. Når du skriv inn ei nettadresse (URL) i nettlesaren din, sender nettlesaren ein HTTP-forespørsel til serveren om å få tilsendt innhaldet på den sida. Serveren svarar med å sende tilbake data, til dømes HTML-kode, bilete og stilark. HTTP brukar som regel TCP som transportprotokoll.

### 4. **HTTPS (HTTP Secure)**
HTTPS er ein sikra versjon av HTTP. Her blir all data kryptert, slik at ingen kan avlytte kommunikasjonen mellom deg og serveren. Dette er spesielt viktig for å beskytte sensitiv informasjon, som til dømes innlogging eller betalingsinformasjon.

### 5. **UDP (User Datagram Protocol)**
UDP er ein alternativ transportprotokoll til TCP. I motsetning til TCP, som er påliteleg men tregare, er UDP raskare men ikkje garantert påliteleg. Dette betyr at data kan kome fram i feil rekkefølge eller ikkje i det heile tatt. UDP er nyttig i situasjonar der hastigheit er viktigare enn absolutt korrektheit, til dømes i videostreaming eller online gaming.

### 6. **DNS (Domain Name System)**
DNS er som internettets telefonbok. Det omset domene (til dømes "www.google.com") til IP-adresser som maskiner kan forstå. Når du skriv inn ei nettadresse, kontrollerer datamaskina din DNS-serveren for å finne IP-adressa til serveren du vil nå.

### 7. **FTP (File Transfer Protocol)**
FTP er ein protokoll for å overføre filer mellom datamaskiner over eit nettverk. Den er mykje brukt til å laste opp eller laste ned filer frå webserverar. FTP har også ein sikra variant som heiter SFTP (Secure File Transfer Protocol) som brukar SSH (Secure Shell) for å kryptere dataoverføringa.

### 8. **SMTP (Simple Mail Transfer Protocol)**
SMTP er den protokollen som vert brukt for å sende e-post over internett. Når du sender ein e-post, bruker e-postklienten din SMTP til å sende meldinga til e-postserveren, som deretter sender den vidare til mottakarens server.

### 9. **IMAP/POP3 (Internet Message Access Protocol/Post Office Protocol)**
Desse protokollane vert brukt til å hente e-post frå ein server. IMAP lar deg lese e-post frå fleire enheter samtidig, ved å lagre e-posten på serveren. POP3 lastar derimot ned e-posten til ein enkelt enhet og slettar den deretter frå serveren.

### Oppsummering:
- **IP**: Adresserer og ruter datapakker mellom datamaskiner.
- **TCP**: Sikrar pålitelig dataoverføring.
- **HTTP/HTTPS**: Brukt til webkommunikasjon.
- **UDP**: Rask, men ikkje like pålitelig som TCP.
- **DNS**: Omset domene til IP-adresser.
- **FTP**: Brukt til filoverføring.
- **SMTP/IMAP/POP3**: Brukt til e-postkommunikasjon.

Desse protokollane samarbeider for å sikre at du kan surfe på nettet, sende e-post, streame videoar, og mykje meir.

Nettverk er bygd opp etter ein lagbasert modell som delar opp kommunikasjonen i fleire nivå. Den mest kjente modellen er **OSI-modellen** (Open Systems Interconnection), som deler opp nettverkskommunikasjonen i sju lag. I praksis brukar vi ofte ein forenkla modell kalla **TCP/IP-modellen**, som har fire lag. Her skal eg forklare begge modellane, men med fokus på korleis data flyttar seg frå sendar til mottakar, lag for lag.

### OSI-modellen (7-lagsmodellen)
OSI-modellen er ein teoretisk modell som deler opp kommunikasjonen i sju lag, frå fysisk overføring til applikasjonar.

1. **Lag 1: Fysisk lag (Physical Layer)**
   - Dette er det lågaste laget, som omfattar den fysiske overføringa av data gjennom kablar, radiobølger eller annan fysisk medium. Her snakkar vi om elektriske signal, radiosignal eller lys i fiberoptiske kablar. Alle komponentar som nettverkskablar, hubbar og radiomottakarar opererer på dette laget.

2. **Lag 2: Lenkelag (Data Link Layer)**
   - Dette laget er ansvarleg for overføring av data mellom to direkte tilknytte noder (f.eks. mellom ein datamaskin og ein ruter) i same nettverk. Her finn vi protokollar som Ethernet (for kablede nettverk) og Wi-Fi (for trådlause nettverk). Dette laget sørgjer også for feiloppdaging og korrigering for å sikre at data kjem fram utan feil.

3. **Lag 3: Nettverkslag (Network Layer)**
   - Nettverkslaget er ansvarleg for ruting av data mellom forskjellige nettverk. Her finn vi IP-protokollen, som bestemmer kvar datapakkane skal sendast vidare i eit nettverk. Rutere opererer på dette laget for å sende pakker til riktig destinasjon basert på IP-adresser.

4. **Lag 4: Transportlag (Transport Layer)**
   - Dette laget sørgjer for påliteleg overføring av data mellom endenodene, og her finn vi protokollar som TCP (Transmission Control Protocol) og UDP (User Datagram Protocol). TCP sørgjer for at data blir sendt, mottatt og satt saman i riktig rekkefølge, medan UDP gir raskare men mindre påliteleg overføring.

5. **Lag 5: Sesjonslag (Session Layer)**
   - Sesjonslaget etablerer, styrer og avsluttar forbindelsar (sesjonar) mellom applikasjonar. Det sørgjer for synkronisering av datautveksling, spesielt ved komplekse overføringar som krev kontinuerlig kommunikasjon.

6. **Lag 6: Presentasjonslag (Presentation Layer)**
   - Dette laget omset data mellom applikasjonslaget og resten av protokollstabelen. Det kan inkludere kryptering, datakomprimering og andre former for datakonvertering. Her omsetjast til dømes datatypar frå eit format til eit anna.

7. **Lag 7: Applikasjonslag (Application Layer)**
   - Applikasjonslaget er det nærmaste brukaren og omhandlar den direkte interaksjonen med programvare, som nettlesarar (HTTP/HTTPS), e-postklientar (SMTP/IMAP), og så vidare. Dette laget sørgjer for at applikasjonen kan kommunisere med nettverket på ein måte som gir meining for brukaren.

### TCP/IP-modellen (4-lagsmodellen)
TCP/IP-modellen er meir praktisk og brukt i den verkelege verda. Denne modellen har fire lag som tilsvarar ulike delar av OSI-modellen:

1. **Nettverksgrensesnitt-laget (Network Interface Layer)**
   - Dette laget tilsvarar både det fysiske laget og lenkelaget i OSI-modellen. Det inkluderer all teknologi som er nødvendig for å overføre data innanfor eit lokalt nettverk, som Ethernet eller Wi-Fi. Det sørgjer for fysisk tilkopling og overføring av data på det lokale nettverket.

2. **Internettlaget (Internet Layer)**
   - Internettlaget tilsvarar nettverkslaget i OSI-modellen og styrer ruting av data over fleire nettverk ved hjelp av IP-protokollen. Det sørgjer for at datapakkar kjem fram til riktig IP-adresse uavhengig av kor mange nettverk dei må passere.

3. **Transportlaget (Transport Layer)**
   - Dette laget samsvarar med transportlaget i OSI-modellen. Det styrer pålitelig dataoverføring mellom ende-til-ende-kommunikasjon, med protokollar som TCP og UDP.

4. **Applikasjonslaget (Application Layer)**
   - Applikasjonslaget tilsvarar applikasjons-, presentasjons- og sesjonslaga i OSI-modellen. Her finn vi protokollar som HTTP, FTP, SMTP, og andre som applikasjonar brukar for å kommunisere over nettverket.

### Dataflyt frå sendar til mottakar (Steg for steg)
La oss sjå på korleis data går gjennom desse laga frå ein sendar til ein mottakar:

1. **Applikasjonslaget**: Brukaren startar ein operasjon, som til dømes å laste inn ei nettside. Nettlesaren (applikasjonen) sender ein HTTP-forespørsel.
2. **Transportlaget**: HTTP-forespørselen blir sendt til transportlaget, som delar opp data i pakkar og legg til ein TCP-header som inneheld informasjon for å sikre at pakkane blir sette saman i riktig rekkefølge.
3. **Internettlaget**: Pakkane blir sendt til internettlaget, der IP-protokollen legg til ein IP-header som inneheld informasjon om mottakarens IP-adresse.
4. **Nettverksgrensesnitt-laget**: Pakkane blir deretter sendt til nettverksgrensesnitt-laget, der dei blir omsatt til fysiske signal (som elektriske pulsar over ein kabel eller radiosignal over Wi-Fi) og sendt gjennom nettverket.
5. **Fysisk overføring**: Dataen beveger seg gjennom fysiske medium (kablar, luft, osv.) til ruteren, som bestemmer kvar dataen skal vidare basert på IP-adresser.
6. **Mottakaren sin nettverksgrensesnitt-lag**: Dataen blir mottatt av mottakarens nettverksgrensesnitt-lag, som oversetter dei fysiske signala tilbake til digitale pakkar.
7. **Mottakaren sitt internettlag**: Pakkane blir sendt til internettlaget på mottakarsida, som les IP-adressane og sender pakkane vidare til riktig transportlag.
8. **Mottakaren sitt transportlag**: Transportlaget set saman dataen, sikrar at alt er mottatt og sender den til applikasjonslaget.
9. **Mottakaren sitt applikasjonslag**: Til slutt kjem dataen fram til applikasjonslaget, som presenterer nettsida i nettlesaren.

Ved å bruke desse laga, kan nettverkskommunikasjon skje på ein strukturert og påliteleg måte, frå sender til mottakar, uavhengig av den fysiske infrastrukturen.