import requests
import typer

from lumos.executor.process_runner import runner
from lumos.parser.parser_service import parser
from lumos.api.api import api
from lumos.formatter.text_formatter import formatter
app = typer.Typer(
    help="Lumos CLI",
    add_completion=False,
)


@app.command(
    context_settings={
        "allow_extra_args": True,
        "ignore_unknown_options": True,
    }
)
def run(ctx: typer.Context):

    if not ctx.args:
        typer.echo("No command provided.")
        raise typer.Exit(code=1)

    command = ctx.args[1:]

    result = runner.execute(command)

    if result.exit_code == 0:
        if result.stdout:
            typer.echo(result.stdout)
        raise typer.Exit(code=0)

    parsed_error = parser.parse(command, result.stderr).to_dict()
    try:

        response=api.analyse(parsed_error)
        formatted_response = formatter.format_response(response,parsed_error)
        typer.echo(formatted_response)
    except requests.HTTPError:
         typer.secho("\nAI analysis unavailable. Showing original error:\n", fg="yellow")
         typer.echo(parsed_error["error_log"])

    except Exception:
        typer.secho("\nSomething went wrong while analyzing the error.\n", fg="red")
        typer.echo(parsed_error["error_log"])   

if __name__ == "__main__":
    app()