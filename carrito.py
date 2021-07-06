from collections import defaultdict

class Carrito:

    def __init__(self): 
        """
        defaultdict obliga que nuestros values del diccionario sean que
        del tipo de dato que se especifica al llamar la funcion 
        """
        self._counts = defaultdict(int)
        #print(self._counts )
    
    #def __init__(self): 
    #    self._counts = dict()
    
    def __call__(self, product: str , quantity=1) -> float:
        self._counts[product]+=quantity
        return self._counts[product]
    
    
    @property
    def counts(self)-> dict: 
        #sin el dict se imprime feito 
        return dict(self._counts)

        
    
if __name__=='__main__':
    compras = Carrito()
    compras("fideos")
    compras("arroz")
    compras("fideos",3)
    print(compras.counts)