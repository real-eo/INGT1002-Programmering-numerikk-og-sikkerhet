# Eksamenspakke INGT1002 - 2 dager

Basert på `emne-innhold`, notatbøkene, tidligere eksamener og `NSMs grunnprinsipper`.

**Eksamen:** 4 timer skriftlig. Del 1 = programmering/numerikk (67 %), Del 2 = IKT-sikkerhet (33 %). **Begge deler må bestås separat.** Det betyr at du ikke kan kompensere svak sikkerhet med sterk numerikk.

**Høyest avkastning på 2 dager:** trapes/Simpson for hånd, fikspunkt/Newton-konvergens, Euler ett/to steg + stabilitet, feilorden, flyttall/kansellering, CIA + trussel/sårbarhet/risiko, risikovurdering + 4T, NSM 4 faser, GDPR 72 timer/DPIA/dataminimering, phishing/ransomware/MFA/backup.

---

## 1. Hva du må kunne

### 1.1 Numerikk - P1 (må kunne)

**Regne for hånd:**
- [ ] Forover-, bakover- og sentraldifferanse - sette inn tall og regne ut.
- [ ] Feilorden: forover/bakover $O(h)$, sentral $O(h^2)$, trapes $O(h^2)$, Simpson $O(h^4)$.
- [ ] Trapesmetoden med $n=2$ og $n=4$; huske vektene $\frac12,1,\dots,1,\frac12$.
- [ ] Simpsons regel med $n=2$ og $n=4$; huske vektene $1,4,2,4,\dots,4,1$ og $h/3$.
- [ ] Halveringsmetoden - oppdatere intervall, telle iterasjoner, $n\ge\log_2((b-a)/\tau)$.
- [ ] Fikspunktiterasjon - vise omskriving $x=g(x)$, derivere $g$, sjekke $|g'(r)|<1$.
- [ ] Newtons metode - én iterasjon for hånd; vurdere konvergens og feilmodi.
- [ ] Eulers metode - ett og to steg, både skalar og 2×2-system; $h=(b-a)/N$.
- [ ] Stabilitet for $x'=\lambda x$: $|1+h\lambda|\le1$, finne maksimal $h$.
- [ ] Gjøre om 2. ordens ODE til førsteordens system.
- [ ] Gauss-eliminasjon 2×2/3×3 for hånd, med og uten pivotering.
- [ ] Kondisjonstall - tolke feilforplantning.

**Kode i blinde:**
- [ ] `forover`, `bakover`, `sentral`
- [ ] `trapes`, `simpson`
- [ ] `fikspunkt`, `newton`
- [ ] `euler` (skalar) og `euler_system`
- [ ] `gauss` (naiv, med/uten pivotering)
- [ ] Plotting av løsning og feil i `loglog` med referanselinje $h^p$

**Forklare:**
- [ ] Hvorfor sentraldifferanse er bedre enn forover.
- [ ] Hvorfor det finnes en optimal $h$ (trunkering vs. avrunding).
- [ ] Hvorfor Newton konvergerer kvadratisk, og når den feiler.
- [ ] Hvorfor implisitte metoder er stabile (A-stabile).
- [ ] Hva stivhet er, og hvorfor eksplisitt Euler må ha liten $h$.
- [ ] Konsistens + stabilitet ⇒ konvergens.
- [ ] Hvorfor pivotering trengs.
- [ ] Hva kondisjonstallet sier.

### 1.2 Flyttall og presisjon - P1

- [ ] IEEE 754 double: 1 fortegn + 11 eksponent + 52 mantisse, bias 1023.
- [ ] Maskinepsilon $\epsilon=2^{-52}\approx2.22\cdot10^{-16}$.
- [ ] Hvorfor `0.1 + 0.2 != 0.3`.
- [ ] Katastrofal kansellering; stabil andregradsformel.
- [ ] Absolutt vs. relativ feil; `math.isclose` / `np.isclose`.
- [ ] `inf`, `nan`, overflow/underflow.
- [ ] Single vs. double presisjon.

### 1.3 NumPy og Matplotlib - P1

- [ ] `np.array`, `dtype`, `shape`, `reshape`, `axis`.
- [ ] `np.linspace` vs. `np.arange`.
- [ ] Vektorisering, broadcasting, `*` vs. `@`.
- [ ] Slicing er view, fancy indexing er kopi; `.copy()`.
- [ ] Boolske masker, `np.where`.
- [ ] `np.linalg.solve`, `norm`, `cond`.
- [ ] `fig, ax`, `plot`, `loglog`, `semilogy`, `legend`, `xlabel`, `savefig`.
- [ ] `np.loadtxt`/`genfromtxt`, `np.nan`, `np.isnan`.

### 1.4 Python - P2 (du kan det meste)

- [ ] Parsons-problemer: riktig rekkefølge, innrykk og avhengigheter.
- [ ] Feilsøking: off-by-one, `range`, indeks, `h`, enheter.
- [ ] Funksjoner med returverdi; ikke mutable standardargumenter.
- [ ] Lister, dict, set, comprehensions.
- [ ] Fil: `with open(...) as f`, `readlines`, `split`, `float`.
- [ ] `try/except`, `raise`.
- [ ] f-strings: `f"{x:.3f}"`, `f"{x:e}"`.
- [ ] PEP8: `snake_case`, 4 spaces, imports øverst.

### 1.5 IKT-sikkerhet - P1

