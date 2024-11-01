### 21 Profinet IRT

#### 21.1 Introduction
- **PROFINET** (PROcess FIeld NETwork) er ein open standard for industriell Ethernet, med utstrakt bruk i prosessautomatisering, produksjonsautomatisering, bilindustri, maskinindustri, og drivkontroll.
- Standardisert under **IEC 61158** og **IEC 61784**, medan sikkerheitskrav vert dekte av **IEC 62061/ISO 13849-1**.
- PROFINET har tre ytelsesklassar basert på tidskrav:
  - **NRT** (non-real time)
  - **RT** (real time)
  - **IRT** (isochronous real time), som er tilpassa bevegelseskontroll og applikasjonar med syklustider under 1 ms.
- Høgprioritetsdata sendast via Ethernet-rammer med **VLAN-prioritering**. Syklustider kan optimerast med dynamisk rammepakking (DFP) og tidsmultipleksert modus med synkroniserte svitsjar.

#### 21.2 Features
- **Kommunikasjonsnivå** frå høgare systemnivå ned til felt- og einingsnivå.
- **Fleksible topologiar** som stjerne- og linjestruktur.
- **Fleksibel sanntidskommunikasjon** med IRT som inkluderer isochronous motion control.
- **Dynamisk rammepakking** for å oppnå korte syklustider.
- **Støtte for fleire overføringsmedia**, inkludert kopar, fiberoptikk og trådlause løysingar.
- **Sømlaus integrasjon av feltbusar** og høg sikkerheit for å forhindre uautorisert tilgang.
- **Påliteleg diagnosesystem** for sikker drift og feilhandsaming. 

PROFINET IRT er utvikla av Siemens og PNO for krevjande industrielle applikasjonar som krev sanntidskommunikasjon.

### 21.3 Conformance Classes
PROFINET har tre konformitetsklassar for ulike automasjonskrav:
- **CC-A**: Grunnleggjande funksjonar for PROFINET I/O og RT-kommunikasjon.
- **CC-B**: Inkluderer funksjonar for nettverksdiagnostikk og topologi. Støttar deterministisk kommunikasjon, men ikkje isokron.
- **CC-C**: Har alle funksjonane i CC-A og CC-B, med høgdeterministisk kommunikasjon gjennom isokron fase. Nyttast i maskinkontroll.

### 21.4 Real-Time Communication – Hard and Soft Real Time
PROFINET skil mellom:
- **NRT** (non-real time): Bruker TCP/IP eller UDP/IP for ikkje-tidskritiske applikasjonar.
- **RT** (real time): Overfører I/O-data via Ethernet-protokollen, med syklustid rundt 10 ms.
- **IRT** (isochronous real time): Kritisk for applikasjonar med syklustid under 1 ms og jitter på 1 µs, til dømes i bevegelseskontroll.

Forskjellen mellom hard og soft real-time er kor strengt tidskrava vert haldne. Hard real-time system krev at meldingar blir overførte innanfor ei spesifisert tidsramme.
Hard real-time systems operate on synchronized clocks to reduce cycle
time and jitter and provide deterministic behavior. 

### 21.5 Realization of Faster Operation
- **PROFINET** er ein open protokoll med kort syklustid (31.25 µs) og svært låg jitter (<1 µs) i IRT-versjonen.
- **Summation frame method**: Samlar data frå fleire noder i éi ramme, med kun éin FCS, noko som aukar gjennomstrøyminga og reduserer syklustid.
- **Full duplex-modus**: Sendar både input- og output-data på same kabel for raskare datalevering til siste node.
- PROFINET V2.3 støttar uavgrensa TCP/IP-kommunikasjon ved fragmentering av store TCP/IP-rammer, som deretter samlast i mottakarens applikasjonslag.

### 21.6 Working of IRT
- IRT bruker **time slice-mechanism**, der nettverkstid delast mellom IRT- og RT-trafikk. Vanlegvis er 25 % av bandbreidda reservert til IRT.
- **Presise tidslott** oppnåast ved:
  1. Ein nøyaktig masterklokke (IEEE 1588v2 PTP) som synkroniserer alle einingar.
  2. Switchar med bufferminne som handterer Ethernet-trafikk under IRT-fasen.

  ### 21.5 Realization of Faster Operation
