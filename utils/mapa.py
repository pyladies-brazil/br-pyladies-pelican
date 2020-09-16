import folium
import geopy
from geopy.geocoders import Nominatim
import yaml

def atualiza_mapa():

    with open('../data/locations.yml', 'r') as capitulos:
        dados_capitulos = yaml.load(capitulos)

    for capitulo in dados_capitulos:
        if capitulo.get("lat") is None and capitulo.get("lon") is None:
            localizador = Nominatim(user_agent = 'myGeodecoder')
            local = localizador.geocode(f"{capitulo['city']}, {capitulo['state']}, Brazil")
            capitulo["lat"], capitulo["lon"] = local.latitude, local.longitude

    with open('../data/locations.yml', 'w') as arquivo_atualizado:
        yaml.dump(dados_capitulos, arquivo_atualizado)

    return

def gera_mapa():

    posicionamento_mapa = [-14.235004, -51.925282] # isso é basicamente o meio do brasil

    mapa = folium.Map(
        location=posicionamento_mapa,
        zoom_start=4
    )

    with open('../data/locations.yml', 'r') as capitulos:
        dados_capitulos = yaml.load(capitulos)

        for capitulo in dados_capitulos:
            print(capitulo['city'], capitulo["lat"], capitulo["lon"])
            folium.Marker([capitulo["lat"], capitulo["lon"]], title=capitulo["city"]).add_to(mapa)

        mapa.save("../themes/default/static/html/mapa.html")

    return

if __name__ == '__main__':
    atualiza_mapa()
    gera_mapa()
