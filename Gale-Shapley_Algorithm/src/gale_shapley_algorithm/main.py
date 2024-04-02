from gale_shapley import gale_shapley

if __name__ == "__main__":
    men_preferences = [
        ["W0", "W1", "W2"],
        ["W1", "W2", "W0"],
        ["W2", "W0", "W1"]
    ]

    women_preferences = [
        ["M0", "M1", "M2"],
        ["M1", "M2", "M0"],
        ["M2", "M0", "M1"]
    ]

    matches = gale_shapley(men_preferences, women_preferences)
    for match in matches:
        print(f"{match[0]} is matched with {match[1]}")