- [ ] CIA + autentisitet, sporbarhet, ikke-benektelse.
- [ ] Trussel, trusselaktør, sårbarhet, risiko, uønsket hendelse - presist.
- [ ] Risikovurdering steg for steg; risikomatrise; 4T; rest-risiko; risikoappetitt.
- [ ] Sikkerhetskultur: definisjon, elementer, tiltak.
- [ ] Tiltakskategorier; forsvar i dybden; minste privilegium; need-to-know; Zero Trust.
- [ ] Autentisering (3 faktorer), MFA, autorisasjon, RBAC/ABAC.
- [ ] Kryptografi: symmetrisk/asymmetrisk, hash, salt, signatur, PKI, TLS.
- [ ] Angrep: phishing, ransomware, DDoS, MITM, SQLi, XSS, supply chain, insider, APT, zero-day.
- [ ] NSM: 4 faser, 21 prinsipper, 118 tiltak.
- [ ] Personvern: GDPR-begreper, prinsipper, behandlingsgrunnlag, DPIA, 72 timer, databehandleravtale, personvernombud.
- [ ] Lover/standarder: personopplysningsloven, sikkerhetsloven, ekomloven, ISO 27001/27002, NSM, NIST CSF.
- [ ] Sikkerhetsmodeller: Bell-LaPadula, Biba, Clark-Wilson, DAC/MAC/RBAC/ABAC, Zero Trust.
- [ ] Hendelseshåndtering: forberedelse, oppdagelse, begrensning, eliminering, gjenoppretting, læring.
- [ ] Cyberhygiene.
- [ ] Eget fagområde: OT/ICS/IoT - safety vs. security, segmentering, legacy-systemer.

### 1.6 Eksamensstrategi

| Tid | Aktivitet |
|---|---|
| 0–5 min | Les hele oppgaven. Marker det du kan først. |
| 5–160 min | Del 1: programmering/numerikk. Start med håndregning og Parsons. |
| 160–235 min | Del 2: sikkerhet. Svar kort og presist; bruk begrepene. |
| 235–240 min | Kontroller at begge deler er besvart, enheter og desimaler. |

- Vis mellomregning - poeng for metode, ikke bare svar.
- Parsons: skriv pseudokode først, sjekk at alle linjer brukes og at innrykk stemmer.
- Kode: enkel og riktig slår elegant og feil.
- **Ikke glem del 2** - begge deler må bestås.

### 1.7 Kode du bør kunne skrive i blinde

```python
import numpy as np

def forover(f, x, h):
    return (f(x + h) - f(x)) / h

def bakover(f, x, h):
    return (f(x) - f(x - h)) / h

def sentral(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

def trapes(f, a, b, n):
    h = (b - a) / n
    s = 0.5*(f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return h*s

def simpson(f, a, b, n):          # n må være partall
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i*h)
    return h*s/3

def fikspunkt(g, x0, tol=1e-10, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_ny = g(x)
        if abs(x_ny - x) < tol:
            return x_ny
        x = x_ny
    return x

def newton(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        x = x - fx/df(x)
    return x

def euler(f, tspan, x0, N):
    t0, tend = tspan
    h = (tend - t0)/N
    T = np.linspace(t0, tend, N+1)
    X = np.zeros(N+1)
    X[0] = x0
    for n in range(N):
        X[n+1] = X[n] + h*f(T[n], X[n])
    return T, X

def euler_system(f, tspan, X0, N):
    t0, tend = tspan
    h = (tend - t0)/N
    T = np.linspace(t0, tend, N+1)
    X = np.zeros((N+1, len(X0)))
    X[0] = X0
    for n in range(N):
        X[n+1] = X[n] + h*np.asarray(f(T[n], X[n]))
    return T, X

def gauss(A, b):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            m = A[i, k]/A[k, k]
            A[i, k:] -= m*A[k, k:]
            b[i] -= m*b[k]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
    return x
```

### 1.8 Felleliste

| Felle | Riktig |
|---|---|
| `range(N)` når du fyller $N+1$ punkter | `range(N)` er riktig for steg, men arrayet må ha `N+1` |
| `h = (b-a)/(N-1)` | `h = (b-a)/N` |
| Simpson med oddetall $n$ | $n$ må være partall |
| `np.arange(a, b, h)` inkluderer $b$ | Den ekskluderer $b$; bruk `linspace` |
| `A*B` for matriseprodukt | `A @ B` |
| `==` på flyttall | `math.isclose` / `np.isclose` |
| `and`/`or` på arrayer | `&`/`|` med parenteser |
| Mutable standardargument | `def f(x, lst=None): lst = lst or []` |
| Glemmer `.copy()` | Slicing er view |
| `math.exp` på array | `np.exp` |
| Glemmer startverdien | `X[0] = x0` |
| Feil enhet (grader/radianer) | `np.sin` tar radianer |
| `input()` gir streng | `float(input(...))` |
| `plt.show()` før `savefig` | Lagre først, eller bruk `fig.savefig` |

---

## 2. Begreper og definisjoner

### 2.1 Numerikk

