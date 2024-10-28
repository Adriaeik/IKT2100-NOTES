### nettverkslaget:

- **Nettverkslaget (Layer 3)** i OSI-modellen er ansvarleg for å dirigere pakkar mellom ulike nettverk ved å bruke IP-adressering.
- **Hovudkomponentar**: Routrar og verts-enheter (sluttbrukarenheter).
- **Oppgåver**: Ruting, adressering, og framføring av datapakkar over fleire nettverk.
- **Protokollar**: IP (Internet Protocol) er den mest kjende protokollen som opererer på dette laget.
- Nettverkslaget er **implementert i både kablede og trådlause enheter** og er ikkje begrensa til spesifikke typar forbindelsar.

### routing:

- **Routing**: Involverer langsiktige beslutningar om kva rute ein datapakke skal følgje for å nå sitt mål. Typiske einingar som utfører routing er **routrar**.
- **Forwarding**: Involverer kortsiktige beslutningar om kva grensesnitt datapakkar skal sendast vidare gjennom etter å ha mottatt dei. Dette skjer lokalt i ein **ruter** eller **switch**.


Her ser det ut som du må identifisere kva handlingar som høyrer til **data plane** og kva som høyrer til **control plane** i nettverkslaget.


### Data plane og control plane:
- **Data plane**: Handlar om å transportere datapakkar frå ein port til ein annan. Handlingar som forwarding og behandling av pakkar skjer her.
- **Control plane**: Handlar om å ta beslutningar om ruting og bygging av forwarding-tabellar.

- **Control plane**: Dette er delen av nettverket som bestemmer korleis datapakkar skal bli rutta. Den handlar om å lage rutingtabellar og å ta avgjerder om kva veg datapakkane skal gå.
- **Data plane**: Dette er delen som faktisk flyttar datapakkar frå ein port til ein annan, basert på rutingtabellen som control plane har bestemt.


### per-router control-plane og SDN control-plane:
- **Per-router control-plane**: Kvar ruter styrer seg sjølv og kommuniserer direkte med andre routrar for å oppdatere routing-tabellar. Dette er ein desentralisert modell.
- **SDN control-plane**: Routing-avgjersler blir gjort av ein sentralisert kontroller som sender ferdige routing-instruksjonar til routrar. Dette er ein sentralisert modell som gir meir fleksibilitet og enklare styring av nettverket.

- **Per-router control-plane**: I denne tilnærminga har kvar ruter si eiga autonome kontrollplane, som betyr at ruteren sjølv tar avgjerder basert på informasjon frå andre routrar og den routing-algoritmen ruteren brukar. Det er ein desentralisert tilnærming.
- **SDN control-plane**: Her blir kontrollplanet skilt frå sjølve forwarding-enheten i ruteren. I staden er det ein sentralisert kontroller (som kan administrere fleire routrar) som tar avgjerdene om ruting, og routrane følger desse instruksjonane.

### Notat om "Match+Action" i rutere:

- **"Match+Action"** skjer på **input-porten** i ein ruter.
  - Når ein pakke kjem inn i ruteren, blir destinasjonsadressa i pakken analysert (match), og ruteren avgjer kor pakken skal sendast vidare (action).
  - Input-porten slår opp destinasjonsadressa i forwarding-tabellen for å finne ut kva output-port som skal brukast.
  - Etter oppslaget blir pakken sendt vidare til switching-fabricen for å flyttast til den bestemte output-porten.

Dette er viktig for effektiv datapakkehandsaming og ruting i moderne nettverksutstyr som routrar.

### Notat om **Packet Dropping**:
- Når ein datapakke blir sendt gjennom switching-fabricen til output-porten, og det ikkje er ledige bufferar, kan to ting skje:
  - **Enten** vil pakkar bli droppa (tapt).
  - **Eller** vil ein annan pakke bli fjerna frå bufferet for å lage plass til den nye pakken (basert på konfigurasjonen).
  - **Viktig**: Pakkar blir aldri sendt tilbake til input-porten.

