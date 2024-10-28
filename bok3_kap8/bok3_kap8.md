**Profibus (Process Field Bus)** er ein vanleg feltbussstandard i industrielle nettverk og er utvikla for å sikre påliteleg kommunikasjon mellom sensorar, aktuatorar og kontrollsystem som PLC-er (Programmable Logic Controllers). Profibus omfattar tre hovudtypar: Profibus DP, Profibus PA og Profibus FMS, som er tilpassa ulike kommunikasjonsbehov i automatiserte miljø.

1. **Profibus DP (Decentralized Periphery)**:
   - Designa for raske og effektive kommunikasjonar mellom ein PLC og fjernmodular som sensorar og aktuatorar.
   - Vanleg i maskin- og prosesskontroll der det er naudsynt med høg oppdateringsfrekvens.
   - Fokuserer på datautveksling med periferieiningar på lågaste nivå i automasjonspyramiden og brukar ofte ein master-slave-arkitektur.

2. **Profibus PA (Process Automation)**:
   - Optimalisert for prosessautomatisering og kan drive sensorar direkte via buss-strømming, noko som reduserer behovet for eksterne strømkjelder.
   - Vanleg i eksplosjonsfarlege miljø som olje- og gassindustrien, der sikkerheit og pålitelegheit er avgjerande.
   - Profibus PA nyttar seg av spesielle protokollar for å ivareta funksjonane i prosessindustrien og er kompatibel med Profibus DP gjennom ein segmentkoplar som handsamar protokollomforming.

3. **Profibus FMS (Fieldbus Message Specification)**:
   - Tidlegare nytta i komplekse nettverksapplikasjonar med krav til omfattande datautveksling mellom distribuerte system, som SCADA-system.
   - Brukar typisk ein meir avansert kommunikasjonsmodell med støtte for funksjonar som datautveksling, kontroll og diagnose.
   - FMS er mindre vanleg i dag, då Profibus DP og PA har dekka dei fleste bruksområda i moderne industriell kommunikasjon.

**Samspel og bruk**:
Desse Profibus-variantane blir ofte integrert i industrielle automasjonssystem som opererer i hierarkiske automasjonspyramider, der DP vert brukt til kontroll på felt- og kontrolleringsnivå, medan PA vert brukt i prosessautomatisering. I tillegg er Profibus mykje nytta i Industry 4.0-konsept for å kommunisere med nyare system som IoT-enheiter, noko som krev integrasjon med moderne protokollar og nettverksstrukturar

**Profibus-PA (Process Automation) - Detaljert Forklaring:**

Profibus-PA er ein versjon av Profibus spesielt utvikla for prosessautomatisering, med særlege eigenskapar tilpassa krava i kontrollsystem og instrumentering i prosessindustrien. Det blir brukt i bransjar som olje, gass, kjemikalieproduksjon, og farmasi, der det er behov for påliteleg kommunikasjon og robustheit i potensielt farlege miljø. Profibus-PA er bygd for å integrerast i industrielle miljø der sensorar, transmitterar, aktuatorar og kontrollsystem samhandlar for å overvake og styre prosessar.

### Viktige Eigenskapar ved Profibus-PA:

1. **Strømforsyning gjennom buskabelen**: Ein av hovudfordelane med Profibus-PA er at einingar (periferieiningar som sensorar og aktuatorar) får straum gjennom den same kabelen som dataoverføringa skjer på. Dette reduserer behovet for separate strømkjelder til kvar eining og forenklar installasjonen.

2. **Bruk i eksplosjonsfarlege område**: Profibus-PA er designa for bruk i eksplosjonsfarlege miljø, noko som er vanleg i prosessindustri der farlege gassar eller kjemikaliar kan vere til stades. Systemet oppfyller IEC-standardane som krev at utstyr må vere eksplosjonssikkert, og det kan installast i slike miljø utan ekstra beskyttelsestiltak.

3. **Dataoverføring via IEC 61158-2**: Profibus-PA brukar fysisk lag-spesifikasjonar frå IEC 61158-2-standarden, som definerer dataoverføringsmetodar tilpassa prosessindustrien. Overføringa skjer med ein synkron, digital signaloverføring ved 31,25 kbit/s, noko som sikrar stabilitet og pålitelegheit over lange avstandar.

