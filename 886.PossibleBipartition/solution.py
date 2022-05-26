from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {_: [] for _ in range(1, n + 1)}

        for person1, person2 in dislikes:
            graph[person1].append(person2)
            graph[person2].append(person1)

        # Initially no groups have been assigned to any person
        # Let their be two groups group#0 and group#1
        groups = {_: None for _ in range(1, n + 1)}

        for person in range(1, n + 1):
            if groups[person] is None:
                # If a person doesn't have a group, assign group #1
                groups[person] = 1
                queue = deque([person])
                while queue:
                    currentPerson = queue.popleft()
                    for dislikedPerson in graph[currentPerson]:
                        if groups[dislikedPerson] is None:
                            # Since these two persons dislikes each other so put the second person(dislikedPerson) in another group.
                            groups[dislikedPerson] = 1 - groups[currentPerson]
                            queue.append(dislikedPerson)
                        elif groups[dislikedPerson] == groups[currentPerson]:
                            # Two persons in which one dislikes other can't be in same group
                            return False

        return True
