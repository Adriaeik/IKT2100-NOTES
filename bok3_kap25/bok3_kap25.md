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

### 25.10 Sikkerheitstruslar i WirelessHART

WirelessHART er utsett for fleire potensielle sikkerheitstruslar, både i det trådlause og kablede nettverket, ettersom det deler ISM-banda med andre trådlause system som Wi-Fi, Bluetooth og ZigBee. Dette kan føre til informasjonssikkerheitsproblem som lekkasje av data, trafikkavbrot, eller manipulering av informasjon.

#### 25.10.1 Interferens
Interferens oppstår når eit uønska signal, som kan ha same frekvens og modulasjon som WirelessHART-signalet, forstyrrar kommunikasjonen.

- **Potensielle interferenskjelder**: Andre system i nærleiken, som Bluetooth, ZigBee og Wi-Fi, kan skape interferens.
- **Tiltak**: WirelessHART bruker teknikkar som **Frequency Hopping Spread Spectrum (FHSS)**, tidsdiversitet og stiadiversitet for å redusere interferens.

#### 25.10.2 Jamming
Jamming inneber ein bevisst forstyrrelse av nettverkssignalet gjennom eit støyende signal med same frekvens og modulasjon som WirelessHART.

- **Effektar av jamming**: Kan vere øydeleggjande for nettverksprestanda, avhengig av angriparen si evne til å injisere forstyrrande signal.
- **Tiltak**: WirelessHART nyttar FHSS og kanalblokkering for å blokkere støyande kanalar, men manuell blokkering reduserer talet på tilgjengelege kanalar for WirelessHART-signal.

#### 25.10.3 Sybil-angrep
Eit Sybil-angrep skjer når ein angripar introduserer fleire identitetar (noder eller programvare) i systemet for å svekke nettverkets funksjonalitet.

- **Tiltak**: Kvar eining i WirelessHART har ein global unik ID, som kombinerer eningstype og enings-ID. Gatewayen vedlikeheld desse unike ID-ane, medan nettverksstyraren tildeler individuelle kallenamn til kvar eining. Desse unike ID-ane og kallenamna sikrar at einingane kan opprette trygge sesjonar med gatewayen og nettverksstyraren, noko som reduserer risikoen for Sybil-angrep. 

Desse tiltaka gir WirelessHART eit robust sikkerheitsnivå for å handtere interferens og potensielle angrep i komplekse industrielle miljø.

### 25.10.4 Kollisjon

Kollisjon skjer når fleire einingar prøver å få tilgang til same kanal samtidig. Dette kan vere tilsikta eller utilsikta, og WirelessHART reduserer risikoen for slike kollisjonar gjennom **kanalhopping** og **tidsdiversitet**.

- **Oppdaging**: Kollisjonar blir oppdaga ved hjelp av **CRC (Cyclic Redundancy Check)**.
- **Tiltak**: Fysisk lag og datalinklag samarbeider for å koordinere tilgang, noko som reduserer kollisjonar.

### 25.10.5 Manipulering

Dersom ein inntrengar har tilgang til nettverksnøkkelen og ein ukryptert DLPDU, kan vedkomande manipulere meldinga og lage ein ny **Message Integrity Code (MIC)** for å få meldinga til å sjå autentisk ut. 

- **Konsekvensar**: Manipulerte pakkar kan omdirigerast til feil destinasjon eller sendast tilbake til kjelda, noko som kan svekke nettverksytelsen.

### 25.10.6 Spoofing

Ved spoofing prøver ein angripar å etterlikne ei ny eining som ønskjer å bli med i nettverket.

- **Metode**: Ein angripar sender ei falsk annonsemelding som om det var frå ei ny eining. Når einingane prøver å bli med, kan angriparen avvise deira tilkobling, eller forhindre dei frå å delta i nettverket.
- **Konsekvensar**: Om angriparen har tilgang til nettverksnøkkelen, kan dette føre til meir skadelege angrep, inkludert blokkering av nettverkstrafikk.

### 25.10.7 Uttømming (Exhaustion)

Eit uttømmingsangrep skjer når ein angripar bruker ei eining til å sende ei rekke meldingar til andre einingar i nettverket, noko som belastar ressursane kraftig.

