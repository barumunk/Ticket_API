import pymongo

# Clase de Catalogo
class CATALOGO:
    def __init__(self,fake):
        self.fake = fake

    def Municipio(self):
        listmunicipio = [
            {"id_mun":"000","nombre":"Selecciona un Municipio"},
            {"id_mun":"001","nombre":"Abasolo"},
            {"id_mun":"002","nombre":"Acuña"},	
            {"id_mun":"003","nombre":"Allende"},
            {"id_mun":"004","nombre":"Arteaga"},
            {"id_mun":"005","nombre":"Candela"},
            {"id_mun":"006","nombre":"Castaños"},
            {"id_mun":"007","nombre":"Cuatro Ciénegas"},
            {"id_mun":"008","nombre":"Escobedo"},
            {"id_mun":"009","nombre":"Francisco I. Madero"},
            {"id_mun":"010","nombre":"Frontera"},
            {"id_mun":"011","nombre":"General Cepeda"},
            {"id_mun":"012","nombre":"Guerrero"},
            {"id_mun":"013","nombre":"Hidalgo"},
            {"id_mun":"014","nombre":"Jiménez"},
            {"id_mun":"015","nombre":"Juárez"},
            {"id_mun":"016","nombre":"Lamadrid"},
            {"id_mun":"017","nombre":"Matamoros"},
            {"id_mun":"018","nombre":"Monclova"},
            {"id_mun":"019","nombre":"Morelos"},
            {"id_mun":"020","nombre":"Múzquiz"},
            {"id_mun":"021","nombre":"Nadadores"},
            {"id_mun":"022","nombre":"Nava"},
            {"id_mun":"023","nombre":"Ocampo"},
            {"id_mun":"024","nombre":"Parras"},
            {"id_mun":"025","nombre":"Piedras Negras"},
            {"id_mun":"026","nombre":"Progreso"},
            {"id_mun":"027","nombre":"Ramos Arizpe"},
            {"id_mun":"028","nombre":"Sabinas"},
            {"id_mun":"029","nombre":"Sacramento"},
            {"id_mun":"030","nombre":"Saltillo"},
            {"id_mun":"031","nombre":"San Buenaventura"},
            {"id_mun":"032","nombre":"San Juan de Sabinas"},
            {"id_mun":"033","nombre":"San Pedro"},
            {"id_mun":"034","nombre":"Sierra Mojada"},
            {"id_mun":"035","nombre":"Torreón"},
            {"id_mun":"036","nombre":"Viesca"},
            {"id_mun":"037","nombre":"Villa Unión"},
            {"id_mun":"038","nombre":"Zaragoza"}
        ]
        return listmunicipio

    def Nivel(self):
        listNivel = [
            {"id_niv":"00","nivel":"selecciona un nivel"},
            {"id_niv":"03","nivel":"preescolar"},
            {"id_niv":"04","nivel":"primaria"},
            {"id_niv":"05","nivel":"secundaria"}
        ]
        return listNivel
    
    def Asunto(self):
        listAsuntos = [
            {"id_asu":"00","asunto":"selecciona un asunto"},
            {"id_asu":"01","asunto":"inscripcion"},
            {"id_asu":"02","asunto":"baja temporal"},
            {"id_asu":"03","asunto":"baja total"},
            {"id_asu":"04","asunto":"reingreso inactivo"},
            {"id_asu":"05","asunto":"reingreso activo"}
        ]
        return listAsuntos


# Clase de conexion
class CONEXION:

    def __init__(self,client):
        self.client = client
    
    def InsertarMunicipios(self):
        try:
            # se creav la base de datos y la coleccion si no existe
            db         = self.client["ticket"]
            municipio  = db['municipio']
            catalogo   = CATALOGO("1")
            municipios = catalogo.Municipio()

            for json in municipios:
                db.municipio.insert_many([json])

            return True
        except:
            return False

    def InsertarNivel(self):
        try:
            # se creav la base de datos y la coleccion si no existe
            db        = self.client["ticket"]
            nivel     = db['nivel']
            catalogo  = CATALOGO("1")
            niveles   = catalogo.Nivel()

            for json in niveles:
                db.nivel.insert_many([json])

            return True
        except:
            return False

    def InsertarAsunto(self):
        try:
            # se creav la base de datos y la coleccion si no existe
            db        = self.client["ticket"]
            asunto    = db['asunto']
            catalogo  = CATALOGO("1")
            asuntos   = catalogo.Asunto()

            for json in asuntos:
                db.asunto.insert_many([json])

            return True
        except:
            return False


# funcion main
def main():
    # conexión a la base de datos mongo
    client = pymongo.MongoClient("mongodb://root:root123@mongo_DB:27017/")
    
    # instancia de la clase conexión
    conexion  = CONEXION(client)
    municipio = conexion.InsertarMunicipios()
    nivel     = conexion.InsertarNivel()
    asunto    = conexion.InsertarAsunto()

    print("Municipio: ",municipio,"\nNivel: ",nivel,"\nAsunto: ",asunto)

if __name__ == "__main__":
	main()