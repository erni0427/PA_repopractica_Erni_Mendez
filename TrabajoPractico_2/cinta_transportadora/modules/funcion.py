from modules.alimentos import Alimento, Papa, Verdura, Zanahoria, Manzana, Kiwi, Fruta

def detectar(diccionario=dict):
    if diccionario['alimento'] == 'kiwi':
        kiwi=Kiwi(diccionario)
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
    