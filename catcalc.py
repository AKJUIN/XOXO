def calculate_rating_distribution(total_points: int, num_ratings: int):
    if num_ratings <= 0:
        raise ValueError("Number of ratings must be greater than zero.")
    
    if total_points <= 0:
        raise ValueError("Total points must be greater than zero.")
    
    max_range = total_points // num_ratings
    midpoint = total_points / 2
    
    ratings = [i * max_range for i in range(1, num_ratings + 1)]
    
    print("Maximum Range between ratings:", max_range)
    print("Midpoint:", midpoint)
    print("Ratings Distribution:", ratings)

if __name__ == "__main__":
    try:
        total_points = int(input("Enter the total number of points:29"))
        num_ratings = int(input("Enter the number of ratings:7"))
        calculate_rating_distribution(total_points, num_ratings)
    except ValueError as e:
        print("Error:", e)
