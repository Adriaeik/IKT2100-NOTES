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


Kapittel 1  
Datamaskinnettverk og Internett

**1.1 Kva er Internett?**

I denne boka vil vi bruke det offentlege Internett som hovudeksempel for å diskutere datanettverk og protokollar. Men kva er eigentleg Internett? Vi kan svare på dette på to måtar:  
1. Ein "nuts and bolts"-beskrivelse av dei grunnleggjande maskinvare- og programvarekomponentane.  
2. Som ei infrastruktur som gir tenester til distribuerte applikasjonar.

**1.1.1 Ein "Nuts-and-Bolts" Beskrivelse**

- **Internett** er eit datanettverk som koplar saman milliardar av datamaskiner verda over.
- Tidlegare var desse hovudsakleg stasjonære PC-ar, arbeidsstasjonar og serverar. No inkluderer dei smarttelefonar, nettbrett og eit mangfald av "ting" som TV-ar, spelkonsollar, termostatar, bilar osv.
- Alle desse einingane vert kalla **hosts** eller **end systems**.
- I 2017 var det estimert rundt 18 milliardar einingar kopla til Internett, med ein prognose på 28,5 milliardar innan 2022.

**Kommunikasjonsliner og Pakkesvitsjar**

- **End systems** er kopla saman via eit nettverk av kommunikasjonsliner og **packet switches**.
- Kommunikasjonsliner kan vere koaksialkabel, kopartråd, optisk fiber eller radiospekter, med varierte overføringshastigheiter (bits per sekund).
- Data vert segmentert og pakka inn i **packets** før dei vert sendt gjennom nettverket.
- **Packet switches** (som **routers** og **link-layer switches**) tek imot og videresender pakkar mot destinasjonen.
  - **Link-layer switches**: Brukast typisk i tilgangsnettverk.
  - **Routers**: Brukast i nettverkskjernen.
- Ruten ein pakke tek frå avsendar til mottakar kallast ei **route** eller **path**.

**Internettleverandørar (ISPs)**

- **ISPs** gir tilgang til Internett for endesystem:
  - Bustad-ISPs (kabel, telefon).
  - Bedrifts- og universitets-ISPs.
  - Offentlege WiFi-ISPs.
  - Mobilnettverk.
- Kvar **ISP** er eit nettverk av pakkesvitsjar og kommunikasjonsliner.
- **ISPs** tilbyr ulike typar nettverkstilgang: kabelmodem, DSL, LAN, mobil trådlaus tilgang.
- **ISPs** for innhaldsleverandørar koplar serverar direkte til Internett.
- **ISPs** er kopla saman gjennom nasjonale og globale høgnivå **ISPs**, som består av høghastigheitsruterar og fiberoptiske liner.
- Alle **ISP-nettverk** køyrer **IP-protokollen** og følgjer namne- og adressekonvensjonar.

**Protokollar og Standardar**

- **End systems**, pakkesvitsjar og andre delar av Internett køyrer **protokollar** for å kontrollere sending og mottaking av informasjon.
- **Transmission Control Protocol (TCP)** og **Internet Protocol (IP)** er sentrale protokollar.
  - **IP-protokollen** spesifiserer formatet på pakkane mellom ruterar og endesystem.
  - **TCP/IP** er samleomgrepet for dei viktigaste protokollane i Internett.
- **Standardar** er viktige for interoperabilitet.
  - Utviklast av **Internet Engineering Task Force (IETF)**.
  - Standarddokument kallast **Requests for Comments (RFCs)**.
  - **IEEE 802 LAN Standards Committee** spesifiserer Ethernet- og WiFi-standardar.

**1.1.2 Ei Tenestebeskriving**

- Internett kan også sjåast som ei infrastruktur som tilbyr tenester til applikasjonar.
- **Distribuerte applikasjonar** inkluderer e-post, websurfing, meldingsapper, karttenester, strøymingstenester, sosiale medium, videokonferansar, spel osv.
- Desse applikasjonane køyrer på **end systems**, ikkje i pakkesvitsjane i nettverkskjernen.
- For å utvikle ei Internett-applikasjon:
  - Skriv program som køyrer på endesystema (f.eks. Java, C, Python).
  - Bruk **socket interface** for at programma kan sende data til kvarandre.
    - Eit sett reglar for korleis sendeprogrammet ber Internett om å levere data til destinasjonsprogrammet.
- Internett tilbyr fleire tenester, og utviklaren må velje teneste som passar for applikasjonen.
  - Meir om dette i kapittel 2.

**Ein Menneskeleg Analogi**

- **Protokollar** er sett av reglar for kommunikasjon, liknande menneskelege interaksjonar.
- **Eksempel 1**: Spørje om tida.
  - Sei "Hei" (initierer kommunikasjon).
  - Motta "Hei" tilbake (respons).
  - Spør "Kva er klokka?".
  - Motta svar.
- **Eksempel 2**: I ein klasse.
  - Læraren spør "Er det nokon spørsmål?".
  - Du rekk opp handa.
  - Læraren seier "Ja...".
  - Du stiller spørsmålet.
  - Læraren svarar.
- **Poeng**: Kommunikasjon krev at begge partar følgjer same protokoll for å lykkast.

**Network Protocols**

