# Bioinfo Brasil - Scholia / Wikidata

### \- [Dashboard](https://lubianat.github.io/bioinfo_brasil/dashboard) - [Tutorial](https://lubianat.github.io/bioinfo_brasil/tutorial.html) - [Página no Wikidata](https://www.wikidata.org/wiki/Wikidata:WikiProject_Scholia/Bioinform%C3%A1tica_brasileira) -

Um projeto para mapear todo os pesquisadores brasileiros da área
de bioinformática e conectá-los entre si através do sistema
Wikidata/Scholia.

## Planejamento

Escopos: bioinformatas que tenham atuado no Brasil e tenham ao menos 1 artigo publicado como autor.

- Listar bioinformatas do Brasil

  - Listar os professores afiliados aos programas de bioinfo do Brasil (FioCruz, USP, UFMG, UFRN, UFPR...)
  - Listar os egressos dos programas de bioinfo do Brasil

- Mapear pesquisadores aos programas afiliados no Wikidata. Para cada programa:

  - Para cada pesquisador da lista:

  - Localizar o item do pesquisador, caso exista, ou criar um novo. Exemplo de item: Helder Nakaya (Q42614737)
  - Mapear artigos ao pesquisador usando a ferramenta Author Disambiguator
  - Adicionar a afiliação ao programa específico de cada um.
  - Adicionar, se possível, detalhes adicionais, como sexo/genero, nacionalidade, data de nascimento, local de nascimento etc (a partir de informações publicamente disponíveis)

- Adicionar campo de trabalho (P101) bioinformática

## Tutoriais

- Alguns tutoriais relativos à integração de programas, eventos e instituições na Wikidata podem ser encontrados no diretório `tutorial/` deste repositório.
- Tutorial no Google Colab: <a href="https://colab.research.google.com/github/lubianat/bioinfo_brasil/blob/master/tutorial/template_raspar_scholia.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Exemplos de tarefas parcialmente concluídas:

- [Programa de bioinformática da USP](https://scholia.toolforge.org/organization/Q102292035)
