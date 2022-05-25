class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        numRooms = len(rooms)
        if numRooms == 0:
            return  True
        # If 0th room has no keys then we can't visit any other room.
        if not rooms[0]:
            return False
        keys = set([0])
        queue = deque([[0, rooms[0]]])
        roomsVisited = 1
        while queue:
            _, keysFound = queue.popleft()
            for key in keysFound:
                if key not in keys:
                    roomsVisited += 1
                    keys.add(key)
                    queue.append([key, rooms[key]])
        return roomsVisited == numRooms
            
