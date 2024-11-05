### Kapittel 5: Introduksjon til Industriell Nettverksdesign

**Industrielle Nettverk** er nettverk som støtter samhandling og kommunikasjon mellom einingar innan industrielle kontrollsystem (ICS). Dette kan vere **lokalnettverk (LAN)** i distribuerte kontrollsystem (DCS) eller **wide-area nettverk (WAN)** i SCADA-system. Kapittelet gir ein oversikt over skilnader mellom industrielle nettverk og forretningsnettverk, der tilgjengelegheit av data er kritisk i industrielle system, medan konfidensialitet og integritet er hovudfokus i forretningsmiljø. 

**Teknologisk Likskap og Ulikskap**: 
Begge nettverkstypar er ofte **Ethernet- og IP-baserte**, men industrielle nettverk prioriterer lav latens og pålitelegheit. Bandbreidde og latens er avgjerande for å støtte sanntidsoperasjonar, som ofte krev deterministisk kommunikasjon med presise tidskrav.

### Hovudpoeng og Forskjellar Mellom Industrielle og Forretningsnettverk
- **Sanntidsoperasjon**: Industrielle nettverk prioriterer sanntidsoperasjon og pålitelegheit med dedikerte ressursar og få, eksplisitte sesjonar, i motsetning til den dynamiske bruken i forretningsnettverk.
- **Topologi**: Industrielle nettverk bruker ofte ring- eller mesh-topologiar for å auke robustheit og redundans, medan forretningsnettverk typisk brukar stjernetopologi.
- **Protokollar**: Industrielle nettverk brukar sanntidsprotokollar og kan inkludere proprietære protokollar tilpassa spesifikke kontrollsystem.

### Nettverksdesign og Segmentering
Kapittelet viser korleis industrielle nettverk er designa med fokus på sanntidsdataoverføring og minimal latens. Eit optimalt design for industriell bruk vil ofte inkludere:
- **Switching** i staden for routing, der mogleg, for å redusere latens.
- Bruk av **Ethernet-brannmurar** for lågnivå sikkerheit utan at det påverkar nettverksytelse.
- **Lag 3-switchar** for betre yting ved å kombinere switching og routing i éin eining, noko som eliminerer nokre av overføringane mellom nodar og reduserer latens.

### Redundans og Høgtilgjengelegheit
Industrielle nettverk er ofte designa for redundans, der system blir kopla til fleire Ethernet-tilkoplingar og kan bruke protokollar som:
- **Spanning Tree Protocol** for å eliminere loopar.
- **VSRP** og **VRRP** for redundante switch- og ruteroppsett med høg tilgjengelegheit.

### Tilpassing til Spesialiserte Protokollar
For å oppfylle krava til sanntidskontroll brukar industrielle nettverk ofte spesifikke, tilpassa topologiar og protokollar. FOUNDATION Fieldbus og andre feltbusser, som PROFIBUS-PA og ControlNet, er baserte på serielle tilkoplingar som krever spesifikke termineringar og buskoplingar for riktig funksjon.

### Vanlege Topologiar i Industrielle Nettverk

Kapittelet beskriver vanlege nettverkstopologiar som blir brukte i industrielle nettverk for å møte spesifikke krav til sanntidsoperasjon, pålitelegheit og sikkerheit. Mens Ethernet- og IP-baserte stjerne- og mesh-topologiar dominerer i forretningsnettverk, treng industrielle nettverk ofte også **ring- og busstopologiar** for å støtte spesifikke kontrollprosessar og krav.

#### Typar Topologiar i Industrielle Nettverk

1. **Busstopologi**:
   - Ein lineær topologi der fleire einingar er tilknytt ein felles bus, ofte via tappepunkt.
   - Brukar terminatorar på kvar ende for å hindre signalrefleksjonar.
   - **Fordelar**: Kostnadseffektiv og enkel for serielt tilknytte einingar, ofte brukt i system med begrensa bandbreiddekrav som FOUNDATION Fieldbus H1.
   - **Ulemper**: Avgrensa ytelse og pålitelegheit på grunn av delt båndbredde.

2. **Meshtopologi**:
   - Vanleg for tilkopling av kritiske einingar som krever høg oppetid og yting.
   - Mange stiar betyr at sjølv om ein tilkopling eller ein eining sviktar, påverkar det ikkje nødvendigvis nettverksytelsen.

