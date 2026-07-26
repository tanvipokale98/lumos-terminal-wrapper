import subprocess
from lumos.executor.command_result import CommandResult

class ProcessRunner:
    def execute(self, command: list[str]) -> CommandResult:
        try:
            result = subprocess.run(command, capture_output=True, text=True,encoding="utf-8",
    errors="replace")
            return CommandResult(
                command=command,
                stdout=result.stdout,
                stderr=result.stderr,
                exit_code=result.returncode
            )
        except Exception as e:
            return CommandResult(
                command=command,
                stdout="",
                stderr=str(e),
                exit_code=-1
            )
        

runner = ProcessRunner()    