### Notat om **Head of Line (HOL) Blocking**:
- **Head of Line (HOL) Blocking** oppstår når ein datapakke som står fremst i køen ventar på å bli sendt vidare, men ikkje kan bli prosessert. Dette forhindrar dei andre pakkane bak i køen frå å bevege seg framover.
  - Dette fenomenet reduserer effektiviteten i køhandteringa, då pakkar som kunne ha blitt sendt vidare, blir blokkert av ein pakke framme i køen.
  
  
### komponentane av IPv4-protokollen:
- IPv4 datagram format.
- Packet handling conventions at routers (e.g., segmentation/reassembly).
- IPv4 addressing conventions.
Desse tre er sentrale komponentar av IPv4-protokollen. Fjern "ICMP (Internet Control Message Protocol)", då det er ein separat protokoll, sjølv om den er tett knytt til IPv4.

### Notat om felta i IPv4-headeren:

1. **Version field**: Dette feltet inneheld IP-versjonen, som for IPv4 vil vere versjon 4.
2. **Type-of-service field**: Dette feltet brukast for å signalisere ønskjer om spesifikk teneste (QoS) ved hjelp av ECN (Explicit Congestion Notification) og Differentiated Service bits.
3. **Fragmentation offset field**: Dette feltet styrer segmentering og samansetjing av pakkar når dei er for store for overføring over eit nettverkssegment.
4. **Time-to-live (TTL) field**: Dette feltet blir redusert med 1 ved kvart ruter-hop. Når det når 0, blir pakken droppa for å unngå endelause looper i nettverket.
5. **Header checksum field**: Inneheld ei sjekksum for å kontrollere feil i headeren.
6. **Upper layer field**: Dette feltet inneheld protokollnummeret for det neste laget, som til dømes TCP eller UDP.
7. **Payload/data field**: Dette feltet inneheld data frå det øvre laget, som til dømes ein TCP- eller UDP-segment.
8. **Datagram length field**: Dette feltet viser den totale lengda av datagrammet, inkludert header og data.

Dette notatet hjelper deg med å forstå dei viktigaste felta i IPv4-headeren og funksjonane deira.


### Notat om IP-adresser:

- **IP-adresser** er alltid knytt til eit spesifikt **grensesnitt (interface)** på ein enhet, ikkje til sjølve enheten. Dette betyr at om ein vert (host) eller ein ruter har fleire nettverksgrensesnitt, vil kvart grensesnitt ha si eiga IP-adresse.
  
- **Vertar (hosts)** med fleire grensesnitt, til dømes ein datamaskin med både Ethernet og Wi-Fi, vil ha ei unik IP-adresse for kvart grensesnitt.
  
- **Routrar** har fleire grensesnitt, eitt for kvart nettverk dei er tilkopla. Kvar av desse grensesnitta vil ha ei unik IP-adresse for å kunne kommunisere på tvers av nettverk.

- For å kunne kommunisere ved hjelp av **IP-protokollen**, må ein enhet ha minst éin IP-adresse. Dette er nødvendig for adressering i nettverket.


### Notat om IP-subnett:

- **IP-subnett** er ei gruppe av enheter på eit nettverk som har ein felles del av IP-adressa sine høgast rangerte bit. Dette betyr at enhetene på same subnett har ein felles **subnettmaske**, som bestemmer kor mange av bitane i IP-adressa som blir brukt til å identifisere subnettet.
  
- **Enheter på same subnett** kan kommunisere direkte med kvarandre utan å passere gjennom ein ruter. Dette er fordi dei deler eit felles adresseområde, og kommunikasjonen skjer innanfor same lokale nettverk.

- Ein IP-subnett er **ikkje** definert av produsenten av utstyret eller at ein alltid har dei første 16 bitane like; subnett kan variere i storleik basert på subnettmaske.

### Notat om subnetting og maksimalt antal grensesnitt:

- For eit nettverk med ein **/24 subnettmaske** som i **223.1.2/24**, har du totalt 256 IP-adresser. Dette kjem av at det er \(2^{(32-24)} = 2^8 = 256\) adresser tilgjengelige i dette subnettet.
  
- **Maksimalt antal grensesnitt** i subnettet vil vere 256, men to av desse IP-adressene er reserverte: éi for nettverksadressa og éi for broadcast-adressa. Dermed har du 254 brukbare IP-adresser for grensesnitt (enheter) i subnettet.

- **Subnettmaske /24** betyr at dei første 24 bitane i IP-adressa er nettverksdelen, og dei siste 8 bitane er for hostar.

### Notat om subnetting med /29:

- For eit subnett med ein **/29 subnettmaske** (som i **223.1.3/29**), har du totalt \(2^{(32-29)} = 2^3 = 8\) adresser tilgjengelege i subnettet.
  
- Av desse 8 adressene er to reserverte: éi for nettverksadressa og éi for broadcast-adressa. Dermed har du 6 brukbare IP-adresser for grensesnitt (enheter) i subnettet.

- **Subnettmaske /29** betyr at dei første 29 bitane i IP-adressa er nettverksdelen, og dei siste 3 bitane er for hostar (grensesnitt).


### DHCP Request Message:

- **DHCP request-meldingar** blir sendt som kringkasting (broadcast) ved å bruke IP-adressa **255.255.255.255** som destinasjon. Dette er typisk når klienten ikkje har ein IP-adresse enda og må nå ein DHCP-server.

- Ein **DHCP request-melding** kan innehalde IP-adressa som klienten ønskjer å bruke, eller ei adresse som klienten tidlegare har fått tildelt.

- **Transaksjons-ID-en** i ein DHCP request-melding blir brukt for å knytte saman framtidige DHCP-meldingar som høyrer til same sesjon (for eksempel mellom ein spesifikk klient og server).

- DHCP request-meldingar er ein obligatorisk del av DHCP-protokollen, og dei blir alltid sendt frå klienten til DHCP-serveren, ikkje omvendt.

### Forskjellar mellom IPv4 og IPv6:

- **Flow Label Field**: Dette feltet er unikt for IPv6. Det er designa for å gi spesifikke flyt-identifikasjonar til pakkar i same datastraum, som kan brukast for Quality of Service (QoS)-behandling.

- **128-bit Source and Destination IP Addresses**: IPv6 brukar 128-bit-adresser, som gjer det mogleg med eit mykje større adresseområde enn IPv4, som berre har 32-bit-adresser. Dette er ein viktig forskjell mellom IPv4 og IPv6.

- **Header Checksum**: Dette feltet finst i IPv4, men ikkje i IPv6. IPv6 har fjerna checksummen for å forenkle ruteprosessen og auke effektiviteten.

- **Time-to-Live (TTL) vs. Hop Limit**: IPv4 nyttar TTL-feltet for å avgrense levetida til ein pakke, medan IPv6 kallar dette feltet for **Hop Limit**, men det fungerer på same måte.

- **Options Field**: IPv4 eit opsjonsfelt, medan IPv6 ikkje har det. IPv6 bruker i staden ekstensjons-headerar for å legge til tilleggsinformasjon.

### DHCP (Dynamic Host Configuration Protocol):

- **Hovudformålet med DHCP** er å gi ein enhet (klient) som koblar seg til eit IP-nettverk, ein IP-adresse automatisk. Dette gjer at klientar kan kommunisere på nettverket utan behov for manuell konfigurering av nettverksinnstillingar.
  
- DHCP tildeler dynamiske IP-adresser, noko som betyr at adresser kan gjenbrukast når enheiter koplar seg frå nettverket, noko som effektiviserer adressebruken.

- DHCP sørger for fleire opplysningar utover IP-adressering, som **subnettmaske**, **standard gateway**, og **DNS-servere**, slik at klienten kan få fullstendig nettverkstilkobling.
