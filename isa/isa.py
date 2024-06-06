import argparse
import sys
import logging
import math

class Operation():
    """
    Class to handle the metrics computations.
    """
    def __init__(self,
            predicted: 'list[float]',
            expected: 'list[float]',
            metrics: str
        ) -> None:
        self.predicted: 'list[float]' = predicted
        self.expected: 'list[float]' = expected
        self.metrics: str = metrics

        if not self._is_consistent():
            #print("Predicted and expected must have the same length")
            raise ValueError("Predicted and expected must have the same length")

    def _is_consistent(self) -> bool:
        """
        Check the consistency of the input list: they must have the same length
        """
        return len(self.predicted) == len(self.expected)

    def _mae(self) -> float:
        """
        Computes the MAE metric
        """
        result: float = 0

        fn = lambda p,e : abs(p, e)
        result = sum(list(map(fn, self.predicted, self.expected)))
        # le due righe sopra sono equivalenti a quelle commentate
        #for x1,x2 in zip(self.predicted, self.expected):
            #result += abs(x1 - x2)
        return result/len(self.predicted)

    def _mse(self) -> float:
        """
        Computes the MSE metric
        """
        result: float = 0
        for x1,x2 in zip(self.predicted, self.expected):
            result += abs(x1 - x2) **2
        return result/len(self.predicted)
    
    def _rmse(self) -> float:
        return math.sqrt(self._mse())

    def compute_metrics(self) -> float:
        """
        Choose which metric execute
        """
        if self.metrics == "MAE":
            return self._mae()
        elif self.metrics == "MSE":
            return self._mse()
        elif self.metrics == "RMSE":
            return self._rmse()
        else:
            return -1

def setup_parser() -> argparse.Namespace:
    """
    Parses the arguments
    """
    parser = argparse.ArgumentParser(
        prog="isa",
        description="Computes error metrics"
    )

    parser.add_argument("--predicted",
        nargs='+',
        type=float,
        required=True,
        help="Predicted values"
    )

    parser.add_argument("--expected",
        nargs='+',
        type=float,
        required=True,
        help="Expected values"
    )

    parser.add_argument("--metrics",
        type=str,
        required=True,
        help="Metrics to compute",
        choices=["MAE","MSE", "RMSE"]
    )
    return parser.parse_args()

def main(arguments):
    """
        Main function
    """
    # 1. interpretazione argomenti da linea di comando

    logging.basicConfig(level=logging.WARNING)
    logging.debug(arguments.predicted)
    logging.debug(arguments.expected)
    logging.debug(arguments.metrics)

    solver = Operation(arguments.predicted, arguments.expected, arguments.metrics)
    return solver.compute_metrics()


if __name__ == "__main__":
    result = main(setup_parser())
    print(f"Result: {result}")
