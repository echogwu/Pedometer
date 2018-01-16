class Filter:

    LOW_PASS_5_HZ = {
        "alpha": [1, -1.80898117793047, 0.827224480562408],
        "beta": [0.095465967120306, -0.172688631608676, 0.095465967120306]
    }
    LOW_PASS_0_HZ = {
        "alpha": [1, -1.979133761292768, 0.979521463540373],
        "beta": [0.000086384997973502, 0.000172769995947004, 0.000086384997973502]
    }
    HIGH_PASS_1_HZ = {
        "alpha": [1, -1.905384612118461, 0.910092542787947],
        "beta": [0.953986986993339, -1.907503180919730, 0.953986986993339]
    }

    def filter_low_5_hz(self, data: list):
        self.filter(data, Filter.LOW_PASS_5_HZ)

    def filter_low_0_hz(self, data: list):
        self.filter(data, Filter.LOW_PASS_0_HZ)

    def filter_high_1_hz(self, data: list):
        self.filter(data, Filter.HIGH_PASS_1_HZ)

    def filter(self, data: list, coeffient: dict) -> list:
        """
        Filter out data that is below or above a certain frequency
        Xo(t) = α0(Xi(t)β0+Xi(t−1)β1+Xi(t−2)β2−Xo(t−1)α1−Xo(t−2)α2)

        Xo means output of the time sequence
        Xi means input of the time sequence
        """
        output = [0, 0]
        alpha = Filter.LOW_PASS_0_HZ["alpha"]
        beta = Filter.LOW_PASS_0_HZ["beta"]

        for i in range(2, len(data)):
            xo = alpha[0](data[i] * beta[0] + data[i - 1] * beta[1] + data[i - 2] * beta[2] -
                          output[i - 1] * alpha[1] - output[i - 2] * alpha[2])
            output.append(xo)

        return output
