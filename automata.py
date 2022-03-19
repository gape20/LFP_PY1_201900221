from Token import Tokenn
from prettytable import PrettyTable
from Sintactico import Sintactico



Simbolos = [":", "~", "[", "]", '"', ",", ";","<",">","'"]
PalabrasReservadas =['formulario', 'tipo', 'valor', 'fondo','valores','evento']
Info = []



def leerArchivo(Archivo):
    Estado = 0
    Acum = ""
    linea = 1
    columna = 0
    
    for Caracter in Archivo:
        if Caracter == "\n":
            linea +=1
            columna = 0
        columna += 1
        if Caracter.isalpha():
            Caracter = Caracter.lower()
        if Estado == 0:
            if Caracter.isalpha():
                Acum += Caracter
            elif Caracter.isdigit():
                Acum += Caracter
            elif Caracter in Simbolos:
                if Acum !='':
                    Info.append(Tokenn(Acum, ObtenerToken(Acum),linea,columna))
                    Acum=''
                if Caracter == '"' or Caracter == "'":
                    Estado = 1
                    Acum += Caracter
                else:
                    Info.append(Tokenn(Caracter, ObtenerToken(Caracter),linea,columna))
        elif Estado == 1:
            if Caracter == '"' or Caracter == "'":
                Acum += Caracter
                Info.append(Tokenn(Acum, 'tk_cadena',linea,columna))
                Acum = ''
                Estado = 0
            else:
                Acum += Caracter
    print("Archivo Analizado")


    x = PrettyTable()
    x.field_names = ["Lexema","linea","columna","Token"]    
    print("============== TABLA DE TOKENS==============")                
    for token in Info:
        x.add_row([token.lexema, token.linea, token.columna, token.token])
    print(x)

    Sintactico(Info)
    GenerarReporteTokens()
    GenerarReporteErrores()
    generariFrame()