3. **Trådløs Mesh-topologi**:
   - Logisk lik kablede mesh-nettverk, men basert på trådløse signal som styrer informasjonsflyt gjennom provisjonering i staden for faste kablar.
   - Brukes ofte i industrielle trådløse nettverk for fleksibilitet og redundans.

4. **Stjernetopologi**:
   - Point-to-multipoint-topologi der ei sentral ressurs støttar mange einingar, illustrert ved ein Ethernet-switch med individuelle tilkoplingar til endepunkt.
   - Vanleg topologi i forretningsnettverk, men brukt i industrielle nettverk for å kople tilgangsswitchar.

5. **Tre-/Gren-topologi**:
   - Hierarkisk oppbygd med ein “stamme” (vanlegvis ein bus) som støtter fleire under-topologiar, ofte bus eller stjerne.
   - Eit eksempel er FOUNDATION Fieldbus H1, der ein bus interkonnektar fleire koplingsboksar som vidare koplar til fleire felteiningar i ein stjerneformasjon.

6. **Ringtopologi**:
   - Einingar er kopla i ein sirkel, der siste node er kopla tilbake til første node.
   - Vanleg for nettverkstilgangsswitchar i industrielle nettverk, noko som gir redundante stiar som sikrar høgare pålitelegheit.

7. **Multihoming/Dual-Homing**:
   - Ein node er kopla til to eller fleire nettverk, som gir redundans eller tilgang til fleire soner.
   - **Sikkerheitsbetraktning**: Multihoming kan utgjere ein risiko, da ein angripar som kompromitterer ein dual-homed server kan bruke den til å bryte seg mellom soner, som kan eksponere sensitiv industriell informasjon.

#### Effekt på Sikkerheit og Segmentering
Nettverkstopologien påverkar både sikkerheit og segmentering. Korrekt val av topologi bidreg til:
- Definering av sikre soner.
- Kontroll av trafikkflyt, forenkla ved bruk av brannmurar og tilgangskontrollistar (ACL) mellom soner.
- Reduksjon av risikoen for uautorisert tilgjenge via dual-homed einingar, noko som understreker betydninga av nettverkssegmentering for sikkerheit i industrielle miljø.

### Nettverkssegmentering i Industrielle Nettverk

Nettverkssegmentering spelar ei avgjerande rolle i industrielle nettverk ved å redusere risiko for dataoverføring til uautoriserte brukarar, oppretthalde systemytelse, og minimere påverknaden av potensielle cyberangrep. Segmentering skaper mindre, meir oversiktlege nettverkssoner, der segmenterte område kan ha spesifikke tilgangs- og sikkerheitskontrollar.

#### Segmentering og VLANs

I eldre Ethernet-nettverk blei segmentering oppnådd ved hjelp av **routere** på lag 3 for å bryte opp det flate nettverket. Med framveksten av **virtuelle LAN (VLAN)** på lag 2, har segmentering blitt meir fleksibel og kostnadseffektiv, då VLAN-IDar kan gi logisk oppdeling utan fysiske routere for kvar sone. 

**Merk**: VLAN-segmentering på lag 2 betyr at einingar med same IP-område, men ulike VLAN-IDar, er logisk isolerte, sjølv om dei kan vere tilkopla same switch. Best praksis er å ha unike IP-områder for kvar VLAN-ID for å unngå feilkonfigurasjon.

#### Segmentering vs. Segregering

- **Segmentering** refererer til å dele opp nettverket eller soner, men med kontrollert kommunikasjon mellom segmenta, noko som opprettheld felles infrastruktur.
- **Segregering** betyr derimot full isolasjon av system utan fysisk tilkopling mellom dei. Til dømes kan to VLAN på same switch vere segmenterte, men ikkje fullstendig segregerte, då dei framleis deler fysisk maskinvare.

#### Nettverkssegmentering i Industrielle Nettverk

For industrielle nettverk bidrar segmentering til å beskytte ulike nettverkssoner med separate funksjonar, for eksempel:
- **Forretningsnettverk** (ERP-systemer, bedriftsnettsider)
- **Operasjonsnettverk** (ICS-servere, arbeidsstasjonar for ingeniørar, HMI-er)
- **Kontrollnettverk** (PLC-er, RTU-er, feltutstyr, IED-er)
- **Prosessnettverk** (analysenettverk, utstyrsovervåkingssystem)
- **Sikkerheitsnettverk** (instrumenterte sikkerheitssystem).

