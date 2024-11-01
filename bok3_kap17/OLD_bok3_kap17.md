**IP og Ethernet** er hovudkomponentane i moderne datanettverk og blir ofte brukte saman for å transportere data mellom datamaskiner og einingar. **Ethernet** er teknologien som sørgjer for fysisk og datalink-lag-kommunikasjon, og spesifiserer korleis data skal sendast over kabel eller trådlaus tilkopling, medan **IP (Internet Protocol)** sørgjer for adressering og ruting av datapakkar på nettverkslaget.

I ei automasjonssetting kan IP og Ethernet brukast for å skape stabile og raske kommunikasjonssystem mellom ulike industrielle einingar, sensorer og kontrollsystem. Med IP/Ethernet får vi fordelar som høgare hastigheit, større fleksibilitet og betre skalerbarheit samanlikna med eldre, meir analoge kommunikasjonsløysingar. Ethernet kan brukast både som eit lokalt nettverk (LAN) og i større distribuerte nettverk, avhengig av behov og utforming.

**HART (Highway Addressable Remote Transducer) Protocol: Kort Introduksjon**

HART-protokollen er ein open nettverksprotokoll for prosesskontroll, utvikla for å fungere saman med eksisterande 4–20 mA analoge signal. Det betyr at HART kan overføre digitale data samtidig som den bevarer den tradisjonelle analoge signalstrukturen, som ofte vert brukt til å overføre måle- og kontrollinformasjon. HART nyttar frekvensskiftnøkling (FSK) til å sende digitale signal over same leiing som analoge signal utan at dette påverkar dei.

**Hovudpunkt om HART:**
- **Topologiar:** HART-nettverk kan vere punkt-til-punkt, multipleksing, eller multidrop-konfigurasjonar. Dette gir fleksibilitet i installasjon og tilpassing til ulike nettverksoppsett.
- **Master-Slave-kommunikasjon:** HART støttar master-slave-kommunikasjon, der ein master (typisk ein datamaskin eller kontroller) initierer kommunikasjon med ein eller fleire slave-enheiter som sensorar eller aktuatorar. 
- **Dataoverføring:** HART overfører digitale data på 1200 bps (bits per sekund), noko som er tilstrekkeleg for å sende parametere og diagnostikk utan å forstyrre dei analoge signala.

**Eksempel på bruksområde:**
- **Kalibrering og diagnostikk:** Gjer det mogleg for feltpersonell å hente detaljerte data for feilsøking og vedlikehald.
- **Multiplexing:** Med fleire HART-enheiter i same nettverk kan ein få fleire data utan behov for meir kabelinfrastruktur, ved bruk av ein multiplexer som kan samle data frå fleire kjelder.

HART er mykje nytta i industriell automatisering, spesielt i system som krev både sanntids analog data og digitale parametere, som til dømes fjernovervåking og kontroll av prosessutstyr.

**17.3 BUILDING A FIELDBUS NETWORK**

Fieldbus-nettverket bruker eit par med leidningar for å både drive feltapparata og overføre prosessignal til den lokale kontrolleren. Ulike topologiar vert brukt for å handtere tovegs digital kommunikasjon (frå eining til vert og omvendt) i eit lokalt nettverk (LAN) sett opp med Fieldbus-teknologi. Blant dei ulike Fieldbus-variantane som er tilgjengelege, er Foundation Fieldbus og PROFIBUS-PA dei mest brukte for prosesskontrollføremål.

Ein typisk DCS (Distributed Control System) brukar skjermede, tvinna par av kablar til å overføre 4–20 mA strømsignal frå sensorar og kontrollsignal til aktuatorar, ventilar, etc., via I/O-kort. Figuren viser eit DCS med fleire tilkoblede feltapparat, kor to leidningar koplar dei saman til systemet.

Eg kan lese og gje samandrag av tekstinnhald som du sender i bilete. Her er samandrag frå overskriftene og innhaldet i biletet du sendte.

