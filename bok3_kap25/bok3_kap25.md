### 25.1 Introduksjon til WirelessHART (WHART)
WirelessHART (ofte forkorta til WHART) er raskt i ferd med å bli ein ny standard for trådløs kommunikasjon i industrien, på same måte som ISA100.11a. Denne standarden har potensial til å revolusjonere prosesskontroll og automasjonsindustrien. Eksisterande trådlause teknologiar som Bluetooth, ZigBee og Wi-Fi har fleire svakheiter som gjer dei uegna i industrielle anlegg:

- **Bluetooth**: Er designa for personlege nettverk (PAN) med avgrensa rekkevidd på opptil 10 meter. Den støttar berre stjernetopologi, med ein master som kan ha maksimalt 7 slavar, noko som begrensar bruken i industrien.
- **ZigBee**: Støttar DSSS (Direct Sequence Spread Spectrum), men ytinga blir ofte sterkt påverka av støy i industrielle miljø.
- **Wi-Fi**: Er ikkje eigna for industrikommunikasjon på grunn av manglande støtte for kanalhopping, og høgt straumforbruk gjer det lite attraktivt i industrien.

**WHART** er den første opne trådlause kommunikasjonsstandarden spesifikt utvikla for prosessindustrien. Den vart offisielt lansert i september 2007 som ein del av HART-spesifikasjonen og inkludert i IEC 61158. I mars 2010 blei WHART godkjent av IEC som den internasjonale trådlause standarden IEC 62591 Ed. 1.0 for trådløs kommunikasjon og prosessautomatisering.

**WHART er designa for industrielle applikasjonar** som:
- Status- og diagnostikkovervåking av einingar,
- Kalibrering,
- Overvåking av kritisk data,
- Feilsøking,
- Igangsetting og tilsyn med prosesskontroll.

**WHART-teknologi**:
- Brukar **DSSS-kanalhopping** basert på IEEE 802.15.4, som gir robust og pålitelig kommunikasjon.
- **Mesh-nettverk**: WHART utnyttar mesh-nettverk med redundante datapath og gjenopprettingsmekanismer for å sikre kommunikasjonen.

**Wireless Mesh Networks (WMNs)**:
WMNs blir stadig meir populært takka vere avansert trådløsteknologi med multi-input multi-output-system og smarte antenner. Nokre hovudeigenskapar ved WMNs er:
- **Sjølvkonfigurerande og sjølvorganiserande**: Tilpassar seg sjølv for optimal drift.
- **Blanda bruk av kablede og trådlause einingar**: Nettverket kan inkludere både kablede og trådlause komponentar.
- **Routande noder**: Kvar nettverksenhet fungerer som ein ruter, noko som gir moglegheit for kommunikasjon gjennom multi-hopping.
- **Gateway-kommunikasjon**: Brukar ein gateway for kommunikasjon mellom einingar.

### 25.2 Viktige Eigenskapar ved WirelessHART
WirelessHART er ein svært pålitelig, sjølvreparerande og sjølvorganiserande mesh-nettverksprotokoll designa for prosessindustrien. Nokre sentrale eigenskapar:

- **Kompatibilitet**: WirelessHART er bakoverkompatibel med eksisterande HART-einingar, støttar HART-kommandoar og enhetsbeskrivingssproget (DLL).
- **Frekvensband**: Opererer i det lisensfrie 2.4 GHz ISM-bandet og bruker IEEE 802.15.4 med DSSS og kanalhopping for kvart enkelt datapakke.
- **TDMA**: Brukar time division multiple access (TDMA) for å koordinere kommunikasjon mellom ulike einingar, og reduserer sannsynet for kollisjonar.
- **Sikkerheit**: Tilbyr sentralstyrt kommunikasjon med AES-128 blokksifre for kryptering, med individuelle nøklar for tilkobling og datalink-nivå nettverksnøklar. Sikkerheit vert ivaretatt på både MAC- og nettverkslaget.
- **Hybrid nettverk**: Kombinerer både trådlause og kablede einingar og har moglegheit for å blokkere spesifikke kanalar for å unngå forstyrringar.
- **Effektiv straumbruk**: Ved å bruke TDMA kan nettverksstyraren førehandsschedule tidsslott, noko som reduserer straumforbruket ved å halde sendarar aktive berre i sine tildelte tidsslott.
- **Kanalhopping**: WirelessHART utnyttar 15 kanalar i 2.4 GHz ISM-spektrumet, med pseudo-random kanalbruk for å unngå forstyrringar. Kanalhopping gjer kommunikasjonen meir pålitelig.
- **Nettverksstyring**: Har ein sentral nettverksstyrar som handterer konfigurasjon, planlegging og ruting, og ein sikkerheitsstyrar for nøkkelhandsaming.

