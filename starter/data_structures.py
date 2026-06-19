"""
Part 2 — Data Structures
=========================
Implement each function below according to its docstring.

Rules:
  - Do NOT rename functions or change their signatures.
  - Do NOT import any third-party libraries (the standard library is fine).
  - Remove the `pass` statement and replace it with your implementation.

Run your tests with:
    pytest tests/test_data_structures.py -v
"""


# ---------------------------------------------------------------------------
# Exercise 1  (5 pts)  — Lists & Sets
# ---------------------------------------------------------------------------

def get_unique_sorted(items: list) -> list:
    """Return a sorted list of unique elements from *items*.

    - Duplicates are removed.
    - The result is sorted in ascending order.
    - Works for lists of numbers or strings (no mixed types will be tested).

    Examples:
        >>> get_unique_sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
        [1, 2, 3, 4, 5, 6, 9]
        >>> get_unique_sorted(["banana", "apple", "apple", "cherry"])
        ['apple', 'banana', 'cherry']
    """
    # TODO: implement this function
    return sorted(set(items))


# ---------------------------------------------------------------------------
# Exercise 2  (5 pts)  — Lists
# ---------------------------------------------------------------------------

def merge_and_sort(list1: list, list2: list) -> list:
    """Merge two lists and return a single sorted list (ascending).

    Duplicates across both lists should be kept (do not deduplicate).

    Examples:
        >>> merge_and_sort([3, 1, 4], [1, 5, 9])
        [1, 1, 3, 4, 5, 9]
        >>> merge_and_sort([], [7, 2])
        [2, 7]
    """
    # TODO: implement this function
    return(sorted(list1 + list2))


# ---------------------------------------------------------------------------
# Exercise 3  (5 pts)  — Dictionaries
# ---------------------------------------------------------------------------

def count_word_frequency(sentence: str) -> dict:
    """Return a dictionary mapping each word to how many times it appears.

    - Split the sentence on whitespace.
    - Convert every word to lowercase before counting.
    - Punctuation is NOT stripped (treat "hello," and "hello" as different).

    Examples:
        >>> count_word_frequency("the cat sat on the mat")
        {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
        >>> count_word_frequency("Hello hello HELLO")
        {'hello': 3}
    """
    # TODO: implement this function
    counts = {}

    for word in sentence.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1

    return counts


# ---------------------------------------------------------------------------
# Exercise 4  (5 pts)  — Dictionaries & Sorting
# ---------------------------------------------------------------------------

def get_top_n(freq_dict: dict, n: int) -> list:
    """Return the top-n keys from *freq_dict* ordered by value (descending).

    If two keys share the same value, sort them alphabetically (ascending).
    Return only the keys (not the values) in a list.
    If n is larger than the dictionary size, return all keys.

    Examples:
        >>> get_top_n({'apple': 5, 'banana': 3, 'cherry': 5, 'date': 1}, 2)
        ['apple', 'cherry']
        >>> get_top_n({'a': 2, 'b': 2}, 5)
        ['a', 'b']
    """
    # TODO: implement this function
    sorted_items = sorted(
        freq_dict.items(),
        key=lambda item: (-item[1], item[0])
    )

    return [key for key, value in sorted_items[:n]]


# ---------------------------------------------------------------------------
# Exercise 5  (5 pts)  — Nested Lists
# ---------------------------------------------------------------------------

def flatten_one_level(nested: list) -> list:
    """Flatten a list of lists by exactly one level.

    Only the first level of nesting is removed. Deeper nesting is left intact.

    Examples:
        >>> flatten_one_level([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
        >>> flatten_one_level([[1, [2, 3]], [4]])
        [1, [2, 3], 4]
        >>> flatten_one_level([])
        []
    """
    # TODO: implement this function
    return [item for sublist in nested for item in sublist]


# ---------------------------------------------------------------------------
# Exercise 6  (5 pts)  — Dictionaries
# ---------------------------------------------------------------------------

def invert_dictionary(d: dict) -> dict:
    """Return a new dictionary with keys and values swapped.

    Assume all values in *d* are unique (so no collisions occur).

    Examples:
        >>> invert_dictionary({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
        >>> invert_dictionary({})
        {}
    """
    # TODO: implement this function
    return {value: key for key, value in d.items()}


# ---------------------------------------------------------------------------
# Exercise 7  (5 pts)  — Sets
# ---------------------------------------------------------------------------

def common_elements(list1: list, list2: list) -> list:
    """Return a sorted list of elements that appear in BOTH lists.

    Use set operations to find the intersection, then sort the result.

    Examples:
        >>> common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        [3, 4]
        >>> common_elements([1, 2], [3, 4])
        []
        >>> common_elements(["a", "b", "c"], ["b", "c", "d"])
        ['b', 'c']
    """
    # TODO: implement this function
    return(sorted(set(list1) & set(list2)))

# ---------------------------------------------------------------------------
# Exercise 8  (5 pts)  — Dictionaries & Loops
# ---------------------------------------------------------------------------

def group_by_first_letter(words: list) -> dict:
    """Group a list of words into a dictionary keyed by their first letter.

    - Keys are lowercase single characters.
    - Values are sorted lists of words (original case preserved) that start
      with that letter (case-insensitive comparison for grouping).
    - Empty strings in the input are ignored.

    Examples:
        >>> group_by_first_letter(["Apple", "ant", "Banana", "avocado"])
        {'a': ['Apple', 'ant', 'avocado'], 'b': ['Banana']}
        >>> group_by_first_letter([])
        {}
    """
    # TODO: implement this function
    result = {}

    for word in words:
        if not word:   # ignore empty strings
            continue

        key = word[0].lower()

        if key not in result:
            result[key] = []

        result[key].append(word)

    # sort each group
    for key in result:
        result[key].sort()

    return result

 