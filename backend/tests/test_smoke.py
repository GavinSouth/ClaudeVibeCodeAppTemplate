"""Smoke test: proves the package imports and the toolchain runs."""

import pytest

import claudevibecodeapptemplate


def test_package_imports() -> None:
    assert claudevibecodeapptemplate.__version__ == "0.1.0"


def test_main_prints_banner(capsys: pytest.CaptureFixture[str]) -> None:
    claudevibecodeapptemplate.main()
    assert "ClaudeVibeCodeAppTemplate backend" in capsys.readouterr().out
