import scrapy


class ProfsSpider(scrapy.Spider):
    name = "profs"
    start_urls = ["https://bioinfo.imd.ufrn.br/index.php?page=people"]

    def parse(self, response):

        prof_path = "html body section#ppgbioinfoprofessors.col-md-12.col-sm-12.col-xsm-12 div.row div.col-md-10.col-sm-10.col-xsm-10 div.row div.col-lg-2.col-md-2.col-sm-12.col-xsm-12 center"

        for profSection in response.css(prof_path):

            yield {
                "professor": profSection.css("div.row h6.name::text").get().strip(),
                "lattes": profSection.css("div.img-people::attr(onclick)").re(
                    r"http\:\/\/lattes\.cnpq\.br\/\d+"
                )[0],
            }
