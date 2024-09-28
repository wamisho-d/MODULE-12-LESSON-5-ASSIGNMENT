from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample list of video titles (this would be replaced by a database or larger data set in a real application)
video_titles = [
    "A Beautiful Mind",
    "Avengers: Endgame",
    "Inception",
    "Interstellar",
    "Jurassic Park",
    "The Dark Knight",
    "The Godfather",
    "The Lord of the Rings",
    "Titanic"
]

# Sort the video titles alphabetically (required for binary search)
video_titles.sort()


def binary_search(titles, target):
    """
    Perform binary search on the sorted list of titles.

    Args:
        titles (list): Sorted list of video titles.
        target (str): Search term.

    Returns:
        str or None: Matched title or None if not found.
    """
    target = target.strip().lower()  # Convert the search term to lowercase for case-insensitive search
    low, high = 0, len(titles) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_title = titles[mid].lower()

        if mid_title == target:
            return titles[mid]  # Return the original title with its case
        elif mid_title < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


@app.route('/search', methods=['GET'])
def search_video():
    target = request.args.get('title')
    if not target:
        return jsonify({"error": "Please provide a title to search"}), 400

    result = binary_search(video_titles, target)
    if result:
        return jsonify({"title": result}), 200
    else:
        return jsonify({"message": "Video not found"}), 404


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)