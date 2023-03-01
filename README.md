# django_portfolio
Krypto portfolio tracker

## Popis projektu
Tento projekt zobrazuje na jednom místě tokeny uživatele, které má umístěny na peněženkách na blockchainu nebo na centralizovaných burzách.

Tomuto projektu předchází projekt portfolio, který se stará o stažení informací o všech tokenech z blockchain peněženek a burz. 
Všechny tyto informace jsou staženy do PostgreSQL databáze, ze které jsou čerpána data pro vizualizaci v tomto projektu. 
Data uživatele s adresami peněženek jsou uloženy v JSON souboru.

Použité technologie: <br>
- Celý projekt je napsán ve frameworku <b>Django</b>
- Data o portfoliu framework získává z databáze <b>PostgreSQL</b>
- Srdce frontendu tvoří jazyky <b>HTML</b>, <b>CSS</b> a pro efekty u grafů je použit <b>JavaScript</b>

### Záložka Přehled
V části Přehled je zobrazen přehled celého portfolia. <br>
- V levé části pod nadpisem je zobrazena dolarová hodnota celého portfolia
- Graf vlevo znázorňuje vývoj dolarové hodnoty v čase
- Graf vpravo znázorňuje procentuální rozložení jednotlivých tokenů podle velikosti dolarové hodnoty
- Tabulka dole rozepisuje zastoupení jednotlivých tokenů v portfoliu

![obrazek](https://user-images.githubusercontent.com/106346624/222254316-451a65f6-1e95-4f8a-af1a-55af17c2f102.png)

### Záložka Grafy
V části Grafy je zobrazeno další rozdělení portfolia podle dolarové hodnoty. <br>
- Tokeny, které jsou na blockchainu, oproti tokenům na centralizovaných burzách
- Tokeny, které jsou v kategoriích Hodl, Staking, Farming a Stable coins
- Tokeny podle jednotlivých sítích a burz

![obrazek](https://user-images.githubusercontent.com/106346624/222254638-a5c24bd5-9910-4ae3-a7a8-1c7d25cd5bc4.png)

### Záložka Grafy - Tabulky
V části Grafy - Tabulky jsou zobrazeny tabulky, ve kterých jsou zobrazeny tokeny roztříděné podle kategorií v části grafy. Do této oblasti se uživatel dostane v záložce
Grafy, pokud klikne vpravo nahoře na link ```Tabulky```. 

![obrazek](https://user-images.githubusercontent.com/106346624/222256558-7157a347-d21f-4450-9f70-64d1c622ab87.png)

### Záložky Staking, Farming, Ceny tokenů, Rest API a Systém
Tyto záložky jsou momentálně ve výstavbě a pracuje se na nich. 

## Závěr
