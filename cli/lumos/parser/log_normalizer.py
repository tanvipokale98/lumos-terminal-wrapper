import re


class LogNormalizer:

    ANSI_PATTERN = re.compile(
        r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])"
    )

    MAX_HEAD_LINES = 100
    MAX_TAIL_LINES = 50

    def normalize(self, raw_log: str) -> str:

        if not raw_log:
            return ""

        log = self.remove_ansi(raw_log)
        log = self.normalize_newlines(log)
        log = self.remove_trailing_spaces(log)
        log = self.trim_large_logs(log)

        return log

    def remove_ansi(self, text: str) -> str:
        return self.ANSI_PATTERN.sub("", text)

    def normalize_newlines(self, text: str) -> str:
        return (
            text.replace("\r\n", "\n")
                .replace("\r", "\n")
        )

    def remove_trailing_spaces(self, text: str) -> str:
        return "\n".join(
            line.rstrip()
            for line in text.split("\n")
        )

    def trim_large_logs(self, text: str) -> str:

        lines = text.split("\n")

        if len(lines) <= self.MAX_HEAD_LINES + self.MAX_TAIL_LINES:
            return text

        head = lines[:self.MAX_HEAD_LINES]
        tail = lines[-self.MAX_TAIL_LINES:]

        omitted = len(lines) - len(head) - len(tail)

        return "\n".join(
            head
            + [
                "",
                f"... ({omitted} lines omitted) ...",
                "",
            ]
            + tail
        )


normalizer = LogNormalizer()