"""MkDocs build hooks for adapting multi-language builds on Read the Docs."""

from __future__ import annotations

import logging
import os
from typing import Any

logger = logging.getLogger(__name__)


def on_config(config: Any, **kwargs: Any) -> Any:
    """Force mkdocs-static-i18n to build a single locale on Read the Docs."""
    locale = os.environ.get("READTHEDOCS_LANGUAGE")
    if not locale:
        # Local development builds all languages so the language switcher works.
        return config

    plugin = config.plugins.get("i18n")
    if plugin is None:
        logger.debug("i18n plugin not configured; skipping locale narrowing")
        return config

    try:
        languages = plugin.config.languages  # type: ignore[attr-defined]
    except AttributeError:
        logger.debug("mkdocs-static-i18n has unexpected configuration state")
        return config

    target = next((lang for lang in languages if lang.locale == locale), None)
    if target is None:
        logger.warning(
            "READTHEDOCS_LANGUAGE=%s not defined in mkdocs i18n languages; "
            "building all locales",
            locale,
        )
        return config

    for lang in languages:
        is_target = lang.locale == locale
        lang.build = is_target
        lang.default = is_target

    plugin.config.build_only_locale = locale  # type: ignore[attr-defined]
    logger.info("Configured mkdocs-static-i18n to build only '%s'", locale)
    return config
