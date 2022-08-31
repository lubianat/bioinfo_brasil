
The Landscape of Brazilian Bioinformatics
=========================================

# Overview

##  Institutions related to Brazilian bioinformaticians
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20Institutions%20related%20to%20Brazilian%20bioinformaticians%0A%23defaultView%3AMap%0ASELECT%20DISTINCT%0A%3Forganization%20%3ForganizationLabel%20%0A%3Fsample_author%20%3Fsample_authorLabel%0A%3Fgeo%20%3Flayer%0A%20WITH%20%7B%0A%20%20%20%20SELECT%20DISTINCT%20%3Forganization%20%3Fgeo%20%0A%20%20%20%20%28SAMPLE%28%3Fauthor%29%20as%20%3Fsample_author%29%20WHERE%20%7B%0A%0A%20%20%7B%3Fauthor%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20UNION%0A%20%20%7B%3Fauthor%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20%0A%20%20%3Fauthor%20wdt%3AP101%20wd%3AQ128570%20.%20%20%20%20%0A%20%20%3Fauthor%20%28%20wdt%3AP108%20%7C%20wdt%3AP463%20%7C%20wdt%3AP1416%20%29%20%2F%20wdt%3AP361%2A%20%3Forganization%20.%20%0A%20%20%3Forganization%20wdt%3AP625%20%3Fgeo%20.%0A%20%20%20%20%7D%0A%20%20%20%20GROUP%20BY%20%3Forganization%20%3Fgeo%20%3Fcount%0A%20%20%20%20ORDER%20BY%20DESC%20%28%3Fcount%29%0A%20%20%20%20LIMIT%202000%0A%20%20%7D%20AS%20%25organizations%0A%20%20WHERE%20%7B%0A%20%20%20%20INCLUDE%20%25organizations%0A%20%20%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%20%20%20%20%20%20%20%0A%20%20%7D%0A%20%20ORDER%20BY%20DESC%20%28%3Fcount%29%0A%0A%0A%20%20"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Bioinformaticians that were/are on Brazil
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20Bioinformaticians%20that%20were%2Fare%20on%20Brazil%0ASELECT%20%3FauthorLabel%20%28COUNT%28DISTINCT%20%3Fwork%29%20AS%20%3Fn%29%20%3Fauthor%20%3Forcid%20WHERE%20%7B%0A%20%20%20%20%3Fauthor%20wdt%3AP101%20wd%3AQ128570%20.%0A%20%20%20%20hint%3APrior%20hint%3ArunFirst%20true%20.%0A%20%20%7B%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155%3B%0A%20%20%7D%0A%20%20UNION%0A%20%20%7B%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%0A%20%20%7D%0A%20%20%3Fwork%20wdt%3AP50%20%3Fauthor.%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fauthor%20wdt%3AP496%20%3Forcids.%0A%20%20%20%20BIND%28IRI%28CONCAT%28%22https%3A%2F%2Forcid.org%2F%22%2C%20%3Forcids%29%29%20AS%20%3Forcid%29%0A%20%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cda%2Cde%2Ces%2Cfr%2Cjp%2Cnl%2Cno%2Cru%2Csv%2Czh%22.%20%7D%0A%7D%0AGROUP%20BY%20%3Fauthor%20%3FauthorLabel%20%3Forcid%0AORDER%20BY%20DESC%20%28%3Fn%29"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Co-authorship network of bioinformaticians in Brazil
  
