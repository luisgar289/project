import web
from pymongo import MongoClient #importa libreria pymongo

urls = (
    '/', 'Index',
    '/amistad', 'Amistad',
    '/ansiedad', 'Ansiedad',
    '/contacto', 'Contacto',
    '/depresion', 'Depresion',
    '/hobby', 'Hobby',
    '/inicio', 'Inicio',
    '/referencias', 'Referencias',
    '/talleres', 'Talleres',
    '/terapia', 'Terapia',
)

app = web.application(urls, globals())
wsgiapp = app.wsgifunc() # Prepara la webapp para funcionar con Gunicorn
render = web.template.render('templates/') #platillas html con una base

class Index:
    def GET(self):
        return render.index()

    def POST(self):
        formulario = web.input()
        nombre = formulario.nombre
        email = formulario.email
        edad = formulario.edad
        client = MongoClient('mongodb+srv://luisgarcia:luisgarcia15@cluster0.7nfcf.mongodb.net/registros?retryWrites=true&w=majority')
        db = client['registros']
        col = db['registro_visitas']
        col.insert_one({
            'nombre': nombre,
            'email': email,
            'edad': edad
            })
        print('Documento guardado')
        return web.seeother('/inicio')

class Amistad:
    def GET(self):
        return render.amistad()

class Ansiedad:
    def GET(self):
        return render.ansiedad()

class Contacto:
    def GET(self):
        return render.contacto()

class Depresion:
    def GET(self):
        return render.depresion()

class Hobby:
    def GET(self):
        return render.hobby()

class Inicio:
    def GET(self):
        return render.inicio()

class Referencias:
    def GET(self):
        return render.referencias()

class Talleres:
    def GET(self):
        return render.talleres()

class Terapia:
    def GET(self):
        return render.terapia()

if __name__ == "__main__": 
    web.config.debug = False
    app.run()