4. **Manchester-koding**: Manchester-koding er ein metode for å kode digitale signal i Profibus-PA, som sikrar påliteleg dataoverføring. Her blir både data og klokkesignal kombinert i eit signal, noko som gjer systemet mindre sårbart for støy og tap av data, spesielt over lengre kablar.

### Fordelar med Profibus-PA i prosessautomatisering:

- **Sikkerheit og diagnostikk**: Profibus-PA gir innebygd støtte for autodiagnose og overvaking av systemstatus, noko som aukar driftssikkerheita og gjer det enklare å følgje med på utstyr og prosessar.
- **Kostnadsreduksjon**: Gjennom felles straum- og datalinjer og støtte for mange einingar på same buskabel, reduserer Profibus-PA kostnadene knytt til kabling og installasjon.
- **Integrasjonsevne**: Profibus-PA kan enkelt integrerast med Profibus-DP, som ofte er brukt i fabrikken sin kontrollseksjon. Dette blir gjort gjennom ein DP-PA-koplar som konverterer signal mellom dei to standardane, og gjer det mogleg å kople prosessautomatisering (PA) og diskret kontroll (DP).

### Typisk bruk av Profibus-PA:

Profibus-PA blir brukt i komplekse prosessmiljø der presisjon og pålitelegheit er kritiske faktorar. Det kan vere alt frå måling av trykk, temperatur og nivå i tankar til styring av ventilar og pumper i prosesslinjer. I slike miljø er det viktig med høg nøyaktigheit og stabil kommunikasjon mellom instrument og kontrollsystem, spesielt i anlegg der feil kan føre til eksplosjonsfare eller utslepp av farlege stoff.

### Topologi og nettverksstruktur:
Profibus-PA brukar ei lineær eller trestrukturert topologi, som kan støtte opptil 126 adressebare einingar og ein kabellengde på opp til 1900 meter. Dette gjer det mogleg å dekke store område med ein enkelt buskabel, noko som er praktisk i store prosessanlegg.

Profibus-PA er derfor ein viktig komponent i moderne automatiserte prosessystem og spelar ei sentral rolle i Industri 4.0-konseptet, der integrasjon av sensornettverk og styringssystem i større datasystem som IoT-nettverk og skybaserte system står sentralt.

**Profibus-DP** og **Profibus-PA**:

### Profibus-DP (Decentralized Periphery)
Profibus-DP er designa for raske kommunikasjonar mellom kontrollerar (som PLC) og periferieiningar som sensorar og aktuatorar i industrielle automatiseringssystem. Denne typen Profibus nyttar ein **master/slave-arkitektur** der ein sentral kontroller (master) sender instruksjonar til og mottek data frå fleire tilknytte einingar (slaves). I Profibus-DP kan systemet også støtte **multiple master-modus**, der fleire mastere kan vere i same nettverk. Når fleire mastere er til stades, brukar Profibus ein "token-passing"-mekanisme for å sikre at berre éin master er aktiv og sender data til ei kvar tid. Dette bidrar til å redusere nettverkskollisjonar, men kan redusere effektiviteten på grunn av ekstra overhead.

Profibus-DP tilbyr både **syklisk** og **asyklisk kommunikasjon**:
- **Syklisk kommunikasjon** går føre seg kontinuerleg på førehand fastsette tidsslotar, noko som gjer det mogleg å sende data fram og tilbake mellom master og slave einingar utan forsinkingar.
- **Asyklisk kommunikasjon** gjer at masteren kan sende data utanfor det faste sykluset for å støtte funksjonar som alarmmeldingar og parameteroppdateringar.

### Profibus-PA (Process Automation)
Profibus-PA er optimalisert for bruk i prosessindustrien og passar spesielt godt i farlege miljø, som til dømes eksplosjonsfarlege soner. Profibus-PA brukar også eit **master/slave-konsept**, men til forskjell frå DP, er enheter i PA-designen forsynte med strøm gjennom bus-kabelen og oppfyller krav til eksplosjonssikring. Profibus-PA brukar **IEC 61158-2-fysisk lag** som standard for dataoverføring, og signalet blir sendt ved hjelp av **Manchester-koding**, som gjer det meir robust mot signalstøy over lengre avstandar.

