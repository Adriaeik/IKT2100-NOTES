# Bok 1 kapittel 2

## 2.1
### Some network apps
- sosiale nettverk
- Web
- text melding
- ...

email sin opbygging kom fra å separere brukar og host med ein `@` slik: `brukar@host`
På den måten kunne man finne vegen fra avsendar til mottakar

### Server - Client
**Sever**
- alltid på (host)
- permanent IP
- oftast ik datasenter

**Client**
- kontakter server
- dynamisk IP (muligens)
- Snakker ikkje direkte med andre klienta
- ikkje nødvendigvis tilkopla til ein kvar tid
- eksempel: HTTP, IMAP, FTP

### Peer-to-Peer Arkitektur (P2P)

- **Ingen alltid-på-server (no always-on server)**:
  - I ein P2P-arkitektur finst det ikkje nokon sentral server som er konstant tilgjengeleg for å handtere førespurnadar og levere tenester. I staden kommuniserer nodane (peers) direkte med kvarandre.

- **Tilfeldige endsystem kommuniserer direkte (arbitrary end systems directly communicate)**:
  - Kvar node i nettverket kan kommunisere direkte med andre noder utan å gå gjennom ein sentralisert server. Dette gjer at nettverket kan skalere på ein meir desentralisert måte.

- **Noder etterspør tenester frå andre noder og leverer tenester i retur (peers request service from other peers, provide service in return to other peers)**:
  - Nodane fungerer både som klientar og serverar. Dei kan be om data eller tenester frå andre noder, samtidig som dei tilbyr eigne ressursar eller data til andre i nettverket.

- **Sjølvskalerande (self scalability)**:
  - Nye noder som blir med i nettverket, tilfører ikkje berre auka etterspørsel etter tenester, men også meir tenestekapasitet. Dette gjer nettverket i stand til å skalere naturleg etter behov.

- **Noder er tidvis tilkopla og byter IP-adresser (peers are intermittently connected and change IP addresses)**:
  - Noder i eit P2P-nettverk er ikkje nødvendigvis alltid pålogga, og dei kan skifte IP-adresse. Dette kan gjere nettverksstyring meir utfordrande, sidan tilgjengelege ressursar kan variere.

- **Kompleks administrasjon (complex management)**:
  - Å administrere eit P2P-nettverk er meir komplisert enn i ein tradisjonell klient-server-modell, sidan nodane kan kome og gå, og ressursar er meir spreidde.

- **Døme: P2P-fildeling (P2P file sharing [BitTorrent])**:
  - Eit godt døme på P2P-arkitektur er fildelingsprotokollar som BitTorrent, der brukarane lastar ned og deler filer direkte frå kvarandre utan behov for ein sentralisert server.

### Applikasjonslaget (Application Layer): OSI-lag 2-7

- P2P-arkitektur opererer på applikasjonslaget, som inkluderer fleire lag i OSI-modellen:
  - **Lag 2-7**: Desse laga omhandlar ulike aspekt av datakommunikasjon, frå datalink til applikasjonslaget sjølv, som styrer brukarinteraksjon og nettverksprotokollar.

  ## 2.2

  ### HTTP
  - application layer protocoll

It  is  important  to  note  that  the  server  sends requested  files  to  clients  without  
storing any state information about the client. If a particular client asks for the same 
object  twice  in  a  period  of  a  few  seconds,  the  server  does  not  respond  by  saying  
that it just served the object to the client; instead, the server resends the object, as 
it  has  completely  forgotten  what  it  did  earlier.  

## 2.3
Socket-programmering er ein teknikk som blir brukt for å opprette kommunikasjon mellom to eller fleire datamaskiner over eit nettverk. Eit "socket" er eit endepunkt for sending eller mottaking av data, og socket-programmering handlar om å bruke desse endepunkta for å utveksle informasjon mellom applikasjonar på ulike datamaskiner.

### Grunnleggjande om Socket-Programmering:

