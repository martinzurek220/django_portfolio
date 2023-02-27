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

![obrazek](https://user-images.githubusercontent.com/106346624/221606760-1d12cd0a-3282-48f7-bf5c-1005fd80fcf4.png)

### Záložka Grafy
V části Grafy je zobrazeno další rozdělení portfolia podle dolarové hodnoty. <br>
- Tokeny, které jsou na blockchainu, oproti tokenům na centralizovaných burzách
- Tokeny, které jsou v kategoriích Hodl, Staking, Farming a Stable coins
- Tokeny podle jednotlivých sítích a burz

![obrazek](https://user-images.githubusercontent.com/106346624/221610154-d46811e4-40b7-4a9b-b3e3-4f6d3480d5d5.png)

### Záložka Grafy - Tabulky
V části Grafy - Tabulky jsou zobrazeny tabulky, ve kterých jsou zobrazeny tokeny roztříděné podle kategorií v části grafy. Do této oblasti se uživatel dostane v záložce
Grafy, pokud klikne vpravo nahoře na link ```Tabulky```. 

![obrazek](https://user-images.githubusercontent.com/106346624/221619754-af88c704-e65d-4fea-8254-05202a46a820.png)

### Záložky Staking, Farming, Ceny tokenů, Rest API a Systém
Tyto záložky jsou momentálně ve výstavbě a pracuje se na nich. 

## Závěr
