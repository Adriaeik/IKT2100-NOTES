### Transportlaget i nettverk**
#### **Oversikt**
Transportlaget i nettverk fungerer som bindeledd mellom applikasjonslaget og nettverkslaget, og tilbyr mekanismar for ende-til-ende-kommunikasjon mellom applikasjonar. Dette inkluderer:
- Multiplexing og demultiplexing
- Påliteleg dataoverføring
- Strøymekontroll
- Overlastkontroll

#### **Transportprotokollar**
1. **UDP (User Datagram Protocol):**
   - Lettvekts, forbindingslaus protokoll.
   - Gir ikkje påliteleg levering, men er rask og brukar lite ressursar.
   - Brukar for applikasjonar som toler tap (t.d. video-strøyming).

2. **TCP (Transmission Control Protocol):**
   - Tilbyr påliteleg og ordna dataoverføring.
   - Mekanismer for:
     - Strøymekontroll
     - Overlastkontroll
     - Oppsett og avslutning av samband

#### **Konsept og prinsipp**
1. **Multiplexing og demultiplexing:**
   - Brukar portnummer for å sikre korrekt overføring mellom applikasjonar.
2. **Påliteleg dataoverføring:**
   - Byggjer på mekanismar som kvittering (acknowledgment) og tidsstyring (timeouts).
   - Modellar som Go-Back-N og Selective Repeat handterer tap og feil i dataoverføring.
3. **Overlastkontroll:**
   - Forhindrar overbelastning av nettverket ved å justere dataoverføringsfarten.

   ### **TCP-algoritmar for overlastkontroll**

TCP er designa for å justere overføringsfarten basert på nettverkstilstanden for å unngå overbelastning. Dette blir oppnådd gjennom ei rekkje algoritmar som samarbeider for å balansere effektiv dataoverføring med nettverkets kapasitet. Dei tre viktigaste algoritmane er:

---

#### **1. Slow Start**
- **Mål:** Gradvis auke overføringsfarten for å oppdage kapasiteten til nettverket.
- **Mekanisme:**
  - Når ein ny TCP-forbindelse blir etablert, byrjar den å sende data forsiktig ved å initialisere **congestion window (CWND)** til ein liten verdi (vanlegvis 1 MSS - Maximum Segment Size).
  - For kvar kvittering (ACK) som blir mottatt, doblar TCP verdien av CWND.
  - Prosessen held fram til anten:
    - Nettverket når kapasitet og pakker går tapt.
    - **CWND** når ei øvre grense sett av mottakaren (receiver window).
- **Fordel:** Reduserer risikoen for overbelastning når forbindelsen startar.

---

#### **2. Congestion Avoidance**
- **Mål:** Unngå nettverksbelastning når kapasiteten nærmar seg.
- **Mekanisme:**
  - Når CWND når ein terskelverdi kalla **ssthresh** (slow start threshold), går TCP over til ein meir forsiktig auke.
  - CWND blir auka lineært i staden for eksponentielt:
    - For kvar RTT (Round-Trip Time), aukar CWND med éin MSS.
  - Dersom tap blir oppdaga (t.d. via timeouts eller dupliserte ACK-ar), blir **ssthresh** sett til halve CWND, og TCP går tilbake til slow start eller andre mekanismar.
- **Fordel:** Gjer det mogleg å utnytte nettverket utan å overskride kapasiteten.

---

#### **3. Fast Retransmit**
- **Mål:** Redusere ventetida når tap av pakker blir oppdaga.
- **Mekanisme:**
  - Når mottakaren oppdagar eit gap i sekvensnummera, sender den dupliserte ACK-ar for den siste korrekt mottatte pakka.
  - Dersom senderen mottar tre dupliserte ACK-ar, tolkar den dette som eit signal om at ein pakke har gått tapt.
  - Senderen retransmitterer straks den tapte pakka utan å vente på timeout.
- **Fordel:** Forkortar responstida ved pakketap og held dataoverføringa meir stabil.

---

### **Samspel mellom algoritmane**
- **Slow Start:** Initialiserer overføringa med forsiktig auke for å finne nettverkskapasiteten.
- **Congestion Avoidance:** Held overføringa stabil nær kapasiteten.
- **Fast Retransmit:** Handterer pakketap raskt for å minimere påverkinga på ytelsen.

Ved å bruke desse algoritmane saman, kan TCP dynamisk tilpasse seg endringar i nettverkstilstanden og maksimere både effektivitet og pålitelegheit.


### **Q&A**
# Transportlaget i nettverk - Spørsmål og Svar

<details>
<summary><strong>Spørsmål 1:</strong> Kva er hovudfunksjonane til transportlaget?</summary>
Transportlaget tilbyr ende-til-ende-kommunikasjon, multiplexing/demultiplexing, påliteleg dataoverføring, strøymekontroll og overlastkontroll.
</details>

<details>
<summary><strong>Spørsmål 2:</strong> Kva skil TCP frå UDP?</summary>
TCP tilbyr påliteleg og ordna dataoverføring med strøymekontroll og overlastkontroll, medan UDP er forbindingslaus, raskare og ikkje påliteleg.
</details>

<details>
<summary><strong>Spørsmål 3:</strong> Kva betyr demultiplexing i transportlaget?</summary>
Demultiplexing sikrar at mottatte datapakkar blir levert til riktig applikasjon ved hjelp av portnummer.
</details>

<details>
<summary><strong>Spørsmål 4:</strong> Korleis handterer TCP overlastkontroll?</summary>
TCP brukar algoritmar som slow start, congestion avoidance og fast retransmit for å justere overføringsfarten basert på nettverkstilstanden.
</details>

<details>
<summary><strong>Spørsmål 5:</strong> Kva er UDP godt eigna for?</summary>
UDP er godt eigna for applikasjonar som toler tap, som videostrøyming eller DNS-forespørslar.
</details>