def generariFrame():  
   
    centro = """<h1><center>iFrame</center></h1>
                        <br></br>
                        <style>
                            table,td {
	                            border: 2px solid black;
                        }
                        </style>
            """

    try:
        
        for ins in Sintactico.instrucciones:
            a = ''
            b = ''
            c = ''
            d = ''
            a = str(ins[0][1])
            b = str(ins[1][1])

            caracteres = "[]'"
            for x in range(len(caracteres)):
                a = a.replace(caracteres[x],"")
            c = a.replace('"',"")

            if c == 'etiqueta' or c == 'label':
                for x in range(len(caracteres)):
                    b = b.replace(caracteres[x],"")
                d = b.replace('"',"")
                centro += f'<h4>{d}</h4>'

            elif c == 'texto' or c == 'input de tipo text':
                e = str(ins[2][1])
                for x in range(len(caracteres)):
                    e = e.replace(caracteres[x],"")
                d = e.replace('"',"")
                centro += f'<textarea cols="10" rows="1" style="resize: both;" placeholder="{d}", id = "nombre"></textarea>'

            elif c == 'grupo-radio' or c == 'grupo de input de tipo radio':
                e = str(ins[1][1])
                for x in range(len(caracteres)):
                    e = e.replace(caracteres[x],"")
                d = e.replace('"',"")
                centro += f'<br> </br><form><h4>{d}</h4><div>'
                f = ins[2][1]
                for sexo in f:
                    str(sexo)
                    for x in range(len(caracteres)):    
                        sexo = sexo.replace(caracteres[x],"")
                        sexo = sexo.replace('"',"")
                    centro +=f'<input type="radio" id="masc" name="masc" value={sexo} id= "radio"><label for="sex">{sexo}</label> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'     

            elif c == 'grupo-option' or c == 'select con respectivos option':
                e = str(ins[1][1])
                for x in range(len(caracteres)):
                    e = e.replace(caracteres[x],"")
                d = e.replace('"',"")
                centro += f'<br> </br> <h4>{d}</h4>'
                f = ins[2][1]
                centro += '<select name="select" id ="select1">'
                for paises in f:
                    str(paises)
                    for x in range(len(caracteres)):    
                        paises = paises.replace(caracteres[x],"")
                        paises = paises.replace('"',"")
                    centro += f'<option value="value1"><h1>{paises}</h1></option>'
                centro += '<br></br></select><br> </br>'

            elif c == 'boton' or c == 'button':
                e = str(ins[1][1])
                for x in range(len(caracteres)):
                    e = e.replace(caracteres[x],"")
                d = e.replace('"',"")
                f = ins[2][1]
                centro += '''
                <script>
            function abrirIframeEntrada() {
                var ifrm = document.createElement("iframe");
                ifrm.setAttribute("src", "file:///E:/UNIVERSIDAD/7mo%20Semestre/LAB%20LENGUAJES/a/formulario.html");
                ifrm.style.width = "1000px";
                ifrm.style.height = "1000px";
                document.body.appendChild(ifrm);


            }
        </script>
        <script>
                function abrirIframeInfo() {
                                    var1 = document.getElementById('nombre').value;
                                    console.log(var1)
                                    var elem2 = document.createElement('label');
                                    elem2.innerHTML = "Nombre: " + var1+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
                                    document.getElementsByTagName('body')[0].appendChild(elem2);
                                    var sexo = document.getElementsByName('masc');
                                    for (i = 0; i < sexo.length; i++) {
                                        if (sexo[i].checked) {
                                            var seleccion = sexo[i].value;
                                            console.log(seleccion)
                                            var elem3 = document.createElement('label');
                                            elem3.innerHTML = "Seleccion: " + seleccion +'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
                                            document.getElementsByTagName('body')[0].appendChild(elem3);

                                        }
                                    }
                                    var combo = document.getElementById("select1");
                                    var selected = combo.options[combo.selectedIndex].text;
                                    console.log(selected)
                                    var elem4 = document.createElement('label');
                                    elem4.innerHTML = "Seleccion: " + selected +'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
                                    document.getElementsByTagName('body')[0].appendChild(elem4);
}  
        </script>
                '''
    
                for entradas in f:
                    if entradas == 'entrada':
                        centro += f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button type="button" onclick=abrirIframeEntrada() value ={entradas}><h4>{d}</h4></button>'

                    elif entradas == 'info':
                        centro += f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button type="button" onclick=abrirIframeInfo() value ={entradas}><h4>{d}</h4></button>'
   
    except:
        print('Hay algun error en el archivo de entrada, ocurrirá un error al seguir corriendo el programa.')
    centro+='''<br> </br>
                            </div>
                        </form>'''
    try:  
        archivo = open('iframe.html', 'w')
    except OSError:
                        archivo = open('iframe.html', 'w')
    head = """<!doctype html>
                    <html lang="en">
                    <meta charset="utf-8">
                    <head>
                        <meta charset="utf-8">
                        <title>iFrame</title>
                        <base href="/">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link rel="icon" type="image/x-icon" href="favicon.ico">
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
                        <style>
                            .navbar {
                                margin-bottom: 20px;
                                background: #A81616;
                                box-shadow: 0px 10px 6px -4px rgba(0, 0, 0, 0.75);
                            }
                            .sombra {
                                box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                            }
                            .modal-backdrop {
                                position: fixed;
                                top: 0;
                                right: 0;
                                bottom: 0;
                                left: 0;
                                z-index: 1040;
                                background-color: #333;
                            }
                            .fondo {
                                background: #37474F;
                            }
                            .b-footer {
                                background: #A81616;
                                padding: 20px;
                            }
                            .modal-content {
                                width: 650px;
                                background: #182D3E;
                                box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                            }
                            .form1 {
                                margin-bottom: 20px;
                                background: #424242;
                                padding: 20px;
                                box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                                list-style: none;
                                text-decoration: none;
                            }
                            .form1,
                            a:visited {
                                color: rgb(8, 8, 8);
                            }
                            .img {
                                display: block;
                                margin: auto;
                            }
                            footer {
                                background: #2B353A;
                                padding: 10px 10px;
                                text-align: center;
                            }
                        </style>
                    </head>
                    <body class="fondo">
                        <header>
                            <nav class="navbar navbar-expand-lg navbar-dark ">
                                <div class="container">
                                    <a class="navbar-brand">
                                        <span class="fa fa-university" aria-hidden="true"></span>LFP - Proyecto 1</a>
                                    </a>
                                </div>
                            </nav>
                        </header>
                        <div class="row">
                            <div class="col-sm"></div>
                            <div class="col-sm-8">
                                <div class="card text-white bg-dark mb-3 sombra"> """
    Bottom = """</div>
                            </div>
                            <div class="col-sm"></div>
                        </div>
                    </body>
                    <div class="b-footer">
                        <div class="container">
                            <div class="row">
                                <div class="col-6 text-white">
                                    <label>201900221 - Gabriel Enrique Perez Meza</label>
                                </div>
                                <div class="col-6  text-white text-center">
                                    <label>USAC</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <footer class="footer text-white">
                        <label>© 2021 USAC, All rights reserved.</label>
                    </footer>
                    </html>"""
    archivo.write(head)
    archivo.write(centro)
    archivo.write(Bottom)
    archivo.close()

