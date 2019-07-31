import urllib.request

# requisita a abertura do site
uuid = "https://httpbin.org/uuid"
pagina = urllib.request.urlopen(uuid)

# Imprime a saida
print(pagina.read())