1. **Socket som eit kommunikasjonsendepunkt:**
   - Ein socket er ein kombinasjon av ei IP-adresse og eit portnummer. IP-adressa identifiserer datamaskina i nettverket, medan portnummeret identifiserer den spesifikke tenesta eller applikasjonen som køyrer på datamaskina.

2. **Typar sockets:**
   - **TCP-sockets (stream sockets):** Brukast for pålitelig, tilkobla kommunikasjon. TCP-sockets etablerer ein vedvarande forbindelse mellom to endepunkt, og sørgjer for at data blir levert i riktig rekkefølge utan tap.
   - **UDP-sockets (datagram sockets):** Brukast for rask, ikkje-tilkobla kommunikasjon. UDP-sockets sender data utan å etablere ein vedvarande forbindelse, noko som kan føre til at data kjem fram i feil rekkefølge eller ikkje i det heile tatt, men med lågare forsinkelse.

3. **Opprette ein socket:**
   - For å kommunisere over nettverket, må ein applikasjon først opprette ein socket ved å spesifisere typen socket (TCP eller UDP), IP-adressa, og portnummeret.

4. **Kommunikasjonsflyt:**
   - **Server-side:**
     - Serveren opprettar ein socket og bind den til ei spesifikk IP-adresse og port. Deretter lyttar serveren etter tilkoplingsforespurnadar frå klientar.
   - **Klient-side:**
     - Klienten opprettar ein socket og prøver å koble til serverens IP-adresse og port. Når tilkoblinga er etablert (i tilfellet med TCP), kan klienten og serveren utveksle data.
   - **Dataoverføring:**
     - Etter at forbindelsen er etablert, kan både klient og server sende og motta data gjennom socketen. Når kommunikasjonen er ferdig, lukkast socketen for å avslutte forbindelsen.

5. **Eit enkelt eksempel på socket-programmering:**
   - I eit typisk program for socket-programmering, vil serveren opprette ein socket, binde den, lytta på ein port, akseptere tilkoblingar, og deretter sende/motta data. Klienten vil opprette ein socket, koble til serveren, og deretter sende/motta data.

### Kvifor er Socket-Programmering Viktig?
Socket-programmering er essensielt for å lage nettverksbaserte applikasjonar, som webserverar, e-postklientar, og online spel. Det gir utviklarar fleksibilitet til å kontrollere korleis data blir sendt og mottatt over nettverket, og til å tilpasse applikasjonar til ulike nettverksmiljø og kommunikasjonsbehov.

Dette er kjernen i mange nettverksbaserte applikasjonar, og det er eit grunnlag for mykje av det vi opplever på internett i dag.

Socket-programmering kan gjerast i mange ulike programmeringsspråk, som Python, C, C++, Java, og mange fleire. Her er eit enkelt eksempel på socket-programmering i Python, som er eit av dei mest brukte språka for nettverksprogrammering på grunn av sitt enkle og lesbare syntax.

### Python-eksempel: Enkel Klient-Server Kommunikasjon

#### Server (server.py)

Dette programmet opprettar ein enkel server som lyttar på ein spesifikk port, aksepterer tilkoblingar frå ein klient, og sender ei melding tilbake til klienten.

```python
import socket

# Opprett ein socket-objekt
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socketen til ei adresse og ein port
server_socket.bind(('localhost', 12345))

# Lytta etter tilkoplingar (maks 5 køplassar)
server_socket.listen(5)

print("Serveren ventar på tilkopling...")

# Aksepter ei tilkopling
client_socket, client_address = server_socket.accept()
print(f"Tilkopla til {client_address}")

# Send ei melding til klienten
client_socket.send("Hei frå serveren!".encode())

# Mottar data frå klienten (opsjonelt)
data = client_socket.recv(1024)
print(f"Melding frå klienten: {data.decode()}")

# Lukk tilkoplinga
client_socket.close()
server_socket.close()
```

#### Klient (client.py)

Dette programmet opprettar ein klient som koblar til serveren, mottar meldinga frå serveren, og sender ei melding tilbake.

