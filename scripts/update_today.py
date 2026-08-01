import json

PATH = "data/2026-08-01.json"

with open(PATH, encoding="utf-8") as f:
    data = json.load(f)

by_slug = {x["slug"]: x for x in data}

# --- Update: burze_alert_rcb_sierpien ---
x = by_slug["burze_alert_rcb_sierpien"]
x["title"] = "Alert RCB dla kilku wojewodztw: burze z gradem i silnym wiatrem utrzymuja sie przez caly weekend"
x["body"] = (
    "W piątek 31 lipca i w sobotę 1 sierpnia Rządowe Centrum Bezpieczeństwa kilkukrotnie rozsyłało "
    "mieszkańcom pilne alerty SMS, najpierw dla ośmiu, potem dla siedmiu województw, ostrzegając przed "
    "gwałtownymi burzami, silnym wiatrem i gradem, co potwierdziły między innymi Polskie Radio 24, TVN24 "
    "Meteo oraz PAP. IMGW wydało w tym czasie ostrzeżenia pierwszego i drugiego stopnia łącznie dla około "
    "dziesięciu regionów kraju. Burze przynoszą grad wielkości kurzych jaj oraz porywy wiatru dochodzące "
    "do stu dwudziestu kilometrów na godzinę, co jest szczególnie groźne po wcześniejszej fali upałów "
    "sięgającej trzydziestu sześciu stopni. Serwis Kaszuby24 informował, że w weekend 1 i 2 sierpnia "
    "najsilniejsze zjawiska przejdą przez Pomorze, gdzie synoptycy nie wykluczają także trąb powietrznych "
    "nad morzem. Straż pożarna zgłaszała już połamane drzewa, zerwane dachy i przerwy w dostawie prądu w "
    "kilku regionach. RCB zaapelowało o unikanie otwartych przestrzeni, plaż i lasów oraz o schronienie "
    "się w budynkach, a władze samorządowe uruchomiły dodatkowe dyżury służb kryzysowych. Synoptycy "
    "ostrzegają, że niebezpieczna pogoda może utrzymać się aż do niedzieli, dlatego RCB zapowiada możliwe "
    "kolejne alerty w najbliższych godzinach."
)
x["sources"].update({
    "https://polskieradio24.pl/pogoda/alert-rcb-dla-siedmiu-wojewodztw-pilny-apel-do-polakow": "Polskie Radio 24",
    "https://kaszuby24.pl/ostrzezenie-imgw-dla-pomorza-burze-i-silny-wiatr-w-weekend-1-2-sierpnia-2026/": "Kaszuby24",
    "https://www.pap.pl/aktualnosci/imgw-ostrzega-przed-burzami-w-dziesieciu-wojewodztwach-1": "PAP",
})
x["last_updated"] = "2026-08-01 04:20"

# --- Update: tusk_regulowane_ceny_paliw ---
x = by_slug["tusk_regulowane_ceny_paliw"]
x["body"] = (
    "Sytuacja na rynku paliw w Polsce pozostaje dynamiczna. Jak informowały pod koniec lipca portale "
    "agroprofil.pl, Super Biznes (se.pl) oraz Dziennik.pl, hurtowa cena oleju napędowego w Orlenie rosła "
    "nieprzerwanie przez 25 kolejnych dni, osiągając rekordowy poziom, a detaliczna cena ON lokalnie "
    "przebiła 8,69 złotego za litr, co eksperci określili jako najwyższy poziom od szczytu z 2022 roku, "
    "mimo relatywnie mocnego złotego. Na przełomie lipca i sierpnia seria podwyżek została jednak "
    "przerwana: notowania ropy Brent spadły o około 15 procent, a Orlen obniżył część hurtowych cen, "
    "najmocniej taniał diesel, podczas gdy benzyna nieznacznie zdrożała, jak podała Interia oraz Super "
    "Biznes. Premier Donald Tusk podtrzymał zapowiedź o możliwym wprowadzeniu regulowanych cen paliw na "
    "czas powrotów z wakacji, mówiąc dla TVN24 Biznes żartobliwie, że był CPN, a teraz ma być CKN. Tusk "
    "skrytykował też decyzję prezydenta Karola Nawrockiego w sprawie podatku od nadzwyczajnych zysków "
    "koncernów paliwowych, nazywając ją ciosem wymierzonym we wszystkich polskich kierowców, co wywołało "
    "ostrą wymianę zdań z politykami Prawa i Sprawiedliwości, w tym Przemysławem Czarnkiem. Kierowcy "
    "odczuwają wahania cen na dystrybutorach z dnia na dzień, a analitycy ostrzegają, że wojna wokół "
    "Iranu może ponownie wywindować ceny ropy."
)
x["last_updated"] = "2026-08-01 04:20"

