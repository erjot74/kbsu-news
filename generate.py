import json
import sys
import urllib.parse
from datetime import datetime
try:
    from zoneinfo import ZoneInfo
    WARSAW = ZoneInfo("Europe/Warsaw")
except Exception:
    WARSAW = None

DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
DATA_PATH = f"data/{DATE}.json"

MONTHS_PL = ["stycznia","lutego","marca","kwietnia","maja","czerwca",
             "lipca","sierpnia","września","października","listopada","grudnia"]

def pl_date_str(dt):
    return f"{dt.day} {MONTHS_PL[dt.month-1]} {dt.year}"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

def is_polish_source(name):
    # crude heuristic: known polish outlets
    polish_markers = ["PAP","RMF24","TVN24","Interia","rp.pl","WP","Onet","Polsat",
                       "Gazeta","Bankier","Money.pl","Niezalezna","Wprost","Dorzeczy",
                       "Infosecurity24","Lublin112","TVP","Radio","Kresy","Euractiv.pl",
                       "Zielona","Goniec","Kronika24","Koteria","Parkiet","Comparic",
                       "Strefa Inwestorow","Forsal","StockWatch","Dziennik","Portal",
                       "Kaszuby","Farmer.pl","Biznesinfo","Eska","Super Express","se.pl",
                       "Nettg","Wgospodarce","Polskie Radio","Agroprofil","Defence24",
                       "Demagog","Episkopat","IPN","OKO.press","Lowcyburz","histmag",
                       "WNP.pl","Super Biznes","Konflikty","Wszystko co najwazniejsze",
                       "Wszystko co najważniejsze","TVN","Dzien Dobry"]
    return any(m.lower() in name.lower() for m in polish_markers)

def render_sources(sources):
    parts = []
    for url, name in sources.items():
        translate = ""
        if not is_polish_source(name):
            enc = urllib.parse.quote(url, safe="")
            translate = f' <a class="translate-link" href="https://translate.google.com/translate?sl=auto&tl=pl&u={enc}">tłumacz</a>'
        parts.append(f'<a href="{url}" target="_blank" rel="noopener">{name}</a>{translate}')
    return " &middot; ".join(parts)

def render_story(x):
    cls = "story lead" if x.get("lead") else "story"
    title = x["title"]
    body = x["body"]
    src_html = render_sources(x["sources"])
    return f'''    <article class="{cls}">
      <h3>{title}</h3>
      <p>{body}</p>
      <div class="src">Źródło(a): {src_html}</div>
    </article>'''

def category_html(cat_key):
    items = [x for x in data if x["category"] == cat_key]
    # sort: lead first, then by last_updated desc
    def sort_key(x):
        return (0 if x.get("lead") else 1, x["last_updated"])
    items_sorted_for_display = sorted(items, key=lambda x: x["last_updated"], reverse=True)
    # cap to 15 most recently updated, but always include lead
    lead_items = [x for x in items if x.get("lead")]
    non_lead_sorted = sorted([x for x in items if not x.get("lead")], key=lambda x: x["last_updated"], reverse=True)
    capped = non_lead_sorted[:15 - len(lead_items)] if len(lead_items) <= 15 else []
    display_list = lead_items + capped
    # order: lead first, then rest by last_updated desc
    rest = sorted([x for x in display_list if not x.get("lead")], key=lambda x: x["last_updated"], reverse=True)
    ordered = lead_items + rest
    html_parts = [render_story(x) for x in ordered]
    return "\n".join(html_parts), len(items), len(ordered)

pl_html, pl_total, pl_shown = category_html("pl")
world_html, world_total, world_shown = category_html("world")

most_recent = max((x["last_updated"] for x in data), default=None)
if most_recent:
    now = datetime.strptime(most_recent, "%Y-%m-%d %H:%M")
    time_part = now.strftime('%H:%M')
else:
    now = datetime.now(WARSAW) if WARSAW else datetime.now()
    time_part = now.strftime('%H:%M')
meta_line = f"Aktualizacja: {pl_date_str(now)}, {time_part}, wygenerowano automatycznie"