- **Metode**: Ved å ha tilgang til nettverksparametre og vere i stand til å berekne MIC for DLPDU, kan angriparen floode nettverket med falske join-førespurnadar.
- **Konsekvensar**: Desse førespurnadane blir til slutt avvist av nettverksstyraren, men dei fører til ressursforbruk og kan føre til alvorleg overbelastning av nettverket.

Desse truslane krev ulike sikkerheitstiltak for å oppretthalde robust og stabil nettverkskommunikasjon i WirelessHART-miljø.

### 25.10.8 Denial of Service (DoS)

DoS-angrep kan lamme nettverket ved å overvelde det med falske førespurnader eller forstyrringar. Metodar for DoS i WirelessHART inkluderer:
- **Falske tidsannonseringar**: Forstyrrar nettverkssynkronisering.
- **Flom med falske join-forespurningar**: Overbelastar nettverksstyraren.
- **Jamming av signalet**: Hindrar kommunikasjon.
- **Erstatting av ukryptert DLPDU og rekalkulering av CRC**: Forstyrrar dataintegriteten.
  
**Tiltak**: MIC-verifisering ved hjelp av AES i CCM-modus kan identifisere manipulerte pakkar, men denne verifiseringa krev tid og kan føre til avvising av ugyldige pakkar.

### 25.10.9 Trafikkanalyse

I trafikkanalyse utnyttar ein angripar at NPDU- og DLPDU-headerfelt er ukrypterte. Dette inkluderer:
- **NPDU-felt**: Kilde- og destinasjonsadresse, sikkerheitsbyte, ANS-utdrag og nonce-teller.
- **DLPDU-felt**: Adressespesifikator og DLPDU-spesifikator.
  
Ved å analysere desse dataene kan ein angripar identifisere bruksratar, perioder med høg aktivitet, og join-forespurningar, noko som kan utnyttast til meir målretta angrep.

### 25.10.10 Wormhole-angrep

Eit wormhole-angrep oppstår når ein angripar etablerer ein tunnel mellom to gyldige einingar, ved å koble dei via ein sterkare kablet eller trådløs link.

- **Utføring**: Ein HART-eining tilkopla WHART via adapterar kan bruke vedlikehaldsportar til å etablere tunnelen.
- **Sårbarhet**: Graph Routing kan vere utsett for wormhole-angrep sidan det nyttar redundante stiar.
- **Forsvar**: Source Routing, som følgjer ei rute frå eining til eining, kan motstå wormhole-angrep, men er mindre pålitelig da feilar i mellomliggende lenker kan føre til at pakkar ikkje når destinasjonen.

**Pakkelekkasje** er ein teknikk som blir brukt for å avverge wormhole-angrep.

### 25.10.11 Selektiv videresending-angrep

Selektiv videresending skjer når ei kompromittert node (ofte frå eit Sybil-angrep) bevisst slepp nokre pakkar i staden for å sende alle vidare. 

- **Black Hole**: Når ingen pakkar blir sendt vidare, skapar det ein "black hole".
- **Selektiv Dropping**: Angriparen slepp berre utvalde pakkar, slik at det ser ut som ein normal drift og ikkje triggar gjenopprettingsmekanismar.

### 25.10.12 Desynkronisering

WirelessHART-nettverket er avhengig av presis tidssynkronisering med ein tidsintervall på 10 ms. Dette blir administrert av **MAC-sub-laget**. Når ein node mottar ei ACK-melding, justerer den klokka si etter denne. 

- **Angrepsmetode**: Om ein kompromittert sender manipulerer tidsdataen, kan det føre til tidsskeivning mellom nodar, noko som resulterer i bortkasta ressursar når nodane prøver å synkronisere seg.

### 25.11 Redundans i WirelessHART

Redundans er viktig i prosesskontrollsystem for å sikre kontinuerleg datatilgang, spesielt der data er kritisk for operasjonen. WirelessHART har redundans på følgande nivå:

- **Trådlause sensornettverk (WSN)**
- **Tilgangspunkt i nettverket**
- **Gateway, nettverksstyrar og sikkerheitsstyrar**

#### 25.11.1 Redundans i Trådlause Sensornettverk (WSN)

Redundans i WSN kan oppnåast på fleire måtar:

