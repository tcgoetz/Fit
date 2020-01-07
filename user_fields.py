"""Objects that represent FIT file user message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.enum_fields import EnumField
import Fit.field_enums as fe


class GenderField(EnumField):
    """A FIT file message field containing the user's gender."""

    _name = 'gender'
    _enum = fe.Gender


class LanguageField(EnumField):
    """A FIT file message field containing the user's language."""

    _name = 'language'
    _enum = fe.Language
