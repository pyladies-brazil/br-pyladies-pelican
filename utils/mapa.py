import os

import folium
import geopy
from geopy.geocoders import Nominatim
import yaml

SITEURL = '{}'.format(os.getenv('SITEURL', 'http://localhost:{}'.format(os.getenv('PORT', '8000'))))

def cria_card(capitulo):
    card_capitulo = ""

    info_css = """
    <link href='https://fonts.googleapis.com/css?family=Montserrat:400,700|Open+Sans:400,600,300,800,700' rel='stylesheet'
        type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Shadows+Into+Light' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Indie+Flower' rel='stylesheet' type='text/css'>
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet"
        type='text/css'>

    <link rel="stylesheet" href="{}/theme/css/normalize.css">
    <link rel="stylesheet" href="{}/theme/css/nprogress.css">
    <link rel="stylesheet" href="{}/theme/css/foundation.min.css">
    <link rel="stylesheet" href="{}/theme/css/style.css">
    <link rel="stylesheet" href="{}/theme/css/post.css">
    <link rel="stylesheet" href="{}/theme/tipuesearch/tipuesearch.css">""".format(SITEURL, SITEURL, SITEURL, SITEURL, SITEURL, SITEURL)

    img_capitulo = """<div><img class="img-location" src="{}{}" width="100" height="100"></div>""".format(SITEURL, capitulo['image'])

    if capitulo.get("url") is not None:
        url_capitulo = """<a target="_blank" href="{}">
                    <span class="location-name">Pyladies {} - {}</span>
                    <i class="fa fa-external-link location-external-link" aria-hidden="true"></i>
                  </a>""".format(capitulo["url"], capitulo["city"], capitulo["state"])
    else:
        url_capitulo = """<span class="location-name">Pyladies {} - {}</span>""".format(capitulo['city'], capitulo['state'])


    redes_capitulo = """<div class="social-icons>
    """

##   <div class="social-icons">
                #     {% if capitulo['twitter'] %}
                #     <a target="_blank" href="{{ capitulo['twitter'] }}">
                #       <span class="fa-stack fa-lg">
                #         <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
                #         <i class="fa fa-twitter fa-stack-1x"></i>
                #       </span>
                #     </a>

    if capitulo.get("twitter") is not None:
        tt_capitulo = """<a target="_blank" href="{}">
                  <span class="fa-stack fa-lg">
                    <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
                    <i class="fa fa-twitter fa-stack-1x"></i>
                  </span>
                </a>""".format(capitulo["twitter"])
        redes_capitulo += tt_capitulo

    if capitulo.get("email") is not None:
        email_capitulo = """<a target="_blank" href="mailto:{}">
                  <span class="fa-stack fa-lg">
                    <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
                    <i class="fa fa-envelope fa-stack-1x"></i>
                  </span>
                </a>""".format(capitulo["email"])
        redes_capitulo += email_capitulo

    if capitulo.get("facebook") is not None:
        fb_capitulo = """
        <a target="_blank" href="{}">
                  <span class="fa-stack fa-lg">
                    <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
                    <i class="fa fa-facebook fa-stack-1x"></i>
                  </span>
                </a>
        """.format(capitulo["facebook"])
        redes_capitulo += fb_capitulo

    if capitulo.get("instagram") is not None:
        ig_capitulo = """<a target="_blank" href="{}">
                  <span class="fa-stack fa-lg">
                    <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
                    <i class="fa fa-instagram fa-stack-1x"></i>
                  </span>
                </a>""".format(capitulo["instagram"])
        redes_capitulo += ig_capitulo

    if capitulo.get("youtube") is not None:
        yt_capitulo = """<a target="_blank" href="{}">
                  <span class="fa-stack fa-lg">
                    <i class="fa fa-circle fa-stack-2x fa-inverse"></i>
                    <i class="fa fa-youtube-square fa-stack-1x"></i>
                  </span>
                </a>""".format(capitulo["youtube"])
        redes_capitulo += yt_capitulo


    redes_capitulo += "</div>"

    print(redes_capitulo)

    card_capitulo += info_css
    card_capitulo += img_capitulo
    card_capitulo += url_capitulo
    card_capitulo += redes_capitulo

    return card_capitulo


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
            card_capitulo = cria_card(capitulo)

            iframe = folium.IFrame(html=card_capitulo, width=300, height=300)
            popup = folium.Popup(iframe, max_widht=1000)

            # print(capitulo['city'], capitulo["lat"], capitulo["lon"])
            folium.Marker(
                            location = [capitulo["lat"], capitulo["lon"]],
                            title = capitulo["city"],
                            popup = popup

                        ).add_to(mapa)

        mapa.save("../themes/default/static/html/mapa.html")

    return

if __name__ == '__main__':
    atualiza_mapa()
    gera_mapa()