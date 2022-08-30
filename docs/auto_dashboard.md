
The Landscape of Brazilian Bioinformatics
=========================================

#  Institutions related to Brazilian bioinformaticians
  

    <iframe style="width: 150%; height: 50vh; border: none;"
    
src=https://query.wikidata.org/embed.html#%23%23title%3A%20Institutions%20related%20to%20Brazilian%20bioinformaticians%0A%23defaultView%3AMap%0ASELECT%20DISTINCT%0A%3Forganization%20%3ForganizationLabel%20%0A%3Fsample_author%20%3Fsample_authorLabel%0A%3Fgeo%20%3Flayer%0A%20WITH%20%7B%0A%20%20%20%20SELECT%20DISTINCT%20%3Forganization%20%3Fgeo%20%0A%20%20%20%20%28SAMPLE%28%3Fauthor%29%20as%20%3Fsample_author%29%20WHERE%20%7B%0A%0A%20%20%7B%3Fauthor%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20UNION%0A%20%20%7B%3Fauthor%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution.%0A%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20%0A%20%20%3Fauthor%20wdt%3AP101%20wd%3AQ128570%20.%20%20%20%20%0A%20%20%3Fauthor%20%28%20wdt%3AP108%20%7C%20wdt%3AP463%20%7C%20wdt%3AP1416%20%29%20%2F%20wdt%3AP361%2A%20%3Forganization%20.%20%0A%20%20%3Forganization%20wdt%3AP625%20%3Fgeo%20.%0A%20%20%20%20%7D%0A%20%20%20%20GROUP%20BY%20%3Forganization%20%3Fgeo%20%3Fcount%0A%20%20%20%20ORDER%20BY%20DESC%20%28%3Fcount%29%0A%20%20%20%20LIMIT%202000%0A%20%20%7D%20AS%20%25organizations%0A%20%20WHERE%20%7B%0A%20%20%20%20INCLUDE%20%25organizations%0A%20%20%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%20%20%20%20%20%20%20%0A%20%20%7D%0A%20%20ORDER%20BY%20DESC%20%28%3Fcount%29%0A%0A%0A%20%20

    referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>
#  Bioinformaticians that were/are on Brazil
  

    <iframe style="width: 150%; height: 50vh; border: none;"
    
src=https://query.wikidata.org/embed.html#%23%23title%3A%20Bioinformaticians%20that%20were%2Fare%20on%20Brazil%0ASELECT%20%3FauthorLabel%20%28COUNT%28DISTINCT%20%3Fwork%29%20AS%20%3Fn%29%20%3Fauthor%20%3Forcid%20WHERE%20%7B%0A%20%20%20%20%3Fauthor%20wdt%3AP101%20wd%3AQ128570%20.%0A%20%20%20%20hint%3APrior%20hint%3ArunFirst%20true%20.%0A%20%20%7B%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155%3B%0A%20%20%7D%0A%20%20UNION%0A%20%20%7B%0A%20%20%20%20%3Fauthor%20%28wdt%3AP108%7Cwdt%3AP1416%29%20%3Finstitution.%0A%20%20%20%20%3Finstitution%20wdt%3AP17%20wd%3AQ155.%0A%20%20%7D%0A%20%20%3Fwork%20wdt%3AP50%20%3Fauthor.%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fauthor%20wdt%3AP496%20%3Forcids.%0A%20%20%20%20BIND%28IRI%28CONCAT%28%22https%3A%2F%2Forcid.org%2F%22%2C%20%3Forcids%29%29%20AS%20%3Forcid%29%0A%20%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cda%2Cde%2Ces%2Cfr%2Cjp%2Cnl%2Cno%2Cru%2Csv%2Czh%22.%20%7D%0A%7D%0AGROUP%20BY%20%3Fauthor%20%3FauthorLabel%20%3Forcid%0AORDER%20BY%20DESC%20%28%3Fn%29

    referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>
#  Co-authorship network of bioinformaticians in Brazil
  

    <iframe style="width: 150%; height: 50vh; border: none;"
    
src=https://query.wikidata.org/embed.html#%23%23title%3A%20Co-
authorship%20network%20of%20bioinformaticians%20in%20Brazil%0A%23%20tool%3A%20scholia%0A%23defaultView%3AGraph%0ASELECT%0A%20%20%3Fauthor1%20%3Fauthor1Label%20%3Fimage1%20%3Frgb%0A%20%20%3Fauthor2%20%3Fauthor2Label%20%3Fimage2%20%0AWITH%20%7B%0A%20%20SELECT%0A%20%20%20%20%3Fauthor1%20%28SAMPLE%28%3Fimage1_%29%20AS%20%3Fimage1%29%0A%20%20%20%20%3Fauthor2%20%28SAMPLE%28%3Fimage2_%29%20AS%20%3Fimage2%29%0A%20%20%20%20%3Frgb%0A%20%20WHERE%20%7B%0A%0A%20%20%20%20%0A%20%20%20%20%7B%3Fauthor1%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution1.%0A%20%20%20%20%20%3Finstitution1%20wdt%3AP17%20wd%3AQ155.%7D%0A%20%20%20%20%0A%20%20%20%20%7B%3Fauthor2%20wdt%3AP108%20%7C%20wdt%3AP1416%20%3Finstitution2.%0A%20%20%20%20%20%3Finstitution2%20wdt%3AP17%20wd%3AQ155.%7D%0A%0A%20%20%20%20%3Fauthor2%20wdt%3AP101%20wd%3AQ128570%20.%0A%20%20%20%20%3Fauthor2%20wdt%3AP101%20wd%3AQ128570%20.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor1%20wdt%3AP21%20%3Fgender%20.%20%7D%0A%20%20%20%20BIND%28%20IF%28%3Fgender%20%3D%20wd%3AQ6581072%2C%20%22008080%22%2C%22B5651D%22%29%20AS%20%3Frgb%29%0A%20%20%20%20%0A%20%20%20%20%3Fwork%20wdt%3AP50%20%3Fauthor1%20%2C%20%3Fauthor2%20.%0A%20%20%20%20%0A%20%20%20%20%23%20Only%20display%20co-
authorship%20for%20certain%20types%20of%20documents%0A%20%20%20%20%23%20Journal%20and%20conference%20articles%2C%20books%2C%20not%20%28yet%3F%29%20software%0A%20%20%20%20VALUES%20%3Fpublication_type%20%7B%20wd%3AQ13442814%20wd%3AQ571%20wd%3AQ26973022%20wd%3AQ17928402%20wd%3AQ947859%20wd%3AQ54670950%20%7D%0A%20%20%20%20FILTER%20EXISTS%20%7B%20%3Fwork%20wdt%3AP31%20%3Fpublication_type%20.%20%7D%0A%0A%20%20%20%20%23%20No%20self-
links.%0A%20%20%20%20FILTER%20%28%3Fauthor1%20%21%3D%20%3Fauthor2%29%0A%20%20%20%20%23%20Images%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor1%20wdt%3AP18%20%3Fimage1_%20%7D%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor2%20wdt%3AP18%20%3Fimage2_%20%7D%0A%20%20%7D%0A%20%20GROUP%20BY%20%3Fauthor1%20%3Fauthor2%20%20%20%20%20%3Frgb%0A%7D%20AS%20%25result%0AWHERE%20%7B%0A%20%20INCLUDE%20%25result%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cda%2Cde%2Ces%2Cfr%2Cjp%2Csv%2Cru%2Czh%22.%0A%20%20%7D%0A%7D%0A

    referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>