#### Hierarkisk Nettverkssegmentering

Segmentering skaper hierarkiske nettverk, der dataflyt mellom segment krever kontrollert tilgang gjennom fleire nettverkslag. Til dømes kan dataoverføring frå eit prosessnettverk til eit anna vere avgrensa for å hindre peer-to-peer kommunikasjon mellom segmenta, noko som gjev auka sikkerheit.

#### Typar Segmentering

Basert på infrastrukturkonfigurasjonen kan segmentering vere:
- **Absolutt**: Full separasjon utan kommunikasjon mellom segment.
- **Kondisjonell**: Kommunikasjon basert på bestemte vilkår.
- **To-vegs**: Gjensidig kommunikasjon mellom segment.
- **Ein-vegs**: Kommunikasjon i berre éin retning mellom segment.

Gjennom slike strategiar kan industrielle nettverk sikre at data berre flyt der det er naudsynt, og kontrollere kommunikasjon mellom dei ulike segmenta, noko som reduserer risiko for laterale cyberangrep og sikrar data integritet.

### Høgare Lags Segmentering i Industrielle Nettverk

Segmentering på høgare lag i OSI-modellen (lag 4–7) kan gi meir presise måtar å styre og avgrense kommunikasjon på. **Segmentering på lag 4–7**, også kjent som **protokollfiltrering** eller **nettverks-whitelisting**, avgrensar nettverksaktivitetar på spesifikke applikasjonar og sesjonar. Dette kan til dømes innebere at berre spesifikke kommandoar for PROFINET er tillatne mellom bestemte einingar, noko som krev avanserte nettverksverktøy som **IPS** eller **neste generasjon brannmurar (NGFW)** som kan inspisere trafikk opp til applikasjonslaget.

### Segmenteringstypar i OSI-modellen

| Lag | Metode | Beskriving | Sikkerheitsfordelar |
|------|--------|------------|---------------------|
| **Fysisk lag** | Air Gap, Data Diode | Full fysisk separasjon, hindrar dataflyt | Maksimal isolasjon, men kan lett omgåast fysisk. |
| **Datalink-lag** | VLAN | Segmenterer gjennom VLANs på lag 2 | Enkel segmentering, men kan vere sårbar for VLAN hopping. |
| **Nettverkslag** | Router, Layer 3 Switch | Segmentering gjennom IP-ruting og ACL | Sterk sikkerheit gjennom ACL og subnetkontroll, reduserer risiko for lag 3-angrep. |
| **Sesjonslag** | Brannmur, IPS | Kontroll over spesifikke nettverkssesjonar | Spesifikk protokollkontroll, mindre effekt på ytelse, men ikkje full isolasjon. |
| **Applikasjonslag** | Proxy, NGFW, Content Filter | Djuppakkeinspeksjon (DPI) for å filtrere på applikasjonsnivå | Høg presisjon i segmentering, men kan redusere ytelse. |

### Fordelar med Segmentering på Høgare Lagsnivå
- **Presisjon**: Ved å avgrense kommunikasjon basert på applikasjonsinnhald kan segmentering på lag 4–7 tilby granular kontroll som ikkje er mogleg på lågare lag.
- **Isolasjon av spesifikke tenester**: Ved å filtrere på kommando- og enhetsnivå hindrar ein at uautoriserte kommandoar blir sendt mellom einingar.
- **Begrensing av trusselbilete**: Djuppakkeinspeksjon kan avdekkje spesifikke truslar som ikkje kan oppdagast ved VLAN-basert segmentering.

### Sikkerheit og Segmentering ved Lagsdeling
Den beste tilnærminga er ein **fleir-lags sikkerheitsstrategi** der fleire lag segmentering blir brukt, avhengig av risikoen i dei spesifikke nettverksområda. Medan VLAN og nettverksbasert segmentering gjev god ytelse, kan segmentering på høgare lag identifisere og isolere spesifikke industriprotokollar og -applikasjonar for auka sikkerheit.

### Utfordringar med VLAN
VLANs kan vere sårbare for ei rekkje lag 2-angrep som **VLAN hopping** og **ARP-forgifting**. VLAN hopping skjer når ein angripar manipulerer VLAN-headerar eller utnyttar trunkingprotokollar for å bevege seg mellom VLANs. Slik hopping kan unngåast ved å avgrense VLAN-trunkar til spesifikke VLANs og deaktivere trunking der det ikkje er naudsynt.

