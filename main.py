from random import randint
from collections import Counter

class Group:
    group: int = 1
    def __init__(self, X: list[float], Y: list[float]) -> None:
        self.X = X
        self.Y = Y
        self.group = self.group
        Group.group += 1  


def generate_dataset(num_of_groups: int, num_of_points: int):
    dataset = []
    for _ in range(0, num_of_groups):
        X = [] 
        Y = []
        for _ in range(num_of_points):
            X.append(randint(1, 10))
            Y.append(randint(1, 10))
        dataset.append(Group(X, Y).__dict__)
    return dataset

def count_elements(data):
        arr = []
        for i in data:
            arr.append(i['group'])
        element_counts = Counter(arr)
        max_count = max(element_counts.values())
        if list(element_counts.values()).count(max_count) > 1:
            # msg.showerror("Error", "Can not classify point, there are two or more points with the same number of neighbours")
            pass
        else:
            return max(element_counts, key=element_counts.get)
        
def sort_distance(element):
        #Sorting array by distance to every point
        return element["distance"]
