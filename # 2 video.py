# Video Sorting with Merge Sort

# Task 1: Merge Sort Implementation

# video.py
class video:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre
    def __repr__(self):
        return f"Title: {self.title}, Duration: {self.duration}, Genre: {self.genre}"
    
def merge_sort(videos):
    if len(videos) <= 1:
        return videos
    mid = len(videos) // 2
    left_half = video[:mid]
    right_half = videos[mid:]

    left_half = merge_sort(left_half)
    right_half = megre_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].title.lower() <= right[right_index]. title.lower():
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Task 3: Testing with Postman

# Request 

# GET /videos?sort=title&order=asc

# Response 

# JSON
[
    {
        "id": 1,
        "title": "Video A",
        "viewCount": 100,
        "uploadDate": "2022-01-01",
        "rating": 4.5
    },
    { 
        "id": 2,
        "title": "Video B",
        "viewCount": 50,
        "uploadData": "2022-01-15",
        "rating": 4.0
    },
    {   "id": 3,
        "title": "Video C",
        "viewCount": "2022-01-03",
        "rating": 4.8
    }
]






    