Sjølv om Profibus-PA har lågare overføringshastigheit enn DP, er det designa for pålitelegheit og sikkerheit i miljø der presisjon og driftstryggleik er kritiske.


### Kommunikasjonsprofil for Profibus-DP
Profibus-DP (Decentralized Periphery) nyttar RS-485 som fysisk medium, som typisk består av ein tvunnet parkabel. Dette er eit robust system som støttar opptil 126 stasjonar, og er brukt i mange industrielle automatiseringsmiljø. Systemet kan køyre på forskjellige fysiske media som fiberoptikk, infraraud overføring, og trådlaus overføring, som gjer det fleksibelt i installasjon.

#### Fysiske eigenskapar:
- Topologien er ein lineær bus, og kabelen må terminerast i begge endar for å sikre god kommunikasjon.
- **Tvunnet parkabel**: Denne typen kabel kan skjerme for elektromagnetisk støy, noko som er viktig i industrielle miljø.
- Støtter forskjellige baudratar: For baudratar over 500 kbaud, er type A kabel foretrukken, medan type B kabel kan nyttast for kortare avstandar med lågare baudratar.
- **Segmentlengde** varierer basert på overføringshastigheit, med støtte frå 9,6 kbps til 12 Mbps.

### Data Link-lag (FDL - Fieldbus Data Link)
FDL, eller datalinklaget, kontrollerer tilgang til bussen og tilbyr mellom anna datatryggleik og telegramstruktur. FDL tilbyr både **SDN** (Serial Data uten kvittering) og **SRD** (Send og motta data med kvittering). Dette gjer det mogleg med pålitelege dataoverføringar ved bruk av kvitteringsmeldingar, noko som gir tryggleik i kommunikasjonen mellom master og slave.

### DDLM (Direct Data Link Mapper) og Brukergrensesnitt
DDLM ligg på topp av OSI-lag 7, og handterer asynkrone service-funksjonar som start/stopp, vedlikehald og alarmmeldingar. Dette gjer at Profibus-DP kan handtere både syklisk og asyklisk kommunikasjon med stor fleksibilitet.

**DDLM (Direct Data Link Mapper)** i Profibus er eit grensesnitt på lag 7 i OSI-modellen, og fungerer som eit bindeledd mellom brukargrensesnittet og dei lågare kommunikasjonslaga, spesielt lag 2 (datalinklaget eller FDL). DDLM har ansvar for å omsette kommandoar frå brukargrensesnittet til handlingar i FDL, og det tilbyr fleire asynkrone funksjonar for å støtte ein effektiv og påliteleg kommunikasjon mellom kontrolleren og tilknytte einingar.

### Viktige oppgåver for DDLM:
1. **Kommunikasjonstjenester**:
   - DDLM tilbyr funksjonar som lesing, skriving, initiering og alarmhandtering. Desse tenestene blir nytta av brukargrensesnittet for operasjonar som oppstart, vedlikehald og diagnostikk.
   - Typiske kommandoar inkluderer `DDLM_Read`, `DDLM_Write`, `DDLM_Init`, `DDLM_Alarm_Ack`, og `DDLM_Abort`, som gjer det mogleg å samhandle med og styre ulike einingar i nettverket på ein fleksibel måte.

2. **Støtte for syklisk og asyklisk kommunikasjon**:
   - **Syklisk kommunikasjon** er viktig for sanntidsdata som til dømes statusoppdateringar og måledata, der data blir sendt til faste tider.
   - **Asyklisk kommunikasjon** kan nyttast for å sende data utanom dei faste tidene, til dømes for å utføre spesifikke kontrollhandlingar, sende alarmar eller oppdatere innstillingar i einingane.