### Sikkerheit og Sårbarheiter i VLAN-segmentering og Høgare Lagssegmentering

VLAN-segmentering gir logisk isolering av nettverkssoner på lag 2 i OSI-modellen, noko som er viktig i industrielle nettverk. Men VLANs kan vere sårbare for lag 2-angrep som kan true nettverkssikkerheita. For å oppnå betre kontroll, kan segmentering også implementerast på høgare lag (4–7) ved bruk av avanserte brannmurar og inntrengingsdeteksjon (IPS).

#### VLAN-sårbarheiter
1. **Flood-angrep**: Eit flood-angrep overfyller switchens MAC-adressetabell, noko som kan forårsake nettverksavbrot.
2. **Spanning Tree-angrep**: Manipulasjon av Spanning Tree Protocol kan endre nettverksstrukturen, og kan føre til redundante vegar som kan forstyrre trafikkflyten.
3. **ARP-forgifting**: Angriparar kan forfalske ARP-meldingar for å omdirigere trafikk mellom einingar på eit VLAN.
4. **VLAN Hopping**: 
   - **Switch Spoofing**: Angriparen konfigurerer ein system til å oppføre seg som ein switch og utnyttar Dynamic Trunking Protocol (DTP), som gir tilgang til fleire VLAN.
   - **Dobbelt-taggingsangrep**: Angriparen legg til to VLAN-IDar i ramma, noko som fører til at ein switch fjernar den første taggen og sender ramma vidare på feil VLAN.

   **Forsvar mot VLAN Hopping**: Begrens tilgjengelege VLAN på trunkar og deaktiver trunking på kritiske punkt.

#### Høgare Lags Segmentering og Brannmurfunksjonar
Segmentering på lag 4–7 gir presis kontroll av spesifikke applikasjonar og protokollar:
- **Applikasjonslagsbrannmurar** kan inspeksjonere innhald på lag 5–7, og kan dermed tillate lesetilgang til ein PLC, men blokkere skrivetilgang for å beskytte kritiske operasjonar.
- **Sesjonsbevisste brannmurar**: Kan verifisere gyldige sesjonar og hindre sofistikerte angrep som ikkje kan fanges opp av enklare brannmurar.
- **Next-Generation Firewalls (NGFW)**: Avanserte brannmurar som brukar djuppakkeinspeksjon (DPI) for å kontrollere spesifikke kommandoar, noko som gir granulær sikkerheitskontroll.

#### Fysisk vs. Logisk Segmentering
- **Fysisk Segmentering**: Brukar fleire fysiske einingar (t.d. separate switchar) for å isolere nettverkssegment, ofte brukt i kritiske miljø som kjerneprosesskontroll.
- **Logisk Segmentering**: VLAN-basert isolering på ein enkelt switch. Kan vere utsatt for sårbarheiter dersom ikkje alle sikkerheitstiltak blir tatt.

#### Tiltak for Forbedra Sikkerheit i VLAN-segmentering
1. **Defense-in-Depth**: Kombiner lag 2 VLAN-segmentering med lag 3-filtrering og høgare lags segmentering for fleire lag med sikkerheit.
2. **IDS-overvåking**: Plasser IDS på spegla eller spanna portar for å overvåke segment som ikkje har innebygde sikkerheitskontrollar.
3. **Spesialtilpassa Utstyr**: Industrisikkerheitsutstyr bør tåle høge temperaturar og krevjande miljø for å oppretthalde stabilitet og sikkerheit i produksjonsmiljø.

#### Tiered (Hierarkisk) Segmentering
Hierarkisk segmentering resulterer ofte i eit trappetrinn-design, der kvart nivå i arkitekturen har strengare tilgangskontroll når ein beveger seg lenger ned i nettverksstrukturen. Dette forenklar bruken av **forsvar-i-dybden**-strategiar, som legg til fleire lag med sikkerheit og stramare kontroller for å beskytte kritiske system.

Segmentering, både på lågare og høgare lag, gir robust nettverkstryggleik og kan hindre eller avgrense spreiing av angrep i industrielle nettverk ved å styre kommunikasjon mellom soner presist.

### Nettverkstenester og Trådlause Nettverk i Industrielle Miljø

