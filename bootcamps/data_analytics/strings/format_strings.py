def main() -> None:
    """
    go use %
    rust use macro(format!) like .format
    """
    people = {
        "name": "some name",
        "age": 25,
        "job": "developer",
        "lang": "python",
    }
    print(
        "My name is %s, I am year's %d old, work as %s with %s"
        % (people["name"], people["age"], people["job"], people["lang"]),
    )
    print(
        "My name is {}, I am year's {} old, work as {} with {}".format(
            people["name"], people["age"], people["job"], people["lang"]
        )
    )
    print(
        "My name is {name}, I am year's {age} old, work as {job} with {lang}".format(
            name=people["name"],
            age=people["age"],
            job=people["job"],
            lang=people["lang"],
        )
    )
    print(
        "My name is {name}, I am year's {age} old, work as {job} with {lang}".format(
            **people
        ),
    )
    print(
        f"My name is {people['name']}, I am year's {people['age']} old, work"
        f" as {people['job']} with {people['lang']}"
    )


if __name__ == "__main__":
    main()
