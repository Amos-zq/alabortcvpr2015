from __future__ import division

from alabortcvpr2015.result import AlgorithmResult, FitterResult


class AAMAlgorithmResult(AlgorithmResult):

    def __init__(self, image, fitter, shape_parameters, costs=0,
                 appearance_parameters=None, gt_shape=None):
        super(AAMAlgorithmResult, self).__init__()
        self.image = image
        self.fitter = fitter
        self.shape_parameters = shape_parameters
        self._costs = costs
        self.appearance_parameters = appearance_parameters
        self._gt_shape = gt_shape

    def costs(self, normalize=False):
        costs = self._costs
        if normalize:
            costs /= self._costs[0]
        return list(costs)

    @property
    def final_cost(self):
        return self.costs[-1]

    @property
    def initial_cost(self):
        return self.costs[0]


class AAMFitterResult(FitterResult):

    def costs(self):
        costs = []
        for j, alg in enumerate(self.algorithm_results):
            costs += alg.costs()

        return costs

    @property
    def final_cost(self):
        r"""
        Returns the final fitting cost.

        :type: `float`
        """
        return self.algorithm_results[-1].final_cost

    @property
    def initial_cost(self):
        r"""
        Returns the initial fitting cost.

        :type: `float`
        """
        return self.algorithm_results[0].initial_cost