import wikipedia as wiki
from FileHandler import FileHandler


class DataSetBuilder:

    def __init__(self):

        self.fileHandler = FileHandler()

    def fill(self, folder="NaN"):

        self.fileHandler.update_path(folder)
        results = wiki.search(folder)

        for result in results:
            wiki_page = wiki.page(result)
            self.fileHandler.write(wiki_page.content, wiki_page.title)
        print("Done printing to %s" % folder)

    def make_file(self, name="NaN", folder="NaN"):

        self.fileHandler.update_path(folder)
        wiki_page = wiki.page(name)
        self.fileHandler.write(content=wiki_page.content, filename=wiki_page.title)

        print("Done printing file %s to folder %s" % (name, folder))