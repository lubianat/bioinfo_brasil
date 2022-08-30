import urllib.parse

import requests
import re


def main():
    get_sparql_from_shortened_wiki_url("https://w.wiki/5dpU")


def get_sparql_from_shortened_wiki_url(wiki_url):
    full_uri = requests.head(wiki_url).headers["location"]
    sparql_query = urllib.parse.unquote(full_uri.split(".org/")[-1])
    title_search = re.search("title:(.*)\n", sparql_query, re.IGNORECASE)
    title = title_search.group(1)
    return sparql_query


def render_embedding_url(query):
    return "https://query.wikidata.org/embed.html#" + urllib.parse.quote(query, safe="")


if __name__ == "__main__":
    main()
