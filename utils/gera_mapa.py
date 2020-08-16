import folium

posicionamento_mapa = [-15.7941, -47.8825]

mapa = folium.Map(
    location=posicionamento_mapa
)

cidades = [{"city": "belo horizonte", "lat": -26.91894, "lon": -49.066059},
           {"city": "belé", "lat": -1.37676, "lon": -48.46647},
         	 {"city": "belo horizonte", "lat": -19.91818, "lon": -43.93705}]

# supondo que o dado vem como
# [{city: "abc", state: "AB", "lat": 123.1237, "lon": 123.456}]
for cidade in cidades:
    folium.Marker([cidade["lat"], cidade["lon"]], title=cidade["city"]).add_to(mapa)


mapa.save("../themes/static/html/mapa.html")
