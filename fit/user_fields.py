"""Objects that represent FIT file user message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum_fields import EnumField
from .field_enums import Gender, Language


class GenderField(EnumField):
    """A FIT file message field containing the user's gender."""

    _name = 'gender'
    _enum = Gender


class LanguageField(EnumField):
    """A FIT file message field containing the user's language."""

    _name = 'language'
    _enum = Language