### 25.3 WirelessHART Nettverksarkitektur
Arkitekturen for eit WirelessHART-nettverk inkluderer WHART-felteiningar, HART-aktiverte felteiningar, handhaldne einingar, tilgangspunkt, gateway, adapterar, nettverksstyrar og sikkerheitsstyrar. Kommunikasjonen mellom trådlause felteiningar og det kablede systemet går via ein gateway. 

- **Tilkobling**: Både punkt-til-punkt og mesh-topologi blir brukt for å knyte saman WHART-felteiningane.
- **Redundant ruting**: Kvar trådløs eining bør ha minst to naboar som kan rute trafikken via grafbasert ruting, noko som gir pålitelig kommunikasjon.

### 25.4 Protokollstakk
WirelessHART-protokollstakken består av fem lag som samsvarer med OSI-modellen:
1. **Fysisk lag**
2. **Data link lag**
3. **Nettverkslag**
4. **Transportlag**
5. **Applikasjonslag**

I tillegg har WirelessHART ein sentral nettverksstyrar som administrerer ruting og kommunikasjonsplanlegging.

**Redundant ruting i WirelessHART**

Redundant ruting betyr at nettverket har fleire alternative kommunikasjonstigar eller "vegar" mellom einingar, noko som gir høgare påliteligheit i tilfelle av forstyrringar eller feil. I eit **WirelessHART-nettverk** utnyttar redundant ruting ein **mesh-topologi**, der kvar eining (node) kan sende data vidare til andre einingar gjennom fleire stiar. Dette konseptet gjer det mogleg for data å finne ein alternativ rute om ei bestemt tilkopling feilar eller vert blokkert av til dømes interferens eller mekaniske hinder.

### Fordelar med redundant ruting
1. **Økt påliteligheit**: Sidan data kan ruterast gjennom fleire stiar, reduserer dette risikoen for at ei enkel feil i ei tilkopling stoppar datatrafikken. Om ein sti er blokkert eller opplever feil, vil nettverket automatisk finne ein annan sti.

2. **Robustheit i industrielle miljø**: Industrimiljø kan vere utfordrande med tanke på forstyrringar frå maskiner, fysiske hinder, eller signalforstyrringar frå andre kommunikasjonssystem. Redundant ruting sikrar at data framleis kan nå målet sitt sjølv i krevjande miljøforhold.

3. **Sjølvhelbredande eigenskapar**: Eit mesh-nettverk som WirelessHART kan sjølvorganisere seg når ein ny node kjem inn, eller når ein node feilar. Nettverket vil automatisk oppdage endringar og tilpasse rutealternativa slik at kommunikasjonen held fram utan avbrot.

### Slik fungerer redundant ruting i WirelessHART
I WirelessHART må kvar trådlause eining ha minst to tilkopla naboar for å sikre at det finst alternative stiar for ruting. Nettverket brukar ein **grafbasert ruting** der ein **sentral nettverksstyrar** handterer planlegginga av dei ulike rutene. Denne styraren vurderer ulike faktorar som signalstyrke, avstand, og interferensnivå for å avgjere kva ruter som skal brukast, og oppdaterer desse kontinuerlig for å sikre optimal ytelse.

I praksis betyr dette at om ei eining mister forbindelsen til ein av naboane sine, kan den likevel sende data gjennom ein annan nabo. Dette aukar sjansane for at dataen når fram, sjølv om ei enkel linje skulle falle ut eller oppleve interferens.