```python
import socket

# Opprett ein socket-objekt
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koble til serveren
client_socket.connect(('localhost', 12345))

# Mottar meldinga frå serveren
data = client_socket.recv(1024)
print(f"Melding frå serveren: {data.decode()}")

# Send ei melding til serveren
client_socket.send(b"Takk, serveren!")

# Lukk tilkoplinga
client_socket.close()
```

### Forklaring:

- **Server:**
  - **`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`**: Opprettar ein socket med IPv4-adressering (AF_INET) og TCP (SOCK_STREAM).
  - **`bind(('localhost', 12345))`**: Bind socketen til 'localhost' (den lokale maskina) og port 12345.
  - **`listen(5)`**: Serveren lyttar etter tilkoblingar, med ei køgrense på 5.
  - **`accept()`**: Aksepterer ein tilkopling frå ein klient.
  - **`send(b"Hei frå serveren!")`**: Sender ei byte-melding til klienten.
  - **`recv(1024)`**: Mottar data frå klienten (opptil 1024 byte).

- **Klient:**
  - **`connect(('localhost', 12345))`**: Knyter klienten til serveren som køyrer på 'localhost' og port 12345.
  - **`recv(1024)`**: Mottar meldinga frå serveren.
  - **`send(b"Takk, serveren!")`**: Sender ei melding tilbake til serveren.

### Køyre Eksemplet:

1. **Køyr serveren**: Først må du køyre server-programmet ved å skrive `python server.py` i terminalen eller kommandolinjen.
2. **Køyr klienten**: Deretter køyrer du klient-programmet ved å skrive `python client.py`.
3. **Interaksjon**: Du vil sjå at serveren mottar tilkopling frå klienten, sender ei melding, og mottar ei melding tilbake frå klienten.

Dette er eit enkelt eksempel, men socket-programmering kan utvidast til å lage komplekse nettverksapplikasjonar som webserverar, chat-applikasjonar, og meir.

## 2.4



**MAC (Media Access Control)** er ein protokoll på datalinklaget (lag 2 i OSI-modellen) som styrer korleis data blir overført mellom nettverkseiningar på same fysiske nettverk. MAC-adresser, som er unike identifikatorar for nettverksgrensesnitt, spelar ei viktig rolle i å sikre at data vert levert til rett mottakar på det lokale nettverket.

MAC-adresser er på 48 bit og er typisk skrive som seks grupper av to heksadesimale tal (til dømes: `00:1A:2B:3C:4D:5E`). Desse adressene blir tildelt av maskinvareprodusenten og skal vere unike for kvar enkelt nettverksadapter, som for eksempel eit ethernet-kort eller ein Wi-Fi-adapter.

I nettverk som Ethernet, styrer MAC-laget tilgang til den fysiske kommunikasjonskanalen og regulerer dataoverføring gjennom metodar som *CSMA/CD* (Carrier Sense Multiple Access with Collision Detection) for kablede nettverk og *CSMA/CA* (Carrier Sense Multiple Access with Collision Avoidance) for trådløse nettverk.

---

**Notater fra Kapittel 2: Applikasjonslaget**

---

**Introduksjon**

- **Nettverksapplikasjoner** er grunnen til at datanettverk eksisterer. Uten nyttige applikasjoner ville det ikke vært behov for nettverksinfrastruktur og protokoller.
- Historisk har applikasjoner som e-post, fjernaksess (Telnet), filoverføring (FTP) og nyhetsgrupper vært viktige.
- **World Wide Web** revolusjonerte bruken av Internett på midten av 1990-tallet.
- Moderne applikasjoner inkluderer:
  - **VoIP** (f.eks. Skype, Facetime, Google Hangouts)
  - **Brukergenerert video** (YouTube)
  - **Strømmetjenester** (Netflix)
  - **Online spill** (Second Life, World of Warcraft)
  - **Sosiale nettverk** (Facebook, Instagram, Twitter)
  - **Lokasjonsbaserte mobilapper** (Yelp, Tinder, Waze)
  - **Meldingstjenester** (WeChat, WhatsApp)

