**Kapittel 2: Om industrielle nettverk**

### Bruken av Terminologi i Denne Boka
- Ulike faguttrykk er sentrale både innan industriell nettverkssikkerheit og industrielle kontrollsystem. Boka vil forklare grunnleggjande omgreper for begge fagområda for å betre kommunikasjon mellom eksperter på cyber-sikkerheit og industrisystem-profesjonelle.
- Viktige uttrykk:
  - **Aktiv**: fysisk eller logisk komponent (t.d. cyber-aktiva, kritiske aktiva)
  - **Enklavar, soner og konduitar**
  - **Forretningsnettverk**
  - **Industrielle kontrollsystem**: DCS, PCS, SIS, SCADA
  - **Industrielle nettverk og protokollar**
  - **Elektronisk sikkerheitsperimeter (ESP)**
  - **Kritisk infrastruktur**
  - Sentrale cyber-sikkerheitsuttrykk: **angrep**, **brudd**, **hendelsar**, **sårbarheiter**, **risiko**, og **sikkerheitstiltak**.

### Vanlege industrielle sikkerheitsråd
- Før sikring av industrielle nettverk bør ein forstå grunnleggjande strukturar og prinsipp for korleis industrielle nettverk er arkitekterte.
- Nokre anbefalingar frå forretningsnettverk kan vere uegna i ein industriell samanheng. Det er viktig å vurdere tilpassa sikkerheitstiltak for å sikre effektive industrinettverk.

### Avanserte sikkerheitsråd for industri
- Vidare enn dei vanlege anbefalingane inneber avansert sikkerheit for industrinettverk ei vurdering av unike risikoar og tiltak knytt til spesifikke komponentar og system (t.d. SCADA og Smart Grid).
- Terminologi som **kritiske cyber-aktiva** vert her handsama i eit breiare perspektiv, der både individuelle og system-baserte tilnærmingar vert omfatta for betre sikkerheitskontroll.

### Vanlege misoppfatningar om industriell nettverkssikkerheit
- Industrielle nettverk har varierande storleik, kompleksitet og risiko, men byggjer ofte på dei same teknologiane og prinsippa.
- Forskjellige sektorar, som Smart Grid, raffinering, og kommersielle bygg, har eigne utfordringar, men også overlappande sikkerheitsbehov.
- Industrielle kontrollsystem (ICS) representerer kun ein del av eit større system, der feltbusnettverk, prosesskontrollnettverk, forretningsnettverk og fjernstyringsnettverk alle bidreg til å skape eit samansett, men kritisk infrastruktur.

**Sikkerheitskontroller og mottiltak**

### Sikkerheitskontroller og mottiltak
- **Sikkerheitskontroller** og **mottiltak** refererer til metodar for å gjennomføre cyber-sikkerheit, til dømes via produkt, teknologi, plan, eller policy for å redusere risiko.

### Brannmurar og Inntrengingsførebyggjande System (IPS)
- **Brannmurar**:
  - Grunnleggjande brannmurar kan filtrere trafikk i éi retning basert på kriterium som IP-adresse eller port.
  - Meir avanserte brannmurar kan overvake heile applikasjonssessjonar, analysere innhaldet i pakkar, og utføre komplekse filterreglar. Unified Threat Management (UTM) einingar kombinerer fleire funksjonar for å beskytte mot avanserte truslar.

- **Deep Packet Inspection (DPI)**:
  - DPI dekodar og analyserer innhaldet i nettverkstrafikk. Brukast ofte i Intrusion Detection Systems (IDS) og Intrusion Prevention Systems (IPS).
  
- **Intrusion Detection System (IDS)** vs. **Intrusion Prevention System (IPS)**:
  - IDS overvakar og alarmerer, men blokkerer ikkje trafikk.
  - IPS kan blokkere trafikk og er ofte sett opp der tilgjengelegheit ikkje er kritisk. IPS kan brukast som IDS ved å konfigurere for å berre varsle om truslar utan å blokkere.

