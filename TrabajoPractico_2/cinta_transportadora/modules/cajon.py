class Cajón: #Se asocia con CintaTransportadora
    def __init__(self, n_elementos=int):
        self.__elementos=[]
        self.__n_elementos=n_elementos
        return
    
    @property
    def elementos(self):
        return(self.__elementos)
    @property
    def n_elementos(self):
        return(self.__n_elementos)

    def agregar(self, Alimento):
        Infed=[]
        if Alimento.nombre == 'undefined':
            print("No se pudo realizar el transporte")
            pass
#            self.Indef.append(Alimento)
#            rint("!!!!!"+self.Indef)
        elif self.__n_elementos > len(self.__elementos):
            self.__elementos.append(Alimento)
        else:
            print("Cajón lleno")
#        print(self.elementos)
    def prom_aw(self, tipo):#nombre_str_alimento=str):
        cont=0
        tot=0
        for e in self.__elementos:
            if isinstance (e, tipo):
                cont += 1
                tot += e.CalcularAW()
        if cont !=0 : 
            return tot/cont
        else: 
            return cont

