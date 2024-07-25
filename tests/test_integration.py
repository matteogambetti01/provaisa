import pytest
import isa.isa as isa
class TestIntegration:
    #Voglio testare la funzione main
    def test_integration_arguments(self,monkeypatch):
        import argparse
        def return_value():
            return argparse.Namespace(
                predicted = [1.0,2.0,3.0],
                expected  = [1.0,2.0,3.0],
                metrics = "MAE"
            ),
        #Devo fare il mocking della funzione setup_parser che viene utilizzata dal main
        monkeypatch.setattr(isa, "setup_parser", return_value)
        assert isa.main(isa.setup_parser) == 0