### 17.3 BUILDING A FIELDBUS NETWORK
Fieldbus-nettverk brukar eit toledarkabelsystem for å drive feltutstyret og for å overføre prosessignal til ein lokal kontroller. Systemet nyttar ulike nettverkstopologiar, inkludert Foundation Fieldbus og PROFIBUS-PA, som hovudsakleg er nytta innan prosesskontroll. Fieldbus-systemet er ein lokalnettverksstruktur (LAN), som støttar tovegskommunikasjon av digitale signal mellom feltutstyr og verten (kontrolleren). 

### 17.3.1 MULTIFIELDBUS DEVICES
Multifieldbus-enheter kan koplast saman i ulike strukturar, som "stjerne"-kopling eller "kjeda" nettverk, der berre to terminatorar er nødvendige i begge tilfelle. Dette sikrar stabilitet og redusert signalforstyrring i nettverket.

### 17.3.2 EXPANDING THE NETWORK
For å utvide nettverket kan ein bruke nettverksregulatorar som hubar, repeaterar, switchar og routerar. Desse einingane regulerer trafikken i nettverket ved å sørgje for rett rute for data og tryggleik. OSI-modellen på sju lag sikrar at desse einingane opererer på riktig nivå for effektiv kommunikasjon.

#### 17.3.2.1 NICs
Network Interface Cards (NICs) koplar serverar, klientar og annan maskinvare til nettverket, omformar data frå datamaskinen til elektriske signal og følgjer spesifikke protokollar som Ethernet for å sikre effektiv og trygg datakommunikasjon.

#### 17.3.2.2 Hubs
Hubar opererer på OSI lag 1 og koplar fleire einingar saman i eit kollisjonsdomene, der alle einingar deler båndbredden og ein eventuell kollisjon kan redusera nettverkseffektiviteten. Hubar kan vere anten passive eller aktive (repeater-hubar).

#### 17.3.2.3 Repeaters
Repeaterar forsterkar signalet i lange kabelstrekningar og kan utvide eit nettverk opp til 9500 meter med fire segment. Repeaterar gir galvanisk isolasjon og bidrar til å oppretthalde signalkvaliteten i lange nettverkstrasear, noko som er avgjerande for spesielle sikkerheitssoner.

Her er eit kombinert samandrag og bullet points frå bilda:

### 17.3.2.4 **Switches**
Ein switch er ein **lag 2-enhet** i OSI-modellen (datalink-laget) og kan gjere intelligente avgjerder basert på header-informasjonen i dataene. Eit switch bygger opp ein tabell for MAC-adresser og distribuerer data berre til den aktuelle porten i staden for å sende til alle.

- **Funksjon**: Filtrerer og sender data berre til den rette mottakaren.
- **Læring**: Bruker MAC-adressar til å bygge opp ein adresse-tabell.
- **Full-duplex modus**: Gjer at kvar port har sin eigen kollisjonsdomene, noko som reduserer sjansen for kollisjonar.
- **Fordelar**: Høyrer ikkje på broadcast-stormar, intelligent frame-forwarding, og læring av hardware-adresser.
- **Metodar for frame-forwarding**:
  - **Store and Forward**
  - **Cut Through (Real Time)**
  - **Fragment Free**

### 17.3.2.5 **Bridges**
Ein bridge koblar saman to eller fleire LAN eller segment i same nettverk. Bridges opererer også på lag 2 i OSI-modellen og kan filtrere trafikk for å unngå overbelastning.

- **Oppgåve**: Forbinder segment som opererer på ulike hastigheiter eller fysiske lag, som kabel og fiberoptikk.
- **Filtrering**: Unngår overflødig trafikk gjennom MAC-adressefiltrering.
- **Fordel**: Kan føre til mindre overbelastning i nettverket, ettersom det kun sender nødvendig trafikk mellom segment.

### 17.3.2.6 **Routers**
Ein router opererer på lag 3 i OSI-modellen (nettverkslaget) og bestemmer korleis pakkar blir sendt mellom nettverk basert på nettverks-adresser.

- **Funksjon**: Sender data mellom nettverk ved å bruke IP-adresser, i staden for MAC-adresser.
- **Tabelltypar**: 
  - **Routed Protocol**: Bruker logiske adresser til å rute pakkar.
  - **Routing Protocol**: Bygger opp dynamiske rutetabellar med protokollar som RIP, EIGRP, og OSPF.
