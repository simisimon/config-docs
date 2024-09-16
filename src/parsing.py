from bs4 import BeautifulSoup
import requests


MAVEN_DOCS_URL = "https://maven.apache.org/ref/3.9.2/maven-model/maven.html"


def parse_maven_docs():
    html_doc  = requests.get(url=MAVEN_DOCS_URL).content

    soup = BeautifulSoup(html_doc, 'html.parser')

    options = soup.find_all('td', align="left")

    print(len(options))

    maven_options = []

    for option in options:
        maven_options.append(option.text.strip())

    with open("..\\data\\maven_options.txt", "w", encoding="utf-8") as dest:
        dest.write(str(maven_options))


def parse_docker_docs():
    # TODO
    pass


def main():
    pass


if __name__ == "__main__":
    parse_maven_docs()