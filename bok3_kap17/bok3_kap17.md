### 17.1 Introduksjon til Ethernet
Ethernet vart utvikla av Xerox’s Palo Alto Research Center i 1976 og har sidan vorte den mest populære fysiske lagsteknologien i lokale nettverk (LAN). Ethernet er standardisert i IEEE 802.3 og legg retningslinjer for oppsett av Ethernet-nettverk, slik at ulike einingar kan kommunisere med kvarandre. Ethernet er kjent for å balansere godt mellom hastigheit, kostnad og enkel installasjon, noko som har gjort det populært.

**Generasjonar av Ethernet:**
1. **Standard Ethernet:** 10 Mbps
2. **Fast Ethernet:** 100 Mbps (IEEE 802.3u) - gir betre feilkorrigering og høgare gjennomstrøyming.
3. **Gigabit Ethernet:** 1 Gbps - utvikla for multimedia og VoIP.
4. **10 Gigabit Ethernet:** 10 Gbps

### 17.1.2 Rammeformat og lengde
Eit Ethernet-rammeformat inneheld mellom minimum 46 byte og maksimum 1500 byte med data. Strukturen er som følgjer:
- **Preamble**: 7 byte for å signalisere byrjinga av ei ramme.
- **SFD (Start Frame Delimiter)**: Identifiserer byrjinga av ramme (10101011).
- **DA/SA**: Adresse for destinasjon og kjelde.
- **Lengde/type-felt**: Angir protokoll eller lengde på data.
- **Datafelt**: Inneheld data frå øvre lag.
- **FCS (Frame Check Sequence)**: Brukar CRC-32 for feildeteksjon.

### 17.2 Industriell Ethernet
Industriell Ethernet er utvikla for røffare omgjevnader i industrien, med robust maskinvare og komponentar som kan handtere støv, høg temperatur, vibrasjon og liknande utfordringar. Industriell Ethernet har spesifikke krav til pålitelegheit, sikkerheit, og QoS (Quality of Service) for å støtte sanntids kommunikasjon i industriprosessar.

### 17.3 Evolution of Real-Time Fieldbuses
Ethernet og TCP/IP er gode nok for generell kontroll på produksjonsgolvet, men dei klarar ikkje handtere kommunikasjon inne i maskiner. Derfor vart real-time fieldbuses utvikla for deterministisk kommunikasjon mellom maskinkontroll, aktuatorar og sensorar. 

Ethernet vart populært som fieldbus på grunn av låge kostnadar og enkel tilgang til Ethernet-komponentar som NICs og CAT5-kablar. Dette førte til utvikling av industrielle Ethernet-protokollar med eigenskapar som real-time og determinisme. Kjende protokollar: EtherCAT, Ethernet Powerlink, EtherNet/IP, SERCOS III, og PROFINET IRT.

### 17.4 Real-Time Deterministic Fieldbus Realization
Tre tilnærmingar for å oppnå real-time determinisme i Ethernet:
1. **Standard software/standard Ethernet**: Byggjer på TCP/IP-lag, men med begrensa real-time støtte.
2. **Open software/standard Ethernet**: Bruker eigne protokollar oppå standard Ethernet for å reservere tid og redusere latency.
3. **Standard software/modified Ethernet**: Kombinerer ny protokoll og spesialtilpassa maskinvare for determinisme.

### 17.5 Introduksjon til EtherNet/IP
I industrien har maskinkontroll tidlegare brukt proprietære nettverk, noko som skapte utfordringar med interoperabilitet. Ved å bruke real-time Ethernet-feltbusar, som EtherNet/IP, kan ein oppnå betre pris og yting. EtherNet/IP vart utvikla av Allen Bradley og ODVA i 2000 som ein del av CIP (Common Industrial Protocol) og brukar TCP/IP for kommunikasjon.

### 17.6 Eigenskapar
Nokre hovudeigenskapar ved EtherNet/IP inkluderer:
- Producer-consumer modell for effektiv kommunikasjon.
- Real-time deterministisk natur for raske oppdateringar.
- Full dupleks drift, QoS-støtte og CSMA/CD for kollisjonsdeteksjon.
- Støtte for både unicast og multicast-adressering.

### 17.7 EtherNet/IP-lagmodell
EtherNet/IP lagmodellen kombinerer CIP frå sesjonslaget oppover og TCP/IP frå transportlaget. UDP og TCP blir brukt for tidskritisk og ikkje-tidskritisk datakommunikasjon høvesvis, og MAC-teknikk for kollisjonsstyring.