- **Fordelar**: 
  - Lager eigne kollisjonsdomener, som reduserer kollisjonar.
  - Filtrerer broadcast og multicast-trafikk.

**17.3.2.7 Gateways**

- Ein gateway utfører protokollkonvertering og lar nettverk med ulike protokollar kommunisere.
- Gatewayar er protokollspesifikke, noko som betyr at ein må bruke korrekt gateway for å overføre data effektivt mellom to nettverk.
- Døme: Data frå eit Foundation Fieldbus HSE-nettverk kan overførast til eit PROFIBUS-nettverk gjennom ein gateway som konverterer protokollen.
- Gatewayar konfigurerast ved å tilpasse dataadresse, datatype, og annan informasjon i protokollen for å passe til formatet på det nye nettverket.

**17.3.2.8 Routers vs. Gateways**

- Router opererer på nettverkslaget (lag 3), medan ein gateway opererer på transportlaget (lag 4).
- Routere regulerer trafikk mellom liknande nettverk (protokollavhengig), medan gatewayar regulerer trafikk mellom ulike nettverk (protokolluavhengig).
  - Døme: Ein router kan koble eit LAN-nettverk med Windows 2000 til internett via TCP/IP-protokollen.
  - Gatewayar kobler ulike nettverksprotokollar, som når ein kobler eit Windows NT-nettverk til eit NetWare-nettverk.
- Routere bruker routing-tabellar, medan gatewayar fungerer som inngangs-/utgangspunkt til eit nettverk, på liknande måte som døra til eit hus.
### 17.4 **Powering Fieldbus Devices**
- Fieldbus-nettverk brukar to straumforsyningslinjer som ber både likestraum og ein kommunikasjonssignal på 31,25 kHz.
- Normale straumforsyningar kan ikkje nyttast her sidan dei kan kortslutte kommunikasjonssignalet.
- Straumforsyningar må overhalde standarden **IEC 61158-2** for å sikre at signala vert overført utan forstyrrelser.
- **Redundante straumforsyningar** bør nyttast for høg systemtilgjenge, slik at ein kan bytte mellom primær og sekundær straum utan avbrot.
- Figur 17.11 viser ein oppsett med terminatorar og IEC 61158-2-kompatibel impedansmodul som stabiliserer signala.

### 17.5 **Shielding**
- Fieldbus-instrument må skjerme kabelane for å unngå elektromagnetiske forstyrringar frå omgivande utstyr som motorar.
- Kabelane bør vere i ein metallkanal som også gjev mekanisk vern.
- **Jording**: Spor og trunk-kablar bør jordast for å unngå interferens og sikre pålitelig kommunikasjon.
- **Kapacitiv skjerming** blir anbefalt ved fleirpunktjordingsbehov for å redusere interferens utan at skjermen fungerer som leiar.
  
Dette gjev ein god oversikt over korleis Fieldbus-nettverk kan beskyttast og stabiliserast gjennom korrekt bruk av straumforsyningar og skjerming, noko som er essensielt i støyende industrielle miljø.

### 17.6 CABLES

Når Fieldbus-signalet beveger seg gjennom "spurs" og "trunks," blir det dempet og kan etter hvert bli for svakt til å gjenkjennes riktig. Derfor er det restriksjoner på maksimal kabellengde, som er avhengig av hvilken type kabel som benyttes. Standardene i IEC 61158-2 definerer typiske kabellengder og spesifikasjoner for ulike kabeltyper for å maksimere bakoverkompatibiliteten.

#### Typer kabler og lengder:
- **Type A**: Støtter opptil 1900 meter med en enkel, skjermet og tvunnet par-kabel.
- **Type B**: Støtter opptil 1200 meter og har flere par, tvinnet og skjermet.
- **Type C** og **Type D**: Har begrenset bruk på grunn av kortere lengde (400 m og 200 m).

#### Fleirkabelinstallasjon:
- Multi-tvunnede par-kabler blir ofte brukt i større installasjoner, da de reduserer installasjonskostnader. Diagrammet viser en flerparskabel fra kontrollrommet til fordelingsbokser, som deretter fører signalene til felt-enheter.

#### Kabelblanding og lengdeberegning:
Når to eller flere typer kabler kombineres i et segment, må total lengde bestemmes ved en formel som sikrer at summen av forholdet mellom hver kabels lengde og maksimale lengde ikke overstiger 1.

