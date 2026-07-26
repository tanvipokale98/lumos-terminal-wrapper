class ParsedError:

    def __init__(
        self,
        language: str,
        command: list[str],
        error_log: str
    ):
        self.language = language
        self.command = command
        self.error_log = error_log


    def to_dict(self):
        return {
            "language": self.language,
            "command": self.command,
            "error_log": self.error_log
        }