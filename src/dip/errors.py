class PlatformError(Exception):
    """Base exception for expected platform failures."""


class ValidationError(PlatformError):
    """Raised when incoming data violates a declared contract."""


class AuthorizationError(PlatformError):
    """Raised when a principal lacks a required permission."""


class NotFoundError(PlatformError):
    """Raised when a platform resource cannot be found."""
