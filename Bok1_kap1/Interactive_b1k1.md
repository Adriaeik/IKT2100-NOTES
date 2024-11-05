Her er eit notat om prosessen vi følgde for å finne sannsynet:

### Oppgåve: Sannsynet for at ein bestemt brukar sender medan dei andre ikkje sender
Vi har ei pakke-svitsja tilkopling der kvar brukar har sannsynet \( P(\text{sender}) = 0.2 \) for å sende data når dei treng det, og dei sender berre data 20 % av tida. I denne oppgåva skulle vi finne sannsynet for at ein bestemt brukar sender data, medan alle andre brukarar ikkje sender.

### Stega vi følgde
1. **Definer sannsyn for inaktivitet:** Først berekna vi sannsynet for at ein brukar **ikkje sender** data, som er \( 1 - 0.2 = 0.8 \).

2. **Finn sannsynet for at ingen sender:** For å finne sannsynet for at ingen sender data, kunne vi multiplisere sannsynet for inaktivitet for alle brukarane. Med \( N_{\text{ps}} = 9 \), er sannsynet for at ingen sender data gitt av:
   \[
   P(\text{ingen sender}) = 0.8^{9} = 0.1342
   \]

3. **Finn sannsynet for at ein spesifikk brukar sender medan dei andre ikkje sender:**
   - Vi valde ein spesifikk brukar som skulle sende data (med sannsyn 0.2).
   - Sannsynet for at alle dei andre åtte brukarane ikkje sender data var \( 0.8^{8} \).
   - Vi multipliserte desse to sannsynene for å finne den kombinerte sannsynet for at akkurat denne brukaren sender medan alle andre ikkje sender:
     \[
     P(\text{ein brukar sender og dei andre ikkje sender}) = 0.2 \times 0.8^{8}
     \]

4. **Berekning:** Ved å setje inn verdiane fann vi:
   \[
   0.2 \times 0.8^{8} = 0.033554432
   \]

### Resultat:
Sannsynet for at ein spesifikk brukar sender data medan dei andre åtte ikkje sender data er omtrent **0.0336**.

I denne oppgåva skal vi finne sannsynet for at **akkurat éin brukar** sender data medan dei andre ikkje sender, uavhengig av kven som sender blant dei ni brukarane.

### Gitt informasjon:
- Det er totalt \( N_{\text{ps}} = 9 \) brukarar.
- Sannsynet for at ein brukar sender data (transmitterer) er \( P(\text{sender}) = 0.2 \).
- Sannsynet for at ein brukar ikkje sender data er \( P(\text{ikkje sender}) = 0.8 \).

### Steg 1: Sannsynet for at ein spesifikk brukar sender og alle andre ikkje sender
Slik vi gjorde tidlegare, kan vi finne sannsynet for at **ein spesifikk brukar** sender data medan alle andre \( 9 - 1 = 8 \) brukarar ikkje sender:

\[
P(\text{ein brukar sender og dei andre ikkje sender}) = 0.2 \times 0.8^{8}
\]

### Steg 2: Kven som helst av dei ni brukarane kan vere den som sender
Sidan kven som helst av dei ni brukarane kan vere den som sender medan alle andre ikkje sender, må vi multiplisere resultatet frå steg 1 med talet på moglege brukarar som kan sende (9):

\[
P(\text{akkurat éin brukar sender}) = 9 \times (0.2 \times 0.8^{8})
\]

### Berekning:
Set inn verdiane:

\[
P(\text{akkurat éin brukar sender}) = 9 \times (0.2 \times 0.8^{8})
\]

Berekna blir dette:

\[
= 9 \times (0.2 \times 0.16777216)
\]
\[
= 9 \times 0.033554432
\]
\[
= 0.301989888
\]

### Svar:
Sannsynet for at akkurat éin av dei ni brukarane sender medan alle andre ikkje sender er om lag **0.30** (eller 30,20 % når avrunda til to desimalar).

For å finne sannsynet for at akkurat **6 av dei 9 brukarane** sender data medan dei resterande 3 brukarane ikkje sender, må vi bruke binomialsannsyn.

### Gitt informasjon:
- Totalt antal brukarar, \( N_{\text{ps}} = 9 \).
- Sannsynet for at ein brukar sender data er \( P(\text{sender}) = 0.2 \).
- Sannsynet for at ein brukar ikkje sender data er \( P(\text{ikkje sender}) = 0.8 \).

### Steg 1: Sannsynet for at ein spesifikk kombinasjon av 6 brukarar sender og 3 ikkje sender
Dersom vi velger ein spesifikk kombinasjon av 6 brukarar som sender og 3 som ikkje sender, kan vi berekne sannsynet for denne kombinasjonen som:

