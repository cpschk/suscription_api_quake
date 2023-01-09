import wikipediaapi
from .dag_functions import QuakeFunctions

class CumtomPyFunctions:

    def extract_ApiQuake():
        '''
            Funcion que extrae los datos relacionados a temblores ocurridos en las ultimas 24 hrs
            tomando la fecha actual como referencia
        '''
        print(f"Extrayendo datos de ApiQuake de las ultimas 24Hrs")
        date_quake = QuakeFunctions.last24hrs()
        quakeDf = QuakeFunctions.extract_eartquake(date_quake[0], date_quake[1])
        # Extraccion de localidad o pais en donde ocurre este fenomeno para mostrar en el reporte
        placeQuake = quakeDf['place'][quakeDf['mag'] == quakeDf['mag'].max()]
        if placeQuake.str.contains(',').iloc[0]:
            placeQuake = placeQuake.str.split(',', expand=True).iloc[0][1]
            print('1', placeQuake)
        else:
            placeQuake = None
            print('2 no se pudo encontrar la localidad pero te puedo dar este dato interesante ...')

    def interest_info():
        '''
            Funcion que tomara el temblor mas alto ocurrido en las ultimas 24 hrs y extraera la localidad donde ocurrio
            para
        '''
        print('Aqui iria informacion relevante del lugar que tuvo el temblor')

        placeQuake = 'Chile'
        wiki_wiki = wikipediaapi.Wikipedia('es')
        page_py = wiki_wiki.page(placeQuake)
        if page_py.exists():
            print("Page - Exists:")
        else:
            raise "la pagina no existe"
        # Page - Exists: False