**Nettverkstenester** i industrielle miljø inkluderer identitets- og tilgangskontroll (IAM), katalogtenester, og domenetenester, som bidreg til å kontrollere tilgang innan industrielle soner. Sjølv om desse tenestene finst i forretningsnettverk, er det viktig at dei ikkje blir delt mellom IT og OT (Operational Technology)-nettverk. Særleg anbefalast det at **domenekontrollerar og IAM-system** for OT-brukarar er isolert frå forretningsnettverket for å redusere risikoen for kompromitterte brukardata ved eit mogleg IT-sikkerheitsbrot.

#### Prinsippet om Minimale Tilganger og Kommunikasjonsvegar (Least Route)
Dette prinsippet slår fast at ei eining berre skal ha minimumstilgangen som krevst for dens funksjon, og kun dei nødvendige tilkoplingane. Ved å opprette **formålsbygde nettverk**, som er optimalisert for spesifikke funksjonar (til dømes kontrollsystem), minimerast risikoen for uønskt kommunikasjon mellom ikkje-relaterte einingar. Til dømes kan ein unngå kommunikasjon mellom produksjonslinjer der det ikkje er naudsynt for prosesskontroll.

### Trådlause Nettverk i Industrielle System
Trådlause nettverk kan vere nyttige i mange industriområde, men dei er sårbare fordi signal kan spreiast utanfor fysisk avgrensa soner. Nokre viktige vurderingar:
- **Radiofrekvenskartlegging**: Viktig for optimal plassering av antenner og for å unngå uønskt signallekkasje.
- **Teknologiar**: Industristandardar som **WirelessHART** og **OneWireless** (basert på IEEE 802.15.4 og ISA 100.11a) nyttast for å sikre påliteleg og trygg kommunikasjon. Begge protokollane støttar mesh-nettverk og har system for å kontrollere tilgang og sikkerheit.

#### Fordelar og Begrensningar ved Trådlause Nettverk
- **Fordelar**: Effektiv tilkopling av avsidesliggande feltutstyr, og i tilfelle der kabling er kostbart eller upraktisk.
- **Begrensningar**: For einingar med batteridrift kan levetid påverke tilgjengelegheita, noko som ofte krev lågare oppdateringsfrekvens i lukka kontrollsløyfer.

Industrielle nettverk nyttar segmentering, tilgangskontroll, og trådlause teknologiar med tilpassa sikkerheitsstrategiar for å møte dei spesifikke krava til prosesskontroll og systemintegritet.

### Fjernaksess i Industrielle Nettverk

Fjernaksess er nødvendig i mange industrielle miljø på grunn av krav til vedlikehald og oppdateringar frå leverandørar, distribuerte arbeidsstader, og utilgjengelege anlegg. Dette kan gjelde alt frå eksterne tekniske problemstillingar til overvakingsdata. Sjølv om sikker fjernaksess ved bruk av VPN, tofaktorautentisering og liknande metodar er mogleg, aukar risikoen for angrep sidan fjernaksess inneber tilkopling til offentlege nett som internett.

#### Tiltak for Tryggare Fjernaksess

1. **Minimalisere angrepsvegar**: 
   - Opprett berre éin tilgangsveg for fjernaksess. Dette gjer at sikkerheitskontrollar kan implementerast og overvåkast betre, og reduserer risikoen for feilkonfigurasjon.

2. **Prinsippet om "minste privilegium"**:
   - Gje berre tilgang til dei systema og oppgåvene ein brukar har spesifikt behov for. Dette inneber at om ein brukar kun treng lese data, bør dei ikkje ha moglegheit til å endre data.

3. **Segmentering og segregering**:
   - Fjern tilgang bør isolerast frå andre system. Dette kan innebere å opprette eigne segment for tredjepartar som berre kan få tilgang til spesifikke einingar dei treng for vedlikehald.

4. **Applikasjonskontroll**:
   - Fjernbrukarar bør autentisere seg til ei sikker applikasjonsserver i staden for å få generell tilgang til nettverket, noko som avgrensar tilgangen til spesifikke applikasjonar.

5. **Bruk av DMZ eller proxy**:
   - Direkte tilgang til kritiske system bør unngås. I staden kan ein opprette tilgang via ei **demilitarisert sone (DMZ)** eller ein proxy for betre overvåking og ekstra sikkerheitskontroll.

6. **Sikre "jump-stasjoner"**:
   - Bruk ein mellombels stasjon for fjernbrukarar før dei får tilgang til industrielle einingar. Dette sikrar fysisk separasjon mellom fjernbrukaren sitt utstyr og det industrielle nettverket.

