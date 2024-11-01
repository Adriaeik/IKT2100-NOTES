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