<iframe style="width: 80%; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#%23%23title%3A%20Co-
authorship%20network%20of%20bioinformaticians%20in%20Brazil%0A%23%20tool%3A%20scholia%0A%23defaultView%3AGraph%0ASELECT%0A%20%20%3Fauthor1%20%3Fauthor1Label%20%3Fimage1%20%3Frgb%0A%20%20%3Fauthor2%20%3Fauthor2Label%20%3Fimage2%20%0AWITH%20%7B%0A%20%20SELECT%0A%20%20%20%20%3Fauthor1%20%28SAMPLE%28%3Fimage1_%29%20AS%20%3Fimage1%29%0A%20%20%20%20%3Fauthor2%20%28SAMPLE%28%3Fimage2_%29%20AS%20%3Fimage2%29%0A%20%20%20%20%3Frgb%0A%20%20WHERE%20%7B%0A%0A%20%20%20%20%0A%20%20%20%20%7B%3Fauthor1%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution1.%0A%20%20%20%20%20%3Finstitution1%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20%20%20%0A%20%20%20%20%7B%3Fauthor2%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution2.%0A%20%20%20%20%20%3Finstitution2%20wdt%3AP17%20wd%3AQ155.%7D%0A%0A%20%20%20%20%3Fauthor2%20wdt%3AP101%20wd%3AQ128570%20.%0A%20%20%20%20%3Fauthor2%20wdt%3AP101%20wd%3AQ128570%20.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor1%20wdt%3AP21%20%3Fgender%20.%20%7D%0A%20%20%20%20BIND%28%20IF%28%3Fgender%20%3D%20wd%3AQ6581072%2C%20%22008080%22%2C%22B5651D%22%29%20AS%20%3Frgb%29%0A%20%20%20%20%0A%20%20%20%20%3Fwork%20wdt%3AP50%20%3Fauthor1%20%2C%20%3Fauthor2%20.%0A%20%20%20%20%0A%20%20%20%20%23%20Only%20display%20co-
authorship%20for%20certain%20types%20of%20documents%0A%20%20%20%20%23%20Journal%20and%20conference%20articles%2C%20books%2C%20not%20%28yet%3F%29%20software%0A%20%20%20%20VALUES%20%3Fpublication_type%20%7B%20wd%3AQ13442814%20wd%3AQ571%20wd%3AQ26973022%20wd%3AQ17928402%20wd%3AQ947859%20wd%3AQ54670950%20%7D%0A%20%20%20%20FILTER%20EXISTS%20%7B%20%3Fwork%20wdt%3AP31%20%3Fpublication_type%20.%20%7D%0A%0A%20%20%20%20%23%20No%20self-
links.%0A%20%20%20%20FILTER%20%28%3Fauthor1%20%21%3D%20%3Fauthor2%29%0A%20%20%20%20%23%20Images%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor1%20wdt%3AP18%20%3Fimage1_%20%7D%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor2%20wdt%3AP18%20%3Fimage2_%20%7D%0A%20%20%7D%0A%20%20GROUP%20BY%20%3Fauthor1%20%3Fauthor2%20%20%20%20%20%3Frgb%0A%7D%20AS%20%25result%0AWHERE%20%7B%0A%20%20INCLUDE%20%25result%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cda%2Cde%2Ces%2Cfr%2Cjp%2Csv%2Cru%2Czh%22.%0A%20%20%7D%0A%7D%0A"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Recent articles by brazilian bioinformaticians
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20Recent%20articles%20by%20brazilian%20bioinformaticians%0ASELECT%20DISTINCT%0A%20%20%3FworkLabel%0A%20%20%3FvenueLabel%0A%20%20%28GROUP_CONCAT%28DISTINCT%20%3Fauthor_label%3B%20separator%3D%22%2C%20%22%29%20AS%20%3Fauthors%29%0A%20%20%28MIN%28%3Fdates%29%20AS%20%3Fdate%29%0A%20%20%28URI%28CONCAT%28%27https%3A%2F%2Fdoi.org%2F%27%2C%20%3FDOI_%29%29%20AS%20%3FDOI%29%0A%20%20%3Fwork%20%0A%20%20WHERE%20%7B%0A%20%20%7B%3Fauthor%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20%3Fauthor%20wdt%3AP101%20wd%3AQ128570%20.%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%3Fwork%20wdt%3AP50%20%3Fauthor.%0A%20%20%3Fauthor%20rdfs%3Alabel%20%3Fauthor_label%20.%20FILTER%20%28LANG%28%3Fauthor_label%29%20%3D%20%27en%27%29%0A%20%20%3Fwork%20wdt%3AP577%20%3Fdatetimes%20.%0A%20%20BIND%28xsd%3Adate%28%3Fdatetimes%29%20AS%20%3Fdates%29%0A%20%20OPTIONAL%20%7B%20%3Fwork%20wdt%3AP356%20%3FDOI_%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fwork%20wdt%3AP1433%20%3Fvenue%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cda%2Cde%2Ces%2Cfr%2Cjp%2Cno%2Cru%2Csv%2Czh%22.%20%7D%20%20%0A%20%20%7D%0A%20%20GROUP%20BY%20%3Fwork%20%3FworkLabel%20%3FvenueLabel%20%3FDOI_%0A%20%20ORDER%20BY%20DESC%28%3Fdate%29%20%20%0ALIMIT%20100%0A%20%20"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Top 20 common topics on Brazilian Bioinformatics
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20Top%2020%20common%20topics%20on%20Brazilian%20Bioinformatics%0A%23defaultView%3ABubbleChart%0A%20%20SELECT%20%0A%20%20%3FthemeLabel%20%0A%20%20%3Fn%0A%20%20%3Fexample_workLabel%20%0A%20%20%3Ftheme%20%0A%20%20%3Fexample_work%20%0A%20%20WITH%20%7B%0A%20%20%20%20SELECT%20%28COUNT%28%3Fwork%29%20AS%20%3Fn%29%20%3Ftheme%20%28SAMPLE%28%3Fwork%29%20AS%20%3Fexample_work%29%0A%20%20%20%20WHERE%20%7B%0A%20%20%20%20%0A%20%20%7B%3Fauthor%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20%0A%20%20%3Fauthor%20wdt%3AP101%20wd%3AQ128570%20.%20%20%20%0A%20%20%3Fwork%20wdt%3AP50%20%3Fauthor.%0A%20%20%3Fwork%20wdt%3AP921%20%3Ftheme%20.%0A%20%20%20%20%7D%0A%20%20%20%20GROUP%20BY%20%3Ftheme%0A%20%20%7D%20AS%20%25result%0A%20%20WHERE%20%7B%0A%20%20%20%20INCLUDE%20%25result%0A%20%20%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cda%2Cde%2Ces%2Cfr%2Cjp%2Cnl%2Cno%2Cru%2Csv%2Czh%22%20.%20%7D%20%0A%20%20%7D%0AORDER%20BY%20DESC%28%3Fn%29%20%0ALIMIT%2020%0A%20%20"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