- **Syklustid og jitter**: PROFINET IRT (Isochronous Real-Time) er optimalisert for høgfrekvente applikasjonar med syklustid heilt ned til 31.25 µs og ein jitter på under 1 µs. Dette er spesielt nyttig i applikasjonar som krev høg determinisme, som robotikk og bevegelseskontroll.
  
- **Frame ID og rask vidareføring**: I PROFINET V2.3 vert adressa til eininga lagt inn i rammehovudet når data skal sendast gjennom ein integrert switch. Dette gjer at switchen kan gjenkjenne ramma og sende den vidare raskt utan å måtte handsame adressa på nytt, noko som reduserer forsinkingar med fleire mikrosekund.

- **Summation Frame Method**: Ein effektiv metode for rask dataoverføring ved å kombinere data frå fleire noder i éi enkelt Ethernet-ramme. Dette reduserer behovet for fleire FCS (Frame Check Sequence)-sjekkar, sidan det berre er éin FCS for heile ramma, noko som aukar gjennomstrøyminga. Denne metoden er spesielt effektiv når noder berre har små mengder I/O-data.

- **Full Duplex System**: PROFINET bruker ein full duplex-modus der både input- og output-data kan sendast samstundes gjennom to-par kabelen. Når ei summation frame blir sendt, sjekka og analysert for kvar node, vert data som allereie er handsama av tidlegare noder fjerna frå ramma. Dette gjer at ramma blir kortare etter kvart som ho går vidare, noko som reduserer syklustida ytterlegare.

- **Fragmentert TCP/IP-kommunikasjon**: PROFINET V2.3 kan handtere store TCP/IP-rammer ved å dele dei opp i mindre fragment som sendast sekvensielt. I mottakaren vert dei opphavlege rammedelane sette saman igjen i applikasjonslaget. Dette gjer det mogleg å kombinere I/O- og TCP/IP-kommunikasjon i same syklustid på 31.25 µs utan behov for spesialutstyr.

### 21.6 Working of IRT
- **Time Slice Mechanism**: IRT bruker ein tidsskjema-basert mekanisme der trafikken på nettverket er delt inn i tidsslot der både IRT- og RT-trafikk har sin plass. Typisk er 25 % av den totale nettverkskapasiteten reservert for IRT-trafikk, medan dei resterande 75 % kan nyttast til RT-trafikk. Dette tidsskjemaet gir IRT-trafikk faste intervall for datalevering, noko som gir høg determinisme og nøyaktig tidsstyring.

- **Buffering av ikkje-IRT-trafikk**: Når ein tidsslot er reservert for IRT-trafikk, vert all ikkje-IRT-trafikk (som RT- eller NRT-data) bufra til tidsslotet for IRT-trafikken er over. Deretter slepp bufra trafikk gjennom ved hjelp av vanleg Ethernet-kommunikasjon, noko som sikrar at kritisk IRT-data alltid har prioritet og minimal ventetid.

- **Tidsnøyaktig synkronisering**:
  1. **Masterklokke**: For å oppnå svært presise tidsslot, krev PROFINET IRT ein masterklokke basert på IEEE 1588v2 (Precision Time Protocol, PTP). Denne synkroniserer alle tilknytte einingar på nettverket for å sikre nøyaktige og identiske tidsslot på tvers av einingar. PROFINET bruker ein variant av PTP kalla Precision Transparent Clock Protocol (PTCP) for å rekne ut forsinkingar i kabling og switchar, noko som gjer at klokka kan justerast nøyaktig etter behov.
  
  2. **Switchar med bufferminne**: For å sikre at IRT-data ikkje vert påverka av annan trafikk, må switchane ha eigne bufferminne for å halde tilbake ikkje-IRT-trafikk under IRT-fasen. Denne buffringa gjer at switchane berre slepp gjennom IRT-trafikk i dei tildelte tidsslotene og sikrar dermed kontinuerleg IRT-kommunikasjon utan forstyrringar.