### Eksempel på redundant ruting
Tenk deg eit nettverk der ein sensor er kopla til to nærliggande noder, Node A og Node B. Om sensorens vanlege rute er via Node A, men Node A opplever ein feil, kan sensoren automatisk bruke Node B som reserveveg til målet. Dette gjeld for kvar node i nettverket, og slik oppnår WirelessHART høg motstandsdyktigheit mot feilar.

### Samandrag
Redundant ruting i WirelessHART gir industrinettverk ei robust og sjølvhelbredande løysing som er tilpassa krevjande miljø, noko som gjer det ideelt for påliteleg prosesskontroll og overvåking i industrielle system.

### 25.4.1 Fysisk lag i WirelessHART

Det fysiske laget i WirelessHART er basert på **IEEE 802.15.4-2006**-standarden og opererer med ei datarate på **250 kbps** (62.5 kbaud) i frekvensområdet **2400–2483.5 MHz**.

**Hovudfunksjonar og spesifikasjonar**:
- **Kanalnummerering**: WirelessHART brukar kanalar nummerert frå 11 til 25, med eit mellomrom på 5 MHz mellom kvar kanal.
- **Modulasjon**: Brukar **Offset-Quadrature Phase Shift Keying (O-QPSK)** med **Direct Sequence Spread Spectrum (DSSS)** for å redusere interferens og auke signalkvaliteten.
- **Sendekraft**: Nominell sendekraft er 10 dBm, og denne kan justerast i discrete steg avhengig av behovet i nettverket.
- **Fysisk PDUs**: Det fysiske lagets protokoll-datainnhald (Physical Layer Protocol Data Unit, PDU) følgjer IEEE-standarden og har ein maksimal nyttelast på **127 byte**.
- **Kanalhopping**: Kanalhopping skjer for kvar pakke som blir sendt, noko som gir betre påliteligheit og redusert risiko for forstyrringar.
- **Clear Channel Assessment (CCA)**: Før data vert sendt, sjekkar CCA om kanalen er ledig, slik at WirelessHART unngår kollisjonar ved overføring.

**Struktur på det fysiske lagets PDU (PPDU)**:
- **Preamble**: 4 byte som markerer starten på dataoverføringa.
- **Delimiter**: 1 byte som markerer byrjinga av PPDU.
- **Lengdefelt**: 1 byte som angir lengda på PDU.
- **Nyttelast**: Variabel lengd, inneheld sjølve dataen som skal sendast.

Denne strukturen bidrar til effektiv kommunikasjon og auka påliteligheit i krevjande industrielle miljø.

### 25.4.2 Data Link Layer i WirelessHART

Data Link Layer (DLL) i WirelessHART har ansvar for pålitelig, feilfri og sikker kommunikasjon mellom einingar ved hjelp av tidsstyrte tidsluker (TDMA). Dette laget innfører fleire mekanismar for å sikre pålitelig kommunikasjon:

- **Feilfri kommunikasjon**: WirelessHART nyttar kanalhopping kombinert med **kanal-blokkering** for å unngå interferens og sikre stabil kommunikasjon.
- **TDMA-teknologi**: TDMA (Time Division Multiple Access) deler kommunikasjonen inn i presise tidsluker, der kommunikasjon mellom einingar skjer på ein trygg og deterministisk måte utan kollisjonar.
- **Sikkerheit**: For å oppnå sikker kommunikasjon er data link layer PDU (DLPDU) kryptert med **AES-128-bits** blokk-sifre.

**Struktur og funksjon av DLPDU**:
- DLPDU består av fleire felt, inkludert ein pakke-type som definerer innhaldet i nyttelasten.
- Ein serie av **100 tidsluker per sekund** dannar ei superramme, og WirelessHART-nettverket kan ha fleire slike superrammer. Ei superramme er aktiv om gongen, og kvar superramme kan ha ulik lengd når den er inaktiv.
- **Administrasjons-superramme**: Har 6400 tidsluker og blir brukt til tilknyttingsforespurnader, ad-hoc kommunikasjon, og spesialformål som overføring av store datablokkar.