7. **Unngå lagring av tilgangskode på fjerntilkobla utstyr**:
   - Unngå å lagre påloggingsinformasjon på den eksterne enden, til dømes hos ein leverandør, sjølv om informasjonen blir sendt over krypterte kanalar.

8. **Lokal avkopling ved hendingsrespons**:
   - Etabler og test prosedyrar som lar lokalt personale avslutte og kople frå fjernaksess i tilfelle ein sikkerheitshendelse.

9. **Loggføring**:
   - Logg all fjernaksess og aktivitetar i løpet av økta. Dette gir verdifull dokumentasjon for seinare undersøkingar og kan hjelpe sikkerheitsanalytikarar å identifisere potensielle angrep.

Ved å følge desse tiltaka kan ein redusere risikoen som fjernaksess medfører i industrielle nettverk, samstundes som ein opprettheld nødvendige vedlikehalds- og overvåkingstjenester.

### Yting i Industrielle Nettverk: Nøkkelaspekt

For å sikre optimal yting i industrielle nettverk, er det avgjerande å forstå følgande fire komponentar: **latens**, **jitter**, **bandbreidde** og **gjennomstrømming**. Desse faktorane påverkar responsen og stabiliteten til nettverket, noko som er essensielt for sanntidskommunikasjon i industrimiljø.

#### Latens og Jitter
- **Latens**: Tida det tek for ein datapakke å reise frå kjelde til mål, ofte målt som "round-trip" som inkluderer både sendinga og stadfesting frå mottakar. Latens kan variere avhengig av nettverkshoppa mellom einingar, der kvar "hop" mellom einingar (som svitsjar, rutere, og brannmurar) legg til latens.
- **Jitter**: Variasjonen i latens over tid. Jitter kan vere kritisk i sanntidssystem, då store variasjonar kan forstyrre presis synkronisering mellom sensorar og kontrollar. Eit konsistent, men forsinka signal er ofte betre enn eit signal med varierande forsinking.

#### Bandbreidde og Gjennomstrømming
- **Bandbreidde**: Den totale datamengda som kan overførast i løpet av eit gitt tidsrom, målt i Mbps eller Gbps. Industrinettverk krev sjeldan stor bandbreidde, men høgare krav kan oppstå ved hendingar som utløser stor mengde multicast- eller broadcast-trafikk.
- **Gjennomstrømming**: Mengda data som faktisk flyttar seg gjennom nettverket, ofte målt i pakkar per sekund (pps). Høg gjennomstrømming er viktig i sanntidsnettverk, då låg gjennomstrømming kan føre til pakketap, noko som skaper forsinking i TCP/IP og kommunikasjonsfeil i UDP/IP.

#### Quality of Service (QoS)
**QoS** vert brukt til å prioritere kritisk trafikk over mindre viktig trafikk. Dette kan vere avgjerande i industrielle nettverk der sanntidsdata (til dømes mellom PLC og HMI) må prioriterast over annan kommunikasjon. Mekanismar for QoS inkluderer:
- **Class of Service (CoS)**: Angir trafikkprioritet på Layer 2 gjennom 802.1p.
- **Type of Service (ToS)**: Angir trafikkprioritet på Layer 3 gjennom 6-bit ToS-feltet i IPv4.

QoS gjer det mogleg å sikre at viktig trafikk vert levert til rett tid, spesielt når nettverket opplever høg belastning. Dette legg ikkje til meir kapasitet, men QoS prioriterer dei mest kritiske datapakkane.

### Oversikt: Viktige Punkt i Nettverkshandtering i Industrielle System

Industrielle nettverk må optimaliserast for å sikre tidskritisk kommunikasjon og påliteleg kontroll over prosessar. Under er nokre av dei viktigaste vurderingane for å oppretthalde sikkerheit og yting i slike nettverk:

#### 1. Network Hops
- **Effekt på Latens**: Kvart nettverkssteg (hop) mellom einingar bidrar til noko latens. Rutere og sikkerheitseiningar på høgare OSI-lag (lag 4-7) kan auke latensen merkbart samanlikna med switchar på lag 2 eller 3.
- **Optimalisering av Design**: Reduksjon av hops ved å bruke til dømes Layer 3-switchar framfor rutere kan redusere latenstid. Kvar ICS-leverandør har ofte krav til tal på einingar som kan vere i ein segment, då unødvendige hops kan forstyrre systemprestasjonen.