- Eit **network protocol** er liknande eit menneskeleg protokoll, men einingane som utvekslar meldingar og utfører handlingar er maskinvare eller programvare på einingar som datamaskiner, smarttelefonar, nettbrett, routerar osv.
- All aktivitet på Internett som involverer to eller fleire kommuniserande einingar er styrt av ein **protokoll**.
  - Eksempel: Protokollar i maskinvare på to fysisk tilknytte datamaskiner kontrollerer bitstraumen på kabelen mellom nettverkskort; **congestion-control protocols** i endesystem kontrollerer overføringsraten av pakkar mellom avsendar og mottakar; protokollar i routerar bestemmer ruta pakkane tek frå kjelde til destinasjon.
- Protokollar køyrer overalt på Internett; difor handlar mykje av denne boka om **computer network protocols**.

**Eksempel på ein nettverksprotokoll**

- Når du skriv inn URL-en til ei nettside i nettlesaren din:
  - Datamaskina di sender ei **connection request message** til webserveren og ventar på svar.
  - Webserveren mottar førespurnaden og returnerer ei **connection reply message**.
  - Når tilkoplinga er etablert, sender datamaskina di ei **GET message** med namnet på nettsida du ønskjer.
  - Webserveren returnerer til slutt nettsida (fila) til datamaskina di.
- Dette illustrerer korleis utveksling av meldingar og handlingane ved sending og mottaking definerer ein protokoll.

**Definisjon av ein protokoll**

> Ein **protokoll** definerer formatet og rekkefølgja av meldingar som vert utveksla mellom to eller fleire kommuniserande einingar, samt handlingane som vert utført ved sending og/eller mottaking av ei melding eller anna hending.

- Internett og datanettverk nyttar eit breitt spekter av protokollar for ulike kommunikasjonstasker.
- Nokre protokollar er enkle, medan andre er komplekse og krevjande å forstå.
- Å meistre feltet **computer networking** inneber å forstå kva, kvifor og korleis når det gjeld **networking protocols**.

---

**1.2 The Network Edge**

- Vi skal no gå djupare inn i komponentane av Internett, startande ved nettverkskanten.
- Fokuset er på dei komponentane vi kjenner best: datamaskiner, smarttelefonar og andre einingar vi brukar dagleg.
- Neste seksjon vil handle om nettverkskjernen og undersøking av switching og routing i datanettverk.

**End Systems**

- I nettverksjargon vert datamaskiner og andre einingar tilkopla Internett kalla **end systems** fordi dei er plassert i kanten av Internett (sjå Figur 1.3).
- **End systems** inkluderer:
  - **Desktop computers**: PC-ar, Macs, Linux-maskiner.
  - **Servers**: Web- og e-postserverar.
  - **Mobile devices**: Laptopar, smarttelefonar, nettbrett.
  - Ei aukande mengd ikkje-tradisjonelle "ting" vert også tilkopla Internett som **end systems** (f.eks. IoT-enheter).

**Hosts**

- **End systems** vert også kalla **hosts** fordi dei hostar (køyrer) applikasjonsprogram som weblesarar, webserverar, e-postklientar osv.
- Omgrepa **hosts** og **end systems** vert brukte om kvarandre.

**Clients og Servers**

- **Hosts** kan kategoriserast som:
  - **Clients**: Vanlegvis stasjonære PC-ar, laptopar, smarttelefonar osv.
  - **Servers**: Meir kraftige maskinar som lagrar og distribuerer websider, strøymer video, handterer e-post osv.
- Dei fleste tenestene vi nyttar (søkeresultat, e-post, websider, videoar, appinnhald) kjem frå serverar i store **data centers**.
  - Per 2020 har Google 19 datasenter på fire kontinent, med til saman fleire millionar serverar.
  - Figur 1.3 viser to slike datasenter.

**Data Centers**

- **Data centers** er store anlegg som huser tusenvis til hundretusenar av serverar.
- Funksjonar:
  - Servarar nettsider og applikasjonar til brukarar.
  - Utfører massiv parallell databehandling for databehovet til selskapet.
  - Tilbyr **cloud computing**-tenester til andre selskap.
- **Hosts** i datasenter kallast ofte **blades** og er montert i **racks**.
- **Data center networks** interkonnektar serverane og sørgjer for effektiv kommunikasjon internt.

**Access in the Enterprise (and the Home): Ethernet and WiFi**

- På bedrifter, universitet og i aukande grad i heimar, vert eit **Local Area Network (LAN)** brukt til å kopla eit endesystem til edge router.
- **Ethernet** er den mest utbreidde tilgangsteknologien i bedrifts-, universitets- og heimenettverk.
  - Ethernet-brukarar nyttar **twisted-pair** kopartråd for å kopla til ein **Ethernet switch**.
  - Ethernet-svitsjar, eller nettverk av slike, er kopla vidare til det større Internett.
  - Typiske overføringshastigheiter:
    - Brukarar: 100 Mbps til fleire Gbps.
    - Serverar: 1 Gbps til 10 Gbps.

- **WiFi** (basert på **IEEE 802.11**-teknologi) gjer det mogleg å kopla til nettverket trådlaust.
  - Brukarane sender/mottar pakkar til/frå eit **access point** som er kopla til bedriftsnettverket, og vidare til Internett.
  - Typisk rekkevidde: Nokre titals meter frå tilgangspunktet.
  - Dagens 802.11-teknologi tilbyr ein delt overføringsrate på over 100 Mbps.

