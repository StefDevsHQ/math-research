"""Error types for the Monotone NAE-3SAT research harness."""


class NAE3Error(Exception):
    """Base class for expected harness errors."""


class ParseError(NAE3Error):
    """Raised when serialized input is malformed or uses an unsupported schema."""


class ValidationError(NAE3Error):
    """Raised when a graph or derived-object invariant is violated."""


class ColoringError(NAE3Error):
    """Raised when a proposed colouring is not a total binary assignment."""