**Kommunikasjonsprosessen i tidsluker**:
- I ein tidsluke sender kjelda ei DLPDU, etterfulgt av ein **ACK (bekreftelse)** frå destinasjonen om den har motteke DLPDU korrekt.
- Om kjelda ikkje mottek og validerer ACK, blir overføringa rekna som ugyldig, og DLPDU vil bli sendt på nytt i neste tilgjengelege tidsluke.
- Om ein link feilar gjentatte gonger, blir denne forkasta, og data blir sendt via ein alternativ rute basert på rutetabellen til kjelda.

**Tidssynkronisering og adressering**:
- Tidssynkronisering blir oppretthalde av gatewayen, som fungerer som hovudkjelda for tid i nettverket. Gatewayen synkroniserer med tilgangspunkta, og synkroniseringa skjer gjennom ei tre-basert klokkejustering.
- **Adresseoppsett**: WirelessHART nyttar IEEE 802.15.4-adressering med ein unik 64-bit IEEE-udvida adresse (EUI-64), ein kort 2-bytes unik adresse i nettverket, og ein 2-bytes nettverks-ID.

**Dataoverføring**:
- Dataoverføring kan vere periodisk eller sporadisk. Overføringar kan bruke ein tidsluke for den første sendinga, ein ekstra tidsluke for ein eventuell retry på ein annan kanal, og ein tredje tidsluke for ein andre retry på ein ny kanal om nødvendig.

Denne strukturen sikrar ein høg grad av påliteligheit, sikkerheit, og stabilitet i dataoverføringar, noko som gjer WirelessHART godt eigna for industrielle prosesskontrollapplikasjonar.

### 25.4.3 Nettverkslaget i WirelessHART

Nettverkslaget i WirelessHART har fleire viktige funksjonar for å sikre effektiv og sikker datakommunikasjon i nettverket. Det sørger for ruting av pakkar, innkapsling av meldingar frå transportlaget, ende-til-ende sikkerheit, blokkdatatransport, og kvittering av broadcasts.

- **Nettverksstyring**: Nettverksstyraren konfigurerer rutetabellane for kvar eining i nettverket og administrerer kommunikasjonen mellom dei ulike WirelessHART-einingane. Kvar eining må kunne videresende pakkar på vegne av andre for å støtte mesh-topologien.

**Ruteprotokollar i WirelessHART**:
1. **Graph Routing**: Nettverksstyraren opprettar ei samling av stiar (grafar) mellom nettverksnoder. Kvar eining lastar ned desse stigrafane og vedlikeheld ein graf-tabell med graf-IDar. Når ein pakke skal sendast, legg kjelde-eininga ein spesifikk graf-ID i nettverksoverskrifta, og kvar node bruker denne ID-en for å velje neste hop.

2. **Source Routing**: Kjelda inkluderer heile ruten i pakkens overskrift. Kvar node videresender så pakken til neste hop basert på informasjonen som allereie ligg i overskrifta. Denne prosessen held fram til pakken når destinasjonen.

3. **Proxy Routing**: Brukt når ei eining enno ikkje har blitt tilkobla nettverket.

**Struktur for Network Layer PDU (NPDU)**:
- **Kontrolloverskrift**: Inneheld adresseringsskjema og eventuell spesialruteinformasjon.
- **TTL (Time-to-Live)**: Ein teller som minkar for kvart hopp, som indikerer kor mange hopp som er igjen før meldinga når destinasjonen.
- **ASN Snippet**: Viser tid sidan pakken blei oppretta, som gir nettverksytelsesinformasjon.
- **Graf-ID**: Styrer pakkens rute mot destinasjonen.
- **Destinasjons- og kjeldeadresse**: Adresser til avsendaren og mottakaren.
- **Utvida ruteinformasjon**: Kan innehalde tillegg for å veilede pakken mot destinasjonen.

**Sikkerheitssublag**:
- Inneheld fleire felt for datakryptering og autentisering av NPDU.
- **Sikkerheitsfelt**: Angir typen sikkerheit som blir brukt, som til dømes join key, unicast session key eller broadcast session key.
- **Message Integrity Code (MIC)**: Sikrar dataens integritet ved å verifisere at dataen ikkje har blitt endra under transport.

