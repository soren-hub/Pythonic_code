from collections import defaultdict


class SalesCount:
    def __init__(self):

        """
        defaultdict obliga que nuestros values del diccionario sean que
        del tipo de dato que se especifica al llamar la funcion 
        """

        self._counts = defaultdict(int)

    # def __init__(self):
    #    self._counts = dict()

    def __call__(self, product: str, quantity=1) -> int:

        self._counts[product] += quantity

        return self._counts[product]

    @property
    def counts(self):
        # sin el dict se imprime feito
        return dict(self._counts)


if __name__ == "__main__":
    sales = SalesCount()
    sales("fideos")
    sales("arroz")
    sales("fideos", 3)
    print(sales.counts)