#### 2. Sikkerheitskontrollar i Nettverket
- **Djupt Pakkeinspeksjon (DPI)**: DPI og IDS/IPS gir høg detaljgrad i inspeksjon, men krev meir prosesseringskraft og kan skape ekstra latens. Ein bør derfor tilpasse og justere signaturar etter det aktuelle miljøet, spesielt i OT-miljø utan internettilgang.
  
#### 3. Safety Instrumented Systems (SIS)
- **Formål med SIS**: SIS er designa for å oppdage og avverje farlege tilstandar ved å sette systemet i ein trygg tilstand. Systema opererer med høg pålitelegheit (Safety Integrity Levels, SIL) som strekk seg frå nivå 1 til 4.
- **Sikker Integrering**: SIS bør helst vere isolert frå andre system, men om integrering er nødvendig, anbefalast direkte, punkt-til-punkt-tilkoblingar for å redusere risiko for kompromittering.
  
#### 4. Ytelsesbetraktningar
For å sikre stabil yting i industrielle nettverk er følgande fire komponentar essensielle:
- **Latens**: Forsinka signal kan tolererast i visse samanhengar, men varierande latens (jitter) kan forstyrre sanntidskommunikasjon.
- **Jitter**: Variasjon i latens er meir problematisk enn høg latens åleine då det skaper uforutsigbarhet i systemet.
- **Bandbreidde og Gjennomstrømming**: Forstå forskjellen mellom total datakapabilitet (bandbreidde) og effektiv datamengde som flyttar seg (gjennomstrømming). Kontroller under stress eller høg aktivitet er kritisk for å unngå pakketap.
  
#### 5. Network Services og Remote Access
- **Identitets- og Tilgangskontroll (IAM)**: IAM bør helst vere separert frå forretningsnettverket for å minimere risiko for uautorisert tilgang til OT-ressursar.
- **Fjernaksess**: Fjernaksess bør vere avgrensa til ein einskild veg og sikre kontroller som VPN og to-faktor autentisering bør nyttast. Det er også viktig å logge all fjernaktivitet.

#### 6. Performance og Type of Service (QoS)
- **QoS og Trafikkprioritering**: QoS er kritisk i industrielle nettverk for å prioritere sanntidskommunikasjon og sikre stabilitet ved høg belastning. ToS (Type of Service) på lag 3 og CoS (Class of Service) på lag 2 bidreg til å prioritere og handtere ulike typar nettverkstrafikk.

Desse prinsippa hjelper med å bygge robuste industrielle nettverk som både tilfredsstiller krav til sanntidsoperasjon og opprettheld høg sikkerheit og pålitelegheit i systemet.

### Oppsummering av Viktige Tema i Vidstrakt Nettverkstilkobling og Smart Grid-Sikkerheit

Industrielle system som er spreidde over store område, som fjernstyrte anlegg, oljeplattformar og vindparkar, krev sikre og pålitelege tilkoblingsmetodar for å samhandle med sentrale kontrollrom. Nøkkelpunkta under samanfattar hovudprinsippa og utfordringane i vidstrakt nettverkstilkobling:

#### 1. Vidstrakt Nettverkstilkobling (WAN)
- **Kommunikasjonsteknologiar**: WAN-koplingar kan nyttast gjennom satellitt, mikrobølgje, radio, fiberoptikk og mobilnettverk.
- **Risiko og Sikkerheit**: Desse koplingane er ofte fysisk tilgjengelege og kan trugast ved manuell manipulering eller ved fjernstyrte tilgangspunkt. Sikkerheitstiltak som GPS-spoofing kan manipulere tidskritiske system som smartnett og synkrofaserar, og må vurderast under risikoanalysar.

#### 2. Smart Grid-Sikkerheit
- **Skala og Tilgjenge**: Smartnett gir omfattande tilgang til elektrisitetsinfrastruktur med hundretusenvis eller millionar av noder, som dermed representerer eit betydelig angrepsoverflate.
- **Kostnadspress og Sikkerheit**: Å oppretthalde sikkerheit i så stor skala kan vere utfordrande, og kostnadskutt kan føre til sårbarheit i produksjonsfasen for smarte målarar.
  
