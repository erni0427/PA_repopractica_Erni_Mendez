class Cajón: #Se asocia con CintaTransportadora
    def __init__(self, n_elementos=int):
        self.elementos=[]
        self.n_elementos=n_elementos
        return
    def agregar(self, Alimento):
        Infed=[]
        if Alimento.nombre == 'undefined':
            print("No se pudo realizar el transporte")
            pass
#            self.Indef.append(Alimento)
#            rint("!!!!!"+self.Indef)
        elif self.n_elementos > len(self.elementos):
            self.elementos.append(Alimento)
        else:
            print("Cajón lleno")
#        print(self.elementos)
    def prom_aw(self, tipo):#nombre_str_alimento=str):
        cont=0
        tot=0
        for e in self.elementos:
            if isinstance (e, tipo):
                cont += 1
                tot += e.CalcularAW()
        if cont !=0 : 
            return tot/cont
        else: 
            return cont