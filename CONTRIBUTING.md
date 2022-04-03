# Contribuindo para Bioinfo Brasil

O primeiro passo para contribuir para o projeto é achar informação que integre com o tema e que ainda não esteja presente na [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page),
aspectos como programas de pós-graduação,
pesquisadores e suas afiliações são todos bem vindos!

Você pode tentar adicionar essa manualmente usando a ótima interface web da [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page),
para esse fim temos um [tutorial](https://lubianat.github.io/bioinfo_brasil/tutorial.html) que pode ser útil.

No entanto, caso deseje adicionar dados em larga escala, você pode seguir de diferentes maneiras.
Atualmente, o método preferido pelo projeto tem sido utilizar uma combinação de [Notebooks Jupyter](https://pt.wikipedia.org/wiki/Projeto_Jupyter)
para extrair e manipular os dados para um formato adequado para a Wikidata e
Google Sheets para reconciliar a informação a itens já existentes na Wikidata.
No momento,
possuímos dois Jupyter Notebooks na pasta 'tutorial' deste repositório explicando o processo que pode ser usado como modelo, contudo,
o passo-a-passo pode ser descrito como:

- Caso a informação esteja num website - como a página de um programa - raspamos a informação usando um dos pacotes de [raspagem de dados](https://pt.wikipedia.org/wiki/Raspagem_de_dados) do Python, [_beautifulsoup4_](https://www.crummy.com/software/BeautifulSoup/).

- Com os dados extraídos para uma planilha (como um .csv),
  inserimos os dados no Google Sheets, utilizando o add-on [Wikipedia e Wikidata Tools](https://workspace.google.com/marketplace/app/wikipedia_and_wikidata_tools/595109124715) para reconciliar a informação a itens da Wikidata.

- Por fim, criamos um novo Notebook Jupyter onde formataremos os dados reconciliados para um formato aceito pelo [Quickstatements](https://www.wikidata.org/wiki/Help:QuickStatements),
  uma ferramenta que permitirá a adição de informação em lotes para a Wikidata.

Tendo uma contribuição que siga a temática do projeto,
sinta-se livre para criar um [_fork_](https://docs.github.com/pt/get-started/quickstart/fork-a-repo) do repositório e enviar suas contribuições como um [_pull request_](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
