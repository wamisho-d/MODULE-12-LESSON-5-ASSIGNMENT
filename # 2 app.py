# Task 2: Flask API Implementation.

from flask import Flask, jsonify
from video import Video, merge_sort

app = Flask(__name__)

# Sample video data
video = [
    Video("The Shawshank Redemption", "2h 22m", "Drama"),
    Video("The Dark Knight", "2h 32m", "Action"),
    Video("12 Angry Men", "1h 36m", "Drama"),
    Video("Schinder's List", "3h 15m", "History"),
    Video("The Lord of the Rings", "2h 58", "Adventure"),
]

@app.route('/videos/sorted', methods=['GET'])
def get_sorted_videos():
    sorted_videos = merge_sort(videos)
    video_data = [{'title': v.title, 'duration': v.duration, 'genre': v.genre} for v in sorted_videos]
    return jsonify(video_data)
if __name__ == '__main__':
    app.run(debug=True)
    
