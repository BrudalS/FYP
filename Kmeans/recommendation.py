def recommend_based_on_emotion(emotion):
    """Recommend actions or settings based on detected emotion."""
    recommendations = {
        "Happy": "Play happy music, set light to yellow",
        "Sad": "Play calming music, set light to blue"
    }
    return recommendations.get(emotion, "No recommendation")