- **Heimenettverk** kombinerer ofte breibandstilgang (kabelmodem eller DSL) med trådlause LAN for å skapa kraftige nettverk i heimen.
  - Eit typisk heimenettverk (sjå Figur 1.9) inkluderer:
    - Ein trådlaus laptop, fleire Internett-tilkopla heimeapparat og ein kablet PC.
    - Eit basestasjon (**wireless access point**) som kommuniserer med trådlause einingar.
    - Ein heimeruter som koplar tilgangspunktet og andre kablede einingar til Internett.
  - Gjer det mogleg for husstanden å ha breibandstilgang overalt i heimen.

---

**Wide-Area Wireless Access: 3G, LTE 4G og 5G**

- **Mobile einingar** som iPhones og Android-telefonar vert brukte til meldingar, deling av bilete, mobilbetalingar, strøyming av film og musikk medan ein er på farten.
- Desse einingane nyttar same trådlause infrastruktur som for mobiltelefoni for å senda/motta pakkar gjennom ein **basestasjon** operert av mobilnettleverandøren.
  - I motsetnad til WiFi, treng brukaren berre vera innanfor nokre titals kilometer frå basestasjonen.
- Telekommunikasjonsselskap har investert stort i **4G**-nettverk, som gir reelle nedlastingshastigheiter opp mot 60 Mbps.
- **5G**, femtegenerasjons trådlause nettverk, er allereie under utrulling og tilbyr endå høgare hastigheiter.
- Meir om dette vert dekka i kapittel 7.

---

**1.2.2 Physical Media**

- **Fysisk medium** refererer til det materielle mediet ein bit reiser gjennom frå kjelde til destinasjon.
  - Ein bit passerer gjennom fleire **transmitter-receiver** par på vegen.
  - For kvart par vert biten sendt ved å propagere elektromagnetiske bølgjer eller optiske pulsar over eit fysisk medium.
- **Typar fysisk medium**:
  - **Guided media**: Bølgjene vert leia langs eit solid medium, som fiberoptisk kabel, twisted-pair kopartråd eller koaksialkabel.
  - **Unguided media**: Bølgjene propagert i atmosfæren eller verdsrommet, som i trådlause LAN eller digitale satellittkanalar.

- **Kostnader**:
  - Den faktiske kostnaden av det fysiske mediet er ofte mindre enn kostnadane knytt til installasjon.
  - Mange installerer fleire typar kablar (twisted pair, optisk fiber, koaksialkabel) i bygningar for framtidig bruk.

---

**Twisted-Pair Copper Wire**

- Det billegaste og mest brukte guida overføringsmediet.
- Har vore nytta av telefonnett i over hundre år.
- **Struktur**:
  - To isolerte kopartrådar, om lag 1 mm tjukke, tvunne saman i ein spiral.
  - Tvistinga reduserer elektrisk interferens frå nærliggande par.
  - Fleire par kan buntast saman i ein kabel med ein beskyttande skjerm.
- **Unshielded Twisted Pair (UTP)**:
  - Vanleg brukt i LAN innanfor bygningar.
  - Datamengder frå 10 Mbps til 10 Gbps, avhengig av trådtykkleik og avstand.

---

**Coaxial Cable**

- Består av to konsentriske koparleiarar.
- Med spesiell isolasjon og skjerming kan koaksialkabel oppnå høge dataoverføringshastigheiter.
- **Bruk**:
  - Vanleg i kabel-TV-system.
  - Brukast i kombinasjon med kabelmodem for Internett-tilgang med hastigheiter opp mot hundrevis av Mbps.
  - Kan fungere som eit delt medium der fleire endesystem er kopla til same kabel.

---

**Fiber Optics**

- Eit tynt, fleksibelt medium som leier lysimpulsar; kvar impuls representerer ein bit.
- **Eigenskapar**:
  - Støttar svært høge overføringshastigheiter, opp til hundrevis av Gbps.
  - Immune mot elektromagnetisk interferens.
  - Låg signaldemping over lange avstandar (opp til 100 km).
  - Svært vanskeleg å tappe (høg sikkerheit).
- **Bruk**:
  - Føretrekt for langdistanse overføring, spesielt internasjonale samband.
  - Vanleg i ryggraden av Internett.
- **Utfordringar**:
  - Høg kostnad på optiske komponentar som sendarar, mottakarar og svitsjar har avgrensa bruken i kortare avstandar som i LAN eller til heimen.

---

**Terrestrial Radio Channels**

- Ber signal i det elektromagnetiske spekteret utan behov for fysiske kablar.
- **Fordelar**:
  - Kan penetrere veggar.
  - Gir mobilitet.
  - Kan dekke lange avstandar.
- **Avhengigheit av miljø**:
  - Signalstyrke påverkast av avstand og hindringar.
  - Multipath fading grunna signalrefleksjon.
  - Interferens frå andre signal.
- **Klassifisering**:
  - **Kort distanse**: 1–2 meter (f.eks. trådlause hovudtelefonar).
  - **Lokalt område**: 10–100 meter (f.eks. WiFi).
  - **Vidt område**: Titals kilometer (f.eks. mobilnettverk).

---

**Satellite Radio Channels**

- Koplar jordbaserte mikrobølgjesendarar/-mottakarar (**ground stations**) via ein kommunikasjonssatellitt.
- **Typar satellittar**:
  - **Geostationary satellites**:
    - Forblir over same punkt på jorda ved å gå i bane 36 000 km over overflata.
    - Introducerer ein signalforsinkelse på rundt 280 millisekund.
    - Brukt i område utan tilgang til DSL eller kabelbasert Internett.
  - **Low-Earth Orbiting (LEO) satellites**:
    - Plassert nærare jorda og bevegar seg rundt planeten.
    - Kan kommunisere med kvarandre og med grunnstasjonar.
    - Treng mange satellittar for kontinuerleg dekning.
    - Potensiell framtidig bruk for Internett-tilgang.

