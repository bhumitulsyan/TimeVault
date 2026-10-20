"""Package metadata/version consistency tests."""

from importlib.metadata import PackageNotFoundError, version

import timevault


def test_dunder_version_matches_installed_distribution() -> None:
    """`timevault.__version__` should reflect installed distribution version."""
    try:
        dist_version = version("timevault")
    except PackageNotFoundError:
        assert timevault.__version__ == "0.0.0+unknown"
    else:
        assert timevault.__version__ == dist_version
