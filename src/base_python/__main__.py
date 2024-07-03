"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Base Python."""


if __name__ == "__main__":
    main(prog_name="base-python")  # pragma: no cover
