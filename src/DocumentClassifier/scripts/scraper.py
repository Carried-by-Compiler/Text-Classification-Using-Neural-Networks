from bs4 import BeautifulSoup as Soup
from urllib.request import Request, urlopen as uReq


url = "https://www.huffingtonpost.com/entry/texas-amanda-painter-mass-shooting_us_5b081ab4e4b0802d69caad89"

class Scraper:

    def __init__(self):
        
        # Data members
        self.web_client = None

    def update_web_client(self, url: str):

        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        self.web_client = uReq(req)

    def get_text(self) -> str:

        result = ""

        html_page = self.web_client.read()
        self.web_client.close()

        page_soup = Soup(html_page, "html.parser")
        text = page_soup.findAll("div", {"class" : "content-list-component yr-content-list-text text"})

        try:

            for t in text:
                try:
                    result += t.find("p").getText()
                except:
                    try:
                        result += "\n"
                        result += t.find("h3").getText().upper()
                        result += "\n"
                    except:
                        result += "\n"
                
                result += "\n"

        except Exception as e:
            result = ""
            print(str(e))

        return result

    def get_text_travel(self):
        """
        It seems like the travel pages for huffpost is different in html structure
        than the rest of them. I have created a separate function to handle travel 
        web pages.
        """

        result = ""

        html_page = self.web_client.read()
        self.web_client.close()

        page_soup = Soup(html_page, "html.parser")
        text = page_soup.findAll("div", {"class" : "cli cli-text"})

        try:

            for t in text:
                try:
                    result += t.find("p").getText()
                except:
                    try:
                        result += "\n"
                        result += t.find("h3").getText().upper()
                        result += "\n"
                    except:
                        result += "\n"
                
                result += "\n"
                    

        except Exception as e:
            result = ""
            print(str(e))

        return result