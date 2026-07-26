from abc import ABC, abstractmethod

from lumos.parser.parsed_error import ParsedError


class BaseParser(ABC):

    @abstractmethod
    def parse(
        self,
        command: list[str],
        stderr: str
    ) -> ParsedError:
        pass