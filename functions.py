FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a textfile todos.txt and returns a list of each line as a todos item.
    :param: filepath: str: "todos.txt"
    :return: todos_local: list: actual todos in the txt file
    """
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(local_todos, filepath="todos.txt"):
    """
    The actual todos list is written to the todos.txt file
    :param: local_todos: List: actual todos
    :param: filepath: str: the filepath to write
    :return: None
    """
    with open(filepath, 'w') as local_file:
        local_file.writelines(local_todos)


# print(__name__)
# # __name__ is a variable with the value "__main__", so a string
if __name__ == '__main__':
    print('Hello')
    print(get_todos())

# if you run this script directly, then the indented code is executed.      __name__ == '__main__'

# if you run this script from outside another file  __name__ == 'functions'