- **Romleg diversitet**: Bruker fleire stiar mellom nettverkskomponentar.
- **Frekvensdiversitet**: Utnyttar kanalhopping for å unngå forstyrringar.
- **Tidsdiversitet**: Tilgang til nettverket på ulike tidspunkt for å redusere kollisjonar.

**Enhetsredundans** kan opprettast ved å sikre fleire ruter til kvar eining for å garantere dataoverføring til gatewayen sjølv ved feil i hovudruten.

### 25.11.2 Redundans ved Nettverkstilgangspunkt

Fleire tilgangspunkt gir auka sti-diversitet og dermed meir redundans i systemet. Eit tilgangspunkt fungerer som eit kommunikasjonsknutepunkt mellom ei eining og gatewayen, og gir både høgare båndbredde og alternative ruter for å sikre pålitelig kommunikasjon.

- **Funksjon**: Tilgangspunktet gir tilgang til fleire kommunikasjonsstiar mot gatewayen og nettverksstyraren.
- **Kostnad og bandbredde**: Teoretisk kan eit nettverk ha eit ubegrensa antal tilgangspunkt, men ein må balansere mellom kostnad, bandbredde og behovet for redundans.

### 25.11.3 Redundans i Gateway, Nettverksstyrar og Sikkerheitsstyrar

Redundans kan implementerast ved å kombinere gateway, nettverksstyrar og sikkerheitsstyrar i éin fysisk gateway-enhet og replikere denne oppsettet fleire stader i nettverket. 

- **Primær og sekundær gateway**: Éin gateway fungerer som primær, medan den andre overtek ved feil. Dei to gatewayane er synkroniserte via ein redundansstyrar som held systemet oppdatert.

### 25.12 Sikkerheitsnøklar i WirelessHART

WirelessHART har ein nøkkelhandteringsstrategi som ikkje er fullt detaljert for både trådlause og kablede delar av nettverket. Standardiserte nøklar inkluderer:

- **AES-128 kryptering** med symmetriske nøklar.
- **Fleirnøkkelarkitektur** som støttar individuelle join-nøklar for kvar eining.
- **Autentisering av data link PDUs** med nettverksnøkkel.
- **Ende-til-ende autentisering** med sesjonsnøkkel.

### Nøkkeltypar i WirelessHART
1. **Join Key**: Unik per eining, må distribuerast før nettverksinitiering.
2. **Session Key**: Brukt for ende-til-ende kommunikasjon.
3. **Network Key**: For autentisering på data-link-nivå.
4. **Handheld Key**: For handhaldne einingar.
5. **Well-known Key**: For spesifikke føremål.

WirelessHART-spesifikasjonen sikrar at nettverksstyraren sender nøklar via gatewayen, medan sikkerheitsstyraren genererer og lagrar nøklane.

### 25.12.1 Join Key

Kvar eining i WirelessHART-nettverket har ein **individuell join key** som fungerer som eit passord for å få tilgang til nettverket. 

- **Distribusjon**: Sikkerheitsadministratoren distribuerer denne nøkkelen manuelt til kvar eining, ofte ved hjelp av ein handhalden eining gjennom einingas vedlikehaldsport.
- **Isolering ved nøkkelendring**: Ved første oppsett eller endring av join key må eininga vere isolert frå nettverket.
- **Funksjonar**: Etter at eininga har join key, kan nettverksstyraren autentisere og gi tilgang til nettverket, og skrive inn eininga si **network key** og **session key** ved vellykka autentisering.

### 25.12.2 Session Key

Kvar eining får **fire sesjonsnøklar** etter vellykka tilkopling eller oppstart:

1. **Unicast gateway session key** mellom gateway og eininga.
2. **Unicast network manager session key** mellom nettverksstyraren og eininga.
3. **Broadcast gateway session key** frå gateway til alle einingar.
4. **Broadcast network manager session key** frå nettverksstyraren til alle einingar.

Einingar kommuniserer ikkje direkte med kvarandre, men via gatewayen. Eininga sender meldingar til gatewayen ved bruk av sin unicast gateway session key, og gatewayen vidareformidlar meldinga til destinasjonseininga med sin unicast gateway session key.

### 25.12.3 Network Key

