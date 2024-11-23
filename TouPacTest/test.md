#### Q1
**a)**
    circuit-switch, som gir garantert båndbredde, ville vert best egna.
**b)**
    yes, because

#### Q2
**1)**
    because the application slice the data into segments
**2)**
    because it sends segmentsnumber

#### Q3
    N = MSS/L < 15*16**3 + 15*16**2 + 15*16*1 + 15 =  65535
    L = MSS/N = veldig liten = 0.008178835736629282 bytes per melding
    
    (536+66)/155 = 3.8838709677419354

#### Q4
    a1->a3->b1->b2->d1->d3
    a2->a4->c1->c2->d2->d3

#### Q6
    adr: 111x ->0
    adr: 11100000 01x -> 1
    adr: 11100000 01000001x -> 2
    adr: 0x -> 011x U 11100001 1x-> 3

    den sjekker kor lenge det stemmer og sender den på beste match
    første adresse går til 3 andre til 1 og siste til 3

#### Q7
vi har låst 128.119.40. og dei to fyrste bita i binære 64 = 2**6, vi har då 64 sub adressa ergo er alle tall med dei to første bitane = 01 på siste decimal pos godkjent.
så adressa 128.119.40.142 funke

64/4 = 16 så vi må låse dei 4 første bitane i subnettet
vi har 
128.119.40.64/28 : 0100
128.119.40.80/28 : 0101
128.119.40.96/28 : 0110
128.119.40.112/28 : 0111


#### Q8 
det vil krasje men går fint, vi unngår delay. det køer

### Q9
med einkel feil er det bare å flippe bitte der kolonna og raden med feil krysser