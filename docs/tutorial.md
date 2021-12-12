# Adicionando cientistas ao sistema Wikidata/Scholia

(Se já conhecer o Wikidata e o Scholia, pule direto para o Passo 1)

## Antes de tudo, por que adicionar alguém ao Wikidata/Scholia?

O [Wikidata](https://www.wikidata.org/) é a base de conhecimento da Wikimedia, a fundação que gere a Wikipédia. No Wikidata, o conhecimento enciclopédico está organizado em uma estrutura de hiperlinks que permite acesso tanto visual quanto computacional a esse conhecimento.

Na prática, o Wikidata torna fácil para pesquisadores e desenvolvedores usarem as informações que estão lá. Não vou entrar em detalhes técnicos, mas é _muito_ mais fácil que lidar com tabelas, ou sistemas como o Lattes e o ORCID.

O [Scholia](https://scholia.toolforge.org/) é um projeto que visa mapear e _toda_ a pesquisa biomédica usando o Wikidata. Uma série de scripts automáticos puxam metadados de artigos pa partir do PubMed e informações de autores a partir do ORCID. Esses bots rodam dia e noite, melhorando o alcance da plataforma.

Bebendo da estrutura do Wikidata, o Scholia gera visualizações automáticas,que compilam informações de diversas esferas, como:

- Autores ([Helder Nakaya](https://scholia.toolforge.org/author/Q42614737))

- Organizações ([Programa de pós em bioinformática da USP](https://scholia.toolforge.org/organization/Q102292035))

- Tópicos ([febre amarela](https://scholia.toolforge.org/topic/Q154874))

- Artigos ([Evolution and epidemic spread of SARS-CoV-2 in Brazil](https://scholia.toolforge.org/work/Q97681095))

![Número de publicações por ano do [Helder Nakaya](https://scholia.toolforge.org/author/Q42614737)](https://cdn-images-1.medium.com/max/2000/1*Nt3TNgUDFfs9o5t2V1qoFQ.png)

_Número de publicações por ano do [Helder Nakaya](https://scholia.toolforge.org/author/Q42614737)_

![Artigos mais recentes publicados por pessoas do [Programa de pós em bioinformática da USP](https://scholia.toolforge.org/organization/Q102292035)](https://cdn-images-1.medium.com/max/2000/1*BdqlCdsbQ3atNl4vGgTHtw.png)

_Artigos mais recentes publicados por pessoas do [Programa de pós em bioinformática da USP](https://scholia.toolforge.org/organization/Q102292035)_

O desafio é que os scripts não conseguem puxar tudo. Muitos autores tem nomes parecido e informações como afiliação a programas de pós-graduação nem sempre são fáceis de achar.

Sendo assim, o sistema depende de nós todos para atingir seu potencial.
Todo mundo pode editar o Wikidata, incluindo a página sobre mim ou a página sobre você. Pode parecer assustador, mas esse modelo “wikipédico” é o que permite o sistema Scholia/Wikidata lidar com a tsunami de informações que existe hoje. Quanto mais gente boa vendo, mais justo o sistema fica.

## “Bacana, mas eu só quero fazer um troço desse pra minha orientadora”

A notícia boa é que dá pra fazer isso rapidinho.

Antes de tudo, uma regra: a Wikidata não é a [casa da mãe joana](https://www.wikidata.org/wiki/Q9698231). Existem certos critérios de notoriedade do Wikidata, e para a pesquisa, a regra é:
_se a pessoa for autor/autora de um artigo revisado por pares, pode entrar._

## **Passo 1: Criando uma conta**

Passo a passo:

- Entre em [wikidata.org](https://www.wikidata.org/wiki/Wikidata:Main_Page)

- Clique no canto superior direito em “Create account” ou “Criar uma conta”

- Crie uma conta, é rápido e fácil

![](https://cdn-images-1.medium.com/max/2000/1*YyaOMgpmDlpjld51V-OHmA.png)

![](https://cdn-images-1.medium.com/max/2000/1*9xp9ZUiVbBU7NrE4xkSx-g.png)

- Agora que você criou uma conta, vai aparecer um monte de coisa introdutória. Pode ignorar tudo e ler depois se quiser, vamos direto ao ponto.

O Wikidata gira em torno de items. Um item no Wikidata pode ser um indivíduo real ou uma organização, ou coisas mais abstratas (como “mitocondria” ou “envelhecimento”). Todas as páginas da Wikipédia têm um item no Wikidata.

Se nosso objetivo é adicionar um pesquisador, o primeiro passo é ver se ele já está no Wikidata. Vá na caixinha de busca por Wikidata e busque pelo nome da pessoa. Por exemplo, para ver se já há um item para o Helder Nakaya, eu procuraria “Helder Nakaya”, “Helder Imoto Takashi Nakaya” e “Helder I Nakaya” antes de criar um novo item.

Obs: Aperte um enter para fazer uma busca com mais profundidade.

![achou](https://cdn-images-1.medium.com/max/2000/1*Idn2f8GbbX_kODLWXF0DTg.png)

_achou_

- Se achar um _item_ para sua pessoa de interesse, pode pular o passo 2 e ir direto para o passo 3. Se não achar, sem problemas, vamos adicionar no passo 2.

## Passo 2: Adicionando um novo item ao Wikidata

Para criar um novo item, vá na barra lateral esquerda (abaixo do símbolo do Wikidata) e clique em “criar um novo item” ou “create a new item”.

![](https://cdn-images-1.medium.com/max/2000/1*HyCyXxoS-80l3ggXVGSNNg.png)

Mude o idioma para ingles, adicione algumas informaçõe básicas e clique em “Criar”. Aqui um exemplo real, criando o item para a [Jaqueline Wang](https://bv.fapesp.br/en/pesquisador/707382/jaqueline-yu-ting-wang/), uma colega que fez o mestrado no programa de Bioinformática da USP:

![](https://cdn-images-1.medium.com/max/2000/1*XCfDYd41VrT9w9KDKI-5dw.png)

Ela ganhou um identificador Q, que aparece ao lado do nome e da URL: [https://www.wikidata.org/wiki/Q106212027](https://www.wikidata.org/wiki/Q106212027)

![](https://cdn-images-1.medium.com/max/2000/1*hdFZsnoBe5vCymWLgJ_Yug.png)

## Passo 3: Adicionando informações básicas ao item

No Wikidata, as informações são armazenadas por meio de _declarações_.
São como campos em um formulário que falam algumas coisas sobre esse item.

O item criado agora ainda não tem nenhuma informação ligada. Caso seja um item pré existente, ele vai ter algumas conexões listadas abaixo do cabeçalho de Declarações.

- De qualquer forma, no fim dessa lista, há um botão escrito “**+ adicionar declaração**”/ “**+add statement**”. Clique nele:

![(pode ser + add statement)](https://cdn-images-1.medium.com/max/2000/1*--_ug30DZG5lM_FSuP0ASw.png)

_(pode ser + add statement)_

O botão abre um formulário genérico para inserir as informações. A primeira informação é que a Jaque é um ser humano. Para isso, começamos a digitar “instancia de” na sessão de propriedades e selecionamos a propriedade “instancia de”.
Agora fazemos o mesmo no campo de valores, na direita, digitamos “humano” e selecionamos o item “ser humano”.

![](https://cdn-images-1.medium.com/max/2000/1*7SONtY35HoHxfvEBxVhG5w.png)

Ao clicar em “publicar”, a declaração é publicada automaticamente no Wikidata, e está disponível em todas as línguas ao mesmo tempo! Esse é um dos benefícios dessa estrutura do Wikidata em comparação com formulários de texto:

![](https://cdn-images-1.medium.com/max/2000/1*JPMl-vrf1TDYSjSIhkQywQ.png)

![](https://cdn-images-1.medium.com/max/2000/1*EBK02GPrpvA2HomBNVnw1A.png)

![](https://cdn-images-1.medium.com/max/2000/1*k1esHH-oW5NnobU_AbCiRg.png)

Vamos adicionar outras informações agora:

- sexo ou genero (_sex or gender_): feminino

![](https://cdn-images-1.medium.com/max/2000/1*Lx3R35iHvgeWRSFOIGgn2A.png)

- ocupação (_occupation_): pesquisador(a)

![](https://cdn-images-1.medium.com/max/2000/1*II2Wi_LBAbGyP0mvJh_7Mg.png)

- afiliação (_affiliation_): Instituto de Biociências da Universidade de São Paulo

![](https://cdn-images-1.medium.com/max/2000/1*hPWCJiuDHtQPut7Fy1AORA.png)

Contudo, colocar só uma declaração é um pouco frágil: como sabemos que uma declaração é verdadeira? Como verificar isso?

![](https://cdn-images-1.medium.com/max/2000/1*5OZazbT1lC9x_yts8Wcufw.png)

![](https://cdn-images-1.medium.com/max/2000/1*O3xMiAjJAochJ8KAp21K3w.png)

O Wikidata auxilia nessa tarefa permitindo a inserção de referências a cada uma das declarações feitas no site. Basta clicar no botão de adicionar referência, e um novo subformulário vai aparecer:

Nele podemos adicionar uma referência.

- URL para referências (_reference URL_): [https://bv.fapesp.br/en/bolsas/189957/development-and-implementation-of-ngs-data-processing-tools-and-database-for-analysis-and-storage-an/](https://bv.fapesp.br/en/bolsas/189957/development-and-implementation-of-ngs-data-processing-tools-and-database-for-analysis-and-storage-an/)

![](https://cdn-images-1.medium.com/max/2000/1*1HX4beOaRQ4jMQOYzD743Q.png)

Exatamente o que significa ser “afiliado” a alguma coisa é um tanto quanto subjetivo. No Wikidata, é um termo bem amplo não significa que alguém é professor, ou tem um vínculo empregatício, um contrato, ou algo do tipo: qualquer coisa que alguém puder considerar uma afiliação, está valendo. Por isso é ainda mais importante ter uma referência.

Se tiver mais de uma afiliação, dá pra adicionar clicando em “_+ add value_”.

Para completar o básico desse item, vou adicionar mais 2 coisas:

- campo de trabalho (_field of work_): bioinformática

- número na Plataforma Lattes (_Lattes ID_): 4694329724121206

![](https://cdn-images-1.medium.com/max/2000/1*LBSA8q7v5TQ30O1pFwdlGg.png)

Vamos ignorar esse ponto de exclamação por enquanto (detalhes técnicos) e seguir adiante.
Dá para adicionar muitas outras informações: ORCID, ID do Google Scholar, ID do Publons e por aí vai. Mas para termos a visualização bonita do Scholia, precisamos conectar os artigos com a pessoa. Para isso, no passo 4, usaremos mais uma ferramenta, o [Author Disambiguator](https://author-disambiguator.toolforge.org/).

## Passo 4: Ligando artigos ao seus autores

O [Author Disambiguator](https://author-disambiguator.toolforge.org/) é uma ferramentinha inteligente que ajuda a trocar as autorias que estão na forma de texto bruto para a forma de links que o Scholia consegue usar.

- A estrutura de organização dessas informações fica mais clara com um exemplo de [artigo](https://www.wikidata.org/wiki/Q94467949):

![](https://cdn-images-1.medium.com/max/2000/1*XK9QpV-xO_Qdi2dP_0p82A.png)

![](https://cdn-images-1.medium.com/max/2000/1*S1oGYO1n1L5Eqz8Z_xiWRA.png)

Nele temos dois autores que já foram desambiguados: [Helder Nakaya](https://www.wikidata.org/wiki/Q42614737) e [Mayana Zatz](https://www.wikidata.org/wiki/Q2920198). Há mais 14 autores nesse artigo, mas nem o script (nem ninguém) ligou com items específicos:

![](https://cdn-images-1.medium.com/max/2000/1*MXZlWeMExPbUNnQiRwPGdQ.png)

Entre eles está a Jaqueline Wang, que acabamos de adicionar ao Wikidata. Poderíamos corrigir na mão, mas isso ficaria rapidamente entediante e é bem passível de erros. Por sorte, o “[Author Disambiguator](http://Author Disambiguator)” faz todo o trabalho duro para a gente, bastando escolhermos visualmente quais artigos são de um certo autor.

- Na página do [Author Disambiguator](https://author-disambiguator.toolforge.org/), a primeira coisa a fazer é o login **de novo** na conta Wikimedia (que criamos no passo 1).

![](https://cdn-images-1.medium.com/max/2000/1*RTkn54Wxl4oHgOOgd_EgOw.png)

![só clicar em Permitir](https://cdn-images-1.medium.com/max/2000/1*kGFPRiEJULPbr5Oe6uMJ7Q.png)

_só clicar em Permitir_

Agora vou buscar por “Jaqueline Wang”, clicar em “Look for author” e ver o que aparece. É comum o sistema demorar *bastante *nas primeiras vezes (aproveite para ajeitar a coluna ou pegar uma água).

![](https://cdn-images-1.medium.com/max/2000/1*a6SvoTtaTo_L2XtAaiHVdA.png)

![](https://cdn-images-1.medium.com/max/2000/1*QPXVTJTxL3nRQN0Ob7nBYw.png)

O Author Disambiguator vai agrupar os artigos de forma automática e arbitrária baseado nos temas e coautorias. No caso, a busca de agora retornou apenas 1 resultado. Para cada artigo, posso marcar os autores que realmente são a pessoa que eu quero adicionar (e não pessoas com nomes parecidos).

![](https://cdn-images-1.medium.com/max/2000/1*c0YF1UjD0CUTFeQZiwYwkw.png)

![](https://cdn-images-1.medium.com/max/2000/1*xUYqmhHWt2FstzpmvfmrJg.png)

Tem uma caixa embaixo de cada grupo escrito “Check all” e “Uncheck all”, que permite marcar vários artigos de uma vez, para facilitar:

![](https://cdn-images-1.medium.com/max/2000/1*rx62Io8x-ttY0UyAUCiPXg.png)

Após ter selecionado todos os artigos do autor de interesse, basta selecionar esse autor na lista de nomes e clicar em “Link selected works to author”. Caso o autor não apareça, dá para adicionar o identificador Q manualmente.

![](https://cdn-images-1.medium.com/max/2000/1*N3fT2yod91MODq8xBO05ow.png)

O sistema vai agora trabalhar para você e fazer todas as alterações em batelada:

![](https://cdn-images-1.medium.com/max/2000/1*VLantiUAu-ayI2TmMk-y4w.png)

Se der uns erros, é normal. Dá para tentar rodar de novo e geralmente funcionad da segunda vez.

Para exemplificar (não precisa fazer isso) vou ao artigo no Wikidata. Se quiser, escolha um artigo que você conectou o autor e veja por lá. Veja aqui que o artigo está ajustado:

![](https://cdn-images-1.medium.com/max/2000/1*XJo2u7WkdAGPh5v-8Ch2nQ.png)

Em paralelo, fiz o mesmo para os artigos que estavam descritos como “Jaqueline Yu Ting Wang”, exatamente do mesmo jeito.

Agora o [Scholia já puxa essas informações ](https://scholia.toolforge.org/author/Q106212027)e gera visualizações ricas, como a rede de coautorias e o mapa de coautores:

![Mapa dos coautores da [Jaqueline Wang](https://scholia.toolforge.org/author/Q106212027)](https://cdn-images-1.medium.com/max/2000/1*3P_ZRho-Pt5KzqeU8OKZew.png)

_Mapa dos coautores da [Jaqueline Wang](https://scholia.toolforge.org/author/Q106212027)_

![Rede dos coautores da [Jaqueline Wang](https://scholia.toolforge.org/author/Q106212027)](https://cdn-images-1.medium.com/max/2000/1*EVfcmKhjwrqYvLRwbz5n8w.png)

_Rede dos coautores da [Jaqueline Wang](https://scholia.toolforge.org/author/Q106212027)_

## Passo 5: Aproveite os dados ligados

Pronto, já fizemos tudo necessário para conectar uma pesquisadora nova ao sistema Scholia/Wikidata. Caso você tenha feito por aí também, parabéns e bem vinda/o ao Wikidata!

Agora você pode conhecer mais sobre a pessoa que você colocou lá no Wikidata, seus colaboradores e tudo mais. Se essa pessoa for você, melhor ainda! Eu descobri coisas sobre minhas coautorias que eu mesmo não sabia.

Com o crescimento da rede interconectada, vários projetos de pesquisa são possíveis: como a rede de pesquisadores mudou ao longo do tempo? Quais áreas do mundo colaboram mais com uma dada instituição? Conseguimos puxar e analisar todas as informações lá, do mesmo jeito que o Scholia faz.

Gostou? Quer contribuir ou saber mais sobre o projeto? Temos um grupo público em [https://t.me/scholiabrasil](https://t.me/scholiabrasil) para dúvidas e ideias de como avançar o projeto, e adoraríamos ver você por lá!
