"""Single source of truth for package version.

Read by both Python (`from qpm.core.version import __version__`)
and Node.js (`fs.readFileSync('packages/core/version.py')` parsed).
"""

__version__ = "0.1.0"


def get_version() -> str:
    """Return the current package version."""
    return __version__
