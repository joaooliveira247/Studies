from icecream.icecream import ic


def main() -> None:
    empty_dict: dict = {}
    empty_dict_2: dict = dict()
    grades = {"Joel": 80, "Tim": 95}
    ic((empty_dict, empty_dict_2, grades))

    ic(grades["Joel"])

    try:
        kates_grade = grades["Kate"]
    except KeyError:
        print("no grade for Kate!")

    joel_has_grade, kate_has_grade = "Joel" in grades, "Kate" in grades

    ic((joel_has_grade, kate_has_grade))

    joels_grade = grades.get("Joel", 0)
    kates_grade = grades.get("Kate", 0)
    no_ones_grade = grades.get("No One")

    ic((joels_grade, kates_grade, no_ones_grade))

    grades["tim"] = 99
    grades["kate"] = 100
    num_students = len(grades)

    ic((grades, num_students))

    tweet: dict[str, str | int | list[str]] = {
        "user": "joelgrus",
        "text": "Data Science is Awesome",
        "retweet_count": 100,
        "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"],
    }

    ic(tweet)

    tweet_keys: str = tweet.keys()
    tweet_values: str | int | list[str] = tweet.values()
    tweet_items: tuple[str, str | int | list[str]] = tweet.items()

    ic((tweet_keys, tweet_values, tweet_items))

    # 1º(not pythonic)2º(pythonic)3º(it's only way)
    ic(("user" in tweet_keys, "user" in tweet, "joelgrus" in tweet_values))


if __name__ == "__main__":
    main()
