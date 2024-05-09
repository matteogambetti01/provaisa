# ISA

isa è un'applicazione da linea di comando che, date due liste di numeri calcola alcune metriche di errore:
- MAE (mean absolute error)
- MSE (mean squared error)

## Installazione
```
python3 -m pip install .
```

## Utilizzo
```
usage: isa [-h] --predicted PREDICTED [PREDICTED ...] --expected EXPECTED [EXPECTED ...] --metrics {MAE,MSE}

Computes error metrics

options:
  -h, --help            show this help message and exit
  --predicted PREDICTED [PREDICTED ...]
                        Predicted values
  --expected EXPECTED [EXPECTED ...]
                        Expected values
  --metrics {MAE,MSE}   Metrics to compute
```
## Esempio
```
> isa --predicted 1 2 3 --expected 1 2 4 --metrics MAE
> Result: 0.3333333333333333
```