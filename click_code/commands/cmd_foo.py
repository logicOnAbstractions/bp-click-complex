from application.foo import Foo
import click


@click.command("foo", short_help="Run the foo mode")
def cli():
    """A dumb basic example of appcode use"""
    # using an object from the application code
    foo = Foo()
    answer = foo.foo("What's up?")
    click.echo(f"Received an answer from appcode: {answer}")