- **Dataflyt og prioritering**: PROFINET IRT bruker VLAN-tagg med høg prioritet (nivå 6) for å sikre at IRT-telegram har forrang i switchane. RT- og IRT-kommunikasjon bypassar nokre OSI-lag for raskare handsaming, noko som reduserer dataleveringstida i sanntidsapplikasjonar ytterlegare.

Denne detaljerte mekanismen for tidssynkronisering og prioritering gjer at PROFINET IRT kan handtere svært krevjande sanntidskommunikasjon i industrimiljø med høg presisjon og låg ventetid.

### 21.7 Time Sensitive Networking (TSN)
- **TSN** er eit sett av standardar som aukar determinismen i Ethernet-nettverk, noko som er essensielt for sanntidsapplikasjonar i industrien. TSN har fokus på Quality of Service (QoS), låg latens og parallell overføring av ulike protokollar i sanntidsnettverk.
- TSN gir syklustid på 31.25 µs og jitter på 1 µs, liknande PROFINET IRT, men har lagt til nye funksjonar som 802.1AS-2019 for meir presis tidssynkronisering og prioritert tidsplanlegging.
- TSN integrerer lag 1, 2 og 3 i OSI-modellen for å auke skalerbarheit og yting i nettverket.

### 21.8 Using IRT
- **Konformitetskrav**: Alle einingar i PROFINET IRT-nettverk må støtte konformitetsklasse C for å sikre sanntidskommunikasjon med dataoppdateringar ned til 31.25 µs og jitter under 1 µs.
- **Konfigurasjon**: PROFINET IRT må konfigurerast nøyaktig for å fastsette talet på tidslot som trengst til IRT-trafikk. Dette inkluderer å spesifisere nettverkstopologi og tidskrav for kvar eining.
- **Isochrone Mode Application**: Nokre einingar støttar ein modus som sikrar at applikasjonen sin oppdateringssyklus er synkronisert med IRT-oppdateringsintervallet. Dette sikrar at prøvetakinga ikkje vert over- eller underestimert.

PROFINET IRT brukar eit tidsstyrt skjema der kvart syklus startar med synkronisering. IRT-data blir sendt i reserverte tidslot, etterfølgt av RT-kommunikasjon.

### Oppsummering av Kapittel 21: Profinet IRT

1. **Introduksjon til Profinet IRT**  
   PROFINET (PROcess FIeld NETwork) er ein open Ethernet-standard brukt i industriell automasjon, med støtte for sanntidskommunikasjon på fleire nivå. Det er tre hovudklassar for ytelse: 
   - **NRT** (non-real time) 
   - **RT** (real time)
   - **IRT** (isochronous real time), som er viktig for applikasjonar med syklustider under 1 ms.

2. **Funksjonar**  
   PROFINET IRT tilbyr fleksibel kommunikasjon, støtte for ulike nettverkstopologiar, høg sikkerheit, diagnostiske funksjonar og rask sanntidskommunikasjon. Det brukar VLAN-prioritering og dynamisk rammepakking for optimalisert datalevering.

3. **Konformitetsklassar (CC)**  
   PROFINET har tre konformitetsklassar: 
   - **CC-A**: Grunnleggjande funksjonar.
   - **CC-B**: Støtte for nettverksdiagnostikk og redundans.
   - **CC-C**: Høgdeterministisk sanntidskommunikasjon for kritiske applikasjonar.

4. **Real-Time Communication – Hard og Soft Real Time**  
   PROFINET IRT nyttar VLAN-tagg og tidsslot for å sikre deterministisk kommunikasjon. Hard real-time krev at data blir sendt innan spesifikke tidsrammer, medan soft real-time tillét små avvik.

5. **Realization of Faster Operation**  
   PROFINET V2.3 brukar metodar som **Summation Frame** for å samle data frå fleire noder i ei ramme, og **full duplex**-modus for raskare dataoverføring. Dette reduserer syklustid og aukar gjennomstrøyminga.

