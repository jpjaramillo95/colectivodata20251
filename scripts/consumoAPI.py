import requests

url="http://localhost:8080/docentes"
repuesta=requests.get(url)

if(repuesta.status_code==200):
    datos=repuesta.json()
    # Llevar los datos a Pandas
else:
    print("Error consumiendo el API")