## Gender distribution in different Brazilian bioinformatics institutions
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3AGender%20distribution%20in%20different%20Brazilian%20bioinformatics%20institutions%0A%23defaultView%3ABarChart%0ASELECT%20%20%3FinstitutionLabel%20%28COUNT%28%3Fgender%29%20AS%20%3FgenderCount%29%20%20%3FgenderLabel%20WHERE%20%7B%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155%3B%0A%20%20%20%20wdt%3AP101%20wd%3AQ128570.%0A%20%20%3Fauthor%20wdt%3AP1416%20%3Finstitution%3B%0A%20%20%20%20wdt%3AP21%20%3Fgender.%0A%20%20%3Finstitution%20wdt%3AP101%20%3Ffield%20.%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D%0AGROUP%20BY%20%20%3Fgender%20%3FgenderLabel%20%3Finstitution%20%3FinstitutionLabel%0AHAVING%20%28COUNT%28DISTINCT%20%3Ffield%29%20%3D%201%29%0A%0AORDER%20BY%20DESC%20%28%3FgenderCount%29%0A"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

# Brazilian bioinformatics software

##  Brazilian bioinformatics software
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20Brazilian%20bioinformatics%20software%0ASELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20WHERE%20%7B%0A%20%20%3Fitem%20%28wdt%3AP31%2F%28wdt%3AP279%2A%29%29%20wd%3AQ7397.%0A%20%20%7B%0A%20%20%20%20%3Fitem%20wdt%3AP1343%20%3Fpaper.%0A%20%20%20%20%3Fpaper%20wdt%3AP50%20%3Fauthor.%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP463%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%0A%20%20%7D%0A%20%20UNION%0A%20%20%7B%0A%20%20%20%20%3Fitem%20%28wdt%3AP126%7Cwdt%3AP178%29%20%3Fauthor.%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP463%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%0A%20%20%7D%0A%20%20%3Finstitution%20wdt%3AP101%20wd%3AQ128570.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22pt-
br%2Cen%22.%20%7D%0A%7D" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

## Em que revistas o software de bioinformática brasileiro tende a ser publicado?
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3AEm%20que%20revistas%20o%20software%20de%20bioinform%C3%A1tica%20brasileiro%20tende%20a%20ser%20publicado%3F%0A%23defaultView%3ABubbleChart%0ASELECT%20DISTINCT%20%3FjournalLabel%20%28COUNT%28DISTINCT%20%3Fitem%29%20AS%20%3FsoftCount%29%20WHERE%20%7B%0A%20%20%3Fitem%20%28wdt%3AP31%2F%28wdt%3AP279%2A%29%29%20wd%3AQ7397%3B%0A%20%20%20%20wdt%3AP1343%20%3Fpaper.%0A%20%20%3Fpaper%20wdt%3AP50%20%3Fauthor.%0A%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP463%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155%3B%0A%20%20%20%20wdt%3AP101%20wd%3AQ128570.%0A%20%20%3Fpaper%20wdt%3AP1433%20%3Fjournal.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22pt-
br%2Cen%22.%20%7D%0A%7D%0AGROUP%20BY%20%3FjournalLabel" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin
 allow-popups"></iframe>  

