"""
Loader shim for _workers_sdk_entropy_import_context.

This module is imported by the .pth file on every Python startup. The entropy
context patches depend on the `_cloudflare` package, which only exists inside
the workers runtime. When running outside of the workers runtime, `_cloudflare`
is not available, so we silently skip loading the patches.
"""

import importlib.util

if importlib.util.find_spec("_cloudflare") is not None:
    import _workers_sdk_entropy_import_context  # noqa: F401
