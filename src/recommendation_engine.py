def get_next_topic(current_topic):
    learning_path = [
        "Regression",
        "Optimization",
        "Neural Networks",
        "CNN"
    ]

    if current_topic in learning_path:
        index = learning_path.index(current_topic)
        if index < len(learning_path) - 1:
            return learning_path[index + 1]

    return current_topic


def recommend_next_step(score, attempts, time_spent, current_topic):

    # Policy-based adaptive logic with explainability

    if score < 50:
        action = "Revision"
        difficulty_adjustment = "Decrease"
        next_topic = current_topic
        reason = "Score below 50 indicates weak understanding. Revision is recommended."

    elif 50 <= score < 75:
        action = "Practice"
        difficulty_adjustment = "Same"
        next_topic = current_topic
        reason = "Score between 50 and 75 indicates moderate understanding. Additional practice is recommended."

    else:
        action = "Advance"
        difficulty_adjustment = "Increase"
        next_topic = get_next_topic(current_topic)
        reason = "Score above 75 indicates strong understanding. Advancing to the next topic."

    return {
        "next_topic": next_topic,
        "action": action,
        "difficulty_adjustment": difficulty_adjustment,
        "reason": reason
    }


if __name__ == "__main__":
    # Simulated student data
    score = int(input("Enter quiz score: "))
    attempts = int(input("Enter number of attempts: "))
    time_spent = int(input("Enter time spent (minutes): "))
    current_topic = input("Enter current topic: ")

    result = recommend_next_step(score, attempts, time_spent, current_topic)

    print("\nRecommendation:")
    print(result)