Det finst berre éin **network key** som blir delt mellom alle einingar for å sikre datalinklaget mot angrep utanfrå.

- **Autentisering**: Nettverksnøkkelen blir brukt til å rekne ut MIC som beskyttar og autentiserer DLPDU (Data Link Protocol Data Unit) mellom einingane.

### 25.12.4 Handheld Key

Handheld key blir distribuert av nettverksstyraren ved hjelp av join key når den blir etterspurt av ein handhalden eining.

- **Peer-to-peer-forbindelse**: Brukt for vedlikehald av einingar gjennom vedlikehaldsporten, utan å involvere gatewayen.
- **Sikrar NPDU**: Handheld key beskyttar data i NPDU (Network Protocol Data Unit) under vedlikehald.

### 25.12.5 Well-known Key

**Well-known key** blir brukt ved tilkopling og sikrar join-request/response-meldingar når eininga enno ikkje har fått nettverksnøkkelen.

- **MIC-beregning**: Well-known key bidreg til å berekne MIC for join-prosessen og ved sending av join-annonseringar, noko som sikrar den første kommunikasjonen mellom eininga og nettverket før full autentisering.

### 25.13 Nøkkelhåndtering i WirelessHART

Effektiv og automatisk nøkkelhåndtering er avgjørande for sikkerheita i WirelessHART-nettverk. Nettverksstyraren fungerer som ein nøkkeldistribusjonssentral, medan sikkerheitsstyraren handterer nøkkelhåndteringa. Hovudprosessane i nøkkelhåndtering omfattar generering, lagring, distribusjon, fornying, tilbakekalling og verifisering av nøklar.

- **Symmetriske nøklar**: WirelessHART bruker berre symmetrisk kryptering, noko som betyr at same nøkkel blir brukt for både kryptering og dekryptering.

### 25.13.1 Nøkkelgenerering
Sikkerheitsstyraren har ansvar for nøkkelgenerering, men WirelessHART-standarden spesifiserer ikkje eksplisitt korleis nøklane skal bli generert, berre at dei må oppfylle sikkerheitskrava for nettverket.

### 25.13.2 Nøkkellagring
Sikker lagring av nøklar er kritisk for nettverkets tryggleik, sjølv om WirelessHART ikkje gir spesifikke retningslinjer for nøkkellagring.

### 25.13.3 Nøkkeldistribusjon
Distribusjon av nøklar til einingane er nettverksstyrarens ansvar, men korleis nettverksstyraren hentar nøklar frå sikkerheitsstyraren er ikkje fullt spesifisert i standarden.

- **Join Key**: Standarden gjev informasjon om korleis join key blir gitt til eininga og deretter delt med nettverksstyraren.

### 25.13.4 Nøkkelfornying
Alle nøklar bør fornyast jamleg for å hindre brute-force-angrep.

- **Fornyingsmekanismar**: Nettverksnøkkelen kan endrast gjennom ein trygg broadcastsending, medan andre nøklar kan fornyast gjennom unicast-sesjonar mellom nettverksstyraren og einingane.
- **Sikkerheitsavhengigheit**: Join key og sesjonsnøklar er avhengige av kvarandre, og svekka sikkerheit i éin nøkkel kan påverke den andre.

### 25.13.5 Nøkkeltildeling og tilbakekalling
Nøkkeltilbakekalling betyr at ein nøkkel blir deaktivert når tilhøyrande eining forlet nettverket.

- **Permanent fråkopling**: Om ei eining forlet nettverket permanent, bør nettverksnøkkelen også endrast for å oppretthalde tryggleiken.
- **Sjølvdestruksjon**: Ved tap av einingsautentisitet, som ved at ein angripar får tilgang, bør eininga sjølvdestruere eller automatisk slette nøkkelen frå nettverket.

### 25.13.6 Nøkkelverifisering
Nøkkelverifisering (key vetting) inneber autentisering av nøkkelen, men WirelessHART har ingen spesifikke kommandoar for nøkkelverifisering.

### 25.14 WHART Nettverksdanning

Oppretting av eit WHART-nettverk følgjer fleire steg før det er klart for industriell bruk:

1. **Innstilling av nettverks-ID og passord**: Nettverksstyraren set opp nettverks-ID og passord, etterfølgt av prosessen med å gi tilgang og sikre sesjonar.
2. **Initialoppsett**: På verkstadgolvet blir passord og nettverks-ID lagt inn i eininga. Eininga blir konfigurert etter behov, inkludert oppdateringsfrekvens.
3. **Join-prosess**: Nettverksstyraren sender ein annonse til eininga, som svarer med ein join-forespurnad.
4. **Autorisasjon**: Nettverksstyraren godkjenner eininga og gir nødvendige nøklar, tidsplanar og rutingsdata, slik at eininga kan begynne å publisere data.

### 25.15 Sammenligning av HART og WirelessHART (WHART)

| Funksjon | HART | WHART |
|----------|------|-------|
| Sikkerheit | Ikkje ein sikker protokoll | Ein sikker protokoll |
| Protokollversjon | HART 6 og nedover | HART 7 og oppover |
| OSI-modell | Løyst kopla | Sterkt kopla |
| Transportlag og høgare | Identisk med WHART | Identisk med HART |
| Applikasjonslag | Kommandonummer, byte-telling, og data | Kommandonummer, byte-telling, og data |
| Nettverkslag | Spesifiserer ikkje nettverks- eller høgare lag | Brukar nettverkslag for trådløs ruting og sikkerheit |
| Data Link-lag | Basert på token-passing | Basert på TDMA |
| Fysisk lag | 4-20 mA analog kabling | IEEE 802.15.4-2006 |

### 25.16 Integrasjon av HART og WHART

HART har vore i bruk i omtrent 25 år, medan WHART er om lag eit tiår gamal. Integrasjon av desse teknologiane er viktig sidan WHART er bakoverkompatibel med HART. Dette betyr at eksisterande HART-nettverk kan utvidast eller oppgraderast med WHART-komponentar.

**Integrasjonseigenskapar**:
- **Bakoverkompatibilitet**: WHART-einingar er kompatible med eksisterande HART-einingar, noko som gjer overgang lettare.
- **Gateway for protokollkonvertering**: Integrasjonen skjer gjennom ein gateway som omformar protokollane for begge teknologiane, slik at WHART og HART kan operere i same system.

### Oppsummering av Kapittel 25: WirelessHART i Industriell Kommunikasjon

Kapittel 25 gir ein grundig gjennomgang av **WirelessHART (WHART)** som ein viktig trådløs standard for industriell prosesskontroll og automatisering. Her blir hovudfunksjonar, sikkerheitstiltak, og nettverksdanning i WHART-nettverk presentert, saman med samanlikningar med den eldre HART-protokollen.

#### Hovudpunkt:
1. **WirelessHART Arkitektur og Protokoll**: WHART byggjer på IEEE 802.15.4-2006 med støtte for mesh-nettverk, kanalhopping, og TDMA for stabil og sikker kommunikasjon. Protokollen er utvikla for å møte krevjande industriell bruk og sikre robust datalevering utan interferens eller datatap.

2. **Nettverksdanning**: Nettverksstyraren administrerer prosessen med å sette opp nettverks-ID, distribuere join-nøklar og konfigurere einingane. Når eininga blir med i nettverket, blir den utstyrt med unike sesjonsnøklar og rutingsinformasjon som legg til rette for sikker og effektiv kommunikasjon.

3. **Sikkerheitsmekanismar**: Kapittelet legg stor vekt på sikkerheit gjennom bruk av AES-128 symmetrisk kryptering. Nøkkeltypar som join key, session key, network key og handheld key blir brukt for å autentisere einingane, sikre ende-til-ende kommunikasjon, og beskytte data mot manipulasjon og andre sikkerheitstruslar.

4. **Sikkerheitstruslar og Tiltak**: WHART står overfor utfordringar som interferens, jamming, spoofing og desynkronisering. Protokollen bruker teknikkar som kanalhopping, frekvensdiversitet, og redundans for å motverke desse truslane og sikre kontinuerleg og stabil drift.

5. **Redundans i Nettverket**: For å auke systempålitelegheit bruker WHART redundans på fleire nivå, inkludert tilgangspunkt, gateway, og nettverksstyrar, samt fleire ruter mellom einingar i det trådlause sensornettverket.