| Begrep | Definisjon |
|---|---|
| Trunkeringsfeil | Feil fra å erstatte en uendelig prosess (derivert/integral) med en endelig tilnærming. |
| Avrundingsfeil | Feil fra at tall lagres med begrenset presisjon. |
| Lokal feil | Feil introdusert i ett enkelt steg. |
| Global feil | Akkumulert feil over hele beregningen. |
| Konsistens | Metoden nærmer seg den eksakte ligningen når $h\to0$. |
| Stabilitet | Feil vokser ikke ukontrollert gjennom beregningen. |
| Konvergens | Løsningen nærmer seg den eksakte når $h\to0$ (eller $n\to\infty$). |
| Konvergensorden | Hvor raskt feilen avtar: $E(h)=O(h^p)$. |
| Skrittlengde $h$ | Avstanden mellom punktene i en diskretisering. |
| Foroverdifferanse | $\frac{f(x+h)-f(x)}{h}$, $O(h)$. |
| Bakoverdifferanse | $\frac{f(x)-f(x-h)}{h}$, $O(h)$. |
| Sentraldifferanse | $\frac{f(x+h)-f(x-h)}{2h}$, $O(h^2)$. |
| Trapesmetoden | Integrasjon ved å erstatte med trapeser; $O(h^2)$. |
| Simpsons regel | Integrasjon ved å erstatte med parabler; $O(h^4)$, krever partall $n$. |
| Halveringsmetoden | Rotfinning ved å halvere et intervall med fortegnsskifte; lineær konvergens. |
| Fikspunkt | $r$ slik at $g(r)=r$. |
| Fikspunktiterasjon | $x_{n+1}=g(x_n)$ for å løse $x=g(x)$. |
| Kontraksjon | $|g'(x)|\le L<1$ i et intervall; garanterer konvergens. |
| Newtons metode | $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$; kvadratisk konvergens nær enkel rot. |
| Sekantmetoden | Derivatfri rotfinning; superlineær (orden $\approx1.618$). |
| Eksplisitt Euler | $x_{n+1}=x_n+h f(t_n,x_n)$; første orden. |
| Implisitt/baklengs Euler | $x_{n+1}=x_n+h f(t_{n+1},x_{n+1})$; A-stabil. |
| Stiv ligning | Ligning med sterkt ulike tidsskalaer; eksplisitte metoder krever svært liten $h$. |
| A-stabil | Stabil for alle $h$ når $\mathrm{Re}\,\lambda<0$. |
| Stabilitetsområde | Mengden $h\lambda$ der metoden er stabil. |
| Startverdiproblem | ODE + initialbetingelse. |
| System av ODE-er | Flere koblede differensialligninger; løses vektorielt. |
| Faseplan | Plot av $x_2$ mot $x_1$ (f.eks. $y'$ mot $y$). |
| Gauss-eliminasjon | Systematisk eliminering til trekantform; $O(n^3)$. |
| Pivotering | Bytte rader for å få størst mulig pivotelement; reduserer avrundingsfeil. |
| LU-dekomponisjon | $A=LU$; gjenbrukbar for mange høyresider. |
| Kondisjonstall | $\kappa(A)=\|A\|\|A^{-1}\|$; mål på feilforplantning. |
| Diagonalt dominant | $|a_{ii}|>\sum_{j\ne i}|a_{ij}|$; garanterer konvergens for Jacobi/Gauss-Seidel. |
| Jacobi/Gauss-Seidel | Iterative løsere for lineære systemer. |

### 2.2 Flyttall

| Begrep | Definisjon |
|---|---|
| Flyttall | Tall lagret som fortegn × signifikand × grunntall^eksponent. |
| Signifikand (mantisse) | Sifferdelen av et flyttall. |
| Eksponent | Potensen i flyttallsrepresentasjonen. |
| Normalisering | Skrive tallet med én ikke-null siffer foran komma. |
| IEEE 754 | Standard for flyttall; double = 1+11+52 bit. |
| Maskinepsilon | Minste $\epsilon$ slik at $1+\epsilon\ne1$; $2^{-52}\approx2.22\cdot10^{-16}$ for double. |
| Katastrofal kansellering | Tap av signifikante siffer ved subtraksjon av nesten like tall. |
| Overflyt/underflyt | Tall utenfor representerbart område; gir `inf` eller $0$. |
| NaN | «Not a Number»; oppstår ved udefinerte operasjoner som $0/0$. |
| Absolutt feil | $|\hat x-x|$. |
| Relativ feil | $|\hat x-x|/|x|$. |

### 2.3 IKT-sikkerhet

| Begrep | Definisjon |
|---|---|
| Informasjonssikkerhet | Beskyttelse av informasjonens konfidensialitet, integritet og tilgjengelighet. |
| CIA-triaden | Konfidensialitet, integritet, tilgjengelighet. |
| Konfidensialitet | Kun autoriserte skal få tilgang til informasjon. |
| Integritet | Informasjon skal være korrekt, komplett og ikke endret av uautoriserte. |
| Tilgjengelighet | Informasjon og tjenester skal være tilgjengelige når autoriserte trenger dem. |
| Autentisitet | Det skal være mulig å verifisere hvem avsenderen/brukeren er. |
| Sporbarhet | Handlinger skal kunne knyttes til en identitet i ettertid. |
| Ikke-benektelse | En part kan ikke benekte å ha utført en handling. |
| Trussel | Potensiell årsak til en uønsket hendelse. |
| Trusselaktør | Den som kan utføre trusselen (kriminell, insider, hacktivist, stat). |
| Sårbarhet | Svakhet som en trussel kan utnytte. |
| Risiko | Sannsynlighet × konsekvens av en uønsket hendelse. |
| Uønsket hendelse | Hendelse som kan skade informasjonsverdier. |
| Risikovurdering | Systematisk identifisering, analyse og evaluering av risiko. |
| Risikomatrise | Rutenett med sannsynlighet × konsekvens. |
| Risikohåndtering | Unngå, redusere, overføre eller akseptere risiko. |
| Rest-risiko | Risiko som gjenstår etter tiltak. |
| Risikoappetitt | Hvor mye risiko organisasjonen er villig til å ta. |
| Sikkerhetskultur | Felles holdninger, verdier, normer og atferd som påvirker sikkerhet i praksis. |
| Sikkerhetstiltak | Handling som reduserer risiko. |
| Forebyggende tiltak | Hindrer hendelsen i å skje. |
| Oppdagende tiltak | Avdekker hendelsen. |
| Korrigerende tiltak | Retter opp etter hendelsen. |
| Forsvar i dybden | Flere uavhengige lag med tiltak. |
| Minste privilegium | Kun nødvendige rettigheter. |
| Need-to-know | Tilgang kun til det man trenger for jobben. |
| Zero Trust | «Never trust, always verify»; ingen implisitt tillit. |
| Autentisering | Verifisere identitet. |
| Autorisasjon | Bestemme hva en autentisert bruker har lov til. |
| MFA | Autentisering med minst to faktorer. |
| RBAC | Rollebasert tilgangskontroll. |
| ABAC | Attributtbasert tilgangskontroll. |
| Symmetrisk kryptografi | Samme nøkkel for kryptering og dekryptering (AES). |
| Asymmetrisk kryptografi | Offentlig/privat nøkkelpar (RSA, ECC). |
| Hash | Envegsfunksjon for integritet/passord. |
| Salt | Tilfeldig verdi per passord som hindrer regnbuebøker. |
| Digital signatur | Hash kryptert med privat nøkkel; gir autentisitet og ikke-benektelse. |
| PKI | Infrastruktur for sertifikater og tillitskjeder. |
| TLS | Kryptert og autentisert transport (HTTPS). |
| Brannmur | Filtrerer nettverkstrafikk etter regler. |
| IDS/IPS | Oppdager/stopper inntrenging. |
| SIEM | Samler og analyserer sikkerhetslogger. |
| DMZ | Demilitarisert sone mellom internett og internnett. |
| Segmentering | Dele nettverket i soner med begrenset trafikk. |
| Backup 3-2-1 | 3 kopier, 2 medier, 1 utenfor lokaliteten. |
| Patch management | Systematisk oppdatering av programvare. |
| Phishing | Bedragerisk melding som lurer deg til å oppgi data eller klikke. |
| Ransomware | Krypterer data og krever løsepenger. |
| DDoS | Overbelastning av tjeneste fra mange kilder. |
| MITM | Angriper mellom to parter avlytter/endrer trafikk. |
| SQL-injeksjon | Innsprøyting av SQL i usikret input. |
| XSS | Innsprøyting av skript som kjøres hos andre brukere. |
| Supply chain-angrep | Angrep via leverandør eller tredjepart. |
| Insider | Person med legitim tilgang som misbruker den. |
| APT | Advanced Persistent Threat; langvarig, målrettet angrep. |
| Zero-day | Sårbarhet uten tilgjengelig patch. |
| CVSS/CVE | Standardisert alvorlighetsscore / sårbarhetsregister. |
| Cyberhygiene | Grunnleggende gode vaner: oppdateringer, MFA, backup, skeptisk til lenker. |
| Hendelseshåndtering | Forberedelse, oppdagelse, begrensning, eliminering, gjenoppretting, læring. |
| Personopplysning | Opplysning som kan knyttes til en identifiserbar person. |
| Sensitive personopplysninger | Særlige kategorier (helse, religion, etnisitet, biometri m.m.), GDPR art. 9. |
| Behandlingsgrunnlag | Rettslig grunnlag for behandling, GDPR art. 6. |
| Dataminimering | Kun nødvendige personopplysninger. |
| Formålsbegrensning | Bruk kun til angitt formål. |
| Innebygd personvern | Personvern by design og by default, GDPR art. 25. |
| DPIA | Personvernkonsekvensvurdering ved høy risiko, GDPR art. 35. |
| Databehandleravtale | Avtale mellom behandlingsansvarlig og databehandler, GDPR art. 28. |
| Personvernombud | DPO; uavhengig rådgiver og kontrollør. |
| GDPR | Personvernforordningen; gjeldende i Norge via EØS og personopplysningsloven. |
| Personopplysningsloven | Norsk lov som gjennomfører GDPR. |
| Sikkerhetsloven | Lov om nasjonal sikkerhet; gjelder sikkerhetsgradert informasjon og samfunnskritiske funksjoner. |
| ISO/IEC 27001 | Krav til ledelsessystem for informasjonssikkerhet (ISMS). |
| ISO/IEC 27002 | Veiledning i sikkerhetstiltak. |
| NSM grunnprinsipper | 21 prinsipper og 118 tiltak i 4 faser. |
| NIST CSF | Identify, Protect, Detect, Respond, Recover. |
| ISMS | Ledelsessystem for informasjonssikkerhet. |
| Sikkerhetsmodell | Formell modell for tilgangskontroll. |
| Bell-LaPadula | Konfidensialitet: no read up, no write down. |
| Biba | Integritet: no read down, no write up. |
| Clark-Wilson | Integritet: velformede transaksjoner og oppgaveadskillelse. |
| DAC/MAC | Eierstyrt / systemhåndhevet tilgangskontroll. |
| Kill chain | Angrepsfaser: rekognosering → våpen → levering → utnyttelse → installasjon → C2 → mål. |
| OT/ICS | Operasjonell teknologi / industrielle styringssystemer; safety vs. security. |

---

## 3. 100 spørsmål med svar

### A. Numerisk derivasjon og integrasjon (1–14)

**1.** Skriv foroverdifferansen for $f'(x)$. Hvilken feilorden har den?
**Svar:** $f'(x)\approx\frac{f(x+h)-f(x)}{h}$, trunkeringsfeil $O(h)$.

**2.** Skriv bakoverdifferansen.
**Svar:** $f'(x)\approx\frac{f(x)-f(x-h)}{h}$, $O(h)$.

**3.** Skriv sentraldifferansen. Hvorfor er den bedre?
**Svar:** $f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}$, $O(h^2)$. $h$-leddene kansellerer i Taylor-utviklingen.