def GenerarReporteTokens():
    centro = """<h1><center>Reporte de Tokens</center></h1>
                        <br></br>
                        <style>
                            table,td {
	                            border: 2px solid black;
                        }
                        </style>
            <table class="default">
                <tr>
                <td align='center'>Lexema</td>
                 <td align='center'>Linea</td>
                 <td align='center'>Columna</td>
                 <td align='center'>Token</td>
                </tr>
            """
    for token in Info:
        centro+=f"<tr><td align='center'>{token.lexema}</td><td align='center'>{token.linea}</td><td align='center'>{token.columna}</td><td align='center'>{token.token}</td></tr>"
    centro += '</table>'
    try:  
        archivo = open('ReporteTokens.html', 'w')
    except OSError:
                    archivo = open('ReporteTokens.html', 'w')
    head = """<!doctype html>
                <html lang="en">
                <meta charset="utf-8">
                <head>
                    <meta charset="utf-8">
                    <title>Reporte de Tokens</title>
                    <base href="/">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link rel="icon" type="image/x-icon" href="favicon.ico">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
                    <style>
                        .navbar {
                            margin-bottom: 20px;
                            background: #A81616;
                            box-shadow: 0px 10px 6px -4px rgba(0, 0, 0, 0.75);
                        }

                        .sombra {
                            box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                        }

                        .modal-backdrop {
                            position: fixed;
                            top: 0;
                            right: 0;
                            bottom: 0;
                            left: 0;
                            z-index: 1040;
                            background-color: #333;
                        }

                        .fondo {
                            background: #37474F;
                        }

                        .b-footer {
                            background: #A81616;
                            padding: 20px;
                        }

                        .modal-content {
                            width: 650px;
                            background: #182D3E;
                            box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                        }

                        .form1 {
                            margin-bottom: 20px;
                            background: #424242;
                            padding: 20px;
                            box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                            list-style: none;
                            text-decoration: none;
                        }

                        .form1,
                        a:visited {
                            color: rgb(8, 8, 8);
                        }

                        .img {
                            display: block;
                            margin: auto;
                        }

                        footer {
                            background: #2B353A;
                            padding: 10px 10px;
                            text-align: center;
                        }
                    </style>
                </head>

                <body class="fondo">

                    <header>
                        <nav class="navbar navbar-expand-lg navbar-dark ">
                            <div class="container">
                                <a class="navbar-brand">
                                    <span class="fa fa-university" aria-hidden="true"></span>LFP - Proyecto 1</a>
                                </a>
                            </div>
                        </nav>
                    </header>

                    <div class="row">
                        <div class="col-sm"></div>
                        <div class="col-sm-8">
                            <div class="card text-white bg-dark mb-3 sombra"> """

    Bottom = """</div>

                        </div>
                        <div class="col-sm"></div>
                    </div>
                </body>

                <div class="b-footer">
                    <div class="container">
                        <div class="row">
                            <div class="col-6 text-white">
                                <label>201900221 - Gabriel Enrique Perez Meza</label>
                            </div>
                            <div class="col-6  text-white text-center">
                                <label>USAC</label>
                            </div>
                        </div>
                    </div>
                </div>
                <footer class="footer text-white">
                    <label>© 2021 USAC, All rights reserved.</label>
                </footer>
                </html>"""
    archivo.write(head)
    archivo.write(centro)
    archivo.write(Bottom)
    archivo.close()