6. **Samanlikning og Integrasjon med HART**: WHART byggjer på den eldre HART-protokollen og er bakoverkompatibel, noko som legg til rette for enkel integrasjon i eksisterande industrielle system ved hjelp av ein gateway som omformar protokollane. WHART er meir sikker og fleksibel enn HART, og støttar fleire moderne funksjonar som ende-til-ende sikkerheit og avansert ruteadministrasjon.

### Konklusjon
WirelessHART representerer ein stor utvikling innan trådløs kommunikasjon for industriell automatisering, og kapittel 25 forklarer korleis WHART sin struktur, sikkerheit og fleksibilitet gjer den til ein foretrukken standard for moderne prosesskontroll. Kapittelet viser også til korleis integrasjon med eldre HART-nettverk kan utførast for å modernisere industrielle system utan å gå på kompromiss med påliteligheit og sikkerheit.

### WirelessHART Kapittel 25: Q&A

#### 1. **Kva er WirelessHART (WHART), og kvifor er det viktig i industriell kommunikasjon?**
   - WirelessHART er ein trådløs standard for industriell automasjon og prosesskontroll. Den sikrar pålitelig og sikker kommunikasjon gjennom mesh-nettverk, kanalhopping, og tidssynkronisering (TDMA), som reduserer interferens og støttar robust datalevering.

#### 2. **Kva rolle speler nettverksstyraren i WHART-nettverket?**
   - Nettverksstyraren administrerer oppsett av nettverket, som å distribuere join-nøklar, opprette tidsplanar for kommunikasjon, og konfigurere einingane slik at dei kan kommunisere effektivt og sikkert.

#### 3. **Kva sikkerheitstiltak brukar WHART for å beskytte data?**
   - WHART bruker AES-128 kryptering, kanalhopping, og fleire nøkkeltypar som join key, session key og network key for å beskytte data mot avlytting, manipulering og andre truslar.

#### 4. **Korleis bidreg kanalhopping til WHART sin sikkerheit?**
   - Kanalhopping gjer at WHART automatisk byter frekvens mellom fleire kanalar, noko som reduserer risikoen for interferens frå andre trådlause nettverk og gjer kommunikasjonen meir pålitelig.

#### 5. **Kva er forskjellen mellom HART og WHART?**
   - HART er ein eldre, kablet protokoll utan innebygd sikkerheit, medan WHART er ein sikker trådløs versjon basert på HART 7-standarden med støtte for trådløs ruting, ende-til-ende sikkerheit, og TDMA på data-link-nivået.

#### 6. **Korleis fungerer nøkkelhandtering i WHART?**
   - Sikkerheitsstyraren genererer og lagrar nøklar, medan nettverksstyraren distribuerer dei til einingane. Nøkkelhandteringa omfattar join keys for tilkopling, session keys for individuell kommunikasjon, og network key for autentisering på data-link-laget.

#### 7. **Kva sikkerheitstruslar kan påverke WHART-nettverk, og korleis blir desse handtert?**
   - WHART står overfor truslar som interferens, jamming, spoofing, og Sybil-angrep. For å beskytte nettverket bruker WHART teknikkar som kanalhopping, redundans, MIC (Message Integrity Code) for dataintegritet, og sikre tidsplanar.

#### 8. **Kva er føremonane med redundans i WHART?**
   - Redundans aukar nettverkspålitelegheit ved å sikre alternative ruter for dataoverføring, inkludert fleire tilgangspunkt, gatewayar, og nettverksstyrarar som kan overta ved feil.

#### 9. **Korleis blir HART og WHART integrert i eksisterande industrielle system?**
   - Integrasjon skjer ved hjelp av ein gateway som fungerer som protokollomformar. WHART er bakoverkompatibel med HART, noko som gjer det lettare å modernisere industrielle anlegg som alt nyttar HART.

#### 10. **Kvifor er AES-128 ein viktig del av WHART si sikkerheit?**
   - AES-128 gir høg grad av sikkerheit gjennom sterk symmetrisk kryptering, som sikrar at berre autoriserte einingar kan lese og sende data. AES-128 sikrar også integriteten av meldingar gjennom MIC, noko som beskyttar mot manipulering og replay-angrep.