**4.** Regn ut foroverdifferansen til $f(x)=x^2$ i $x=1$ med $h=0.1$.
**Svar:** $\frac{1.21-1}{0.1}=2.1$ (eksakt 2).

**5.** Samme med sentraldifferanse.
**Svar:** $\frac{1.21-0.81}{0.2}=2.0$ (eksakt).

**6.** Hva er den totale feilen i numerisk derivasjon, og hva er optimal $h$?
**Svar:** Trunkering $O(h^p)$ + avrunding $O(\epsilon/h)$. Forover: $h\sim\sqrt{\epsilon}\approx10^{-8}$. Sentral: $h\sim\epsilon^{1/3}\approx10^{-5}$.

**7.** Skriv formelen for andrederivert med sentraldifferanse.
**Svar:** $f''(x)\approx\frac{f(x+h)-2f(x)+f(x-h)}{h^2}$, $O(h^2)$.

**8.** Skriv den sammensatte trapesformelen.
**Svar:** $T=h\left[\frac{f_0}{2}+f_1+\cdots+f_{n-1}+\frac{f_n}{2}\right]$, $h=\frac{b-a}{n}$.

**9.** Regn ut $\int_0^1 x^2\,dx$ med trapes, $n=2$.
**Svar:** $h=0.5$; $0.5(0+0.25+0.5)=0.375$. Eksakt $1/3\approx0.333$.