---

**2.1 Prinsipper for Nettverksapplikasjoner**

- **Utvikling av nettverksapplikasjoner** involverer programmer som kjører på ulike endesystemer og kommuniserer over nettverket.
- **Programvare på endesystemer**: Applikasjoner kjører på sluttbrukernes enheter og kommuniserer over nettverket uten behov for spesialprogramvare på nettverkskjernen (rutere, svitsjer).
- **Eksempler**: Nettlesere, e-postklienter, streamingapplikasjoner.

**2.1.1 Nettverksapplikasjonsarkitekturer**

- **Applikasjonsarkitektur**: Strukturen på hvordan applikasjonen er bygget over endesystemene.
- To hovedtyper:
  - **Klient-server-arkitektur**:
    - En **alltid-på server** betjener forespørsler fra mange **klienter**.
    - Serveren har en **fast IP-adresse**.
    - **Klienter** initierer kommunikasjon med serveren.
    - **Eksempler**: Web-servere, e-postservere.
    - **Skalering**: Bruk av datasentre med mange servere for å håndtere stor trafikk.
  - **Peer-to-peer (P2P) arkitektur**:
    - **Minimal eller ingen avhengighet** av dedikerte servere.
    - **Peers** kommuniserer direkte med hverandre.
    - Hver peer fungerer som både **klient og server**.
    - **Selvskalerende**: Kapasiteten øker med antall brukere.
    - **Utfordringer**: Sikkerhet, ytelse, pålitelighet.
    - **Eksempler**: Fildelingsapplikasjoner som BitTorrent.

**2.1.2 Kommunikasjon mellom Prosesser**

- **Prosesser**: Programmer som kjører på et endesystem.
- **Interprosesskommunikasjon**: Prosesser på samme maskin kommuniserer via operativsystemet.
- **Nettverkskommunikasjon**: Prosesser på ulike maskiner kommuniserer ved å sende meldinger over nettverket.
- **Klient og Server Prosesser**:
  - **Klientprosess**: Initierer kommunikasjonen.
  - **Serverprosess**: Venter på å bli kontaktet.
  - **Eksempel**: Nettleseren (klient) kommuniserer med en webserver (server).
- **Sockets**:
  - **Grensesnitt** mellom applikasjonslaget og transportlaget.
  - **API** som tillater applikasjoner å sende og motta data over nettverket.
  - **Analogi**: En socket er som en dør mellom applikasjonen og transportlaget.
- **Adresseprosesser**:
  - **IP-adresse**: Identifiserer verten i nettverket.
  - **Portnummer**: Identifiserer prosessen på verten.
  - **Velkjente porter**: Standardiserte portnumre for kjente tjenester (f.eks. HTTP på port 80).

**2.1.3 Transporttjenester Tilgjengelig for Applikasjoner**

- **Transportlaget** tilbyr tjenester til applikasjoner over nettverket.
- **Fire dimensjoner av tjenester**:
  1. **Pålitelig dataoverføring**: Garantert levering av data uten feil.
  2. **Gjennomstrømming (Throughput)**: Garantert minimum båndbredde.
  3. **Timing**: Garanterte leveransetider (forsinkelse).
  4. **Sikkerhet**: Kryptering, autentisering, dataintegritet.
- **Applikasjoner har ulike behov** avhengig av deres natur (f.eks. e-post vs. videokonferanse).

**2.1.4 Transporttjenester Levert av Internett**

- **TCP (Transmission Control Protocol)**:
  - **Forbindelsesorientert**: Krever opprettelse av forbindelse før dataoverføring.
  - **Pålitelig dataoverføring**: Garanterer at data ankommer uten feil og i riktig rekkefølge.
  - **Flytkontroll**: Justerer dataoverføringshastigheten mellom sender og mottaker.
  - **Kongestionkontroll**: Regulerer trafikk for å unngå overbelastning i nettverket.