def GenerarReporteErrores():
    centro = """<h1><center>Reporte de Errores</center></h1>
                        <br></br>
                        <style>
                            table,td {
	                            border: 2px solid black;
                        }
                        </style>
            <table class="default">
                <tr>
                <td align='center'>Lexema</td>
                 <td align='center'>Linea</td>
                 <td align='center'>Columna</td>
                 <td align='center'>Token</td>
                </tr>
            """
    for token in Info:
        if token.token == 'tk_desconocido':
            centro+=f"<tr><td align='center'>{token.lexema}</td><td align='center'>{token.linea}</td><td align='center'>{token.columna}</td><td align='center'>{token.token}</td></tr>"
    centro += '</table>'
    try:  
        archivo = open('ReporteErrores.html', 'w')
    except OSError:
                    archivo = open('ReporteErrores.html', 'w')
    head = """<!doctype html>
                <html lang="en">
                <meta charset="utf-8">
                <head>
                    <meta charset="utf-8">
                    <title>Reporte de Errores</title>
                    <base href="/">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link rel="icon" type="image/x-icon" href="favicon.ico">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
                    <style>
                        .navbar {
                            margin-bottom: 20px;
                            background: #A81616;
                            box-shadow: 0px 10px 6px -4px rgba(0, 0, 0, 0.75);
                        }

                        .sombra {
                            box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                        }

                        .modal-backdrop {
                            position: fixed;
                            top: 0;
                            right: 0;
                            bottom: 0;
                            left: 0;
                            z-index: 1040;
                            background-color: #333;
                        }

                        .fondo {
                            background: #37474F;
                        }

                        .b-footer {
                            background: #A81616;
                            padding: 20px;
                        }

                        .modal-content {
                            width: 650px;
                            background: #182D3E;
                            box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                        }

                        .form1 {
                            margin-bottom: 20px;
                            background: #424242;
                            padding: 20px;
                            box-shadow: 0px 10px 20px -4px rgba(0, 0, 0, 0.75);
                            list-style: none;
                            text-decoration: none;
                        }

                        .form1,
                        a:visited {
                            color: rgb(8, 8, 8);
                        }

                        .img {
                            display: block;
                            margin: auto;
                        }

                        footer {
                            background: #2B353A;
                            padding: 10px 10px;
                            text-align: center;
                        }
                    </style>
                </head>

                <body class="fondo">

                    <header>
                        <nav class="navbar navbar-expand-lg navbar-dark ">
                            <div class="container">
                                <a class="navbar-brand">
                                    <span class="fa fa-university" aria-hidden="true"></span>LFP - Proyecto1 1</a>
                                </a>
                            </div>
                        </nav>
                    </header>

                    <div class="row">
                        <div class="col-sm"></div>
                        <div class="col-sm-8">
                            <div class="card text-white bg-dark mb-3 sombra"> """

    Bottom = """</div>

                        </div>
                        <div class="col-sm"></div>
                    </div>
                </body>

                <div class="b-footer">
                    <div class="container">
                        <div class="row">
                            <div class="col-6 text-white">
                                <label>201900221 - Gabriel Enrique Perez Meza</label>
                            </div>
                            <div class="col-6  text-white text-center">
                                <label>USAC</label>
                            </div>
                        </div>
                    </div>
                </div>
                <footer class="footer text-white">
                    <label>© 2021 USAC, All rights reserved.</label>
                </footer>
                </html>"""
    archivo.write(head)
    archivo.write(centro)
    archivo.write(Bottom)
    archivo.close()

def PalabraReservada(lexema):
    if str(lexema) in PalabrasReservadas:
        return True
    else: 
        return False

def ObtenerError():
    print("============== TABLA DE ERRORES==============") 
    y = PrettyTable()
    y.field_names = ["Lexema","linea","columna","Token"]
    error =[]
    for token in Info:
        if token.token == 'tk_desconocido':
            error.append(token)
            y.add_row([token.lexema, token.linea, token.columna, token.token])
    print(y)
    return error

def ObtenerToken(lexema):
    if lexema == 'formulario':
        return "tk_formulario"
    elif lexema == 'tipo':
        return 'tk_tipo'
    elif lexema == 'valor':
        return 'tk_valor'
    elif lexema == 'fondo':
        return 'tk_fondo'
    elif lexema == 'valores':
        return 'tk_valores'
    elif lexema == 'evento':
        return 'tk_evento'
    elif lexema ==':': 
        return 'tk_dosPuntos'
    elif lexema =='~': 
        return 'tk_guionCurvo'
    elif lexema =='[': 
        return 'tk_corcheteI'
    elif lexema ==']': 
        return 'tk_corcheteD'
    elif lexema =='"': 
        return 'tk_comillas'
    elif lexema ==',': 
        return 'tk_coma'
    elif lexema ==';': 
        return 'tk_puntoComa'
    elif lexema =='>': 
        return 'tk_mayorQue' 
    elif lexema =='<': 
        return 'tk_menorQue'  
    elif lexema == "'":
        return "tk_comillasSimples"
    elif lexema == 'entrada':
        return 'tk_entrada'
    elif lexema == 'info':
        return 'tk_info'
    else:
        return 'tk_desconocido'

