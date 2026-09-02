class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                sum_of_previous_two = record[-2] + record[-1]
                record.append(sum_of_previous_two)
            elif op == 'D':
                double_previous = record[-1] * 2
                record.append(double_previous)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
        
        return sum(record)
                
        