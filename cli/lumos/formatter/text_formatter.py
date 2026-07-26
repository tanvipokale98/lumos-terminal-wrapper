from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax


class TextFormatter:

    console = Console()

    @staticmethod
    def format_response(analysis: dict, original_error: str | None = None):

        error_summary = analysis.get(
            "errorSummary",
            "No summary available"
        )

        root_cause = analysis.get(
            "rootCause",
            "No root cause identified"
        )

        debugging_steps = analysis.get(
            "debuggingSteps",
            []
        )

        confidence = analysis.get(
            "confidence",
            0
        )

        TextFormatter.console.print(
            Panel(
                Markdown(error_summary),
                title="❌ Error Summary",
                expand=False
            )
        )

        TextFormatter.console.print(
            Panel(
                Markdown(root_cause),
                title="🔍 Root Cause",
                expand=False
            )
        )

        steps = "\n".join(
            f"- {step}"
            for step in debugging_steps
        )

        TextFormatter.console.print(
            Panel(
                Markdown(steps),
                title="🛠 Suggested Debugging Steps",
                expand=False
            )
        )

        TextFormatter.console.print(
            Panel(
                str(confidence),
                title="📊 Confidence Score",
                expand=False
            )
        )

        if original_error:
            TextFormatter.console.print()
            TextFormatter.console.print(
                "[bold cyan]▶ Original Error[/bold cyan] "
                "[dim](for reference)[/dim]"
            )

            TextFormatter.console.print(
                Panel(
                    Syntax(
                        original_error,
                        "text",
                        line_numbers=True,
                        word_wrap=True,
                    ),
                    title="Compiler / Runtime Error",
                    border_style="dim",
                    expand=False
                )
            )


formatter = TextFormatter()