**10.** Skriv Simpsons regel.
**Svar:** $S=\frac{h}{3}[f_0+4f_1+2f_2+4f_3+\cdots+4f_{n-1}+f_n]$, $n$ partall.

**11.** Regn ut samme integral med Simpson, $n=2$.
**Svar:** $\frac{0.5}{3}(0+4\cdot0.25+1)=\frac13$ - eksakt for andregradspolynom.

**12.** Hvilken feilorden har trapes og Simpson?
**Svar:** Trapes $O(h^2)$, Simpson $O(h^4)$ (global feil).

**13.** Hvorfor er Simpson eksakt for polynomer av grad ≤3?
**Svar:** Feilleddet inneholder $f^{(4)}$, som er null for grad ≤3.

**14.** Hva skjer hvis $n$ er oddetall i Simpson?
**Svar:** Formelen er ugyldig - Simpsons regel krever partall $n$ (oddetall antall punkter).

### B. Ligningsløsning (15–25)

**15.** Hva er et fikspunkt for $g$?
**Svar:** Et punkt $r$ slik at $g(r)=r$.

**16.** Hvordan løser man $f(x)=0$ med fikspunktiterasjon?
**Svar:** Skriv om til $x=g(x)$ (f.eks. isoler $x$ eller $g(x)=x-cf(x)$), og iterer $x_{n+1}=g(x_n)$.

**17.** Når konvergerer fikspunktiterasjonen?
**Svar:** Hvis $g$ er kontinuerlig og $|g'(r)|<1$ i en omegn av fikspunktet (kontraksjon). Divergerer hvis $|g'(r)|>1$.

**18.** Hvilken konvergensorden har fikspunktiterasjon?
**Svar:** Lineær med rate $|g'(r)|$. Hvis $g'(r)=0$, blir den minst kvadratisk.

**19.** Hva er halveringsmetoden, og hvilke krav stilles?
**Svar:** Krever $f$ kontinuerlig og fortegnsskifte $f(a)f(b)<0$. Halver intervallet og velg halvdelen med fortegnsskifte. Konvergerer alltid, lineært.

**20.** Hvor mange iterasjoner trengs for toleranse $\tau$ på $[a,b]$?
**Svar:** $n\ge\log_2\left(\frac{b-a}{\tau}\right)$. For $[0,1]$, $\tau=10^{-6}$: 20 iterasjoner.

**21.** Skriv Newtons iterasjon.
**Svar:** $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$.

**22.** Hvilken konvergensorden har Newton, og når?
**Svar:** Kvadratisk nær en enkel rot ($f'(r)\ne0$); lineær ved multippel rot.

**23.** Når feiler Newton?
**Svar:** $f'(x_n)=0$ (deling på null), dårlig startgjetting, syklisk/divergerende oppførsel, multippel rot.

**24.** Sammenlign bisection og Newton.
**Svar:** Bisection: robust, alltid konvergens, lineær, krever fortegnsskifte. Newton: rask (kvadratisk), krever derivert og godt startgjetting.

**25.** Hva er sekantmetoden?
**Svar:** $x_{n+1}=x_n-f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}$; superlineær (orden $\approx1.618$), ingen derivert.

### C. Differensialligninger (26–38)

**26.** Skriv eksplisitt Euler.
**Svar:** $x_{n+1}=x_n+h f(t_n,x_n)$, $t_n=a+nh$.

**27.** Hva er lokal og global feil for Euler?
**Svar:** Lokal trunkeringsfeil $O(h^2)$ per steg; global feil $O(h)$ (første orden).

**28.** Regn ett steg med Euler for $x'=x$, $x(0)=1$, $h=0.1$.
**Svar:** $x_1=1+0.1\cdot1=1.1$.

**29.** Regn to steg.
**Svar:** $x_2=1.1+0.1\cdot1.1=1.21$ (eksakt $e^{0.2}=1.2214$).

**30.** Skriv baklengs Euler.
**Svar:** $x_{n+1}=x_n+h f(t_{n+1},x_{n+1})$. Implisitt - må løses for $x_{n+1}$ (fsolve/Newton).