html = f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Podsumowanie dnia: Polska i Świat</title>
<meta name="description" content="Regularnie aktualizowane, zweryfikowane podsumowanie najważniejszych wiadomości z Polski i świata.">
<style>
  :root{{--bg:#0b0d10;--panel:#14171c;--panel-2:#1b1f26;--border:#262b33;--text:#eef1f5;--text-dim:#9aa4b2;--accent:#e6473a;--accent-2:#3aa6e6;--maxw:920px;}}
  *{{box-sizing:border-box;}}
  html,body{{margin:0;padding:0;}}
  body{{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.55;}}
  a{{color:var(--accent-2);text-decoration:none;}}
  a:hover{{text-decoration:underline;}}
  header.site{{border-bottom:1px solid var(--border);padding:28px 20px 22px;background:linear-gradient(180deg,#14171c 0%,#0b0d10 100%);}}
  .wrap{{max-width:var(--maxw);margin:0 auto;padding:0 8px;}}
  .brand h1{{font-size:22px;margin:0;letter-spacing:0.2px;}}
  .brand h1 span{{color:var(--text-dim);font-weight:400;}}
  .meta-line{{color:var(--text-dim);font-size:13px;margin-top:6px;}}
  .verified-badge{{display:inline-flex;align-items:center;gap:6px;background:rgba(58,166,42,0.12);border:1px solid rgba(58,166,42,0.35);color:#7bd88f;font-size:12px;padding:4px 10px;border-radius:999px;margin-top:10px;}}
  main{{max-width:var(--maxw);margin:0 auto;padding:28px 20px 60px;}}
  section.category{{margin-bottom:38px;}}
  .cat-header{{display:flex;align-items:center;gap:10px;margin-bottom:16px;}}
  .cat-tag{{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.6px;padding:4px 10px;border-radius:6px;}}
  .cat-tag.pl{{background:rgba(230,71,58,0.15);color:#ff8377;border:1px solid rgba(230,71,58,0.4);}}
  .cat-tag.world{{background:rgba(58,166,230,0.15);color:#7cc8f5;border:1px solid rgba(58,166,230,0.4);}}
  .cat-header h2{{font-size:13px;color:var(--text-dim);margin:0;font-weight:600;text-transform:uppercase;letter-spacing:0.5px;}}
  article.story{{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:18px 20px;margin-bottom:12px;}}
  article.story.lead{{background:var(--panel-2);border-color:#33261f;}}
  article.story h3{{margin:0 0 8px;font-size:17px;font-weight:650;}}
  article.story p{{margin:0;color:#d6dbe2;font-size:14.5px;}}
  article.story .src{{margin-top:10px;font-size:12.5px;color:var(--text-dim);}}
  article.story .src a{{color:var(--accent-2);}}
  .translate-link{{display:inline-flex;align-items:center;gap:4px;font-size:11.5px;color:#c9a227;text-decoration:none;border:1px solid rgba(201,162,39,0.4);background:rgba(201,162,39,0.1);padding:1px 7px;border-radius:5px;margin-left:6px;}}
  footer.site{{border-top:1px solid var(--border);padding:24px 20px 40px;color:var(--text-dim);font-size:12.5px;}}
  @media (max-width:520px){{.brand h1{{font-size:19px;}}article.story h3{{font-size:16px;}}}}
</style>
</head>
<body>
<header class="site"><div class="wrap">
  <div class="brand"><h1>Podsumowanie dnia <span>: Polska i Świat</span></h1></div>
  <div class="meta-line">{meta_line}</div>
  <div class="verified-badge">zweryfikowane w co najmniej dwóch niezależnych, wiarygodnych źródłach</div>
  <div class="meta-line" style="margin-top:8px;"><a href="https://erjot74.github.io/kbsu-news/archive/" target="_blank" rel="noopener">Archiwum poprzednich wydań (30 dni)</a></div>
</div></header>
<main>
  <section class="category">
    <div class="cat-header"><span class="cat-tag pl">Polska</span><h2>Najważniejsze wydarzenia z kraju</h2></div>
{pl_html}
  </section>
  <section class="category">
    <div class="cat-header"><span class="cat-tag world">Świat</span><h2>Najważniejsze wydarzenia ze świata</h2></div>
{world_html}
  </section>
</main>
<footer class="site"><div class="wrap">
  <div>Treść generowana automatycznie, weryfikowana i sprawdzana pod kątem fałszywych informacji w co najmniej dwóch niezależnych, wiarygodnych źródłach przed publikacją.</div>
  <div>Strona aktualizowana automatycznie co godzinę, z zachowaniem pełnej listy newsów z całego dnia.</div>
  <div><a href="https://erjot74.github.io/kbsu-news/archive/" target="_blank" rel="noopener">Zobacz archiwum poprzednich wydań</a></div>
</div></footer>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"pl total={pl_total} shown={pl_shown}")
print(f"world total={world_total} shown={world_shown}")
print("index.html written")
