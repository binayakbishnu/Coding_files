class Example:
    class_variable = 8

    def __init__(self, user_input):
        self.instance_variable = user_input

    def print_output(self):
        print(self.class_variable)
        print(self.instance_variable)
        print(Example.class_variable)
        print(Example.instance_variable)    # error


example = Example(9)

example.print_output()

