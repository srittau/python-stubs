from .Formatting import Font, Alignment, Borders, Pattern, Protection

class XFStyle:
    num_format_str: str
    font: Font
    alignment: Alignment
    borders: Borders
    pattern: Pattern
    protection: Protection

default_style: XFStyle