3. **Mapping av data**:
   - DDLM sørger for at data blir korrekt mappar frå brukargrensesnittet til det underliggande datalinklaget (FDL). Dette inkluderer organisering av data som telegram og styring av busstilgang.
   - Mappinga gjer det mogleg å sende spesifikke kommandoar til bestemte einingar i nettverket, noko som er viktig for å sikre nøyaktig kontroll og respons.

4. **Støtte for Profibus sine beskrivingar og spesifikasjonar**:
   - DDLM nyttar *GSD-filer* (Generic Station Description) som inneheld informasjon om eigenskapane til kvar eining. Dette gjer det lettare å konfigurere og administrere kvar eining.
   - Andre spesifikasjonar inkluderer *EDD* (Electronic Device Description) og *FDT* (Field Device Tool), som legg til rette for kompatibilitet og integrasjon i Profibus-nettverk.

5. **Master-slave-arkitektur og token-passing**:
   - I Profibus-DP sin master-slave-arkitektur har DDLM ei viktig rolle i å handtere kommunikasjon mellom ein *master* (vanlegvis ein kontroller) og *slaves* (sensorar, aktuatorar).
   - Ved multimaster-oppsett nyttar Profibus-DP ein *token-passing*-mekanisme der tokenet blir delt mellom fleire mastere for å regulere tilgang til bussen. DDLM bidrar til å sikre at berre éin master sender data om gangen, noko som reduserer kollisjonar.

### Praktisk nytte i automasjonssystem:
DDLM er viktig i industrielle automasjonssystem der ein ønskjer både fleksibel og robust kommunikasjon mellom forskjellige typar feltutstyr og kontrollerar. Ved å tilby desse tenestene på lag 7, gjer DDLM det mogleg å handtere komplekse kontroll- og kommunikasjonsscenario på ein effektiv måte, og det sikrar at dataflyten mellom forskjellige komponentar i Profibus-nettverket går smidig og stabilt.

Her er ei oppsummering av informasjonen frå bileta du lasta opp om **Data Telegram** og **Device Profile** i Profibus-DP og Profibus-PA.

### 1. **Data Telegram**
Data-telegrammet i Profibus (spesielt Profibus-DP) følgjer standarden **IEC-61158-2** og er bygd opp med kontroll- og datafelt:
- **Typar av telegram**:
  - Telegram utan datafelt, som inneheld seks kontrollbyte.
  - Telegram med eit fast lengde-datafelt (8 data-byte og 6 kontrollbyte).
  - Telegram med variabel lengde, som støtter mellom 0 og 244 byte med data og mellom 9 og 11 kontrollbyte.
  - Kort kvittering (1 byte) for å bekrefte mottaking av data.
  - Token-telegram for busstilgangskontroll (3 byte).

Denne strukturen gir fleksibilitet og moglegheit til å styre og kontrollere dataoverføring i sanntid, noko som er avgjerande i industrielle miljø.

### 2. **Device Profile**
Ein **Device Profile** definerer standardiserte parameter og funksjonar for eit feltutstyr, noko som sikrar interoperabilitet mellom utstyr frå ulike produsentar.
- **Profilklassar**:
  - **Klasse A**: Inkluderer grunnleggjande parameter som er nødvendige for prosessautomatisering, som prosessvariablar, målt verdi, fysisk eining og ein unik merking (tag) for eininga.
  - **Klasse B**: Bygger på klasse A og inkluderer fleire funksjonar som skalaringsfaktorar, statusflagga og alarmgrenser.

### 3. **PA Block Model**
Blokkmodellen til Profibus-PA omfattar fleire blokktypar som organiserer funksjonane og eigenskapane til feltutstyr:
- **Transducer Block**: Denne blokka behandlar signal frå sensorar og konverterer desse til data som kan brukast vidare. Transducer-blokker kan måle ulike parameter som temperatur, trykk og nivå.
- **Physical Block**: Inneheld informasjon om sjølve eininga, inkludert serienummer, som sikrar unik identifikasjon.
- **Function Block**: Prosesserer og styrer prosessdata for spesifikke oppgåver som styring av aktuatorar og prosessvariablar.
- **Device Management**: Handterer diagnostikk, oppdateringar og vedlikehald av enheten. 

