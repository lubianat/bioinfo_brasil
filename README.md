# Bioinfo Brasil - Scholia / Wikidata

## Planejamento


Escopos: bioinformatas que tenham atuado no Brasil e tenham ao menos 1 artigo publicado como autor. 

1. Listar bioinformatas do Brasil
- Listar os professores afiliados aos programas de bioinfo do Brasil (FioCruz, USP, UFMG, UFRN, UFPR...)
- Listar os egressos dos programas de bioinfo do Brasil

1. Mapear pesquisadores aos programas afiliados no Wikidata. Para cada programa:
- Para cada pesquisador da lista:

- Localizar o item do pesquisador, caso exista, ou criar um novo. Exemplo de item: Helder Nakaya (Q42614737)
- Mapear artigos ao pesquisador usando a ferramenta Author Disambiguator
- Adicionar a afiliação ao programa específico de cada um.
- Adicionar, se possível, detalhes adicionais, como sexo/genero, nacionalidade, data de nascimento, local de nascimento etc (a partir de informações publicamente disponíveis)
- Adicionar campo de trabalho (P101) bioinformática


## Estrutura do Repositório:

- organizações 
  - USP
  - UFRN
  - UFMG
  - FioCruz
  - LNCC
  - UFPR
  - etc

- utils
  - utils.py
  
Para cada organização:

- organização (ex: USP)
  - README.md
  - professores.txt (lista de nomes) 
  - egressos.txt (lista de nomes)
  - src (código associado a esse processamento)
  - (...)
  - 
## Exemplos de tarefas parcialmente concluídas:

- [Programa de bioinformática da USP](https://scholia.toolforge.org/organization/Q102292035)
 ]