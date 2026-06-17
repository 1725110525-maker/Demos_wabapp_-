import web
render = web.template.render('views')
class contactos:
    def GET(self):
        return render.contactos()