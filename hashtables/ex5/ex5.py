# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    set_queries = set()
    for I in queries:
        set_queries.add(I)
    for path in files:
        list_path = path.split('/')
        if list_path[-1] in set_queries:
            result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