6. **Time Slice Mechanism**  
   PROFINET IRT brukar tidsdelingsmekanismar for å prioritere IRT-trafikk. IRT-trafikk blir sendt i reserverte tidslot, medan annan trafikk blir bufra til IRT-fasen er over. Ein nøyaktig **masterklokke** synkroniserer alle einingar i nettverket.

7. **Time Sensitive Networking (TSN)**  
   TSN-standarden aukar determinismen i Ethernet og er kompatibel med PROFINET. TSN støttar svært nøyaktig tidssynkronisering og QoS, og gir betre skalering og yting for sanntidsapplikasjonar.

8. **Bruk av IRT**  
   Alle einingar i PROFINET IRT-nettverk må støtte konformitetsklasse C for sanntidskrav. Nøyaktig konfigurasjon er nødvendig for å fastsette tidslot for IRT-trafikk, og **Isochrone Mode** kan brukast for å synkronisere applikasjonssyklus med IRT-oppdatering.

Denne oppsummeringa dekker hovudfunksjonane og eigenskapane i PROFINET IRT for sanntidsindustrielle nettverk.

Her er ei punktvis forklaring av dei viktigaste omgrepa og forkortingane brukt i kapittel 21:

- **PROFINET**: PROcess FIeld NETwork, ein Ethernet-basert kommunikasjonsstandard for industriell automasjon.

- **IRT (Isochronous Real Time)**: PROFINET-modus for ekstremt låg syklustid (<1 ms) og høg determinisme, brukt til tidskritiske applikasjonar som bevegelseskontroll.

- **RT (Real Time)**: Sanntidskommunikasjon med mindre strenge krav enn IRT. Typisk syklustid på rundt 10 ms.

- **NRT (Non-Real Time)**: Ikkje-tidskritisk kommunikasjon som kan handtere mindre kritiske dataoverføringar.

- **CC-A, CC-B, CC-C**: Konformitetsklassar i PROFINET som definerer funksjonsnivå. 
  - **CC-A** er grunnleggjande funksjonar, 
  - **CC-B** inkluderer diagnostikk og redundans, 
  - **CC-C** støttar høgdeterministisk sanntid med IRT.

- **VLAN (Virtual Local Area Network)**: Teknologi for å prioritere trafikk ved å dele opp eit fysisk nettverk i fleire virtuelle nettverk. VLAN-prioritering vert brukt i PROFINET for å prioritere IRT-trafikk.

- **QoS (Quality of Service)**: Mekanismar som sikrar prioritering av viktige datapakkar for å oppretthalde høg kvalitet på sanntidstenester.

- **FCS (Frame Check Sequence)**: Feilsjekk i Ethernet-rammer som sikrar at data ikkje er korrupt. 

- **Summation Frame Method**: Metode der fleire nodar sine data blir samla i ei enkelt ramme med ein FCS, noko som aukar effektiviteten.

- **Time Slice Mechanism**: Tidsdeling brukt i PROFINET for å sikre at IRT-trafikk får faste intervall (tidslot) for prioritet i overføringa.

- **PTP (Precision Time Protocol)**: Standard for tidssynkronisering i nettverk, brukt i PROFINET for nøyaktig synkronisering av alle einingar.

- **TSN (Time Sensitive Networking)**: Ei samling av standardar som aukar determinismen og redusert forsinking i Ethernet-nettverk, kompatibel med PROFINET for sanntidsapplikasjonar.

- **IEEE 1588v2**: Versjon av PTP som gir høg presisjon i tidssynkronisering over nettverk, brukt i PROFINET IRT.

- **Isochrone Mode Application**: Modus som låser applikasjonens syklus til PROFINET IRT sitt oppdateringsintervall, slik at dataprøvetaking skjer på presise intervall.

### QnA

**Spørsmål 1:**  
*Kva er PROFINET, og kva er hovudbruksområda?*

