import argparse
import sys
import logging

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
            logging.critical("Predicted and expected must have the same length")
            sys.exit()

    def _is_consistent(self) -> bool:
        """
        Check the consistency of the list: they must have the same length
        """
        return len(self.predicted) == len(self.expected)

    def _mae(self) -> float:
        """
        Compute the MAE metric
        """
        result: float = 0
        for i in range(0, len(self.predicted)):
            result += abs(self.predicted[i] - self.expected[i])
        return result/len(self.predicted)

    def _mse(self) -> float:
        # TODO
        return -1

    def compute_metrics(self) -> float:
        """
        Choose which metric execute
        """
        if self.metrics == "MAE":
            return self._mae()
        elif self.metrics == "MSE":
            return self._mse()
        else:
            return -1


def main():
    # 1. interpretazione argomenti da linea di comando
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
        choices=["MAE","MSE"]
    )

    logging.basicConfig(level=logging.WARNING)

    arguments = parser.parse_args()
    logging.debug(arguments.predicted)
    #print(arguments.predicted)
    logging.debug(arguments.expected)
    #print(arguments.expected)
    logging.debug(arguments.metrics)
    #print(arguments.metrics)

    solver = Operation(arguments.predicted, arguments.expected, arguments.metrics)
    result = solver.compute_metrics()
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
