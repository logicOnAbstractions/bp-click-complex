from application.bar import Bar


class Foo:
    def __init__(self):
        """"""
        self.bar = Bar()

    def foo(self, arg):
        return self.bar.bar(arg)
