from query_understanding import analyze_query
from recommendation_engine import recommend_next_step

def main():

    # Step 1: Query Understanding
    user_query = input("Enter student query: ")
    query_result = analyze_query(user_query)

    print("\nQuery Understanding Result:")
    print(query_result)

    # Step 2: Student Performance Input
    score = int(input("\nEnter quiz score: "))
    attempts = int(input("Enter number of attempts: "))
    time_spent = int(input("Enter time spent (minutes): "))

    recommendation = recommend_next_step(
        score,
        attempts,
        time_spent,
        query_result["topic"]
    )

    print("\nFinal Recommendation:")
    print(recommendation)


if __name__ == "__main__":
    main()