**1.3 Nettverkskjernen**

Etter å ha undersøkt kanten av Internett, skal vi no fordjupe oss i **nettverkskjernen**—eit nett av pakkesvitsjarar og lenker som koplar saman Internett sine endesystem (sjå Figur 1.10).

---

**1.3.1 Packet Switching**

- I nettverksapplikasjonar utvekslar **end systems** meldingar.
  - Meldingar kan innehalde kontrollfunksjonar eller data (t.d. e-post, JPEG-bilete, MP3-filer).
- For å sende ei melding, deler kjelda lange meldingar opp i mindre delar kalla **packets**.
- Mellom kjelde og destinasjon reiser pakkane gjennom **communication links** og **packet switches** (hovudsakleg **routers** og **link-layer switches**).
- Pakkar blir send over kvar lenke med full overføringsrate.
  - Tida for å sende ein pakke på L bit over ei lenke med overføringsrate R bits/sek er L/R sekund.

**Store-and-Forward Transmission**

- Dei fleste pakkesvitsjarar nyttar **store-and-forward transmission**.
  - Pakkesvitsjen må motta heile pakka før han kan begynne å sende den vidare på utgåande lenke.
- Eksempel (Figur 1.11):
  - Kjelda sender tre pakkar på L bit kvar til destinasjonen via ein router.
  - Total forsinkelse for éin pakke er 2L/R (tid for å sende til router + tid for router å sende til destinasjon).
- Generelt for N lenker:
  - **End-to-end delay**: $d_{\text{end-to-end}} = N \times \frac{L}{R}$

**Queuing Delays and Packet Loss**

- Kvar pakkesvitsj har fleire tilknytte lenker og ein **output buffer** for kvar lenke.
  - Om ei pakke kjem når lenka er opptatt, må ho vente i bufferen (**queuing delay**).
- Forsinkelsar varierer med nettverksbelastninga (**congestion**).
- Begrensa bufferplass kan føre til **packet loss** når bufferen er full.
  - Anten den nye pakka eller ei allereie køa pakke blir droppa.

**Forwarding Tables and Routing Protocols**

- Routerar bestemmer kva lenke ein pakke skal vidare på ved hjelp av **forwarding tables**.
  - Kvar **end system** har ei unik **IP address**.
  - Routeren brukar destinasjonsadressa i pakka for å slå opp riktig utgåande lenke.
- **Routing protocols** konfigurerer forwarding tables automatisk.
  - Bestemmer t.d. kortaste veg til destinasjonen.

---

**1.3.2 Circuit Switching**

- To hovudmetodar for å flytte data gjennom nettverk:
  - **Packet switching**: Data sendt i pakkar utan reserverte ressursar.
  - **Circuit switching**: Ressursar langs ruta blir reserverte for heile kommunikasjonsøkta.
- **Circuit-switched networks** (t.d. tradisjonelle telefonnettverk):
  - Før sending må ein opprette ein ende-til-ende **circuit**.
  - Ressursar (buffere, overføringsrate) blir reserverte og gir garantert kapasitet.
- **Multiplexing** i circuit-switched nettverk:
  - **Frequency-Division Multiplexing (FDM)**:
    - Frekvensspekteret delt mellom forbindelsar.
    - Kvar forbindelse får eit frekvensband (t.d. 4 kHz i telefonnett).
  - **Time-Division Multiplexing (TDM)**:
    - Tida delt inn i rammer og tidsluker.
    - Kvar forbindelse får ein tidsluke i kvar ramme.
- Ulemper med circuit switching:
  - Ineffektiv bruk av ressursar ved inaktivitet.
  - Kompleksitet ved oppretting av samband og signalering.

**Packet Switching Versus Circuit Switching**

- **Packet switching** fordelar:
  - Betre utnytting av nettverksressursar.
  - Meir effektiv ved at kapasitet blir delt dynamisk basert på behov.
  - Enklare og billigare å implementere.
- **Ulemper**:
  - Variabel ende-til-ende-forsinkelse (ikkje ideelt for sanntidstenester).
- **Eksempel**:
  - Med 1 Mbps lenke og brukarar som er aktive 10% av tida:
    - **Circuit switching**: Maks 10 samtidige brukarar.
    - **Packet switching**: Kan handtere mange fleire brukarar med minimal sannsyn for forsinkelse.

---

**1.3.3 Eit Nettverk av Nettverk**

- **Access ISPs** koplar endesystem til Internett.
  - Må vidare koplast saman for full global kommunikasjon.
- **Network Structures**:
  - **Struktur 1**: Alle access ISPs kopla til ein global transit ISP.
    - Urealistisk grunna kostnader og skalering.
  - **Struktur 2**: Fleire globale transit ISPs konkurrerer og interkonnektar.
  - **Struktur 3**: Hierarki med **tier-1 ISPs**, regionale ISPs og access ISPs.
    - **Tier-1 ISPs** (t.d. AT&T, NTT) på toppen av hierarkiet.
  - **Struktur 4**: Inkluderer **Points of Presence (PoPs)**, **multi-homing**, **peering**, og **Internet Exchange Points (IXPs)**.
    - **PoPs**: Stader der kundar kan kopla seg til ein ISP.
    - **Multi-homing**: ISPs koplar seg til fleire andre ISPs for pålitelegheit.
    - **Peering**: ISPs på same nivå koplar direkte utan kostnad (settlement-free).
    - **IXPs**: Fysiske stader der fleire ISPs kan peere.
