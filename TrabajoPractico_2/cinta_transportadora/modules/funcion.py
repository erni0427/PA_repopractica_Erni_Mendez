from modules.alimentos import Alimento, Papa, Verdura, Zanahoria, Manzana, Kiwi, Fruta

def detectar(diccionario=dict): #para identificar de que alimento se trata
    if diccionario['alimento'] == 'kiwi': 
        kiwi=Kiwi(diccionario) #Si el valor de 'alimento' en el diccionario es 'kiwi', la función crea una instancia de la clase Kiwi pasando el diccionario como argumento, y luego devuelve esa instancia.
        return kiwi
    elif diccionario['alimento'] == 'papa':
        papa=Papa(diccionario)
        return papa
    elif diccionario['alimento'] == 'manzana':
         manzana=Manzana(diccionario)
         return manzana
    elif diccionario['alimento'] == 'zanahoria':
        zanahoria=Zanahoria(diccionario)
        return zanahoria
    elif diccionario['alimento'] == 'undefined':
        #indefinido=Indefinido(diccionario)
        #return indefinido
        pass
    