Nettverkslaget i WirelessHART kombinerer desse ruting- og sikkerheitsmekanismane for å sikre ein robust, skalerbar og sikker kommunikasjon, noko som er avgjerande i industrielle prosesskontrollmiljø.

### 25.4.4 Transportlag i WirelessHART

Transportlaget i WirelessHART sikrar ende-til-ende levering av pakkar i kommunikasjonar som krev kvittering, slik som forespurnad-svar-trafikk.

**Hovudfunksjonar**:
- **Segmentering og samanstilling**: Data blir automatisk segmentert ved kjelda og sett saman igjen ved destinasjonen.
- **Kryptering**: Brukar enten **Join Key** eller ein av sesjonsnøklane for å kryptere transportlagets PDU (TPDU), noko som sikrar pålitelig kommunikasjon.
- **Identiske nøklar**: Einingar som kommuniserer må ha identiske join keys for å kunne dekryptere dataen.
- **Innkapsling**: Transportlaget innkapslar applikasjonslag-dataen og fungerer som eit konvergenspunkt mellom HART og WirelessHART.

### 25.4.5 Applikasjonslaget i WirelessHART

Applikasjonslaget i WirelessHART brukar standard HART-kommandobasert struktur og ligg på øvste nivå i protokollstakken.

**Typar kommandoar**:
1. **Universal Commands**: Støttast av alle WHART-einingar.
2. **Common Practice Commands**: Frivillige kommandoar som gjeld for mange ulike typar einingar.
3. **Device Family Commands**: Produsentspesifikke kommandoar, valfrie etter behov i felteiningar.
4. **Wireless Commands**: Støtte for WHART-spesifikke einingar, nødvendige for nettverksdrift.

**Funksjonar i applikasjonslaget**:
- Ansvarleg for å tolke meldingane, identifisere kommandonummer, utføre spesifikke kommandoar, og generere svar.
- Nettverksstyraren brukar applikasjonslagskommandoar for å konfigurere og administrere heile WHART-nettverket.

Applikasjonslaget er derfor kritisk for riktig drift og kommunikasjon i WirelessHART-nettverket, og støttar både generelle og spesifikke kommandoar for ulike einingar.

### 25.5.1 Nettverksstyrar i WirelessHART

Nettverksstyraren er hovudkontrollsenteret for WirelessHART-nettverket, men er ikkje ein fysisk eining – det er ein programvare som fungerer som mottakar og distributør av HART-kommandoar.

**Hovudfunksjonar**:
- **Organisering og overvåking**: Nettverksstyraren organiserer, overvåkar og opprettar strukturen i HART-nettverket.
- **Kommunikasjonsplanlegging**: Planlegg kommunikasjon mellom einingar og handterer både dedikerte og delte ressursar.
- **Rutingadministrasjon**: Ansvarleg for ruting i nettverket og for å sikre stabil kommunikasjon.
- **Nettverksstatus**: Rapporterer nettverkshelsa til vertsapplikasjonen og administrerer når einingar blir med i eller forlèt nettverket.

**Ytelsesmål**:
Ytinga til nettverksstyraren kan vurderast ut frå faktorar som:
- Maksimalt antal einingar som kan koplast til nettverket,
- Tida det tek å initialisere nettverket,
- Tida det tek for ei eining å bli med i nettverket,
- Samt total gjennomstrøyming i systemet.

### 25.5.2 Sikkerheitsstyrar i WirelessHART

Sikkerheitsstyraren arbeider tett saman med nettverksstyraren for å sikre at berre autoriserte einingar får tilgang til nettverket, og for å gi autorisasjons- og krypteringsnøklar for å sikre trygg kommunikasjon.

**Viktige eigenskapar**:
- **Enkel sikkerheitsstyrar per nettverk**: Det er berre éin aktiv sikkerheitsstyrar per WHART-nettverk.
- **Støtte for fleire nettverk**: Sikkerheitsstyraren kan tene fleire nettverk samtidig.
- **Klient-server-forhold**: Arbeidar i eit klient-server-forhold med nettverksstyraren.
- **Grensesnitt**: Grensesnittet mellom sikkerheitsstyraren og nettverksstyraren er ikkje definert i WHART-standarden, noko som gir fleksibilitet i implementeringa.

