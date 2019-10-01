# -*- coding: utf-8 -*-


class PenmanError(Exception):
    """Base class for errors in the Penman package."""


class LayoutError(PenmanError):
    """Raised on invalid graph layouts."""


class DecodeError(PenmanError):
    """Raised on PENMAN syntax errors."""

    def __init__(self,
                 message: str = None,
                 filename: str = None,
                 lineno: int = None,
                 offset: int = None,
                 text: str = None):
        self.message = message
        self.filename = filename
        self.lineno = lineno
        self.offset = offset
        self.text = text

    def __str__(self):
        parts = []
        if self.filename is not None:
            parts.append('File "{}"'.format(self.filename))
        if self.lineno is not None:
            parts.append('line {}'.format(self.lineno))
        if parts:
            parts = ['', '  ' + ', '.join(parts)]
        if self.text is not None:
            parts.append('    ' + self.text)
            if self.offset is not None:
                parts.append('   ' + (' ' * self.offset) + '^')
        elif parts:
            parts[-1] += ', character {}'.format(self.offset)
        if self.message is not None:
            parts.append('{}: {}'.format(self.__class__.__name__,
                                         self.message))
        return '\n'.join(parts)


class SurfaceError(PenmanError):
    """Raised on invalid surface information."""


class ModelError(PenmanError):
    """Raised when a graph violates model constraints."""