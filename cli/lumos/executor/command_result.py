from dataclasses import dataclass

@dataclass
class CommandResult:
    command: list[str]
    stdout: str
    stderr: str
    exit_code: int

