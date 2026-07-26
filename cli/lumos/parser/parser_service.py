from lumos.parser.base_parsor import BaseParser
from lumos.parser.parsed_error import ParsedError
from lumos.parser.log_normalizer import normalizer


class ParserService:

    def parse(
        self,
        command: list[str],
        stderr: str
    ):

        normalized=normalizer.normalize(stderr)

        return ParsedError(
            language=command[0] if command else "",
            command=command,
            error_log=normalized
        )

parser = ParserService()