Dette blokksystemet organiserer dataflyten i Profibus-PA, slik at utstyr kan kommunisere og samhandle effektivt i komplekse industrielle miljø.

**GSD (General Station Description) i Profibus**

GSD (General Station Description) er ein filstandard i Profibus som spesifiserer kommunikasjonen og funksjonaliteten til eit feltutstyr. Kvar Profibus-eining har ei unik GSD-fil levert av produsenten, som inneheld alle naudsynte data for å konfigurere, integrere og bruke eininga korrekt i eit Profibus-nettverk.

### Funksjonar og Innhald i GSD
Ein GSD-fil inneheld informasjon som gjer at systemet kan forstå og samhandle med eininga. Dette inkluderer:
- **Identifikasjon**: Inkluderer produsentnamn (Vendor_Name) og utstyrs-ID, slik at systemet kan identifisere produsenten og spesifikasjonane for eininga.
- **Kommunikasjonsparametrar**: Informasjon om baudrate, støtta opsjonar, I/O-signalar, og tidsintervall for kommunikasjon.
- **I/O-konfigurasjon**: Definerer antall inngangs- og utgangssignalar samt lengde og timing, som gir detaljar om signalbehandling.
- **Feilhandsaming og diagnostikk**: Opplysningar om korleis eininga handterer feilsituasjonar, som bidreg til påliteleg drift i automatiserte system.

### Bruk av GSD
1. **Forenkla Oppsett og Integrasjon**:
   - GSD-filene gir plug-and-play-funksjonalitet ved å sikre at einingar frå ulike produsentar kan fungere saman i same system utan komplisert programmering.
   - Konfigurasjonsverktøy kan lese GSD-filer for å hente ut informasjon om eininga, som gjer oppsett og vedlikehald enklare.

2. **Typar av GSD**:
   - **GSD for kompakte einingar**: Her er blokkkonfigurasjonen definert av produsenten, og det krevst minimal konfigurering frå brukarens side.
   - **GSD for modulære einingar**: Her er ikkje alle blokker ferdigdefinerte av produsenten, og brukaren må konfigurere oppsettet basert på moduloppbygging av eininga.

### Spesifikasjonar og Struktur
GSD-filer har tre hovudtypar spesifikasjonar:
- **Generelle spesifikasjonar**: Inkluderer grunnleggjande informasjon som namn på eining og produsent, samt overføringshastigheit.
- **Master-spesifikasjonar**: Gir informasjon om maksimalt antall slavesystem ein master kan handtere, samt støtte for opplastings- og nedlastingsopsjonar.
- **Slave-spesifikasjonar**: Definerer funksjonane og eigenskapane til eininga i nettverket, som for eksempel I/O-konfigurasjon og tidsstyring.

### Teknologisk Integrasjon: GSD, FDT, og EDD
GSD fungerer saman med FDT (Field Device Tool) og EDD (Electronic Device Description) for å støtte avansert parametisering, diagnostikk og sanntidsjustering av einingar. Dette gjer det mogleg å oppdatere og tilpasse einingar i drift, og gir betre fleksibilitet i kontinuerlege prosessar som prosessautomatisering.

### Oppsummering
GSD-filen er eit kritisk element i Profibus-nettverk som legg til rette for enkel integrasjon, konfigurering og vedlikehald av feltutstyr. Ved å definere all nødvendig informasjon for kommunikasjon og funksjonar, sikrar GSD at einingane kan operere sømløst saman i komplekse industrielle automasjonssystem.

Her er ei oversikt over **EDD (Electronic Device Description)** og **FDT/DTM (Field Device Tool / Device Type Manager)**, som begge er viktige for integrasjon og konfigurering av feltutstyr i Profibus-system.

### EDD (Electronic Device Description)
EDD er eit kraftig programverktøy som nyttar **Electronic Device Description Language (EDDL)** for å beskrive konfigurasjonsparametrar og funksjonar til eit feltutstyr. Dette inkluderer informasjon om verdiskala, måleeiningar, og standardverdiar.

