from Scraping import Scraping

if __name__ == "__main__":
	url = input("Ingresa un link: ")
	ModuloScraping = Scraping()
	ModuloScraping.scrapingImages(url)
	ModuloScraping.scrapingPDF(url)
	ModuloScraping.scrapingLinks(url)
	ModuloScraping.scrapingHtml(url)