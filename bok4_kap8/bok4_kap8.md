### Notat: Kapittel 8 - Risikovurdering og sårbarheitsvurderingar

---

### Cyber Security and Risk Management
Sikkerheit handlar om korleis ein organisasjon forstår og handterer risiko. Risiko kan oppstå i ulike delar av verksemda, inkludert IT-infrastruktur, automasjon og kontrollsystem, og fysiske eigedomar. Hovudmålet med å implementere cybersikkerheitskontrollar er å redusere risiko, men effektiviteten av desse kontrollane avheng av organisasjonen sin risikooppfatning og -toleranse.

For å sikre ICS (Industrial Control System) med ein avgrensa mengde ressursar, må organisasjonen forstå kva som utgjer ein akseptabel risiko. Risikotoleransen kan handterast på fire måtar:
1. **Mitigasjon:** Organisasjonen reduserer risikoen direkte.
2. **Transferal:** Andre aktørar handterer risikoen (f.eks. gjennom forsikring).
3. **Unngåing:** Risikable aktivitetar vert eliminert.
4. **Aksept:** Risikotoleransen vert definert av interessentane.

Risikoen må kontinuerleg vurderast og responderast på, spesielt sidan risikolandskapet stadig endrar seg. 

---

### Methodologies for Assessing Risk within Industrial Control Systems
Risikoanalysen startar med å etablere ein risiko- og sårbarheitsvurderingsprosess som er spesialtilpassa industrielle system. Fleire metodologiar eksisterer, som å analysere truslane, kartlegge sårbarheitene og gjennomføre ei vurdering av eksponering for å setje inn relevante sikkerheitskontrollar.

---

### System Characterization
Kartlegging av systemet er avgjerande for å forstå kva som er verna og kor truslar kan påverke. Dette inneber å dokumentere:
- Systemfunksjonar
- Bruk av teknologi og protokollar
- Fysiske eigenskapar og netverkstilkoblingar
Denne informasjonen danner grunnlaget for å identifisere moglegheiter for truslar og sårbarheiter.

---

### Threat Identification
Truslar kan vere både interne og eksterne, med intensjonelle eller utilsikta motiv. Eksemplar på truslar inkluderer:
- Eksterne aktørar som hackergrupper eller statlege aktørar
- Interne tilsette eller tredjepart som kan utføre handlingar ved eit uhell eller med vilje
- Fleire rapportar peiker på at mange truslar kjem frå interne aktørar, og at sårbarheiter ofte utnyttast ved tilfeldige feil.

---

### Vulnerability Identification
Identifisering av sårbarheiter avdekkjer svakheiter som kan utnyttast av truslar. I industrielle system kan dette omfatte både nettverksbaserte og programvarerelaterte sårbarheiter, men også dei som oppstår gjennom mangelfull praksis i tilknyting til oppdateringar og vedlikehald.

---

### Risk Classification and Ranking
Risikovurderinga prioriterer truslar og sårbarheiter basert på sannsynet for at dei skjer, samt potensialet for skade. Denne prioriteringa gjer det mogleg å bestemme kva sikkerheitstiltak som vil ha størst effekt på å redusere risikoen innanfor budsjett og tidsramme.

---

### Risk Reduction and Mitigation
Risikoen reduserast ved å tilpasse sikkerheitskontrollar som tar direkte sikte på prioriterte truslar og sårbarheiter. Dette kan omfatte tiltak som å oppgradere brannmurar, implementere anti-virus-programvare, sikre tilgangskontrollar, og utvikle prosedyrar for patch- og oppdateringshandtering.

---

### Kva er risiko?
ISO definerer risiko som ein "potensiell trussel som kan utnytte sårbarheiter ved ein ressurs og påføre skade på organisasjonen." Definisjonen inneheld tre hovudelement:
- **Trusselsannsyn**: Sannsynet for at ein trusselepisode skal inntreffe.
- **Sårbarheit**: Ein svakheit som kan utnyttast av ein trussel.
- **Konsekvensar**: Potensielle konsekvensar som påverkar ressursen sin drift.

#### Reduksjon av risiko
Risiko kan reduserast ved å fjerne sårbarheiter (f.eks. med programvareoppdateringar) eller ved å avgrense skaden etter eit angrep (f.eks. gjennom segmentering av nettverket eller å setje opp sikkerheitssoner). 

---

### Trusselvurdering
Eit trussel kan definerast som ein kombinasjon av følgjande:
- **Trusselkilde eller aktør**: Den som utfører trusselen (f.eks. ein hacktivist, insider, eller ein statleg aktør).
- **Trusselvektor**: Metoden eller vegen trusselen følgjer (t.d. eit infisert USB-port eller ein opna nettverksport).
- **Trusselmål**: Ressursen eller systemet som vert angripe.

Ved å avgrense nokon av desse faktorane kan risikoen reduserast. Eit eksempel på dette kan vere å deaktivere ubrukt nettverkstenester på ein ICS-kontroller for å redusere mogelege angrepsvektorar.

---

### Trusselaktørar og deira eigenskapar
Ein trusselaktør treng tre hovudeigenskapar for å kunne utføre eit cyberangrep:
1. **Kompetanse** til å utføre angrepet.
2. **Intensjon** om å skade.
3. **Mogelegheit** til å starte angrepet.

Det finst mange verktøy tilgjengelege, både open-kjelde og kommersielle, som gjer det mogeleg for aktørar med lite erfaring å angripe ICS. Samtidig er det vanskelegare å kontrollere utanforståande aktørar enn interne.

---

### Sårbarheiter
Sårbarheiter kan vere kjende og uoppdaga, og representerer ein vesentleg risiko i industrielle nettverk. Ei kartlegging i 2014 viste at meir enn 80 % av kjende sårbarheiter i ICS-komponentar hadde blitt oppdaga etter Stuxnet-angrepet i 2010. Denne sårbarheitskartlegginga held fram i fagmiljø og på konferansar som Black Hat og DEFCON.

---

### Konsekvensar av angrep
Konsekvensar av cyberangrep kan vere omfattande. Eit kjent eksempel er Target-brekket i 2013 som fekk omfattande økonomiske konsekvensar. I ICS-samanheng kan konsekvensane omfatte:
- Driftstans og forringing av produktkvalitet
- Mekanisk skade på utstyr
- Hendingar med fare for utvida miljø- og helseskade

Konsekvensane for ICS strekker seg vidare enn systemet sjølv og påverkar heile drifta og tryggleiken til menneska og miljøet rundt.
