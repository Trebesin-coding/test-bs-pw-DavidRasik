from bs4 import BeautifulSoup
import requests
import json


def main():

    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser") 
    
    # <--- Úkol: popiš krátce, co tohle dělá¨
    #  Odpoved: Toto (po uprave) ulozi podpromenou "soup", nasledne se spusti BeautifulSoup a umozni prochazet kod html, nasledne diky tomu muzeme hledat podle prvku nize

    # ingredience_1 = soup.select("h2")
    ingredience_vsechny = soup.select("h2")

    ingredience = {
        ingredience_vsechny[0].text,
        ingredience_vsechny[1].text,
        ingredience_vsechny[2].text,
        ingredience_vsechny[3].text,
    }


    if not ingredience:
        print("Nenasel jsem ingredienci 1")
    else:
        print(ingredience)


    data = {
        "Ingredience:": ingredience
    }


    with open ("recept.json", "w", encoding="utf-8") as soubor:
        json.dump(data, soubor, ensure_ascii=False)



if __name__ == "__main__":
    main()