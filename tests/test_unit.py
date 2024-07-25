import pytest
#from isa.isa import Operation
import isa.isa as isa
class TestUnit:
    #Notare che i test sono praticamente uguali, cambiano i parametri di ingresso (nel caso dei primi due test)
    def test_mae_0(self):
        #Due liste identiche il risultato sarà sempre 0, questo verrà fatto dal property based test.....
        p = [1.0,2.0,5.0]
        e = [1.0,2.0,5.0]
        expected_result = 0
        op = isa.Operation(predicted = p, expected = e, metrics = "MAE")
        computed_value = op.compute_metrics()

        assert computed_value == expected_result
    
    #Modo per saltare un test
    @pytest.mark.skip("Temp skip.")
    def test_mae_1(self):
        p=[1.0,2.0,5.0]
        e=[1.0,2.0,4.0]
        expected_value = 0.33
        op = isa.Operation(predicted=p, expected=e, metrics="MAE")
        computed_value = op.compute_metrics()
        #Uso pytest approx per approssimare il risultato dato che la metrica restituisce 0.33333333 invece di 0.33
        assert pytest.approx(computed_value) == expected_value

    def test_raises_exception(self):
        #Controllo se chiamando il metodo con sue liste di dimensione diversa ottengo l'errore ValueError
        with pytest.raises(ValueError):
            isa.Operation([1.0,2.0],[1.0],"MAE")

    #Stesso test con parametri diversi che vengono definiti da mark.parametrize
    @pytest.mark.parametrize("p,e,m,r",[ #variabili che verranno istanziate automaticamente
        ([1.0,2.0,3.0],[1.0,2.0,3.0], "MSE",0), #prima combinazione di variabili
        ([2.0,3.0,5.0],[2.0,3.0,4.0], "MSE",1/3), #seconda combinazione di variabili
        ([1.0,2.0,3.0],[1.0,2.0,3.0], "RMSE",0) #terza combinazione di variabili
    ])
    def test_parametrized(self, p, e, m, r):
        # expected_result = 0

        op = isa.Operation(predicted = p, expected = e, metrics = m)
        computed_value = op.compute_metrics()

        assert computed_value == r

    #Esempio di mocking, la metrica non è ancora stata sviluppata
    def test_rmse(self, monkeypatch):
        p=[1.0,2.0,3.0]
        e=[1.0,2.0,3.0]
        expected_result = 0

        op = isa.Operation(predicted=p,expected=e,metrics="RMSE")

        #Imposto manualmente il valore che dovrebbe restituire la metrica dato che non è ancora stata implementata
        monkeypatch.setattr(op,"compute_metrics", lambda: 0)
        computed_value = op.compute_metrics()

        assert computed_value == expected_result

    def test_rmse_0(self):
        p = [1.0,2.0,5.0]
        e = [1.0,2.0,5.0]
        expected_result = 0
        op = isa.Operation(predicted = p, expected = e, metrics = "RMSE")
        computed_value = op.compute_metrics()

        assert computed_value == expected_result

    def test_rmse_1(self):
        import math
        p = [1.0,2.0,5.0]
        e = [1.0,2.0,4.0]
        expected_result = math.sqrt(1/3)
        op = isa.Operation(predicted = p, expected = e, metrics = "RMSE")
        computed_value = op.compute_metrics()

        assert computed_value == expected_result
        


"""
    VARI ESEMPI DI TEST ERRATI
    def test_non_test(self):
        p = [1.0,2.0,5.0]
        e = [1.0,2.0,5.0]
        expected_result = 0
        op = Operation(predicted = p, expected = e, metrics = "MAE")
        computed_value = op.compute_metrics()
        #Quello sopra non è un test perchè non fa nessun assert
        #return computed_value == expected_result # Neanche questo è un test dato che deve esserci assert e non return
        try: 
            assert computed_value == expected_result
        except:
            assert True
        #Anche questo è sbagliato, l'assert non deve essere all'interno di un try-except
"""
    