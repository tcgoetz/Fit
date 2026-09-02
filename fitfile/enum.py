"""Objects that represent enum values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import enum


def name_for_enum(enum_instance):
    """Return the name if variable is enum or UnknownEnumValue."""
    return getattr(enum_instance, 'name', enum_instance)


class UnknownEnumValue():
    """Returned when a value can not be cast to an Enum."""

    def __init__(self, value):
        """Return a UnknownEnumValue instance."""
        self.value = value
        self.name = f'{type(self).__name__}_{value}'

    @classmethod
    def from_string(cls, string, default=None):
        """Return a UnknownEnumValue instance created from a string."""
        return cls(string)

    def __eq__(self, other):
        """Test two UnknownEnumValue instances for equivelence."""
        return (other and (isinstance(other, UnknownEnumValue) and self.value == other.value)
                or (not isinstance(other, UnknownEnumValue) and self.value == other))

    def __ne__(self, other):
        """Test two UnknownEnumValue instances for equivelence."""
        return not self.__eq__(other)

    def __hash__(self):
        """Return a hash value for a UnknownEnumValue instance."""
        return self.value

    def __repr__(self):
        """Return a string representation of a UnknownEnumValue instance."""
        return f'<{type(self).__name__}.{self.name}: {self.value}>'


class Enum(enum.Enum):
    """A enum that can convert strings to enum values."""

    @classmethod
    def _from_string(cls, string):
        try:
            return cls(string)
        except Exception:
            return getattr(cls, string)

    @classmethod
    def strict_from_string(cls, string):
        """Return an instance of Enum instantiated with string."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            return None

    @classmethod
    def from_string(cls, string, default=None):
        """Return an instance of Enum instantiated with string or an instancxe of UnknownEnumValue if not found."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            if default:
                return default
            return UnknownEnumValue(string)


class CaseInsensitiveEnum(Enum):
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


class FuzzyEnum(Enum):
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
