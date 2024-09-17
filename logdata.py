import requests
import json
#Se importan los módulos requests para realizar solicitudes HTTP y json para manipular datos en formato JSON



def obtenerIpDedeDominio(dominio):
    """
    Esta función toma un dominio como entrada, realiza una búsqueda DNS para obtener la dirección IP
    del dominio y luego usa esa IP para determinar la región geográfica desde la que se está accediendo.
    """
    print("---------Dominio -> " + str(dominio) + "-----------")

    # Realiza una solicitud GET a la API de networkcalc para obtener registros DNS del dominio
    resultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/" + str(dominio))

    # Verifica si hay registros de tipo A en la respuesta JSON
    if resultadoBusqueda.json()['records'] != None:
        # Itera sobre cada registro de tipo A y obtiene la dirección IP
        for i in range(len(resultadoBusqueda.json()['records']['A'])):
            ip = resultadoBusqueda.json()['records']['A'][i]['address']
            # Realiza una solicitud GET a la API de ipinfo para obtener la región de la IP
            resultadoRegion = requests.get("https://ipinfo.io/" + str(ip) + "?token=74bc917a25b741")
            # Imprime la región obtenida para la IP
            print("la region de la ip -> " + str(ip) + " es " + str(resultadoRegion.json()['region']))


def optenerEmail(dominio):
    """
    Esta función toma un dominio como entrada y obtiene una lista de correos electrónicos asociados
    al dominio utilizando la API de Hunter.
    """
    # Realiza una solicitud GET a la API de Hunter para buscar correos electrónicos asociados al dominio
    resultadosEmail = requests.get("https://api.hunter.io/v2/domain-search?domain=" + str(
        dominio) + "&api_key=344ff07dbe78869fe56eba9c0f1ebc3bf225fb08")

    # Verifica si hay correos electrónicos en la respuesta JSON
    if resultadosEmail.json()["data"]["emails"] != None:
        # Itera sobre cada correo electrónico encontrado y lo imprime
        for correo in range(len(resultadosEmail.json()["data"]["emails"])):
            print("correo: " + str(resultadosEmail.json()["data"]["emails"][correo]["value"]))


# Lista de dominios de 100 empresas famosas en Colombia
dominios_empresas_colombianas = [
    "ecopetrol.com.co",
    "grupoavvillas.com.co",
    "bancolombia.com",
    "santander.com.co",
    "grupoargos.com.co",
    "nexenta.com",
    "grupoexito.com",
    "celsia.com",
    "caracoltv.com",
    "rcn.com.co",
    "postobon.com.co",
    "avianca.com",
    "sodimac.com.co",
    "bancafianc.com",
    "d1.com.co",
    "supranational.com",
    "tigo.com.co",
    "entelchile.net",
    "colpatria.com.co",
    "carreras.com.co",
    "panamericana.com.co",
    "falabella.com.co",
    "centauro.com.co",
    "samsclub.com.co",
    "carulla.com",
    "mintransporte.gov.co",
    "mueblesdico.com",
    "colfondos.com",
    "pepsi.com.co",
    "mercedesbenz.com.co",
    "renault.com.co",
    "chevrolet.com.co",
    "honda.com.co",
]

# Itera sobre cada dominio en la lista y ejecuta las funciones para obtener IPs y correos electrónicos
for i in dominios_empresas_colombianas:
    obtenerIpDedeDominio(i)
    optenerEmail(i)