## Quais pacotes bioconductor autores associados ao Brasil na sua publicação?
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3AQuais%20pacotes%20bioconductor%20autores%20associados%20ao%20Brasil%20na%20sua%20publica%C3%A7%C3%A3o%3F%0A%23defaultView%3ABubbleChart%0ASELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20%28COUNT%28DISTINCT%20%3Fauthor%29%20AS%20%3Fauthors%29%20WHERE%20%7B%0A%20%20%3Fitem%20wdt%3AP10892%20%3Fproject_id%20%3B%0A%20%20%20%20wdt%3AP1343%20%3Fpaper.%0A%20%20%3Fpaper%20wdt%3AP50%20%3Fauthor.%0A%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP463%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22pt-
br%2Cen%22.%20%7D%0A%7D%0AGROUP%20BY%20%3Fitem%20%3FitemLabel" referrerpolicy="origin" sandbox="allow-scripts allow-
same-origin allow-popups"></iframe>  

##  Brazilian bioinformatics databases
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20Brazilian%20bioinformatics%20databases%0ASELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20WHERE%20%7B%0A%20%20%3Fitem%20%28wdt%3AP31%2F%28wdt%3AP279%2A%29%29%20wd%3AQ8513.%0A%20%20%7B%0A%20%20%20%20%3Fitem%20wdt%3AP1343%20%3Fpaper.%0A%20%20%20%20%3Fpaper%20wdt%3AP50%20%3Fauthor.%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP463%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%0A%20%20%7D%0A%20%20UNION%0A%20%20%7B%0A%20%20%20%20%3Fitem%20%28wdt%3AP126%7Cwdt%3AP178%29%20%3Fauthor.%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP463%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%0A%20%20%7D%0A%20%20%3Fauthor%20wdt%3AP101%20wd%3AQ128570.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22pt-
br%2Cen%22.%20%7D%0A%7D" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

# University of São Paulo Bioinformatics theses

