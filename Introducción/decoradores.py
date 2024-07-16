def saludar(function):
    def decorador_saludar():
        print(f"la función '{function.__name__}' dice hola")
        return function

    return decorador_saludar


@saludar
def example_one():
    pass


@saludar
def example_two():
    pass


@saludar
def example_tree():
    pass


example_one()
example_two()
example_tree()

"""
Extra
"""


def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La función '{function.__name__} se ha llamado {counter_function.call_count}' veces."
        )
        return function

    counter_function.call_count = 0
    return counter_function


@call_counter
def example_function_4():
    pass


@call_counter
def example_function_5():
    pass


example_function_4()
example_function_4()
example_function_4()
example_function_4()
example_function_5()
example_function_4()
example_function_5()
