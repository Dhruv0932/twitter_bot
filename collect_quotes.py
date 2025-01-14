import json as _json

import scrapper  as _scrapper

if __name__ == '__main__':
    quotes=_scrapper.scrape_quotes()
    with open("quotes.json", mode="w") as quotes_file:
        _json.dump(quotes, quotes_file, ensure_ascii=False, indent=2 )
    