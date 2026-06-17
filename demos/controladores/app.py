import web 

urls = (
    '/', 'contrallers.index.Index',
    '/contactos', 'contrallers.contactos.contactos'
)
app = web.application(urls, globals())

                             
    
if __name__ == "__main__":
    app.run()