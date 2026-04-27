from __future__ import annotations

from ._types import Length, Number


def escape(text: str) -> str:
    """Make the text safe to use in SVG.
    """
    pass


def mm(val: Number) -> Length:
    """Explicitly specify mm unit for the value.
    """
    pass


def px(val: Number) -> Length:
    """Explicitly specify px unit for the value.
    """
    pass
