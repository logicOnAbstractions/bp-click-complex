from application.bar import Bar
import click


@click.command("bar", short_help="Run the bar mode directly")
def cli():
    """ Just to add more options to entries """
    # using an object from the application code
    bar = Bar()
    answer = bar.hello_world()
    click.echo(f"Bar says: {answer}")
