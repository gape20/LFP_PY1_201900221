from Token import Tokenn
from error import error
class Sintactico:
    actual = "tk_Desconocido"
    posicion = 0
    listaTokens = []
    Error = False
    instruccion = ""
    instrucciones = []
    acum = []
    aux = []

    def __init__(self, listaTokens):
        self.listaTokens = listaTokens
        self.listaTokens.append((Tokenn("#", "tk_ultimo",0,0)))
        posicion = 0
        self.actual = listaTokens[posicion]
        self.Inicio()

    def Comprobar(self, tokenn):
        if self.actual.token != tokenn:
            if self.Error == False:
                self.Error = True

                print(f"Se recibio '{self.actual.lexema}' -- Se esperaba un token {str(tokenn)} -- En la linea {self.listaTokens[self.posicion].linea}")
                
        if self.actual.token != "tk_ultimo":
            if self.actual.token == "tk_cadena" or self.actual.token == "tk_entrada" or self.actual.token == "tk_info":
                self.acum.append(self.actual.lexema)
            self.posicion += 1
            self.actual = self.listaTokens[self.posicion]

    def Inicio(self):
        self.Formulario()
        #print(self.instrucciones)
        #for ins in self.instrucciones:
            #print(ins)
        self.Repertir()

    def Formulario(self):
        self.Comprobar('tk_formulario')
        self.Comprobar('tk_guionCurvo')
        self.Comprobar('tk_mayorQue')
        self.Comprobar('tk_mayorQue')
        self.Comprobar('tk_corcheteI')
        self.BloqueIntruccion()
        self.Comprobar('tk_corcheteD')

    def Repertir(self):
        if self.actual.token != 'tk_ultimo':
            self.Formulario()
            #print(self.instrucciones)
            self.Repertir()
    
    def BloqueIntruccion(self):
        self.CuerpoInstuccion()
        self.instrucciones.append(self.aux)
        self.aux = []
        if self.actual.token == 'tk_coma':
            self.Comprobar('tk_coma')
            self.BloqueIntruccion()
        
    def CuerpoInstuccion(self):
        self.Comprobar('tk_menorQue')
        self.BloqueElementos()
        self.Comprobar('tk_mayorQue')

    def BloqueElementos(self):
        self.Elementos()
        if self.actual.token == 'tk_coma':
            self.Comprobar('tk_coma')
            self.BloqueElementos()

    def Elementos(self):
        if self.actual.token == 'tk_tipo':
            self.instruccion = 'tipo'
            self.tipo()
        elif self.actual.token == 'tk_valor':
            self.instruccion = 'valor'
            self.valor()
        elif self.actual.token == 'tk_valores':
            self.instruccion = 'valores'
            self.valores()
        elif self.actual.token == 'tk_evento':
            self.instruccion = 'evento'
            self.evento()
        elif self.actual.token == 'tk_fondo':
            self.instruccion = 'fondo'
            self.fondo()
        self.aux.append([self.instruccion, self.acum])
        self.acum = []

    def tipo(self):
        self.Comprobar('tk_tipo')
        self.Comprobar('tk_dosPuntos')
        self.Comprobar('tk_cadena')

    def valor(self):
        self.Comprobar('tk_valor')
        self.Comprobar('tk_dosPuntos')
        self.Comprobar('tk_cadena')

    def valores(self):
        self.Comprobar('tk_valores')
        self.Comprobar('tk_dosPuntos')
        self.Comprobar('tk_corcheteI')
        self.BloqueValores()
        self.Comprobar('tk_corcheteD')

    def evento(self):
        self.Comprobar('tk_evento')
        self.Comprobar('tk_dosPuntos')
        self.Comprobar('tk_menorQue')
        if self.actual.token == 'tk_entrada':
            self.Comprobar('tk_entrada')
        elif self.actual.token == 'tk_info':
            self.Comprobar('tk_info')
        self.Comprobar('tk_mayorQue')
        
    def BloqueValores(self):
        self.Comprobar('tk_cadena')
        if self.actual.token == 'tk_coma':
            self.Comprobar('tk_coma')
            self.BloqueValores()
            
    def fondo(self):
        self.Comprobar('tk_fondo')
        self.Comprobar('tk_dosPuntos')
        self.Comprobar('tk_cadena')