- **Struktur 5**: Dagens Internett inkluderer også **content-provider networks**.
  - **Eksempel**: Google sitt eige globale nettverk med datasenter kopla direkte til ISPs og IXPs.
  - **Føremon**: Reduserer kostnader og aukar kontroll over tenestelevering.
- **Oppsummering**:
  - Internett er eit komplekst nettverk av nettverk.
  - Består av ulike nivå av ISPs, frå lokale access ISPs til globale tier-1 ISPs.
  - Samarbeid og interkonneksjon mellom desse nettverka er avgjerande for global kommunikasjon.

  **1.4 Forsinkelse, Tap og Gjennomstrøyming i Pakke-svitsja Nettverk**

Internett som infrastruktur introduserer nødvendigvis forsinkelse (delay), kan oppleve pakkeloss, og avgrensar gjennomstrøyminga (throughput) mellom endesystem. Å forstå og kvantifisere desse faktorane er essensielt for å kunne utvikle effektive nettverksapplikasjonar og protokollar.

---

**1.4.1 Oversikt over Forsinkelse i Pakke-svitsja Nettverk**

Ein pakke som reiser frå kjelde til destinasjon opplever fleire typar forsinkelsar ved kvart nodalpunkt (host eller router):

- **Prosesseringsforsinkelse ($d_{\text{proc}}$)**: Tida det tek for ein router å undersøke pakkens header og bestemme kor den skal sendast vidare. Vanlegvis i mikrosekundområdet.

- **Køforsinkelse ($d_{\text{queue}}$)**: Tida pakka ventar i køen før den kan bli overført på utgåande lenke. Varierer avhengig av nettverkstrafikk og kan range frå mikrosekund til millisekund.

- **Transmisjonsforsinkelse ($d_{\text{trans}}$)**: Tida det tek å skyve alle pakkebitane ut på lenka. Gitt ved formelen:
  $$  d_{\text{trans}} = \frac{L}{R} $$
  der $L$ er pakkelengda i bit, og $R$ er overføringsraten i bits per sekund.

- **Propageringsforsinkelse ($d_{\text{prop}}$)**: Tida det tek for ein bit å reise frå avsendar til mottakar over lenka. Gitt ved:
  $$
  d_{\text{prop}} = \frac{d}{s}
  $$
  der $d$ er avstanden mellom nodane, og $s$ er propagasjonshastigheita (nær lysets hastigheit, $2 \times 10^8$ til $3 \times 10^8$ m/s).

Den totale nodale forsinkelsen er summen av alle desse komponentane:
$$
d_{\text{nodal}} = d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}
$$

---

**1.4.2 Køforsinkelse og Pakketap**

**Trafikkintensitet ($La/R$)** er ein viktig parameter for å estimere køforsinkelse, der:

- $L$ er gjennomsnittleg pakkelengde (bit).
- $a$ er gjennomsnittleg ankomstrate av pakkar (pakkar per sekund).
- $R$ er overføringsraten (bits per sekund).

**Køforsinkelse aukar dramatisk** når trafikkintensiteten nærmar seg 1:
- Når $La/R \geq 1$, overgår ankomstraten overføringskapasiteten, noko som fører til at køen veks uavgrensa og køforsinkelsen går mot uendeleg.
- For $La/R < 1$, kan køforsinkelsen vere minimal dersom pakkar kjem sporadisk, men kan bli betydelig dersom pakkar kjem i burst.

**Pakketap** oppstår når køen har begrensa kapasitet:
- Når køen er full og nye pakkar kjem til, må pakkar droppast.
- Sannsynet for pakketap aukar med trafikkintensiteten.

---

**1.4.3 Ende-til-Ende Forsinkelse**

For ein sti med $N-1$ mellomliggande routerar (og dermed $N$ lenker), er den totale ende-til-ende-forsinkelsen (med neglisjerbar køforsinkelse) gitt ved:
$$
d_{\text{end-end}} = N \times (d_{\text{proc}} + d_{\text{trans}} + d_{\text{prop}})
$$
der $d_{\text{trans}}$ og $d_{\text{prop}}$ er transmisjons- og propageringsforsinkelsen på kvar lenke.

---

**1.4.4 Gjennomstrøyming i Datanettverk**

**Instantan gjennomstrøyming** refererer til overføringsraten (bps) på eit gitt tidspunkt, medan **gjennomsnittleg gjennomstrøyming** er total overført datamengde delt på total overføringstid:
$$
\text{Gjennomsnittleg gjennomstrøyming} = \frac{F}{T}
$$
der:
- $F$ er filstorleiken (bit).
- $T$ er total overføringstid (sekund).

**Flaskehalsen** i eit nettverk er den lenka med lågast overføringsrate ($R_{\text{min}}$):
- Gjennomstrøyminga er avgrensa av flaskehalsen:
  $$
  \text{Gjennomstrøyming} = \min\{R_1, R_2, \dots, R_N\}
  $$
  der $R_i$ er overføringsraten på lenke $i$.

**Eksempel 1:**

- Eit nettverk med to lenker frå server til klient:
  - Server til router: $R_s$ bps.
  - Router til klient: $R_c$ bps.
