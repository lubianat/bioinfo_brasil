##########################################################################################################################
#        This generator is broken due to the https://meta.wikimedia.org/wiki/WikiCite/WDQS_graph_split (Jun, 2,2025)     #
#                                                                                                                        #
##########################################################################################################################
import urllib.parse
import yaml
import requests
import re
from mdutils.mdutils import MdUtils


def main():
    mdFile = MdUtils(
        file_name="docs/dashboard.md",
        title="The Landscape of Brazilian Bioinformatics",
    )
    with open("docs/dashboard.yaml", "r") as c:
        config = yaml.load(c.read(), Loader=yaml.FullLoader)
    for category in config["queries"]:
        if category == "general":
            mdFile.new_header(1, "Overview")

            for query in config["queries"]["general"]:
                if query is not None:
                    update_markdown(mdFile, query)

        if category == "software":
            mdFile.new_header(1, "Brazilian bioinformatics software")

            for query in config["queries"]["software"]:
                if query is not None:
                    update_markdown(mdFile, query)

        if category == "thesis":
            mdFile.new_header(1, "University of São Paulo Bioinformatics theses")

            for query in config["queries"]["thesis"]:
                if query is not None:
                    update_markdown(mdFile, query)

    mdFile.create_md_file()


def update_markdown(mdFile, query):
    title, sparql_query = get_sparql_from_shortened_wiki_url(query)
    iframe = render_embedding_iframe(sparql_query)
    mdFile.new_header(2, title)
    mdFile.new_line(iframe)
    mdFile.new_line("")


def get_sparql_from_shortened_wiki_url(wiki_url):
    session = requests.Session()  # so connections are recycled

    full_uri = session.head(wiki_url, allow_redirects=True).url
    sparql_query = urllib.parse.unquote(full_uri.split(".org/")[-1])
    sparql_query = sparql_query.replace("embed.html#", "")
    title_search = re.search("title:(.*)\n", sparql_query, re.IGNORECASE)
    title = title_search.group(1)
    return title, sparql_query


def render_embedding_iframe(query):
    url = render_embedding_url(query)
    return (
        """<iframe style="width: 80%; height: 50vh; border: none;" """
        f"""src="{url}" referrerpolicy="origin" """
        """sandbox="allow-scripts allow-same-origin allow-popups"></iframe>"""
    )


def render_embedding_url(query):
    return "https://query.wikidata.org/embed.html#" + urllib.parse.quote(query, safe="")


if __name__ == "__main__":
    main()
