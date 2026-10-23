"""Smoke test: proves the package imports and the toolchain runs."""

import pytest

import ontherecord


def test_package_imports() -> None:
    assert ontherecord.__version__ == "0.1.0"


def test_main_prints_banner(capsys: pytest.CaptureFixture[str]) -> None:
    ontherecord.main()
    assert "OnTheRecord backend" in capsys.readouterr().out