#### Funksjonar og Bruksområde:
- **Konfigurasjon og oppsett**: EDD gjer at produsentar kan lage EDD-filer som inneheld dei nødvendige data for oppsett og parametisering av utstyret. Dette gjer det enklare å handtere utstyret frå kontrollsystemet sitt verktøy.
- **Dokumentasjon og administrasjon**: EDD blir også brukt til asset management, e-handel, og dokumentasjon, noko som kan redusere treningskostnader og gi enklare datavalidering.

#### Fordelar:
- Ein felles standard reduserer behovet for fleire verktøy, og gir betre konsistens i data.
- EDD sikrar at informasjonen frå feltutstyret er lett tilgjengeleg for ingeniørverktøy og kontrollsystem, som bidrar til effektiv drift og vedlikehald.

### FDT/DTM (Field Device Tool / Device Type Manager)
FDT/DTM er ein **open grensesnittspesifikasjon** som er produsentuavhengig og er utvikla for å støtte integrering av feltutstyr i operatørprogrammet via ein DTM, som er eit spesifikt brukergrensesnitt for kvart feltutstyr.

#### Funksjonar:
- **Konfigurasjon og parametisering**: FDT/DTM gjer at brukaren kan parametrisere, konfigurere og diagnostisere feltutstyr i eit standardisert miljø. 
- **Utvidet diagnostikk**: DTM kan tilpassast kvar eining og gir avansert diagnostikk og vedlikehaldsfunksjonar som eksisterande verktøy kanskje ikkje støttar.
- **Protokolluavhengig**: FDT/DTM er protokolluavhengig, noko som betyr at det kan integrere fleire typar feltutstyr utan at ein må tilpasse systemet til kvar enkelt protokoll.

#### Implementering:
- **DTM** kan implementerast ved hjelp av ulike teknologiar som Visual Basic eller høgare programmeringsspråk, avhengig av kompleksiteten til eininga.
- FDT-rammeverket gjer det mogleg for brukarar å få tilgang til mange funksjonar og eigenskapar i feltutstyret, som tidlegare var vanskeleg å få tak i på tvers av ulike system.

#### Fordelar for Brukar:
- Gir ein integrert plattform for vedlikehald og konfigurering av feltutstyr.
- Betre tilpassa for avansert styring og bedriftsadministrasjon.
- Sikrar at brukaren har tilgang til tilleggsfunksjonar og vedlikehaldsalternativ på ein meir effektiv måte, sidan FDT/DTM støttar einingane sine spesifikke behov i automasjonssystemet.

Her er ein detaljert oversikt over **Network Configuration**, **Bus Monitor**, **Timestamp** og **Redundancy** i Profibus:

### 1. Network Configuration
**Network Configuration** i Profibus bruker GSD-filene (General Station Description) som er levert av produsenten for å sette opp kommunikasjonen mellom kontrollerar og tilknytte einingar (slaver). GSD-filene inneheld viktige opplysningar som produsent-ID, baudrate, I/O-data-konfigurasjon, og andre eigenskapar.

- **Oppstartsprosess**: Ved oppstart vil masteren laste inn GSD-filene til alle slaver og setje opp adressene deira basert på parameterverdiane i GSD-filene.
- **Adresseallokering**: Kvar slave har ei unik adresse i området 0 til 125, noko som gjer det mogleg for masteren å kommunisere effektivt med alle tilknytte einingar.

### 2. Bus Monitor
Ein **Bus Monitor**, eller protokollanalysator, er eit programverktøy som overvåker og diagnostiserer aktivitetar på Profibus-nettverket. Dette er typisk ein PC med spesialprogramvare og -maskinvare som kan fange opp og analysere datatrafikken på bussen.

- **Tidsstempling**: Kvar melding på nettverket blir merka med høgoppløyselege tidsstempel, noko som gir eksakt informasjon om når kvar melding blir sendt.
- **Feildiagnose**: Bus Monitor kan identifisere og analysere problem, slik at operatørar raskt kan oppdage feil i utstyret eller kommunikasjonen utan å påverke nettverksytelsen.