# --- Update: iran_wojna_eskalacja ---
x = by_slug["iran_wojna_eskalacja"]
x["body"] = (
    "Konflikt zbrojny między Stanami Zjednoczonymi i Izraelem a Iranem trwa od kilku miesięcy i w piątek "
    "31 lipca ponownie się zaostrzył. Według Wall Street Journal, na które powołały się Bloomberg i "
    "Fortune, prezydent Donald Trump wydał polecenie przygotowania nowej fali uderzeń na irańską "
    "infrastrukturę energetyczną, które mogą ruszyć już w ten weekend. Euronews podał, że Waszyngton "
    "wznowił bezpośrednie ataki na Iran dzień po tym, jak irańskie siły próbowały, bezskutecznie, "
    "uderzyć w bazy wojskowe w Jordanii, co dodatkowo podniosło napięcie w regionie. Washington Post "
    "opisał, że naloty doprowadziły do przerw w dostawach prądu i niedoborów paliw w irańskich miastach, "
    "osłabiając gospodarkę. CENTCOM potwierdziło zakończenie kolejnej serii nalotów, a Iran zapowiedział "
    "kontrolę nad Cieśniną Ormuz, kluczowym szlakiem transportu ropy. Według CNN i CBS News liczba ofiar "
    "po obu stronach sięga już tysięcy, w tym kilkunastu Amerykanów. Senat USA po raz kolejny odrzucił "
    "próbę ograniczenia wojennych uprawnień prezydenta. Reakcje są mieszane: część kongresmenów ostrzega "
    "przed eskalacją i ryzykiem dla żeglugi w Zatoce Perskiej, a sojusznicy USA w regionie apelują o "
    "deeskalację, obawiając się skutków dla cen ropy."
)
x["sources"]["https://www.euronews.com/2026/07/30/washington-resumes-direct-attacks-on-iran-a-day-after-its-foiled-strikes-on-jordanian-base"] = "Euronews"
x["last_updated"] = "2026-08-01 04:20"

# --- Update: gaza_hamas_rozbrojenie ---
x = by_slug["gaza_hamas_rozbrojenie"]
x["sources"]["https://www.spokesman.com/stories/2026/jul/31/hamas-israel-to-hold-firm-in-gaza-unless-other-sid/"] = "The Spokesman-Review"
x["last_updated"] = "2026-08-01 04:20"

# --- Update: usa_blanche_nominacja_prokurator_generalny ---
x = by_slug["usa_blanche_nominacja_prokurator_generalny"]
x["sources"]["https://www.cnbc.com/2026/07/29/todd-blanche-attorney-general-trump-irs-audit-cornyn.html"] = "CNBC"
x["sources"]["https://www.forbes.com/sites/alisondurkee/2026/07/30/trump-floats-pulling-todd-blanches-nomination-until-cornyn-and-tillis-leave-senate/"] = "Forbes"
x["last_updated"] = "2026-08-01 04:20"

# --- Update: japonia_trzesienie_ziemi_kumamoto (refresh confirmation, count unchanged) ---
x = by_slug["japonia_trzesienie_ziemi_kumamoto"]
x["last_updated"] = "2026-08-01 04:20"

# --- New entry: Russian attack on Lviv/Kryvyi Rih ---
new_entry = {
    "slug": "rosja_atak_lwow_krzywy_rog",
    "category": "world",
    "lead": False,
    "title": "Rosja zmasowanym atakiem rakietowym uderzyla w Lwow i Krzywy Rog, sa ranni i zniszczenia",
    "body": (
        "W nocy z czwartku na piątek, 30 na 31 lipca, Rosja przeprowadziła jeden z największych ostatnio "
        "ataków rakietowo dronowych na Ukrainę, uderzając między innymi w Lwów, Krzywy Róg oraz Kijów, co "
        "potwierdziły niezależnie PAP, RMF24, TVN24 oraz Interia. Według mera Lwowa Andrija Sadowego w "
        "wyniku uderzenia rakietowego w mieście rannych zostało około dwudziestu osób, zapaliły się "
        "budynki mieszkalne, a pod gruzami wciąż mogli znajdować się ludzie, gdy trwała akcja ratunkowa. "
        "Defence24 oraz TVP Info podały, że rosyjskie rakiety balistyczne uderzyły też w Krzywy Róg, "
        "gdzie odnotowano zabitych i rannych. Atak wywołał reakcję po polskiej stronie granicy: jak "
        "informowały RMF24, TVN24 oraz Radio dla Ciebie, w związku ze skalą nalotu polskie wojsko "
        "podniosło w powietrze samoloty myśliwskie, a w Lublinie, Krasnymstawie i innych miejscowościach "
        "Lubelszczyzny około czwartej nad ranem zawyły syreny alarmowe, budząc mieszkańców i wywołując "
        "poruszenie, które opisywały też Dorzeczy oraz rp.pl. Wojsko Polskie zapewniło, że działania "
        "miały charakter prewencyjny i nie odnotowano naruszenia polskiej przestrzeni powietrznej. "
        "Władze ukraińskie zapowiedziały dalsze wsparcie dla poszkodowanych miast i wezwały zachodnich "
        "sojuszników do wzmocnienia obrony przeciwlotniczej."
    ),
    "sources": {
        "https://www.pap.pl/aktualnosci/ukraina-mer-lwowa-okolo-20-rannych-w-miescie-po-rosyjskim-ataku-rakietowym": "PAP",
        "https://www.rmf24.pl/fakty/polska/news-polska-poderwala-mysliwce-mieszkancow-lublina-obudzily-syren,nIdn,1011892": "RMF24",
        "https://tvn24.pl/lublin/rosyjski-atak-na-ukraine-w-lublinie-i-krasnymstawie-zawyly-syreny-st9165102": "TVN24",
        "https://wydarzenia.interia.pl/ukraina-rosja/news-tragiczna-noc-w-ukrainie-ataki-na-lwow-i-krzywy-rog,nId,23521789": "Interia",
        "https://defence24.pl/wojna-na-ukrainie-raport-specjalny-defence24/rosyjskie-rakiety-uderzyly-we-lwow-i-krzywy-rog-sa-zabici-i-ranni": "Defence24",
        "https://dorzeczy.pl/kraj/921973/syreny-alarmowe-o-godz-4-na-lubelszczyznie-polacy-oburzeni-dzialaniem-sluzb.html": "Dorzeczy",
    },
    "last_updated": "2026-08-01 04:20",
}
data.append(new_entry)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("done, total entries:", len(data))