#### 3. Advanced Metering Infrastructure (AMI)
- **Komponenter i AMI**: AMI består av smarte målarar, kommunikasjonssystem, og AMI-hovudserver for å samle, lagre og dele data.
- **Sikkerheitsutfordringar**: Smartmålarane er databehandlande einingar med prosessorar og minne, som kan utnyttast til å manipulere data. Denne utbreidde bruken gjer AMI til ei stor angrepsflate som kan samanliknast med Internett.

### Avsluttande Merknad
For å sikre desse nettverka er det kritisk å forstå systemfunksjonaliteten i industrielle kontrollsystem og å følgje grunnleggande prinsipp for sikker nettverksdesign. Vidare studier av industrielle nettverksprotokollar vil støtte integrerte nettverk med høg sikkerheit og robustheit.

#### Spørsmål og Svar
1. **Kva er hovudutfordringane med vidstrakt nettverkstilkobling i industrielle system?**
   - Vidstrakt nettverkstilkobling (WAN) bind saman kontrollrom og fjerntliggjande industriområde gjennom teknologiar som satellitt, mikrobølgje og fiberoptikk. Utfordringane omfattar fysisk tilgjenge for ukjende brukarar og risiko for manipulasjon gjennom teknikkar som GPS-spoofing.

2. **Korleis påverkar GPS-spoofing industrielle system?**
   - GPS-spoofing kan manipulere tidssensitive system som synkrofaserar i smartnett og føre til avvik i tidsdata, som igjen kan påverke stabiliteten i straumnettet eller andre prosesskontrollsystem.

3. **Kva er smartnett, og kvifor treng det spesielle sikkerheitsvurderingar?**
   - Smartnett er eit omfattande system som integrerer avansert måleteknologi og kommunikasjon for styring og distribusjon av energi. På grunn av sitt store omfang og mange tilkoblingar representerer det eit stort angrepsflate, som krev ekstra sikkerheitskontrollar.

4. **Kva er Advanced Metering Infrastructure (AMI), og kva for sikkerheitsutfordringar kjem med det?**
   - AMI består av smarte målarar, kommunikasjon, og eit hovudsystem for å samle og administrere måledata. Utfordringar inkluderer risiko for utnytting av smarte målarar som har prosessorar og kan manipulere data.

5. **Korleis kan sikkerheit sikrast i eit vidstrekt smartnett?**
   - Sikkerheit i smartnett kan styrkast ved segmentering av nettverket og kontroll av tilgangen mellom ulike nodar. Det er òg viktig å sikre både fysisk tilkomst og å implementere avanserte deteksjonssystem for å overvake uvanleg aktivitet.

6. **Kva er hovudkomponentane i eit smartnett?**
   - Eit smartnett består av smarte målarar, kommunikasjonsnettverk, og eit administrasjonssystem. Desse komponentane samhandlar med mange andre system, som energistyringssystem og ICS-serverar, noko som krev avansert sikkerheitsstyring.

7. **Kva er "prinsippet om minst mogleg rute," og kvifor er det viktig i industriell nettverksdesign?**
   - Prinsippet om minst mogleg rute handlar om å gje eit system tilgang berre til dei nettverksressursane som er nødvendige for funksjonen det skal utføre. Dette minskar risikoen for uønskt tilgang og styrkjer det overordna sikkerheitsnivået.

8. **Kvifor kan AMI vere meir sårbar samanlikna med andre industrielle nettverk?**
   - AMI er svært tilgjengeleg, og dei store kostnadane knytt til produksjon og distribusjon av smarte målarar kan føre til sårbarheiter. Sidan målarane opererer i eit så stort omfang, er det ein betydelig risiko for feil og angrep som kan påverke store delar av infrastrukturen.

9. **Kva rolle speler distribuerte system som synkrofaserar i smartnett?**
   - Synkrofaserar overvakar spenning og straum på tvers av eit stort område og sikrar synkronisert drift i energinettet. Dei er avhengige av GPS-timing, og GPS-spoofing kan føre til feil i synkroniseringa, noko som kan påverke stabiliteten til nettet.

10. **Kva sikkerheitstiltak kan redusere risikoen for utnytting av vidstrakte nettverkstilkoblingar?**
    - Tiltak inkluderer å sikre fysiske tilkoplingspunkt, implementere kryptering og autentisering, og å bruke avanserte deteksjonssystem som kan overvake og reagere på uvanleg aktivitet i systemet.