- **UDP (User Datagram Protocol)**:
  - **Forbindelsesløs**: Ingen oppsett før dataoverføring.
  - **Upålitelig dataoverføring**: Ingen garantier for levering eller rekkefølge.
  - **Lav overhead**: Mindre forsinkelse og ressursbruk.
- **TLS (Transport Layer Security)**:
  - **Sikkerhetsforbedring** over TCP.
  - **Kryptering**: Beskytter data mot avlytting.
  - **Autentisering**: Verifiserer identiteten til kommuniserende parter.
  - **Dataintegritet**: Sikrer at data ikke er endret under overføring.
- **Manglende tjenester i dagens protokoller**:
  - **Gjennomstrømmingsgarantier**: Ingen garanti for minimum båndbredde.
  - **Timinggarantier**: Ingen garanti for maksimal forsinkelse.
  - **Applikasjoner må selv håndtere** behov for spesifikke timing- eller båndbreddekrav.

**Eksempler på Applikasjoner og Valg av Transportprotokoll**

- **E-post (SMTP)**: Bruker TCP for pålitelig levering.
- **Web (HTTP)**: Bruker TCP for pålitelighet.
- **Filoverføring (FTP)**: Bruker TCP.
- **Strømmetjenester (YouTube, Netflix)**:
  - Ofte TCP, men kan bruke UDP for lavere forsinkelse.
- **Internett-telefoni (VoIP)**:
  - Kan bruke UDP for lavere forsinkelse.
  - Tolererer noe datatap.
- **Valg av protokoll avhenger av** applikasjonens krav til pålitelighet, forsinkelse og båndbredde.

---

**Oppsummering**

- **Nettverksapplikasjoner** er kjernen i hvorfor nettverk eksisterer.
- **Utviklere** må forstå applikasjonsarkitekturer og kommunikasjonsprinsipper.
- **Valg av transportprotokoll** er kritisk og basert på applikasjonens behov.
- **Sikkerhet** er en viktig faktor og kan implementeres over transportlaget (f.eks. TLS over TCP).
- **Begrensninger** i dagens protokoller krever at applikasjoner selv håndterer visse krav.

**Notater fra Kapittel 2: Weben og HTTP**

---

**Introduksjon til Weben og HTTP**

- **Historisk kontekst**: Før tidlig på 1990-tallet ble Internett hovedsakelig brukt av forskere og akademikere for grunnleggende tjenester som e-post, filoverføring og fjernaksess.
- **World Wide Web (WWW)**: Introduksjonen av Weben tidlig på 1990-tallet av Tim Berners-Lee revolusjonerte Internett, gjorde det tilgjengelig for allmennheten og endret måten folk kommuniserer og henter informasjon på.
- **On-demand tilgang**: Weben er attraktiv fordi den gir brukere tilgang til informasjon når de ønsker det, i motsetning til tradisjonelle medier som kringkasting og TV.

---

**2.2.1 Oversikt over HTTP**

- **HyperText Transfer Protocol (HTTP)**: Applikasjonslagsprotokollen som driver Weben. Definert i RFC 1945, RFC 7230 og RFC 7540.
- **Klient og server**: HTTP er implementert i to programmer—et klientprogram (f.eks. nettlesere som Chrome eller Firefox) og et serverprogram (f.eks. Apache eller Microsoft IIS).
- **Websider og objekter**:
  - En **Webside** består av en base HTML-fil og flere **objekter** (bilder, videoer, skript osv.).
  - Hvert objekt er identifisert av en **URL** (Uniform Resource Locator) som består av en vert (hostname) og en sti (pathname).
- **Stateless protocol**: HTTP er tilstands­løs; serveren lagrer ingen informasjon om klienten mellom forespørsler.
- **Klient-server arkitektur**: Weben bruker denne arkitekturen hvor servere er alltid på og venter på forespørsler fra klienter.

---

**2.2.2 Ikke-persistente og Persistente Tilkoblinger**

