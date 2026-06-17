import web
import math

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class Calculadora:
    def GET(self):
        numero_1 = 0.0
        numero_2 = 0.0
        resultado = 0.0
        return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        operacion = formulario['operacion']
        if operacion == 'limpiar':
            return render.calculadora(0.0, 0.0, 0.0)
        numero_1 = float(formulario['numero_1']) if formulario['numero_1'] != "" else 0.0
        numero_2 = float(formulario['numero_2']) if formulario['numero_2'] != "" else 0.0

        if operacion == 'suma':
            resultado = numero_1 + numero_2
        elif operacion == 'resta':
            resultado = numero_1 - numero_2
        elif operacion == 'multiplicacion':
            resultado = numero_1 * numero_2
        elif operacion == 'division':
            if numero_2 != 0:
                resultado = numero_1 / numero_2
            else:
                resultado = 'No_valido'
        elif operacion == 'potencia':
            resultado = numero_1 ** numero_2
        elif operacion == 'raiz':
            if numero_1 >= 0:
                resultado = math.sqrt(numero_1)
            else:
                resultado = 'No_valido'
        elif operacion == 'modulo':
            if numero_2 != 0:
                resultado = numero_1 % numero_2
            else:
                resultado = 'No_valido'
        elif operacion == 'limpiar':
            

            

        return render.calculadora(numero_1, numero_2, resultado)

    
if __name__ == "__main__":
    app.run()