**31.** Hvorfor er baklengs Euler bedre på stive ligninger?
**Svar:** Den er A-stabil: stabil for alle $h$ når $\mathrm{Re}\,\lambda<0$. Eksplisitt Euler krever $h\le2/|\lambda|$.

**32.** Utled stabilitetskravet for eksplisitt Euler på $x'=\lambda x$.
**Svar:** $x_{n+1}=(1+h\lambda)x_n$; krever $|1+h\lambda|\le1$. For $\lambda<0$: $h\le2/|\lambda|$.

**33.** For $\lambda=-20$, hva er maksimal $h$?
**Svar:** $h\le0.1$.

**34.** Skriv Eulers metode for et system.
**Svar:** $\mathbf{x}_{n+1}=\mathbf{x}_n+h\mathbf{f}(t_n,\mathbf{x}_n)$, med vektorer.

**35.** Gjør $y''+cy'+ky=0$ om til et førsteordens system.
**Svar:** $y_1=y$, $y_2=y'$; $y_1'=y_2$, $y_2'=-ky-cy_2$.

**36.** Hva er et faseplan?
**Svar:** Plot av $y'$ mot $y$ (eller $x_2$ mot $x_1$); viser baner uten tidsakse.

**37.** Hva beskriver Lotka-Volterra?
**Svar:** Byttedyr/rovdyr: $x'=\alpha x-\beta xy$, $y'=\delta xy-\gamma y$; gir svingninger.

**38.** Hva menes med konsistens, stabilitet og konvergens?
**Svar:** Konsistens: metoden stemmer med ODE-en når $h\to0$. Stabilitet: feil vokser ikke ukontrollert. Konvergens: $x_n\to x(t)$ når $h\to0$. For konsistente metoder er stabilitet ⇔ konvergens (Lax).

### D. Lineære systemer (39–40)

**39.** Hva er kompleksiteten til naiv Gauss-eliminasjon, og hvorfor pivotering?
**Svar:** $O(n^3)$ for eliminasjon, $O(n^2)$ for tilbakesubstitusjon. Pivotering unngår divisjon på små tall og håndterer null på diagonalen.

**40.** Hva sier kondisjonstallet?
**Svar:** $\kappa(A)=\|A\|\|A^{-1}\|$; hvor mye relativ feil i $b$ forsterkes i $x$: $\frac{\|\delta x\|}{\|x\|}\lesssim\kappa(A)\frac{\|\delta b\|}{\|b\|}$. $\kappa=1$ er best.

### E. Flyttall (41–48)

**41.** Hvordan er en IEEE 754 double lagret?
**Svar:** 64 bit: 1 fortegn, 11 eksponent (bias 1023), 52 mantisse. Verdi $(-1)^s(1.m)_2 2^{e-1023}$.

**42.** Hva er maskinepsilon for double?
**Svar:** $2^{-52}\approx2.22\cdot10^{-16}$.

**43.** Hvorfor er `0.1 + 0.2 != 0.3`?
**Svar:** 0.1 og 0.2 har uendelig binær brøkutvikling og avrundes; summen blir `0.30000000000000004`.

**44.** Hva er katastrofal kansellering?
**Svar:** Tap av signifikante siffer når man subtraherer nesten like tall; relativ feil eksploderer.

**45.** Hvordan løser man andregradsligningen stabilt?
**Svar:** $x_1=\frac{-b-\operatorname{sign}(b)\sqrt{b^2-4ac}}{2a}$, $x_2=\frac{c}{a x_1}$. Unngår $-b+\sqrt{\cdot}$ når $b$ er stor.

**46.** Hvordan sammenligner man flyttall?
**Svar:** `math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12)` eller `np.isclose`; aldri `==`.

**47.** Hva er `inf` og `nan`?
**Svar:** `inf` = overflyt/deling på null. `nan` = udefinert ($0/0$, $\infty-\infty$); `nan != nan` er `True`.

**48.** Hva er forskjellen på single og double?
**Svar:** Single: 32 bit (1+8+23), $\epsilon\approx1.2\cdot10^{-7}$, ~7 siffer. Double: 64 bit, $\epsilon\approx2.2\cdot10^{-16}$, ~16 siffer.

### F. NumPy og Matplotlib (49–56)

**49.** Forskjell på `np.linspace(a,b,n)` og `np.arange(a,b,h)`?
**Svar:** `linspace` gir $n$ jevnt fordelte punkter inkl. $b$. `arange` gir steg $h$, ekskl. $b$, og er utsatt for flyttallsfeil.

**50.** Hva er vektorisering?
**Svar:** Operasjoner på hele arrayer i C-løkker internt, i stedet for Python-løkker; raskere og kortere kode.

**51.** Hva er broadcasting?
**Svar:** NumPy utvider dimensjoner med størrelse 1 slik at arrayer av ulik form kan kombineres, f.eks. `A - A.mean(axis=0)`.

**52.** Forskjell på `A*B` og `A@B`?
**Svar:** `*` er elementvis; `@` er matrisemultiplikasjon.

**53.** Er en slice en kopi?
**Svar:** Nei, en slice er en view; endringer påvirker originalen. Bruk `.copy()` ved behov. Fancy indexing gir kopi.

**54.** Hvordan velger man elementer med en betingelse?
**Svar:** `x[x > 0]` (boolske masker); `np.where(cond, a, b)`.

**55.** Hvordan løser man et lineært system i NumPy, og hvorfor ikke invertere?
**Svar:** `x = np.linalg.solve(A, b)`. Raskere og numerisk mer stabilt enn `np.linalg.inv(A) @ b`.