- Gjennomstrøyminga er:
  $$
  \text{Gjennomstrøyming} = \min\{R_s, R_c\}
  $$

**Eksempel 2:**

- Eit nettverk med $N$ lenker og overføringsrater $R_1, R_2, \dots, R_N$.
- Gjennomstrøyminga er avgrensa av den minste overføringsraten:
  $$
  \text{Gjennomstrøyming} = \min\{R_1, R_2, \dots, R_N\}
  $$

**Eksempel 3:**

- Med fleire samtidige overføringar som deler ei felles lenke med kapasitet $R$ bps.
- Om $M$ overføringar deler likt på lenka:
  $$
  \text{Gjennomstrøyming per overføring} = \frac{R}{M}
  $$

---

**Oppsummering**

For å kunne designe effektive nettverk og applikasjonar, er det avgjerande å forstå dei matematiske aspekta ved forsinkelse og gjennomstrøyming i pakke-svitsja nettverk. Ved å modellere og analysere desse faktorane kan ein identifisere flaskehalsar, forutseie køforsinkelsar og optimalisere nettverkets ytelse.

**1.5 Protokollag og Tenestemodellar**

Internett er ein svært kompleks struktur med mange komponentar: applikasjonar, protokollar, ulike endesystem, pakkesvitsjarar og forskjellige typar link-level media. For å organisere denne kompleksiteten, nyttar vi ei lagdelt arkitektur.

---

**1.5.1 Lagdelt Arkitektur**

Ein menneskeleg analogi kan hjelpe oss å forstå dette konseptet. Tenk på flysystemet: Det involverer billettkontor, bagasjesjekk, gatepersonale, pilotar, fly, flygeleiarar og eit globalt rutesystem. For å beskrive dette komplekse systemet, kan vi dele det opp i lag basert på dei ulike handlingane som skjer:

- **Billettlag**: Kjøp og klage på billettar.
- **Bagasjelag**: Innsjekking og henting av bagasje.
- **Gatelag**: Ombordstiging og avstiging ved gaten.
- **Takeoff/Landing-lag**: Avgang og landing på rullebanen.
- **Flyrute-lag**: Navigering av flyet mellom flyplassar.

Kvart lag tilbyr tenester til laget over ved å utføre visse handlingar og bruke tenestene frå laget under. Denne modulariteten gjer det enklare å oppdatere eller endre implementeringa av eit lag utan å påverke resten av systemet, så lenge tenesta som vert levert er den same.

---

**Protokollagdeling**

I nettverksprotokollar organiserer vi protokollar og tilhøyrande maskinvare og programvare i lag. Kvart lag har sine protokollar og tilbyr tenester til laget over gjennom ein **service model**. Eit lag tilbyr tenester ved å:

1. Utføre spesifikke handlingar innanfor laget.
2. Bruke tenestene frå laget direkte under.

Eit eksempel er at lag \( n \) kan tilby pålitelig levering av meldingar ved å bruke ein upålitelig teneste frå lag \( n - 1 \), og legge til funksjonalitet for å oppdage og sende på nytt tapte meldingar.

**Fordelar og Ulemper med Lagdeling**

- **Fordelar**:
  - Gjev ei strukturert tilnærming for å diskutere systemkomponentar.
  - Modularitet som gjer det enklare å oppdatere komponentar utan å påverke andre lag.
- **Ulemper**:
  - Kan føre til duplisering av funksjonalitet på fleire lag (t.d. feilhåndtering).
  - Kan oppstå behov for informasjon på eitt lag som berre er tilgjengeleg på eit anna lag, noko som bryt med prinsippet om separasjon av lag.

**Internet Protokollstakken**

Internett-protokollstakken består av fem lag:

1. **Applikasjonslaget**: Her finst nettverksapplikasjonar og applikasjonsprotokollar som HTTP, SMTP og FTP. Applikasjonslaget er distribuert over fleire endesystem der applikasjonar utvekslar **meldingar**.

2. **Transportlaget**: Transporterer applikasjonsmeldingar mellom applikasjonsendepunkt. Dei to hovudprotokollane er **TCP** og **UDP**.
   - **TCP**: Tilbyr pålitelig, forbindingsorientert teneste med flytkontroll og kongestionkontroll.
   - **UDP**: Tilbyr ein enkel, upålitelig, forbindingslaus teneste utan flytkontroll eller kongestionkontroll.
   - Transportlagsenhetar kallast **segment**.

3. **Nettverkslaget**: Ansvarleg for å flytte **datagram** frå ein host til ein annan. Hovudprotokollen er **IP**, som definerer datagramformat og ruting mellom kildar og destinasjonar. Nettverkslaget inkluderer også rutingprotokollar.

4. **Lenkelaget**: Flyttar **rammer** frå ein node til den neste på ruta. Tenestene avheng av spesifikke lenkelagsprotokollar som Ethernet, WiFi og PPP. Eit datagram kan bli handsama av ulike lenkelagsprotokollar på ulike lenker langs ruta.

5. **Fysisk lag**: Flyttar individuelle bitar i ein ramme frå ein node til den neste over det fysiske mediet (t.d. kopartråd, fiberoptikk). Protokollane er avhengige av det fysiske mediet.

---

**1.5.2 Innkapsling**

**Innkapsling** er prosessen der kvart lag legg til sin eigen headerinformasjon til dataene frå laget over:

