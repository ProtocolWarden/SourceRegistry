# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Velascat
from enum import StrEnum


class InstallKind(StrEnum):
    """How a source's installed state is verified.

    - ``cli_tool``: Python CLI installed via ``uv tool install``;
      verify reads ``direct_url.json`` from the tool's site-packages.
    - ``library``: Python library installed via pip. (placeholder.)
    - ``binary``: Prebuilt binary. (placeholder.)
    - ``external``: Out-of-process service (e.g. a bun monorepo);
      verify by ``git rev-parse HEAD`` in the local clone.
    - ``none``: No verification beyond local-path existence.
    """
    CLI_TOOL = "cli_tool"
    LIBRARY = "library"
    BINARY = "binary"
    EXTERNAL = "external"
    NONE = "none"


class InstallMode(StrEnum):
    DEV = "dev"
    CI = "ci"
    PROD = "prod"
