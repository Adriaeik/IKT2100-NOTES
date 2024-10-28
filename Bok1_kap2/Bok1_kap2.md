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