- **Applikasjonslaget** sender ei melding \( M \) til transportlaget.
- **Transportlaget** legg til sin header \( H_t \), og dannar eit **segment** (\( H_t + M \)).
- **Nettverkslaget** legg til sin header \( H_n \), og dannar eit **datagram** (\( H_n + H_t + M \)).
- **Lenkelaget** legg til sin header \( H_l \), og dannar ei **ramme** (\( H_l + H_n + H_t + M \)).

På mottakarsida blir prosessen reversert (de-innkapsling), der kvar header blir fjerna i omvendt rekkefølge.

**Analogien med eit brev**:

- **Melding**: Sjå på ei intern melding (f.eks. eit notat) som applikasjonsdata.
- **Segment**: Notatet blir lagt i ein intern konvolutt med mottakarens namn (transportlaget).
- **Datagram**: Den interne konvolutten blir lagt i ein ekstern konvolutt med adresse (nettverkslaget).
- **Ramme**: Den eksterne konvolutten blir sendt gjennom postsystemet (lenkelaget og fysisk lag).

---

**1.6 Nettverk Under Angrep**

Internett er kritisk for mange institusjonar og enkeltpersonar, men står overfor mange sikkerheitsutfordringar der "bad guys" prøver å skade systema våre.

**Truslar og Angrep**

1. **Malware (Skadeleg Programvare)**:
   - **Virus og Ormar**: Kan infisere einheter via Internett og utføre skadelege handlingar som å slette filer eller stjele privat informasjon.
   - **Botnet**: Infiserte maskinar kan bli del av eit nettverk kontrollert av angriparar for å utføre ytterlegare angrep som spam eller DDoS.

2. **Denial-of-Service (DoS) Angrep**:
   - **Vulnerability Attack**: Utnyttar sårbarheiter i applikasjonar eller operativsystem for å krasje tenester.
   - **Bandwidth Flooding**: Overveldar målserveren med ein flaum av pakkar, slik at legitim trafikk ikkje når fram.
   - **Connection Flooding**: Opprettar mange falske TCP-forbindelsar for å bruke opp ressursane til serveren.

3. **Packet Sniffing**:
   - **Sniffing**: Ein passiv mottakar avlyttar trafikk for å stjele sensitiv informasjon.
   - **Sårbarheiter**: Spesielt i trådlause nettverk og delte medium som Ethernet.

4. **IP Spoofing og Maskering**:
   - **IP Spoofing**: Angriparen sender pakkar med falsk kjeldeadresse.
   - **Maskering**: Angriparen utgir seg for å vere ein annan brukar eller system.

---

**Behov for Sikkerheitstiltak**

- **Kryptografi**: Beskytte data gjennom kryptering for å hindre uautorisert tilgang.
- **Endepunktautentisering**: Sikre at kommunikasjon skjer mellom legitime partar.
- **Forsvar mot DoS-angrep**: Utvikle metodar for å oppdage og avverge ulike typar DoS-angrep.
- **Overvaking og Deteksjon**: Aktivt overvake nettverk for mistenkeleg aktivitet.

**Internettets Oprinnelege Design og Sikkerheit**

- Internett vart opprinneleg designa for eit miljø med gjensidig tillit, utan fokus på sikkerheit.
- I dagens miljø med mange utrustlege brukarar er det nødvendig å innføre sikkerheitsmekanismer.
- Kommunikasjon mellom brukarar som ikkje stolar på kvarandre er vanleg, og nettverket må kunne handtere dette på ein trygg måte.

---

**Avslutning**

Sikkerheit i nettverk er ein kritisk del av moderne datanettverk. Som nettverksingeniørar og -brukarar må vi forstå truslane og implementere tiltak for å beskytte systema våre mot ulike angrep.

**1.7 Historien til Datanettverk og Internett**

Denne seksjonen gir ein oversikt over utviklinga av datanettverk og Internett frå tidleg på 1960-talet fram til i dag, delt inn i fleire viktige periodar:

---

**1.7.1 Utviklinga av Pakke-svitsjing: 1961–1972**

- **Bakgrunn**: På 1960-talet dominerte telefonsystemet, som brukte krets-svitsjing, den globale kommunikasjonen. Men behovet for å kopla saman datamaskiner og håndtera "burst"-trafikk førte til nye idear.

- **Leonard Kleinrock (MIT)**: Publiserte det første arbeidet om pakke-svitsjing i 1961, og viste gjennom køteori effektiviteten av denne metoden for ujamn trafikk.

- **Paul Baran (RAND Institute)** og **Donald Davies (NPL, England)**: Arbeidde uavhengig med konseptet pakke-svitsjing for sikre kommunikasjonssystem.

- **ARPAnet (1969)**: Det første pakke-svitsja nettverket, initiert av ARPA (seinare DARPA), kopla saman fire universitet: UCLA, SRI, UC Santa Barbara og University of Utah.

---

**1.7.2 Proprietære Nettverk og Internettverking: 1972–1980**

- **Internettverking**: Behovet for å kopla saman ulike nettverk førte til utviklinga av konseptet "internettverking".

- **Vinton Cerf og Robert Kahn**: Utvikla grunnleggjande prinsipp for internettverking og publiserte i 1974 arbeidet som leidde til TCP/IP-protokollen.

- **Separasjon av TCP og IP**: For å støtte ulike typar applikasjonar (både pålitelig og upålitelig overføring) blei TCP delt i TCP (Transport Control Protocol) og IP (Internet Protocol).

