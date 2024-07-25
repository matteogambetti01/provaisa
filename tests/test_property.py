import isa.isa as isa
from hypothesis import given, strategies, settings
class PropertyTest:
    @given(
            #I dati devono essere delle liste
            strategies.lists(
                #all'interno delle liste devono esserci delle tuple
                strategies.tuples(
                    strategies.decimals(allow_nan = False, allow_infinity = False) #i valori sono decimali non nulli
                ), min_size = 2, max_size = 2 #genero una lista di esattamente due elementi
            )
    )
    @settings(max_examples = 100)
    def test_property_always_geq_0(self, l):
        p,e = l
        op = isa.Operation(predicted=p, expected= e, metrics="MAE")
        res = op.compute_metrics()
        assert res >= 0
