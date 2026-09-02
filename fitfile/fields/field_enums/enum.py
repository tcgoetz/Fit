"""Objects that represent FIT file enum fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ...enum import Enum, UnknownEnumValue


class Enum(Enum):
    """A enum representing a FIT file message field value."""
    pass


class CaseInsensitiveFieldEnum(Enum):
    """A enum representing a field value that can be instantiated with a case insensitive match."""

    @classmethod
    def from_string_ext(cls, string):
        """Return an instance of Enum instantiated with string using a case insensitive match."""
        for name, value in cls.__members__.items():
            if name.lower() == str(string).lower():
                return value
        return UnknownEnumValue(string)

    @classmethod
    def from_string(cls, string, default=None):
        """Return an instance of Enum instantiated with string."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            if default:
                return default
            return cls.from_string_ext(string)


class FuzzyFieldEnum(Enum):
    """A enum representing a field value that can be instantiated with a fuzzy match."""

    @classmethod
    def from_string_ext(cls, string):
        """Return an instance of Enum instantiated with string using a fuzzy match."""
        for name, value in cls.__members__.items():
            if name.lower() in str(string).lower():
                return value
        return UnknownEnumValue(string)

    @classmethod
    def from_string(cls, string, default=None):
        """Return an instance of Enum instantiated with string."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            if default:
                return default
            return cls.from_string_ext(string)