- **Andre nettverk**: Parallelt med ARPAnet oppstod andre nettverk som ALOHANet (Hawaii), Telenet, Cyclades (Frankrike), og IBM's SNA.

---

**1.7.3 Ein Proliferasjon av Nettverk: 1980–1990**

- **Vekst av ARPAnet**: Frå rundt 200 til over 100 000 tilkopla vertsmaskinar ved slutten av 1980-talet.

- **Universitetsnettverk**: Nettverk som BITNET, CSNET og NSFNET vart oppretta for å kople saman akademiske institusjonar.

- **Standardisering av TCP/IP (1983)**: Alle vertar på ARPAnet gjekk over til å bruke TCP/IP-protokollen.

- **Utvikling av DNS**: Domenenamnsystemet (DNS) blei introdusert for å mappe menneske-lesbare namn til IP-adresser.

- **Minitel (Frankrike)**: Eit tidleg eksempel på eit nasjonalt datanettverk som tilbød elektroniske tenester til hushaldningar.

---

**1.7.4 Internett-eksplosjonen: 1990-talet**

- **Kommersialisering av Internett**: NSFNET opna for kommersiell bruk, og kommersielle ISPar tok over infrastrukturen.

- **World Wide Web (WWW)**: Oppfunne av Tim Berners-Lee (1989–1991), med utvikling av HTML, HTTP, webservere og nettlesarar.

- **Nettlesarkrigen**: Konkurranse mellom Netscape og Microsoft bidrog til rask utvikling av nettlesarteknologi.

- **Killer-applikasjonar**:
  - **E-post**: Utbreiing av elektronisk postkommunikasjon.
  - **Web**: Eksplosiv vekst av websider og nettbaserte tenester.
  - **Instant Messaging**: Sanntidskommunikasjon mellom brukarar.
  - **Peer-to-Peer Fildeling**: Tjenester som Napster muliggjorde deling av musikkfiler.

---

**1.7.5 Det Nye Tusenåret**

- **Breidbånd og Høg-hastigheits Internett**: Utbreiing av kabel, DSL, fiber og trådlause teknologiar (WiFi, 4G, 5G) har auka tilgangen til Internett.

- **Smarttelefonar og Mobil Internett**: Konstant og trådløs tilgang har ført til nye applikasjonar og tenester.

- **Sosiale Nettverk**: Plattformar som Facebook, Twitter og Instagram har endra måten folk kommuniserer og deler informasjon på.

- **Innhaldsleverandørnettverk**: Selskap som Google og Microsoft har bygd eigne globale nettverk for å betra tenesteyting og redusere kostnader.

- **Skytjenester**: Fleire organisasjonar flyttar applikasjonar og data til skyen, med tilbydarar som Amazon Web Services, Microsoft Azure og Alibaba Cloud.

---

**1.8 Oppsummering**

I dette kapittelet har vi fått ein omfattande introduksjon til datanettverk og Internett:

- **Nettverkskomponentar**: Vi har sett på endesystem, applikasjonar, protokollar, pakkesvitsjarar og ulike fysiske medium.

- **Nettverksarkitektur**: Forstått forskjellen mellom tilgangsnettverk (tilkoplar brukarar til nettverket) og nettverkskjernen (ruting og overføring av data).

- **Pakkesvitsjing vs. Krets-svitsjing**: Utforska fordelar og ulemper ved dei to hovudmetodane for dataoverføring i nettverk.

- **Forsinkelse, Tap og Gjennomstrøyming**: Innført grunnleggjande konsept og matematiske modellar for å analysere ytelsen til nettverk.

- **Protokollagdeling**: Lært om den fem-laga Internett-protokollstakken (applikasjon, transport, nettverk, lenke og fysisk lag) og korleis desse samarbeider.

- **Sikkerheit**: Diskutert truslar som malware, DoS-angrep og pakkesniffing, og viktigheten av å implementere sikkerheitsmekanismer.

- **Historisk Perspektiv**: Følgt utviklinga av datanettverk frå dei tidlege konsepta av pakke-svitsjing til dagens komplekse og globale Internett.

---

**Vegen Vidare**

Boka følgjer ein top-down tilnærming, som betyr at vi startar med dei øvste laga i protokollstakken og arbeider oss nedover. Dette gir oss ei forståing av applikasjonane og tenestane før vi dykker ned i korleis nettverket er bygd for å støtte desse.

**Kapitteloversikt:**

1. **Datanettverk og Internett**: Innleiande konsept og oversikt (dette kapittelet).
2. **Applikasjonslaget**: Studerer protokollar og tenester på applikasjonsnivå.
3. **Transportlaget**: Utforskar mekanismane for dataoverføring mellom applikasjonar.
4. **Nettverkslaget: Dataplanet**: Ser på korleis pakkar blir rutet gjennom nettverket.
5. **Nettverkslaget: Kontrollplanet**: Dybde i rutingprotokollar og kontrollmekanismar.
6. **Lenkelaget og LAN**: Undersøker lokale nettverk og lenkelagsprotokollar.
7. **Trådlause og Mobile Nettverk**: Fokus på trådlause teknologiar og mobilitet.
8. **Sikkerheit i Datanettverk**: Dykker ned i sikkerheitsprotokollar og mekanismar.

Gjennom denne strukturen vil vi gradvis bygge opp ein djup forståing av korleis moderne datanettverk fungerer, frå dei høgaste applikasjonslaga til dei lågaste fysiske laga, og korleis dei ulike komponentane samarbeider for å levere dei tenestane vi tek for gitt i dag.