Sikkerheitsstyraren har hovudansvaret for å oppretthalde sikkerheita i nettverket gjennom nøkkelstyring og overvåking av nettverkssikkerheita.

### 25.5.3 Gateway i WirelessHART

Ein **gateway** i WirelessHART-nettverket fungerer som eit kommunikasjonsledd mellom vertsapplikasjonar og felteiningar. Den kan sjåast som ein trådløs versjon av marshaling-panel og koplingsboksar, og har både ein virtuell gateway-funksjon og eitt eller fleire tilgangspunkt. Det er éin gateway per nettverk.

**Hovudfunksjonar**:
- **Bufring og protokollkonvertering**: Ansvarleg for å lagre data midlertidig og for å konvertere mellom ulike protokollar, slik at vertsapplikasjonar kan kommunisere med felteiningane.
- **Klokkesynkronisering**: Gatewayen fungerer som tidskjelde for nettverket.

**Nødvendige eigenskapar**:
- **Nettverks- og sikkerheitsstyring**: Gatewayen må støtte funksjonar for å administrere nettverket og sikkerheita.
- **Fleire utgangsprotokollar**: Skal støtte fleire protokollar for integrasjon med ulike vertsapplikasjonar som DCS, PLC, og datahistorikk-system.
- **Fleire tilkoplingar**: Gatewayen opptrer som ein server og kan sende data til fleire sluttbrukarar samtidig.
- **Interoperabilitet**: Må vere kompatibel med ulike system.
- **Sikker overføring**: Støtte sikker protokolloverføring over Ethernet gjennom sterk kryptering.
- **Tilgangsnivå**: Bør ha ulike sikkerheitstilgangar for ulike brukarar.

### 25.5.4 Adapter i WirelessHART

Ein **adapter** gjer det mogleg å integrere eksisterande HART-felteiningar i eit WirelessHART-nettverk. Adapteren gir ein parallell kommunikasjonskanal til den eksisterande 4-20 mA strømsløyfa utan å forstyrre det vanlege signalet.

**Viktige eigenskapar**:
- **HART-merke**: Adapteren må ha ein HART-tag (identifikator).
- **Uforstyrra signal**: Må ikkje påverke det normale 4-20 mA signalet.

Adapteren gir altså ein trådløs kommunikasjonskanal til eksisterande HART-einingar og gjer dei tilgjengelege i WirelessHART-nettverket.

### 25.6 Latens og Jitter i WirelessHART

**Latens** er den tidsforsinkelsen det tek for måledata å nå kontrollaren, medan **jitter** refererer til variasjonar i denne forsinkelsen. Latens og jitter kan påverke prosesskontrollen dersom dei er for høge. 

WirelessHART er ein **tidsynkronisert kontrollprotokoll**, noko som ikkje er tilgjengeleg i mange andre protokollar. Denne tidsynkroniseringa gjer at målingar kan planleggjast presist, noko som nesten eliminerer både latens og jitter.

- **Hastigheit samanlikna med andre system**: WirelessHART har ei overføringsrate på **250 Kbits/s**, medan FOUNDATION Fieldbus opererer med 31.25 Kbits/s. Dette gir WirelessHART ein kommunikasjonstid på **4 µs per bit**, mot 32 µs per bit for FOUNDATION Fieldbus.
- **Tidsluke og meldingsoverføring**: Ein typisk tidsluke på 10 ms er nok til å sende og motta ei kvittering for ei melding. Ein WHART-melding på 128 byte krev berre 4 ms for å nå destinasjonen, noko som reduserer latens til eit minimum.
- **Optimert nettverk**: Latens kan reduserast ytterlegare ved hjelp av effektiv tidsplanlegging, kanal-blokkering, kanalhopping, og velplasserte tilgangspunkt. Dette sikrar at latens alltid er mykje mindre enn respons-tidene til dei fleste fysiske prosessar, slik at det ikkje påverkar praktisk prosesskontroll.