**Svar:**  
PROFINET (PROcess FIeld NETwork) er ein Ethernet-basert kommunikasjonsstandard for industriell automasjon, brukt i prosess- og produksjonsautomatisering, bilindustri, maskinindustri og drivkontroll.

---

**Spørsmål 2:**  
*Kva er forskjellen mellom NRT, RT og IRT i PROFINET?*

**Svar:**  
- **NRT (Non-Real Time):** Ikkje-tidskritisk kommunikasjon for mindre viktige data.
- **RT (Real Time):** Sanntidskommunikasjon for meir tidssensitive applikasjonar, med typisk syklustid rundt 10 ms.
- **IRT (Isochronous Real Time):** Ekstremt tidskritisk kommunikasjon med syklustid under 1 ms og låg jitter, brukt i bevegelseskontroll og andre kritiske applikasjonar.

---

**Spørsmål 3:**  
*Kva er hovudfunksjonen til VLAN i PROFINET IRT?*

**Svar:**  
VLAN (Virtual Local Area Network) blir brukt for å prioritere IRT-trafikk, slik at tidskritiske data kan få forrang i nettverket, og sikre påliteleg sanntidskommunikasjon.

---

**Spørsmål 4:**  
*Kva er Summation Frame Method, og kvifor er den viktig?*

**Svar:**  
Summation Frame Method samlar data frå fleire noder i ei enkelt ramme med berre éin FCS-sjekk. Dette aukar effektiviteten og reduserer syklustid ved å redusere mengda av kontrollsjekkar som krevjast.

---

**Spørsmål 5:**  
*Kva er Time Slice Mechanism, og korleis fungerer det i PROFINET IRT?*

**Svar:**  
Time Slice Mechanism deler opp tid i faste slot (tidsperiodar) for å prioritere IRT-trafikk. IRT-trafikk blir sendt i desse reserverte tidslot, medan all annan trafikk (som RT) vert bufra og sendt etterpå. Dette sikrar determinisme og forutsigbar datalevering.

---

**Spørsmål 6:**  
*Kva funksjon har Precision Time Protocol (PTP) i PROFINET IRT?*

**Svar:**  
PTP (Precision Time Protocol) sørgjer for nøyaktig synkronisering mellom alle einingar i nettverket. PROFINET IRT brukar PTP-varianten IEEE 1588v2 for å oppnå svært presise tidsslot, noko som er kritisk for IRT-kommunikasjon.

---

**Spørsmål 7:**  
*Kva er Time Sensitive Networking (TSN), og korleis relaterer det til PROFINET?*

**Svar:**  
TSN (Time Sensitive Networking) er eit sett av standardar for å auke determinismen i Ethernet-nettverk. TSN støttar presis tidssynkronisering og QoS-funksjonar, og det er kompatibelt med PROFINET for sanntidsapplikasjonar i industrien.

---

**Spørsmål 8:**  
*Kva er dei tre konformitetsklassane i PROFINET, og kva funksjonar tilbyr dei?*

**Svar:**  
- **CC-A:** Grunnleggjande funksjonar for PROFINET I/O og enkel sanntidskommunikasjon.
- **CC-B:** Støtte for nettverksdiagnostikk og redundans.
- **CC-C:** Full støtte for høgdeterministisk sanntid med IRT, brukt i applikasjonar som krev isokron fase.

---

**Spørsmål 9:**  
*Kva er Isochrone Mode Application i PROFINET IRT?*

**Svar:**  
Isochrone Mode Application er ein modus som synkroniserer applikasjonens oppdateringssyklus med PROFINET IRT sitt oppdateringsintervall. Dette sikrar at dataprøvetaking skjer på presise tidspunkter, og forhindrar feil i datainnsamling.

---

**Spørsmål 10:**  
*Korleis bidrar PROFINET IRT til å oppnå høg determinisme i sanntidsnettverk?*

**Svar:**  
PROFINET IRT oppnår høg determinisme gjennom Time Slice Mechanism, VLAN-prioritering, og PTP-synkronisering, som til saman gir presise tidsintervall for datalevering og minimal ventetid i tidskritiske applikasjonar.
