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