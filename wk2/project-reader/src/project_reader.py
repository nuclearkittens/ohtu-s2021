import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        cont = toml.loads(content)
    
        # tän vois tehdä varmasti elegantimmin lol Xd
        name = cont['tool']['poetry']['name']
        descr = cont['tool']['poetry']['description']
        deps = cont['tool']['poetry']['dependencies'].keys()
        dev_deps = cont['tool']['poetry']['dev-dependencies'].keys()
        return Project(name, descr, deps, dev_deps)