#### Kabellengde og strømforbruk:
Felt-enheter i Fieldbus-systemer trekker strøm fra nettverket, noe som skaper spenningstap langs ledningene. Maksimal kabellengde og antall enheter som kan kobles til påvirkes av strømforbruket og kabelens motstand.

Formelen som brukes til å beregne maksimal kabellengde når flere kabeltyper kombineres i et Fieldbus-segment, er som følger:

$$
\frac{L_x}{L_{\text{max } x}} + \frac{L_y}{L_{\text{max } y}} \leq 1
$$

Der:
- $L_x$ = lengde på kabeltype x
- $L_y$ = lengde på kabeltype y
- $L_{\text{max } x}$ = maksimal lengde for kabeltype x
- $L_{\text{max } y}$ = maksimal lengde for kabeltype y

Denne formelen sikrer at summen av hver kabels proporsjonale lengde i forhold til dens tillatte maksimallengde ikke overskrider 1. Hvis dette kravet oppfylles, kan kombinasjonen av kabler i segmentet betraktes som innenfor de tillatte grensene for lengde.

Her er eit samandrag med viktige punkt frå dei nye seksjonane:

---

### 17.7 NUMBER OF SPURS AND DEVICES PER SEGMENT
- **Spur**: Eit kort kabelsegment som går ut frå hovudkabelen og koplar til ein eining.
- **Lengde og utforming**:
  - Maksimal lengde kan variere frå 1 m til 120 m; vanlegvis held ein den under 10 m.
  - Høgrisikoområder bør unngå lengre spurlengder.
- **Tabell 17.2**: Viser sambandet mellom talet på einingar per spur og maksimal spurlengde, med variasjon for oppsett med éin til fire einingar per spur.
- **Tree Topology**: Kvar tilkopling frå ein junction box vert rekna som ein eigen spur. Figur 17.14 viser eit døme på eit tre-nettverk med ulik spurlengde.

### 17.8 POLARITY
- **Polarisert feltbussignal**: Alternativ spenning frå einingane vert lagt til DC-signal for å sikre at polariteten er riktig.
  - **Manchester-koding** sikrar polarisering gjennom å endre polariteten i kvar bit-periode.
- **Non-polariserte einingar**: Nokre feltbuss-einingar kan koblast til uavhengig av polaritet og kan automatisk detektere kva terminal som er positiv og kva som er negativ.
- **Blandede nettverk**: Dersom ein nettverksseksjon har både polariserte og non-polariserte einingar, må polariteten takast omsyn til for dei polariserte einingane.

For å beregne segmentstrømmen \( I_{\text{seg}} \) i eit Fieldbus-segment, nyttast følgjande formel:

$$
I_{\text{seg}} = \sum I_B + \max I_{\text{FDE}} + I_{\text{MOD}} + \sum I_{\text{startup}}
$$

Der:
- $\sum I_B $: Summen av grunnstraumen trekt av kvart feltapparat.
- $\max I_{\text{FDE}}$: Maksimal straum trekt av den største elektronikkstrømmen i segmentet.
- $I_{\text{MOD}}$: Modulasjonsstraum for segmentet, som er typisk 9 mA for Foundation Fieldbus og PROFIBUS-PA.
- $\sum I_{\text{startup}}$: Ekstra straum trekt ved oppstart av enkelte einingar, dersom aktuelt.

**Eksempel:**
Dersom du har spesifikke verdier for $I_B$, $I_{\text{FDE}}$, $I_{\text{MOD}}$, og $I_{\text{startup}}$ for feltapparata, kan desse pluggast inn for å finne total segmentstrøm.

### 17.10 Linking device
linke saman sammen Foundation Fieldbus H1 til høgare fart HSE og PROFIBUS-PA nettverk til PROFIBUS-DP. interne buffera tar seg av fatrtforskjellen.

### 17.11 DEVICE COUPLER
kobla samen spurskabel og deira trunks.
Det er ti typer device couplers; nonisolated og isolated.
straunmbegrensing på optill 60mA (eldre utstyr) 

TRUNKGUARD nkan begrense straumen ned til 2mA
