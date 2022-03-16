from Token import Tokenn
from error import error
from prettytable import PrettyTable
import os




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
    centro += '''
    <h4>nombre</h4>
                        <textarea cols="10" rows="1" style="resize: both;" placeholder="placeholder"></textarea>
                        <br>
                        </br>
                        <form>
                            <h4>Sexo</h4>
                            <div>
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <input type="radio" id="masc" name="masc" value="masculino">
                                <label for="masc">Masculino</label> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <input type="radio" id="fem" name="masc" value="femenino">
                                <label for="fem">Femenino</label>
                                <br> </br>
                                <h4>Pais</h4>
                                <select name="select">
                                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                    <option value="value1"><h1>Value 1</h1></option>
                                    <option value="value2"><h1>Value 2</h1></option>
                                    <option value="value3"><h1>Value 3</h1></option>
                                    <br> </br>
                                  </select>
                                <br> </br>
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <button type="button"><h4>EVENTO</h4></button>
                                <br> </br>
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
        return 'tk_valor'
    elif lexema == 'fondo':
        return 'tk_fondo'
    elif lexema == 'nombre':
        return 'tk_nombre'
    elif lexema == 'valores':
        return 'tk_valores'
    elif lexema == 'evento':
        return 'tk_evento'
    elif lexema ==':': 
        return 'tk_dosPuntos'
    elif lexema =='~': 
        return 'tk_GuionCurvo'
    elif lexema =='[': 
        return 'tk_CorcheteI'
    elif lexema ==']': 
        return 'tk_CorcheteD'
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
    else:
        return 'tk_desconocido'