### 3. Timestamp
**Timestamping** i Profibus er avgjerande for å sikre presis oppfølging av hendingar, spesielt i samband med alarmar og diagnostikk. Dette gjer det mogleg å tilordne spesifikke tidspunkter til hendingar, som igjen kan brukast til å analysere og prioritere feilmeldingar og systemalarmar.

- **Systemklokke**: Profibus-nettverket nyttar ein systemklokke i masteren som sender ut tidsstempel til slave-einingane.
- **Hendingar og Prioritering**: Meldingar blir klassifiserte basert på prioritet. Alarmar får høgare prioritet og tidsstemplast, medan mindre kritiske hendingar får lågare prioritet.

### 4. Redundancy
**Redundancy** i Profibus sikrar høg tilgjengeligheit og pålitelegheit ved å ha reservekomponentar klare til å ta over dersom primærkomponentar feilar. Profibus kan implementere fleire typar redundans:

- **Master Redundancy**: Sikrar at ein sekundær master kan ta over dersom den primære feilar.
- **Media Redundancy**: Doblar kablar og nettverk for å sikre at ein kabelfeil ikkje stoppar kommunikasjonen.
- **Slave Redundancy**: Kvar slave kan ha eit hovud- og eit reserveinterface, der reserveinterfacet (kalla RedCom) kan ta over kommunikasjonen dersom hovudinterfacet feilar. 

Dette redundanssystemet gir høg pålitelegheit og minimalt med nedetid, noko som er viktig i automatiserte og kritiske miljø som prosessindustri og produksjonsanlegg.

Her er ei oppsummering av PROFIsafe og PROFIdrive basert på informasjonen i dei opplastede bileta:

### PROFIsafe
**PROFIsafe** er ei løysing for sikkerheitskritiske applikasjonar som er implementert i lag 7 av OSI-modellen i Profibus-systemet. Den er spesielt designa for å takle utfordringar i samband med feil i dataoverføring, som kan omfatte tap eller repetisjon av data, feil sekvens, og korrupsjon av meldingar. PROFIsafe legg til rette for trygg kommunikasjon mellom einingar som nødstoppsknappar og sikkerheitskontrollar.

#### Hovudfunksjonar:
- **Sikkerheitsnivå**: PROFIsafe støtter sikkerheitskrav opp til SIL3 (Safety Integrity Level 3) og KAT4 i samsvar med standardane EN954 og SIL.
- **Tilleggsfunksjonar for sikkerheit**: 
  - Nummerering av sekvensielle tryggleiks-telegram for å sikre korrekt rekkjefølgje.
  - Identifikatorar mellom sender og mottakar, implementert som eit passord for ekstra autentisering.
  - Ekstra kontrollar som **CRC** (Cyclic Redundancy Check) og timeout for meldingar, som sikrar påliteleg overføring.

### PROFIdrive
**PROFIdrive** er ein standard brukt for elektriske drivsystem innan automasjon. Den gir støtte for fleire typer drivstyring, frå enkle frekvensomformarar til avanserte servosystem. PROFIdrive definerer seks applikasjonsklassar avhengig av kompleksiteten til applikasjonen.

#### Applikasjonsklassar:
1. **Standard Drive (klasse 1)**: Kontrollert av settpunktsverdiar som styrer rotasjonshastigheit.
2. **Standard Drive med Teknologiske Funksjonar (klasse 2)**: Gjer det mogleg å dele opp automasjonsprosessen i mindre delar og fordele styringsfunksjonar til drive-kontrolleren.
3. **Positioning Drive (klasse 3)**: Inkluderer ein posisjonskontroller i driven, til dømes for presis plassering.
4. **Central Motion Control (klasse 4 og 5)**: Fleire drives samordnar bevegelsessekvensen og blir styrte av ei numerisk maskin (ofte brukt i robotikk).
5. **Distributed Automation (klasse 6)**: Støtter slave-til-slave kommunikasjon og gjer det mogleg med klokkestyre prosessar og elektroniske akslingar.

PROFIsafe og PROFIdrive gjer Profibus-systemet eigna til bruk i kritiske miljø som krev både høg tryggleik og nøyaktig styring.