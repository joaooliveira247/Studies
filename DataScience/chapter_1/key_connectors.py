from collections import Counter, defaultdict


def number_of_friends(user: dict, friendships: dict) -> int:
    return len(friendships[user["id"]])


def foaf_ids_bad(user: dict, friendships: dict) -> list:
    return [
        foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
    ]


def friends_of_friends(user: dict, friendship: dict) -> Counter:
    return Counter(
        foaf_id
        for friend_id in friendship[user["id"]]
        for foaf_id in friendship[friend_id]
        if foaf_id != user["id"] and foaf_id not in friendship[user["id"]]
    )


def data_scientists_who_like(
    target_interest: str, interests: list[tuple[int, str]]
) -> list:
    return [
        user_id
        for user_id, user_interest in interests
        if user_interest == target_interest
    ]


def most_common_interests_with(
    user: dict,
    interests_by_user_id: defaultdict,
    user_ids_by_interest: defaultdict,
) -> Counter:
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )


def main() -> None:
    # this represents edge's of graph
    users: list[dict[str, int | str]] = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"},
    ]

    # this represents connections(vertix)
    friendship_paris: list[tuple[int, int]] = [
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (5, 7),
        (6, 8),
        (7, 8),
        (8, 9),
    ]

    friendships = {user["id"]: [] for user in users}

    for i, j in friendship_paris:
        friendships[i].append(j)
        friendships[j].append(i)

    total_connections: int = sum(
        number_of_friends(user, friendships) for user in users
    )

    avg: float = total_connections / len(users)

    print(f"Total Connections: {total_connections} | Average: {avg}")

    num_friends_by_id = [
        (user["id"], number_of_friends(user, friendships)) for user in users
    ]

    # centralidade de grau
    num_friends_by_id.sort(
        key=lambda id_n_friend: id_n_friend[1], reverse=True
    )

    print(num_friends_by_id)

    print(foaf_ids_bad(users[0], friendships))

    print(friends_of_friends(users[3], friendships))

    interests: list[tuple[int, str]] = [
        (0, "Hadoop"),
        (0, "Big Data"),
        (0, "HBase"),
        (0, "Java"),
        (0, "Spark"),
        (0, "Storm"),
        (0, "Cassandra"),
        (1, "NoSQL"),
        (1, "MongoDB"),
        (1, "Cassandra"),
        (1, "HBase"),
        (1, "Postgres"),
        (2, "Python"),
        (2, "scikit-learn"),
        (2, "scipy"),
        (2, "numpy"),
        (2, "statsmodels"),
        (2, "pandas"),
        (3, "R"),
        (3, "Python"),
        (3, "statistics"),
        (3, "regression"),
        (3, "probability"),
        (4, "machine learning"),
        (4, "regression"),
        (4, "decision trees"),
        (4, "libsvm"),
        (5, "Python"),
        (5, "R"),
        (5, "Java"),
        (5, "C++"),
        (5, "Haskell"),
        (5, "programming languages"),
        (6, "statistics"),
        (6, "probability"),
        (6, "mathematics"),
        (6, "theory"),
        (7, "machine learning"),
        (7, "scikit-learn"),
        (7, "Mahout"),
        (7, "neural networks"),
        (8, "neural networks"),
        (8, "deep learning"),
        (8, "Big Data"),
        (8, "artificial intelligence"),
        (9, "Hadoop"),
        (9, "Java"),
        (9, "MapReduce"),
        (9, "Big Data"),
    ]

    users_ids_by_interest: dict = defaultdict(list)
    interest_by_user_id: dict = defaultdict(list)

    for user_id, interest in interests:
        users_ids_by_interest[interest].append(user_id)
        interest_by_user_id[user_id].append(interest)

    print(
        users_ids_by_interest,
        interest_by_user_id,
    )

    print(
        most_common_interests_with(
            users[0], interest_by_user_id, users_ids_by_interest
        )
    )


if __name__ == "__main__":
    main()