### 25.7 Sameksistens-teknikkar

WirelessHART opererer i det lisensfrie ISM-bandet, som også blir brukt av andre trådlause system som Bluetooth, Wi-Fi og ZigBee. For å unngå forstyrringar frå slike system og sikre pålitelig kommunikasjon mellom trådlause felteiningar og kablede system, har WirelessHART implementert ulike **sameksistens-teknikkar**.

### 25.7.1 Kanalhopping i WirelessHART

WirelessHART-nettverk utnyttar kanalhopping som ein metode for å redusere forstyrringar frå andre trådlause system, som Bluetooth, Wi-Fi og ZigBee.

- **Kanalutval**: WirelessHART bruker 15 kanalar i ISM-bandet og ein **pseudo-random kanalhoppingssekvens** for å sikre at ein bestemt kanal ikkje blir brukt over lang tid, noko som reduserer risikoen for vedvarande forstyrringar.
- **Slotted Hopping**: WirelessHART bruker slotted hopping, der kanalbruken varierer etter mønster og er avhengig av faktorar som kanaloffset, ASN (Absolute Slot Number) og talet på aktive kanalar. Dette bidrar til å fordele signalbruken og minimere RF-forstyrringar.

### 25.7.2 Direct Sequence Spread Spectrum (DSSS)

WirelessHART bruker DSSS for å forbetre signal-til-støy-forholdet og auke mottakarens sensitivitet.

- **Spreiing av signalet**: DSSS sprer signalet over heile frekvensbanda tildelt til WirelessHART, noko som gjer det lettare for nettverket å oppdage signalet midt i støy.
- **Kodebasert dekoding**: WHART-einingar kan dekode den kodede informasjonen i signalet, medan andre system berre oppfattar det som kvit støy. Dette sikrar at berre WHART-einingar kan tolke signalet riktig, sjølv når fleire radiosignal overlappar kvarandre. 

Desse teknikkane gjer WirelessHART meir motstandsdyktig mot interferens og sikrar pålitelig datakommunikasjon i industrielle miljø.

### 25.7.3 Lavstyrkesending i WirelessHART

WirelessHART-enheter bruker lågeffektsending samanlikna med andre trådlause system som RFID-lesarar og Bluetooth. Dette reduserer sjansen for interferens frå slike system. 

- **IEEE 802.15.4-standarden**: WHART nyttar denne standarden for lågeffektsending, som kan rekke opptil 200 meter med forsterkarar. For kortare avstandar brukar enkle lågstrømsforsterkarar som sender signal frå ein enhet til den neste, og minimerer slik RF-forureining i spekteret.

### 25.7.4 Blacklisting og Kanalevaluering

WirelessHART kan bli konfigurert til å unngå ofte brukte kanalar, noko som reduserer sannsynet for interferens. Før sending sjekkar WHART-eininga om kanalen er fri. Om det blir oppdaga annan aktivitet, ventar eininga og prøver igjen på eit anna tidspunkt og ein annan kanal.

### 25.7.5 Spatial Diversity

Spatial diversity handlar om strategisk plassering av trådlause einingar for å minimere sameksistensproblemer med nærliggande trådlause einingar.

- **Antenne-diversitet**: Mottakaren vel det beste signalet frå fleire antenner, noko som reduserer interferens.
- **Retningsantenner**: Sender signal i ein spesifikk retning for å redusere RF-forstyrringar.

### 25.8 Tidsynkronisert Mesh-protokoll (TSMP) i WirelessHART

Tidsynkronisering er essensielt i WirelessHART for å sikre presis kommunikasjon. Protokollen baserer seg på **TDMA (Time Division Multiple Access)** og kanalhopping for å gi både effektiv kommunikasjon og auka sikkerheit.