- **Ikke-persistente tilkoblinger**:
  - Hver HTTP-forespørsel/respons sendes over en ny TCP-tilkobling.
  - **Prosess**:
    1. Klienten åpner en TCP-tilkobling til serveren.
    2. Sender en HTTP-forespørsel.
    3. Serveren sender en HTTP-respons.
    4. Tilkoblingen lukkes.
  - **Ulemper**:
    - Overhead ved å opprette og lukke TCP-tilkoblinger.
    - Hver objektforespørsel krever to RTTs (Round-Trip Times).
- **Persistente tilkoblinger** (standard i HTTP/1.1):
  - Flere HTTP-forespørsler/responser kan sendes over samme TCP-tilkobling.
  - **Fordeler**:
    - Reduserer antall TCP-tilkoblinger.
    - Reduserer total forsinkelse (RTT).
    - Tillater **pipelining**: Klienten kan sende flere forespørsler uten å vente på responser.

---

**2.2.3 HTTP-meldingsformat**

- **HTTP-forespørselsmelding**:
  - **Struktur**:
    - **Forespørselslinje**: Metode (GET, POST, HEAD, PUT, DELETE), URL, HTTP-versjon.
    - **Header-linjer**: Tilleggsinformasjon som Host, Connection, User-agent osv.
    - **Tom linje**: Indikerer slutten på header-seksjonen.
    - **Entitetskropp**: Data (brukes hovedsakelig med POST-metoden).
  - **Eksempel**:
    ```
    GET /index.html HTTP/1.1
    Host: www.example.com
    Connection: close
    User-agent: Mozilla/5.0
    ```
- **HTTP-responsmelding**:
  - **Struktur**:
    - **Statuslinje**: HTTP-versjon, statuskode (f.eks. 200, 404), statusmelding.
    - **Header-linjer**: Informasjon som Date, Server, Content-Type osv.
    - **Tom linje**.
    - **Entitetskropp**: Det forespurte innholdet.
  - **Vanlige statuskoder**:
    - **200 OK**: Forespørselen var vellykket.
    - **301 Moved Permanently**: Ressursen er flyttet permanent.
    - **400 Bad Request**: Forespørselen kunne ikke forstås av serveren.
    - **404 Not Found**: Ressursen ble ikke funnet.
    - **505 HTTP Version Not Supported**: HTTP-versjonen støttes ikke.

---

**2.2.4 Bruker-server Interaksjon: Cookies**

- **Formål**: Tillater servere å holde oversikt over brukersesjoner og lagre tilstandsinformasjon.
- **Komponenter**:
  1. **Set-cookie** header i HTTP-responsen fra serveren til klienten.
  2. **Cookie** header i HTTP-forespørselen fra klienten til serveren.
  3. **Cookie-fil** på klientens maskin, administrert av nettleseren.
  4. **Back-end database** på serveren for å lagre brukerinformasjon.
- **Hvordan det fungerer**:
  - Første gang en bruker besøker en nettside, tildeler serveren et unikt ID og sender det i Set-cookie headeren.
  - Nettleseren lagrer denne ID-en i sin cookie-fil.
  - Ved senere forespørsler sender nettleseren ID-en tilbake til serveren i Cookie headeren.
  - Serveren bruker ID-en til å hente eller oppdatere brukerens informasjon i databasen.
- **Personvern**: Cookies kan være kontroversielle da de kan spore brukeradferd over tid.

---

**2.2.5 Web Caching**

- **Definisjon**: En **Web cache** eller **proxy-server** er en nettverksentitet som lagrer kopier av nylig forespurte objekter for å redusere båndbreddebruk og forbedre responstid.
- **Fordeler**:
  - **Redusert responstid**: Klienter kan få raskere tilgang til innhold fra cachen enn fra den opprinnelige serveren.
  - **Redusert båndbreddebruk**: Mindre trafikk over nettverket, spesielt over flaskehalslenker.
