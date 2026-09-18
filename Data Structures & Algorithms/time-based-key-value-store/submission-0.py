class TimeMap:

    def __init__(self):
        self.timestamps = {} # key : (value, time)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp are strictly increasing order
        if key not in self.timestamps:
            self.timestamps[key] = [(value, timestamp)]
        else:
            self.timestamps[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        else:
            array = self.timestamps[key] #self.timestamps[key] is the array
            left = 0
            right = len(array) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if array[mid][1] == timestamp:
                    print(array[mid][0])
                    return array[mid][0]
                else:
                    if timestamp < array[mid][1]:
                        right = mid - 1
                    elif timestamp > array[mid][1]:
                        left = mid + 1
            if right == -1:
                return ""
            return array[right][0]

        
                
                


            
        
    


         