- **Kommunikasjonsplanlegging**: Strukturen for kommunikasjon skjer gjennom grafbaserte ruter som definerer stiar mellom einingar (hops) i nettverket. Alle einingar følgjer ein **ASN (Absolute Slot Number)**, som gir dei riktig timing for tidsluka dei skal kommunisere i. Gatewayen fungerer som hovudklokka for å synkronisere heile nettverket.
- **Tidsstempel**: Kvar felt-enhet får eit tidsstempel med nøyaktigheit på 1 ms over heile nettverket, noko som gir svært presis tidsstyring som ikkje er tilgjengeleg i mange andre protokollar.

### 25.9 Sikkerheit i WirelessHART

WirelessHART er ein IEC-godkjent standard som gir trygg og pålitelig meldingsoverføring i prosesskontroll og automasjonsmiljø. Nettverket er bygd opp som eit mesh-nettverk der kvar felteining kan ha éin eller fleire sensorar som samlar inn prosessdata og sender desse vidare til andre felt-einingar.

- **Sikker overføring av informasjon**: Ruteinformasjon, sikkerheitsnøklar, og tidsinformasjon blir trygt overført mellom einingar. Data beveger seg gjennom WirelessHART-nettverket som kommandoar, og protokollen sikrar at desse kommandoane er **konfidensielle, integrerte, og autentiske**.

### 25.9.1 OSI-lagsbasert sikkerheit i HART og WirelessHART

WirelessHART bruker ulike sikkerheitstiltak på OSI-modellen sine lag:
- **Nettverkslaget og nedover**: I WirelessHART er data kryptert og sikra frå nettverkslaget og nedover.
- **Applikasjons- og transportlag**: Desse laga får ikkje krypteringsdekning, i motsetning til dei lågare laga, som sørger for sikkerheitsfunksjonane som WirelessHART tilbyr på den trådlause delen av nettverket.

### 25.9.2 Ende-til-ende-sikkerheit i WirelessHART

Ende-til-ende-sikkerheit sikrar at data som reiser frå ein kjelde- til ein destinasjonseining er verna gjennom heile overføringa. Denne sikkerheita blir håndtert av nettverkslaget.

- **Sesjonsoppretting**: Ei felteining kan ikkje opprette ein direkte sesjon med ei anna felteining. I staden må data reise via ein gateway. Ein sesjon kan opprettast mellom ei felteining og ein gateway eller mellom ei felteining og nettverksstyraren.
- **Kryptering og dekryptering**: Data frå kjeldeeininga blir først kryptert med ein unik symmetrisk sesjonsnøkkel, sendt til gatewayen, der gatewayen dekrypterer dataen og krypterer det igjen med sesjonsnøkkelen til destinasjonseininga før det sendast vidare.

### 25.9.3 Network Layer PDU (NPDU) i WirelessHART

NPDU på nettverkslaget inneheld fleire felt som støttar sikkerheita, inkludert sikkerheitskontroll, ein teller og ein **Message Integrity Code (MIC)**.

- **Kryptering**: NPDU-nyttelasta (transportlagets PDU) blir kryptert ved hjelp av AES med ein 128-bits nøkkel.
- **Konfidensialitet, integritet og autentisering**: Nettverkslaget gir ende-til-ende konfidensialitet og sikrar dataintegritet og autentisering.

#### 25.9.3.1 Security Control Byte (SCB)
- SCB definerer typen sikkerheit som vert brukt. Den øvre delen av byte-verdien er reservert for framtidige behov, medan den nedre delen spesifiserer sikkerheitstypen (som sesjonsnøkkel, join-nøkkel, eller handhaldne nøkkel).

#### 25.9.3.2 Message Integrity Code (MIC)
- **MIC** sikrar autentisitet og integritet for datakjelda. MIC bereknast frå fire byte-strengar: NPDU header, NPDU nyttelast, AES-nøkkel, og ein **nonce**. 
- **Nonce**: Ein 13-byte verdi som forsvarar mot reply-attacks. Første byte er enten sett til einar (for join-respons meldingar) eller nullar, dei neste 4 bytene utgjer ein teller, og dei siste 8 bytene inneheld kjeldeadressa.

Denne strukturen gir ein sikker og robust dataintegritet for overføringar i WirelessHART-nettverket, og sikrar at data ikkje vert endra eller manipulert undervegs.