##  USP Bioinformatics theses on Wikidata
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20USP%20Bioinformatics%20theses%20on%20Wikidata%0ASELECT%20%3Fitem%20%3FitemLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP4101%20%3Fstatement%20.%20%0A%20%20%3Fstatement%20ps%3AP4101%20wd%3AQ835960%20.%20%0A%20%20%3Fstatement%20pq%3AP9945%20wd%3AQ102292035%20.%20%0A%0A%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20en%20language%0A%7D"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Tópicos mais comuns nas teses do programa
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23%23title%3A%20T%C3%B3picos%20mais%20comuns%20nas%20teses%20do%20programa%0ASELECT%20DISTINCT%20%3Ftopic%20%3FtopicLabel%0A%28COUNT%20%28DISTINCT%20%3Fitem%29%20as%20%3Fcount%29%0A%28SAMPLE%28%3Fitem%29%20as%20%3Fsample_item%29%0A%28SAMPLE%28%3FitemLabel%29%20as%20%3Fsample_itemLabel%29%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP4101%20%3Fstatement%20.%20%0A%20%20%3Fstatement%20ps%3AP4101%20wd%3AQ835960%20.%20%0A%20%20%3Fstatement%20pq%3AP9945%20wd%3AQ102292035%20.%20%0A%20%20%0A%20%20%3Fitem%20wdt%3AP921%20%3Ftopic%20.%20%0A%20%20%20%20%0A%20%20%3Ftopic%20rdfs%3Alabel%20%3FtopicLabel.%20%0A%20%20FILTER%20%28LANG%20%28%3FtopicLabel%29%20%3D%20%22en%22%29%0A%20%20%0A%20%20%3Fitem%20rdfs%3Alabel%20%3FitemLabel.%20%0A%20%20FILTER%20%28LANG%20%28%3FitemLabel%29%20%3D%20%22en%22%29%0A%20%20%0A%7D%0AGROUP%20BY%20%3Ftopic%20%3FtopicLabel%0AORDER%20BY%20DESC%28%3Fcount%29"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Maiores teses do programa de bioinformática da USP catalogadas no Wikidata
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#embed.html%23%23title%3A%20Maiores%20teses%20do%20programa%20de%20bioinform%C3%A1tica%20da%20USP%20catalogadas%20no%20Wikidata%0ASELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20%3Fn_pages%20%20%20%3Fauthor%20%20%3FauthorLabel%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP4101%20%3Fstatement%20.%20%0A%20%20%3Fstatement%20ps%3AP4101%20wd%3AQ835960%20.%20%0A%20%20%3Fstatement%20pq%3AP9945%20wd%3AQ102292035%20.%20%0A%20%20%0A%20%20%3Fitem%20wdt%3AP1104%20%3Fn_pages%20.%0A%20%20%3Fitem%20wdt%3AP50%20%3Fauthor%20.%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20en%20language%0A%7D%0AORDER%20BY%20DESC%28%3Fn_pages%29"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Média de páginas das teses do programa de bioinformática da USP catalogadas no Wikidata
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#embed.html%23%23title%3A%20M%C3%A9dia%20de%20p%C3%A1ginas%20das%20teses%20do%20programa%20de%20bioinform%C3%A1tica%20da%20USP%20catalogadas%20no%20Wikidata%0ASELECT%20%0A%3Ftype%20%20%3FtypeLabel%20%28AVG%28%3Fn_pages%29%20as%20%3Faverage_page_count%29%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP4101%20%3Fstatement%20.%20%0A%20%20%3Fstatement%20ps%3AP4101%20wd%3AQ835960%20.%20%0A%20%20%3Fstatement%20pq%3AP9945%20wd%3AQ102292035%20.%20%0A%20%20%0A%20%20%3Fitem%20wdt%3AP31%20%3Ftype%20.%20%0A%20%20%0A%20%20%3Fitem%20wdt%3AP1104%20%3Fn_pages%20.%0A%20%20%3Fitem%20wdt%3AP50%20%3Fauthor%20.%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20en%20language%0A%7D%0AGROUP%20BY%20%3Ftype%20%20%3FtypeLabel"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Pessoas que mais foram bancas nas defesas do programa
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#embed.html%23%23title%3A%20Pessoas%20que%20mais%20foram%20bancas%20nas%20defesas%20do%20programa%0ASELECT%20DISTINCT%20%3Fcommittee_member%20%3Fcommittee_memberLabel%0A%28COUNT%20%28DISTINCT%20%3Fitem%29%20as%20%3Fcount%29%0A%28SAMPLE%28%3Fitem%29%20as%20%3Fsample_item%29%0A%28SAMPLE%28%3FitemLabel%29%20as%20%3Fsample_itemLabel%29%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP4101%20%3Fstatement%20.%20%0A%20%20%3Fstatement%20ps%3AP4101%20wd%3AQ835960%20.%20%0A%20%20%3Fstatement%20pq%3AP9945%20wd%3AQ102292035%20.%20%0A%20%20%0A%20%20%3Fitem%20wdt%3AP9161%20%3Fcommittee_member%20.%20%0A%20%20%20%20%0A%20%20%3Fcommittee_member%20rdfs%3Alabel%20%3Fcommittee_memberLabel.%20%0A%20%20FILTER%20%28LANG%20%28%3Fcommittee_memberLabel%29%20%3D%20%22en%22%29%0A%20%20%0A%20%20%0A%20%20%3Fitem%20rdfs%3Alabel%20%3FitemLabel.%20%0A%20%20FILTER%20%28LANG%20%28%3FitemLabel%29%20%3D%20%22en%22%29%0A%20%20%0A%7D%0AGROUP%20BY%20%3Fcommittee_member%20%3Fcommittee_memberLabel%0AORDER%20BY%20DESC%28%3Fcount%29"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Pessoas que participaram mais de bancas juntos no programa
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#embed.html%23%23title%3A%20Pessoas%20que%20participaram%20mais%20de%20bancas%20juntos%20no%20programa%0ASELECT%20DISTINCT%20%0A%3Fcommittee_member1%20%3Fcommittee_member1Label%0A%3Fcommittee_member2%20%3Fcommittee_member2Label%0A%28COUNT%28DISTINCT%20%3Fitem%29%20as%20%3Fcount%29%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP4101%20%3Fstatement%20.%20%0A%20%20%3Fstatement%20ps%3AP4101%20wd%3AQ835960%20.%20%0A%20%20%3Fstatement%20pq%3AP9945%20wd%3AQ102292035%20.%20%0A%20%20%0A%20%20%3Fitem%20wdt%3AP9161%20%3Fcommittee_member1%20.%20%20%0A%20%20%3Fitem%20wdt%3AP9161%20%3Fcommittee_member2%20.%20%0A%20%20%0A%20FILTER%28%3Fcommittee_member2%20%21%3D%20%3Fcommittee_member1%29%20%0A%20%20%0A%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%20%0A%20%23%20Heuristic%20to%20remove%20duplicates%0A%20FILTER%20%28xsd%3Ainteger%28STRAFTER%28STR%28%3Fcommittee_member2%29%2C%20%22http%3A%2F%2Fwww.wikidata.org%2Fentity%2FQ%22%29%29%20%3E%20xsd%3Ainteger%28STRAFTER%28STR%28%3Fcommittee_member1%29%2C%20%22http%3A%2F%2Fwww.wikidata.org%2Fentity%2FQ%22%29%29%29%0A%7D%0AGROUP%20BY%0A%3Fcommittee_member1%20%3Fcommittee_member1Label%0A%3Fcommittee_member2%20%3Fcommittee_member2Label%0AORDER%20BY%20%0A%20%20DESC%28%3Fcount%29"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  

