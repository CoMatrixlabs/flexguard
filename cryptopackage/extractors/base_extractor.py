import abc

class Extractor(Scoped):
    """
    An extractor extracts record
    """

    @abc.abstractmethod
    def init(self, conf: ConfigTree) -> None:
        pass

    @abc.abstractmethod
    def extract(self) -> Any:
        """
        :return: Provides a record or None if no more to extract
        """
        return None

    def get_scope(self) -> str:
        return 'extractor'