### 17.8 Producer-Consumer Model
EtherNet/IP er basert på ein producer-consumer modell, der data ikkje er knytt til spesifikke kjelde- eller destinasjonsadresser. Denne modellen gir effektiv slave-til-slave-kommunikasjon, der kvar mottakar filtrerer data grunna kringkasting.

### 17.9 Infrastruktur for EtherNet/IP-applikasjonar
EtherNet/IP støttar både tidskritisk og ikkje-tidskritisk data og brukar aktiv infrastruktur. Lag 2 og 3 i OSI-modellen blir kobla saman via switchar, som gir VLAN-støtte for å separere tidskritisk og ikkje-tidskritisk trafikk.

### 17.10 Karakterisering av EtherNet/IP-trafikk
- **Explicit messaging**: Ikkje-tidskritisk trafikk, brukt til konfigurasjon og diagnose. Kan vere både unicast (TCP/IP) og multicast (t.d. ARP, DHCP).
- **Implicit messaging**: Tidskritisk trafikk, brukt til datautveksling mellom kontroller og I/O-enheiter, typisk i UDP/IP.

### 17.11 Sameksistens av EtherNet/IP med CIP
CIP (Common Industrial Protocol) er plassert i prosesslaget saman med andre tenester som HTTP, FTP og DNS, og bruker TCP for ikkje-tidskritiske og UDP for tidskritiske meldingar. 

### 17.12 Prioritering av meldingar i EtherNet/IP
EtherNet/IP nyttar QoS (Quality of Service) for å prioritere tidskritiske data. To QoS-typar er definert: Differentiated Services (Diffserv) og IEEE 802.1Q (VLAN tagging). CIP-rammer med høgare prioritet kan hoppe fram i køen og blir sendt før andre rammer, som vist i figuren.

### Oppsummering av Kapittel 17: Ethernet og Industrielle Applikasjonar

1. **Introduksjon til Ethernet**  
   Ethernet er ein standardisert LAN-teknologi som vart utvikla på 1970-talet og har blitt svært populær grunna balansen mellom hastigheit, kostnad og installasjonsvennlegheit. Ethernet har gjennomgått fleire generasjonar, inkludert Fast Ethernet, Gigabit Ethernet og 10 Gigabit Ethernet.

2. **Industriell Ethernet**  
   Industriell Ethernet er utvikla for røffe industrielle miljø og er robust mot påverknadar som høg temperatur, støv og vibrasjon. Denne typen Ethernet har krav til pålitelegheit, nettverkssikkerheit og Quality of Service (QoS) for å støtte sanntidskommunikasjon.

3. **Utvikling av Real-Time Fieldbuses**  
   Tradisjonell Ethernet og TCP/IP klarar ikkje sanntidskrav for kontrollsystem, så real-time fieldbuses som EtherCAT, EtherNet/IP, og PROFINET IRT vart utvikla for deterministisk kommunikasjon i industrien.

4. **Real-Time Deterministic Fieldbus Realization**  
   Det finst tre tilnærmingar for real-time determinisme: standard programvare på standard Ethernet, open programvare på standard Ethernet, og standard programvare på modifisert Ethernet.

5. **EtherNet/IP**  
   EtherNet/IP er ein CIP-basert protokoll utvikla for industriell automasjon som støttar både UDP (for tidskritiske data) og TCP (for ikkje-tidskritiske data). Den nyttar CSMA/CD for å handtere tilgang til felles nettverk.

6. **Producer-Consumer Modell**  
   EtherNet/IP nyttar ein producer-consumer modell, som tillét effektiv dataoverføring der mottakarane filtrerer data frå kringkasting utan spesifikke adressekrav.

7. **Infrastruktur for EtherNet/IP-applikasjonar**  
   EtherNet/IP nyttar både aktiv og passiv infrastruktur med VLAN-støtte for å separere tidskritisk og ikkje-tidskritisk trafikk. Dette gir moglegheit for effektiv trafikkstyring i industrielle nettverk.

8. **Trafikkarakterisering i EtherNet/IP**  
   Trafikken er delt i **explicit messaging** (ikkje-tidskritisk) og **implicit messaging** (tidskritisk), der implicit messaging nyttar UDP/IP for rask datautveksling mellom kontrollerar og I/O-enheiter.

9. **Sameksistens med CIP**  
   CIP er plassert i prosesslaget saman med andre tenester og bruker UDP og TCP for tidskritiske og ikkje-tidskritiske meldingar, høvesvis.

10. **Prioritering av Meldingar (QoS)**  
    EtherNet/IP bruker QoS for å prioritere tidskritiske data. Differentiated Services (Diffserv) og IEEE 802.1Q er brukt for å markere høgprioriterte rammer som kan få prioritet i nettverkskøen. 