### Industrielt kontrollsystem (ICS)
- **Industrielle kontrollsystem (ICS)** er eit breitt spekter av system som gir kontroll og overvåking i industrielle miljø.
- ICS omfattar ulike systemtypar som Prosesskontrollsystem (PCS), Distribuert kontrollsystem (DCS), SCADA, og Sikkerheitsinstrumenterte system (SIS).
- ICS inneheld typisk verktøy for prosesslogikk og brukergrensesnitt (HMI) for å overvake og kontrollere prosessen.

**DCS eller SCADA?**

- **Opprinnelig forskjell**: DCS og SCADA hadde tidlegare klart skilte arkitekturar, men desse grensene har blitt mindre tydelege med teknologiutviklinga. Begge systema er laga for å overvåke og kontrollere industrielt utstyr.
- **Funksjonar**:
  - **Overvåking**: Leser data og viser informasjon til operatørar og andre applikasjonar, som "historian"-system og avanserte kontrollprogram.
  - **Kontroll**: Set parameterar og utfører instruksjonar for å drive prosessen.
  - **Arbeidsstasjonar**: Kan vere brukt berre til overvåking, til å justere prosesslogikk, eller som grensesnitt (HMI) for meir aktiv kontroll.
- **Misforståing**: ICS blir ofte omtala som SCADA, men ikkje alle ICS-system er SCADA-system.

**Industrielle Nettverk**

- Eit ICS er ofte kopla saman som ein del av eit større nettverk som inkluderer kontrollutstyr, felles applikasjonar og område-spesifikke feltutstyr.
- Arkitekturen involverer lokal og sentralisert overvåking og kontroll. Spesialiserte system i ICS er kopla saman til eit **Industrielt Nettverk** som muliggjør kommunikasjon mellom komponentane.

**Industrielle Protokollar**

- ICS brukar ofte spesialiserte protokollar, som kan vere **leverandør-spesifikke** (t.d. Honeywell CDA, GE SRTP, Siemens S7) eller **offentlege/lisensierte** (t.d. OPC, Modbus, DNP3, CIP, PROFIBUS).
- Fleire av desse protokollane er tilpassa for Ethernet-nettverk og brukar Internett-protokoll (IP) med både UDP og TCP.
- **Sikkerheitsutfordringar**: Protokollane var ikkje opprinneleg laga med cyber-sikkerheit i tankane og kan vere sårbare for angrep.

**Nettverk, Routable og Nonroutable Nettverk**

- **Nonroutable Nettverk**: Tradisjonelt seriell kommunikasjon som Modbus/RTU, DNP3, og fieldbus-nettverk. Dei forbinder enheter, gir kommunikasjon og mogleggjer fjerntilgong og kontroll, men har ingen IP-basert routing.
- **Routable Nettverk**: Nettverk som bruker Internet Protocol (IP), til dømes TCP/IP eller UDP/IP. Eldre ICS-protokollar er også tilpassa IP, som Modbus/TCP og DNP3 over TCP/UDP.
- **Interaksjon og sårbarheit**: Routable og nonroutable nettverk overlappar ofte ved grensa mellom kontroll- og tilsynsnivå, noko som krever spesifikk cyber-sikkerheit. Nonroutable nettverk blir ofte feilaktig sett på som tryggare, men i praksis er mange like sårbare gjennom tilknytte IP-baserte system eller fjernaksess (t.d. via modem eller trådlause system).

**Forretningsnettverk (Enterprise Network)**

- **Forretningsnettverk og ICS**: Industrielle kontrollsystem (ICS) er sjeldan isolerte. Dei er typisk knytta saman med forretningsnettverk som støttar bedriftsfunksjonar som produksjonsplanlegging, lagerstyring og vedlikehald.
- **Funksjonell Samankobling**: Industrielle nettverk og forretningsnettverk dannar saman ei ende-til-ende løysing, som kan inkludere redundans og robuste industrielle komponentar.
- **Delte Tenester**: Nokre system og tenester kan eksistere i både forretnings- og industrielle nettverk, som katalogtenester og databasar. Det er anbefalt å replikere slike system i begge miljø for å redusere potensielle angrepsflater.

Dette kapitlet legg ikkje vekt på forretningsnettverk utanom korleis dei kan fungere som ein angrepsvektor mot ICS.

FORTSETT FRÅ ZONES AND ENCLAVES s22