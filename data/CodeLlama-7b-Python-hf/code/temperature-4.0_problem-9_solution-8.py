from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    size = len(numbers)
    result = [None] * size
    result[0] = max([numbers[0]] + [numbers[1]])
    for i, num in enumerate(numbers[1:], start=1):
        if num >= numbers[i-1]:
            result[i] = num
        else:
            result[i] = result[i-1]

    for item in [None, max([result[0]] + numbers[:])]:
        try:
            result.remove(item)
        except TypeError:
            continue

    return list(set(result))  # list(set()) is for removing multiple None in result to ensure len == len origin


class ParetoElimination():
    def _find_best(self, pareto: 'set[ParetoElement]',
                   number_of_best: 'int', max_func: 'Callable') -> 'set[ParetoElement]':
        if len(pareto) < 1 or number_of_best < 0:
            return None
        best = None
        try:
            best = set(
                sorted(tuple([tuple(item)]+[(item.val,)
                                            for iitem in self.items if iitem.val < item.val), key=lambda x: (-max(x)))[0:number_of_best], key=len)[0])

        except IndexError:
            return tuple(best)
        best.pop()  # removing the (val) item from tuple
        best_values = tuple([p for p in best])

        to_pop = []
        for i in pareto:
            if len([None for j in best_values if i[j-1].val < i.value[j] if i[j-1].val != 0]) is len(best_values):
                to_pop.append(i)

        for i in to_pop:
            try:
                pareto.remove((i,))
            except KeyError:
                continue

        return pareto, pareto, best[0]