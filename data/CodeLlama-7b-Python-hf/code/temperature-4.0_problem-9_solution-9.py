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

    def find_best(self, input_data: 'List[set[Tuple]]', total_best: 'int') -> 'tuple[tuple[tuple[list[ParetoElement]], tuple[ParetoElement]], tuple[ParetoElement, list[ParetoElement]], set[list]':
        """ Find best n elements in a given input set of multiple lists. It is a general solution for multiple
        input sets and it uses elimination of dominated values.
        """

        assert type(input_data).__name__ == 'list'
        paretos = tuple([p[:] for p in input_data])
        max_func = None
        if all([type(i.value[0]).__name__ == 'IntegerValue'
                for j in set(paretos).union([i for j in set(self.items).union(paretos)])
                   for k in j if k[1] == 1 and k in tuple(self.items)]),\
        "The problem does not use discrete integers as optimization variable "
        if type(max(input_data)).__name__.find('Integ') is not -1 or max(input_data).__class__ is not DiscreteValue and all([abs(y.value for y in x) != abs(x).value[0].value or y.value == 0 for x in input_data]
                                                                                                                                   for i in tuple([(k.val+1,) for k in input_data[0]])):
            return (None, None, paretos.pop)
        to_pop = set([tuple([x for x in set(self.items)-set([x if type(x) is tuple else x for z in set(paretos)]) if x.value[0].val == 0])], [
                    tuple()])
        if all([tuple((i,)) in to_pop or len(set([(k[0].value[len(list(k.value)[0]))].value for k in i])) is len(list(set([k for j in i if k in i[0]]))) for i in paretos]):
            return None, None