- **Hvordan det fungerer**:
  1. Klientkonfigurasjon: Nettleseren er satt opp til å sende forespørsler via cachen.
  2. Cache-sjekk: Cachen sjekker om den har en fersk kopi av det forespurte objektet.
  3. Serverforespørsel: Hvis ikke, henter cachen objektet fra den opprinnelige serveren.
  4. Lagring og levering: Cachen lagrer en kopi og sender objektet til klienten.
- **Conditional GET**:
  - Brukes av cachen for å sjekke om en lagret kopi av et objekt er oppdatert.
  - Sender en If-Modified-Since header til serveren.
  - Serveren svarer med 304 Not Modified hvis objektet ikke er endret.

---

**2.2.6 HTTP/2**

- **Introduksjon**: Standardisert i 2015 som en oppdatering av HTTP/1.1 for å forbedre ytelse og effektivitet.
- **Hovedmål**:
  - **Redusere forsinkelse**: Tillater multipleksing av forespørsler og responser over en enkelt TCP-tilkobling.
  - **Forbedre utnyttelse av båndbredde**: Reduserer behovet for flere parallelle TCP-tilkoblinger.
  - **Header-komprimering**: Effektiviserer overføringen av HTTP-headerinformasjon.
- **Nøkkelfunksjoner**:
  - **Framing**: HTTP-meldinger brytes ned i mindre binære rammer som kan interleaves, noe som løser problemet med Head-of-Line (HOL) blocking.
  - **Prioritering**: Klienter kan tildele prioritet til forespørsler for optimal ressurslevering.
  - **Server Push**: Serveren kan proaktivt sende ressurser til klienten uten at de eksplisitt er forespurt, basert på antatt behov.
- **Fordeler over HTTP/1.1**:
  - **Bedre ytelse**: Raskere sideinnlasting og redusert forsinkelse.
  - **Effektiv ressursbruk**: Mindre overhead og bedre utnyttelse av tilgjengelig båndbredde.
- **HTTP/3 og QUIC**:
  - **QUIC**: En ny transportprotokoll over UDP som tilbyr funksjoner som multipleksing og lav latens.
  - **HTTP/3**: Designet for å operere over QUIC, viderefører forbedringene fra HTTP/2.

---

**Oppsummering**

- **HTTP** er grunnlaget for kommunikasjon på Weben, og forståelse av dets mekanismer er essensielt for nettverkskommunikasjon.
- **Persistente tilkoblinger og HTTP/2** har forbedret effektiviteten og hastigheten på Web-kommunikasjon betydelig.
- **Cookies og caching** spdns.enterprise.comiller viktige roller i tilstandshåndtering og ytelsesoptimalisering, men reiser også spørsmål om personvern.
- **Fremtidige protokoller** som HTTP/3 og QUIC fortsetter å utvikle Webens infrastruktur for å møte moderne krav til hastighet og sikkerhet.


**Notater fra Kapittel 2: Elektronisk Post på Internett**

---

**Introduksjon til Elektronisk Post**

- **Historisk betydning**: E-post har vært en av de mest populære applikasjonene på Internett siden begynnelsen, og har utviklet seg til å bli mer avansert og kraftfull over tid.
- **Asynkron kommunikasjon**: E-post tillater brukere å sende og lese meldinger når det passer dem, uten behov for å koordinere tidsplaner.
- **Fordeler over vanlig post**: Rask levering, enkel distribusjon og lav kostnad. Moderne e-post støtter vedlegg, hyperkoblinger, HTML-formatering og innebygde bilder.

---

**2.3.1 Simple Mail Transfer Protocol (SMTP)**

- **Hovedprotokoll for e-post**: SMTP er definert i RFC 5321 og er kjerneprotokollen for overføring av e-post på Internett.
- **Klient- og serversider**: SMTP har to sider; klienten kjører på avsenderens mailserver, og serveren kjører på mottakerens mailserver. Begge sider kjører på alle mailservere.
- **Begrensninger**:
  - **7-bits ASCII**: SMTP støtter kun 7-bits ASCII-tegnsett i meldingskroppen, noe som krever at binære data må kodes før sending.
