def canCompleteCircuit(gas, cost):
    total_gas = 0
    remaining_gas = 0
    start_index = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        remaining_gas += gas[i] - cost[i]

        if remaining_gas < 0:
            remaining_gas = 0
            start_index = i + 1

    if total_gas >= 0:
        return start_index
    else:
        return -1


print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))
