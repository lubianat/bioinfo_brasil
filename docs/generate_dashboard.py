import urllib.parse
import yaml
import requests
import re
from mdutils.mdutils import MdUtils


def main():
    mdFile = MdUtils(
        file_name="docs/auto_dashboard.md",
        title="The Landscape of Brazilian Bioinformatics",
    )
    with open("docs/dashboard.yaml", "r") as c:
        config = yaml.load(c.read(), Loader=yaml.FullLoader)
    for query in config["queries"]:
        if query is not None:
            title, sparql_query = get_sparql_from_shortened_wiki_url(query)
            iframe = render_embedding_iframe(sparql_query)
            mdFile.new_header(1, title)
            mdFile.new_line(iframe)
    mdFile.create_md_file()


def get_sparql_from_shortened_wiki_url(wiki_url):
    session = requests.Session()  # so connections are recycled

    full_uri = session.head(wiki_url, allow_redirects=True).url
    sparql_query = urllib.parse.unquote(full_uri.split(".org/")[-1])
    title_search = re.search("title:(.*)\n", sparql_query, re.IGNORECASE)
    title = title_search.group(1)
    return title, sparql_query


def render_embedding_iframe(query):
    url = render_embedding_url(query)
    return f"""
    <iframe style="width: 150%; height: 50vh; border: none;"
    src={url}
    referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>"""


def render_embedding_url(query):
    return "https://query.wikidata.org/embed.html#" + urllib.parse.quote(query, safe="")


if __name__ == "__main__":
    main()