- **Overføringsprosess**:
  1. **Avsender**: Brukeren komponerer en melding og sender den via sin brukeragent (e-postklient).
  2. **Avsenders mailserver**: Meldingen plasseres i en utgående kø.
  3. **SMTP-klient**: Avsenderens mailserver åpner en TCP-tilkobling til mottakerens mailserver på port 25.
  4. **SMTP-håndtrykk**: Klienten og serveren utveksler kommandoer og responser for å etablere kommunikasjon.
  5. **Meldingsoverføring**: Meldingen overføres over TCP-tilkoblingen.
  6. **Mottakers mailserver**: Meldingen lagres i mottakerens postkasse.
  7. **Mottaker**: Brukeren henter meldingen fra sin mailserver via sin brukeragent.

- **Direkte forbindelse**: SMTP etablerer en direkte TCP-forbindelse mellom avsenderens og mottakerens mailserver, uten mellomliggende servere.
- **Kommandoer og responser**:
  - Typiske SMTP-kommandoer: HELO, MAIL FROM, RCPT TO, DATA, QUIT.
  - Serveren gir svar med koder og meldinger som indikerer status.

---

**2.3.2 Meldingsformat for E-post**

- **RFC 5322**: Spesifiserer formatet for e-postmeldinger, inkludert header-linjer og meldingskropp.
- **Header-linjer**:
  - **Obligatoriske**: From:, To:
  - **Valgfrie**: Subject:, CC:, BCC:, osv.
  - Hver header-linje består av et nøkkelord, kolon og en verdi.
- **Meldingskropp**:
  - Følger etter en tom linje som skiller den fra header-seksjonen.
  - Inneholder selve meldingen i ASCII-format.
- **Forskjell fra SMTP-kommandoer**:
  - Header-linjene er en del av e-postmeldingen, mens SMTP-kommandoer brukes under overføringen mellom mailservere.

---

**2.3.3 Mail Access Protokoller**

- **Utfordring**: Mottakeren må hente meldinger fra mailserveren, men SMTP er en push-protokoll og ikke egnet for dette.
- **Løsninger**:
  - **HTTP**:
    - Brukes av webbaserte e-posttjenester (f.eks. Gmail).
    - Mottakerens brukeragent (nettleser eller app) henter meldinger via HTTP.
    - Krever at mailserveren har en HTTP-grensesnitt i tillegg til SMTP.
  - **IMAP (Internet Mail Access Protocol)**:
    - Definert i RFC 3501.
    - Lar brukeren få tilgang til og administrere meldinger direkte på mailserveren.
    - Støtter funksjoner som mappeorganisering, flagging av meldinger og synkronisering mellom enheter.
- **Fordel med delt mailserver**:
  - Brukerens mailserver er alltid på og koblet til Internett, slik at meldinger kan mottas når som helst.
  - Brukere trenger ikke å ha sine egne mailservere på lokale maskiner.

---

**Oppsummering**

- **E-postsystemets komponenter**:
  - **Brukeragent**: Programmet som brukeren interagerer med for å sende og motta e-post.
  - **Mailservere**: Håndterer lagring og overføring av meldinger.
  - **Protokoller**: SMTP for sending av e-post mellom servere; IMAP eller HTTP for tilgang til e-post fra mailserveren.
- **Protokollfunksjonalitet**:
  - **SMTP**: Brukes for å overføre meldinger fra avsenderens mailserver til mottakerens mailserver over TCP.
  - **IMAP**: Tillater fleksibel og kontinuerlig tilgang til meldinger på serveren.
  - **HTTP**: Gir webbasert tilgang til e-post, ofte brukt i nettbaserte e-posttjenester.
- **Viktighet av e-post**: Fortsetter å være en essensiell og mye brukt tjeneste på Internett, med protokoller som utvikler seg for å møte moderne behov.


