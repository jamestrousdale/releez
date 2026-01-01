from __future__ import annotations

from typing import TYPE_CHECKING

from releez.settings import ReleezSettings
from releez.version_tags import AliasTags

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_settings_reads_pyproject_tool_releez_kebab_case(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / 'pyproject.toml').write_text(
        '[tool.releez]\nalias-tags = "major"\ngit-remote = "upstream"\n',
        encoding='utf-8',
    )

    settings = ReleezSettings()
    assert settings.alias_tags == AliasTags.major
    assert settings.git_remote == 'upstream'


def test_settings_reads_releez_toml(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / 'releez.toml').write_text(
        'alias_tags = "minor"\n',
        encoding='utf-8',
    )

    settings = ReleezSettings()
    assert settings.alias_tags == AliasTags.minor


def test_settings_reads_env_vars(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv('RELEEZ_ALIAS_TAGS', 'major')

    settings = ReleezSettings()
    assert settings.alias_tags == AliasTags.major
