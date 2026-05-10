# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 ProtocolWarden
class SourceRegistryError(Exception):
    """Base exception for SourceRegistry."""


class SourceNotFoundError(SourceRegistryError):
    """Raised when a source entry cannot be resolved."""


class DuplicateSourceError(SourceRegistryError):
    """Raised when duplicate source names are provided."""


class GitOperationError(SourceRegistryError):
    """Raised when a git operation fails."""


class RegistryLoadError(SourceRegistryError):
    """Raised when loading source registry data fails."""