**56.** Hvordan lager man et log-log-plott for feilanalyse?
**Svar:** `fig, ax = plt.subplots(); ax.loglog(h, feil, 'o-'); ax.loglog(h, h**2, 'r--')`. Stigningstallet viser feilordenen.

### G. IKT-sikkerhet (57–100)

**57.** Hva står CIA for?
**Svar:** Confidentiality, Integrity, Availability - konfidensialitet, integritet, tilgjengelighet.

**58.** Definer konfidensialitet og gi tiltak.
**Svar:** Kun autoriserte skal få tilgang. Tiltak: kryptering, tilgangskontroll, MFA, need-to-know.

**59.** Definer integritet og gi tiltak.
**Svar:** Data skal være korrekte, komplette og ikke endret av uautoriserte. Tiltak: hashing, signaturer, versjonskontroll, tilgangskontroll, logging.

**60.** Definer tilgjengelighet og gi tiltak.
**Svar:** Tjenester skal være tilgjengelige når autoriserte trenger dem. Tiltak: redundans, backup, DDoS-beskyttelse, vedlikehold, beredskap.

**61.** Skille trussel, sårbarhet og risiko.
**Svar:** Trussel = potensiell årsak til uønsket hendelse. Sårbarhet = svakhet som kan utnyttes. Risiko = sannsynlighet × konsekvens av at trussel utnytter sårbarhet.

**62.** Hvordan beregnes risiko?
**Svar:** $R=S\times K$ (sannsynlighet × konsekvens), eller kvalitativt i en risikomatrise.

**63.** Nevn stegene i en risikovurdering.
**Svar:** 1) Kontekst/omfang, 2) identifiser verdier, 3) identifiser trusler, 4) identifiser sårbarheter, 5) vurder sannsynlighet og konsekvens, 6) beregn risiko, 7) risikohåndtering, 8) dokumenter og følg opp.

**64.** Hva er de fire risikohåndteringsstrategiene?
**Svar:** Unngå, redusere, overføre (forsikring/outsourcing), akseptere.

**65.** Hva er rest-risiko?
**Svar:** Risikoen som gjenstår etter at tiltak er iverksatt.

**66.** Hva er en risikomatrise?
**Svar:** Rutenett med sannsynlighet × konsekvens, fargekodet for risikonivå; brukes til prioritering.

**67.** Definer sikkerhetskultur.
**Svar:** Felles holdninger, verdier, normer og atferd som påvirker hvordan ansatte håndterer sikkerhet i praksis.

**68.** Hva kjennetegner god sikkerhetskultur?
**Svar:** Ledelsesforankring, tydelige retningslinjer, opplæring, åpen rapportering uten skyld, læring av hendelser, sikkerhet som alles ansvar.

**69.** Hvilke tre kategorier sikkerhetstiltak finnes?
**Svar:** Forebyggende (hindre), oppdagende (avdekke), korrigerende/gjenopprettende (rette opp).

**70.** Hva er forsvar i dybden?
**Svar:** Flere uavhengige lag med tiltak, slik at én feil ikke kompromitterer hele systemet.

**71.** Hva er minste privilegium?
**Svar:** Brukere/prosesser skal kun ha de rettighetene de trenger for oppgaven - ikke mer.

**72.** Hva er de tre autentiseringsfaktorene?
**Svar:** Noe du vet (passord), noe du har (token), noe du er (biometri). MFA = minst to.

**73.** Hva er autorisasjon, og hva er RBAC?
**Svar:** Autorisasjon = hva en autentisert bruker har lov til. RBAC = rollebasert tilgangskontroll.

**74.** Symmetrisk vs. asymmetrisk kryptering?
**Svar:** Symmetrisk: samme nøkkel (AES), rask. Asymmetrisk: offentlig/privat nøkkel (RSA/ECC), løser nøkkelutveksling, tregere.

**75.** Hashing vs. kryptering?
**Svar:** Hash er envegsfunksjon (kan ikke reverseres), brukes til integritet/passord. Kryptering er reversibel med nøkkel.

**76.** Hvorfor salt i passordlagring?
**Svar:** Unik tilfeldig verdi per passord hindrer regnbuebøker og gjør like passord ulike. Bruk bcrypt/Argon2.

**77.** Hva er en digital signatur?
**Svar:** Hash av meldingen kryptert med avsenders private nøkkel; gir autentisitet, integritet og ikke-benektelse.

**78.** Hva gjør TLS?
**Svar:** Krypterer og autentiserer trafikk mellom klient og server (HTTPS), med sertifikater og nøkkelutveksling.

**79.** Hva er phishing, og hvordan beskytter man seg?
**Svar:** Bedragerisk melding som lurer deg til å oppgi data/klikke. Beskyttelse: opplæring, MFA, e-postfilter, sjekk av avsender/lenker, rapportering.

**80.** Hva er ransomware, og hva er beste vern?
**Svar:** Krypterer data og krever løsepenger. Beste vern: offline/immutable backup, patching, MFA, segmentering, testet gjenoppretting.

**81.** Hva er DDoS?
**Svar:** Overbelastning av tjeneste med mange forespørsler fra mange kilder. Vern: rate limiting, CDN, scrubbing, redundans.

**82.** Hva er MITM?
**Svar:** Angriper plasserer seg mellom to parter og avlytter/endrer trafikk. Vern: TLS, sertifikatvalidering, HSTS.

**83.** Hvordan hindrer man SQL-injeksjon?
**Svar:** Parametriserte spørringer/prepared statements, inputvalidering, minste privilegium på databasebruker.

**84.** Hva er XSS?
**Svar:** Innsprøyting av skript i nettsider som kjøres hos andre brukere. Vern: output-encoding, CSP, inputvalidering.

