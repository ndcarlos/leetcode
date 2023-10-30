class Solution:
    def average(self, salary: List[int]) -> float:
        count = len(salary)
        max_sal = int(max(salary))
        min_sal = int(min(salary))
        average = (sum(salary) -(max_sal + min_sal)) / (count-2)

        return average