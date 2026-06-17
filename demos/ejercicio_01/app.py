import web

urls = (
    '/', 'Index',
    '/Clientes', 'Clientes',
    '/Usuario', 'Usuario'

)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

    app.run()
class clientes:
    def GET(self):
        return render.Clientes()
    app.run()
class Usuario:
    def GET(self):
        return render.Usuario()
if __name__ == "__main__":
    app.run()