##  Rede de co-participação em bancas do programa de bioinfo USP (colorindo afiliados ao programa)
  
<iframe style="width: 80%; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#embed.html%23%23defaultView%3AGraph%0A%23title%3A%20Rede%20de%20co-
participa%C3%A7%C3%A3o%20em%20bancas%20do%20programa%20de%20bioinfo%20USP%20%28colorindo%20afiliados%20ao%20programa%29%0ASELECT%20DISTINCT%20%0A%3Fcommittee_member1%20%3Fcommittee_member1Label%20%3Frgb%0A%3Fcommittee_member2%20%3Fcommittee_member2Label%20%3Frgb2%0A%28COUNT%28DISTINCT%20%3Fitem%29%20as%20%3Fcount%29%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP4101%20%3Fstatement%20.%20%0A%20%20%3Fstatement%20ps%3AP4101%20wd%3AQ835960%20.%20%0A%20%20%3Fstatement%20pq%3AP9945%20wd%3AQ102292035%20.%20%0A%20%20%0A%20%20%3Fitem%20wdt%3AP9161%20%3Fcommittee_member1%20.%20%20%0A%20%20%3Fitem%20wdt%3AP9161%20%3Fcommittee_member2%20.%20%0A%20%20%0A%20%20OPTIONAL%7B%0A%20%20%20%20VALUES%20%3Faffiliation%20%7Bwd%3AQ102292035%7D%0A%20%20%20%20%3Fcommittee_member1%20wdt%3AP1416%20%3Faffiliation%20.%7D%20%0A%20%20BIND%28if%28%3Faffiliation%20%3D%20%20wd%3AQ102292035%2C%20%220082a3%22%2C%20%22000000%22%29%20as%20%3Frgb%29%0A%20%20%0A%20%20OPTIONAL%7B%0A%20%20%20%20VALUES%20%3Faffiliation2%20%7Bwd%3AQ102292035%7D%0A%20%20%20%20%3Fcommittee_member2%20wdt%3AP1416%20%3Faffiliation2.%7D%20%20%0A%20%20BIND%28if%28%3Faffiliation2%20%3D%20%20wd%3AQ102292035%2C%20%220082a3%22%2C%20%22000000%22%29%20as%20%3Frgb2%29%0A%0A%20FILTER%28%3Fcommittee_member2%20%21%3D%20%3Fcommittee_member1%29%20%0A%20%20%0A%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%20%0A%20%23%20Heuristic%20to%20remove%20duplicates%0A%20FILTER%20%28xsd%3Ainteger%28STRAFTER%28STR%28%3Fcommittee_member2%29%2C%20%22http%3A%2F%2Fwww.wikidata.org%2Fentity%2FQ%22%29%29%20%3E%20xsd%3Ainteger%28STRAFTER%28STR%28%3Fcommittee_member1%29%2C%20%22http%3A%2F%2Fwww.wikidata.org%2Fentity%2FQ%22%29%29%29%0A%7D%0AGROUP%20BY%0A%3Fcommittee_member1%20%3Fcommittee_member1Label%20%3Frgb%0A%3Fcommittee_member2%20%3Fcommittee_member2Label%20%3Frgb2%0AORDER%20BY%20%0A%20%20DESC%28%3Fcount%29"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>  