\[
P(\text{6 sender og 3 ikkje sender}) = (0.2)^6 \times (0.8)^3
\]

### Steg 2: Antall moglege kombinasjonar der 6 av 9 brukarar sender
Vi må rekne ut talet på moglege måtar å velje 6 brukarar som sender av dei 9 brukarane. Dette kan vi gjere ved å bruke binomialkoeffisienten, som gir oss antal måtar å velje \( k = 6 \) brukarar frå \( n = 9 \):

\[
\binom{9}{6} = \frac{9!}{6!(9 - 6)!} = \frac{9!}{6! \times 3!} = 84
\]

### Steg 3: Total sannsyn for at akkurat 6 brukarar sender
No kan vi finne total sannsyn ved å multiplisere sannsynet for ein enkelt kombinasjon (frå steg 1) med talet på slike kombinasjonar (frå steg 2):

\[
P(\text{akkurat 6 sender}) = 84 \times (0.2)^6 \times (0.8)^3
\]

### Berekning:
Set inn verdiane og berekn:

1. \( (0.2)^6 = 0.000064 \)
2. \( (0.8)^3 = 0.512 \)

No multipliserer vi saman:

\[
P(\text{akkurat 6 sender}) = 84 \times 0.000064 \times 0.512
\]
\[
= 84 \times 0.000032768
\]
\[
= 0.002751552
\]

### Svar:
Sannsynet for at akkurat 6 av dei 9 brukarane sender data medan dei resterande 3 ikkje sender, er om lag **0.0028** (eller 0,28 % når avrunda til fire desimalar).

```python
from math import comb

# Parametre
Nps = 9       # Totalt antal brukarar
k = 6         # Antal brukarar som sender
p_send = 0.2  # Sannsynet for at ein brukar sender
p_not_send = 1 - p_send  # Sannsynet for at ein brukar ikkje sender

# Berekne sannsynet
probability = comb(Nps, k) * (p_send ** k) * (p_not_send ** (Nps - k))
```

For å finne sannsynet for at **meir enn 5 brukarar** sender data av totalt 9 brukarar, må vi summere sannsynet for at nøyaktig 6, 7, 8, og 9 brukarar sender data.

### Gitt informasjon:
- Totalt antal brukarar \( N_{\text{ps}} = 9 \).
- Sannsynet for at ein brukar sender data er \( P(\text{sender}) = 0.2 \).
- Sannsynet for at ein brukar ikkje sender data er \( P(\text{ikkje sender}) = 0.8 \).

### Sannsynet for at meir enn 5 brukarar sender:
Vi må finne summen av sannsyn for følgjande tilfelle:
- Sannsynet for at **6 brukarar** sender.
- Sannsynet for at **7 brukarar** sender.
- Sannsynet for at **8 brukarar** sender.
- Sannsynet for at **9 brukarar** sender.

Formelen for sannsynet for at \( k \) brukarar sender blant \( N_{\text{ps}} \) brukarar er:
\[
P(\text{nøyaktig } k \text{ sender}) = \binom{N_{\text{ps}}}{k} \times (P(\text{sender}))^k \times (P(\text{ikkje sender}))^{N_{\text{ps}} - k}
\]

### Python-kode
Her er Python-kode som bereknar dette sannsynet:

```python
from math import comb

# Parametre
Nps = 9       # Totalt antal brukarar
p_send = 0.2  # Sannsynet for at ein brukar sender
p_not_send = 1 - p_send  # Sannsynet for at ein brukar ikkje sender

# Sannsyn for at meir enn 5 brukarar sender
probability_more_than_5 = sum(
    comb(Nps, k) * (p_send ** k) * (p_not_send ** (Nps - k))
    for k in range(6, Nps + 1)
)

# Skrive ut resultatet
print(f"Sannsynet for at meir enn 5 brukarar sender er: {probability_more_than_5:.4f}")
```

### Forklaring av koden:
- `comb(Nps, k)`: Reknar ut binomialkoeffisienten for å velje \( k \) brukarar blant \( N_{\text{ps}} \).
- For \( k \) verdiane 6 til 9 (representerer tilfella der meir enn 5 brukarar sender), bereknar vi sannsynet for kvart tilfelle.
- Summen av desse sannsynene gir total sannsyn for at meir enn 5 brukarar sender.

### Forventa resultat:
Når du køyrer koden, vil den berekne sannsynet for at meir enn 5 brukarar sender data.