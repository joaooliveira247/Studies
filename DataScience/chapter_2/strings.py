from icecream.icecream import ic


def main() -> None:
    # in python we can express strings with single quotes ou double quotes
    # in another languages single quotes express a char
    single_quoted_string: str = "data science"
    double_quoted_string: str = "data science"

    ic(single_quoted_string)
    ic(double_quoted_string)

    tab_string: str = "\t"
    ic(len(tab_string))

    # if you use r-strings you don't need use escape \
    not_tab_string: str = r"\t"
    ic(len(not_tab_string))
    ic(not_tab_string)

    multi_line_string: str = """
    "Hope" is the thing with feathers
    That perches in the soul
    And sings the tune without the words
    And never stops at all,

    - Emily Dickinson, Hope is the Thing with Feathers
    """

    print(multi_line_string)

    # we can concat string by differents ways:
    first_name, last_name = "Joel", "Grus"
    ic(first_name + " " + last_name)
    ic("{0} {1}".format(first_name, last_name))
    ic(f"{first_name} {last_name}")

    # strings also supports slicing or any sequence operatios
    # 'cause it's an sequence o char's
    slice: str = "Joel Grus"
    ic(slice[:4])


if __name__ == "__main__":
    main()
