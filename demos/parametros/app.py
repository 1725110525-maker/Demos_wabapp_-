import web 

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)
app = web.application(urls, globals())
render = web.template.render('templates')
                             
class Index:
    def GET(self):
        return render.index()

class Parametros:
    def GET(self):
        titulo = "titulo desde Python"
        descripcion = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        return render.parametros(titulo,descripcion)

if __name__ == "__main__":
    app.run()