**85.** Nevn vanlige malware-typer.
**Svar:** Virus, orm, trojaner, ransomware, spyware, rootkit, keylogger, botnet.

**86.** Hva er en insider-trussel?
**Svar:** Ansatt/partner med legitim tilgang som misbruker den - ondsinnet eller uaktsom.

**87.** Hva er APT?
**Svar:** Advanced Persistent Threat: langvarig, målrettet angrep, ofte statlig støttet, med skjult tilstedeværelse.

**88.** Hva er zero-day og CVSS?
**Svar:** Zero-day = sårbarhet uten tilgjengelig patch. CVSS = standardisert alvorlighetsscore 0–10.

**89.** Hva er 3-2-1-regelen for backup?
**Svar:** 3 kopier, 2 ulike medier, 1 utenfor lokaliteten (gjerne 1 offline/immutable).

**90.** Hva er NSMs grunnprinsipper?
**Svar:** 21 prinsipper og 118 tiltak i 4 faser: identifisere og kartlegge, beskytte og opprettholde, oppdage, håndtere og gjenopprette.

**91.** Hva er en personopplysning, og hva er sensitive personopplysninger?
**Svar:** Personopplysning = opplysning som kan knyttes til en identifiserbar person. Sensitive = særlige kategorier (helse, religion, etnisitet, biometri, seksuell orientering m.m.), GDPR art. 9.

**92.** Hva er behandlingsgrunnlag etter GDPR?
**Svar:** Rettslig grunnlag etter art. 6: samtykke, avtale, rettslig forpliktelse, vitale interesser, offentlig oppgave eller berettiget interesse.

**93.** Nevn tre personvernprinsipper.
**Svar:** Dataminimering (kun nødvendige data), formålsbegrensning (kun angitt formål), lagringsbegrensning (ikke lenger enn nødvendig).

**94.** Hva er en DPIA?
**Svar:** Personvernkonsekvensvurdering (Data Protection Impact Assessment), GDPR art. 35; kreves ved behandling som medfører høy risiko.

**95.** Hva gjør man ved brudd på personopplysningssikkerhet?
**Svar:** Meld til Datatilsynet innen 72 timer (art. 33) hvis risiko for rettigheter; varsle berørte ved høy risiko (art. 34); dokumenter i bruddregister.

**96.** Hva er en databehandleravtale, og hva er et personvernombud?
**Svar:** Databehandleravtale (art. 28) regulerer behandling utført på vegne av behandlingsansvarlig. Personvernombud (DPO) er uavhengig rådgiver og kontrollør.

**97.** Nevn relevante lover og standarder for IKT-sikkerhet.
**Svar:** Personopplysningsloven/GDPR, sikkerhetsloven, ekomloven, åndsverkloven, straffeloven (datakriminalitet), ISO/IEC 27001 (ISMS), ISO/IEC 27002 (tiltak), NSM grunnprinsipper, NIST CSF.

**98.** Forklar Bell-LaPadula, Biba og Clark-Wilson.
**Svar:** Bell-LaPadula: konfidensialitet - no read up, no write down. Biba: integritet - no read down, no write up. Clark-Wilson: integritet - velformede transaksjoner og oppgaveadskillelse.

**99.** Nevn fasene i hendelseshåndtering.
**Svar:** Forberedelse, oppdagelse/analyse, begrensning, eliminering, gjenoppretting, læring (post-incident).

**100.** Hva er cyberhygiene, og hva er spesielt med OT/ICS-sikkerhet?
**Svar:** Cyberhygiene = grunnleggende gode vaner: oppdateringer, sterke unike passord + passordmanager, MFA, backup, skeptisk til lenker/vedlegg, minste privilegium, rapporter hendelser. OT/ICS: safety vs. security, segmentering, legacy-systemer, patch-utfordringer, Purdue-modellen.

---

## 4. Todagers plan

**Dag 1 - numerikk + flyttall**
- Formiddag: derivasjon/integrasjon + fikspunkt/Newton. Gjør `H25` og `S26` numerikkdel.
- Ettermiddag: ODE + lineære systemer + flyttall. Skriv de 8 funksjonene i [1.7](#17-kode-du-bør-kunne-skrive-i-blinde) fra hukommelsen.
- Kveld: sikkerhet Uke 37 + 40 (`Introduksjon og sikkerhetskultur`, `Trusler og sårbarheter`).

**Dag 2 - sikkerhet + simulering**
- Formiddag: `Personvern og cyber risikovurdering` + `Eksamen, sikkerhetstiltak og repetisjon` + NSM 4 faser.
- Ettermiddag: full simulering på 4 timer (velg `H25` eller `S26`), rett med `h25_lf.pdf` / `s26-lf-fixed.pdf`.
- Kveld: gå gjennom feil, les begrepslista, sov.

**Beste enkeltressurser:**
- `Formelark_numerikk_2025_ver1.pdf` - sjekk om det er tillatt hjelpemiddel.
- `Euler_problem.ipynb` - lokal/global feil og stabilitet.
- `System_Euler.ipynb` - systemer, Lotka-Volterra, implisitte metoder.
- `numderint.ipynb` - derivasjon, trapes, Simpson.
- `fixed_point_iteration.ipynb` - konvergens/divergens og cobweb.
- `newton_method_autograd.ipynb` - Newton med automatisk derivasjon.
- `Faglige_avklaringer_INGT1002.pdf` - presis begrepsbruk og risikoanalyse; les denne før sikkerhetsdelen.

Vil du ha dette lagret som en Markdown- eller PDF-fil, bytt til agent-modus og si fra - jeg er låst til lesemodus her.