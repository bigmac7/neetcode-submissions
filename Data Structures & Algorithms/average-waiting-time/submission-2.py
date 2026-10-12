class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = customers[0][0] #first arrival time
        waiting_times = []
        for customer in customers:
            arrival = customer[0]
            prep = customer[1]
            if arrival > current_time:
                waiting_times.append(prep)
                current_time = arrival + prep
                continue
            current_time += prep
            waiting_time = current_time - arrival
            waiting_times.append(waiting_time)
        return sum(waiting_times) / len(customers)
    