from unittest.mock import patch

import pytest

from tomlrun.cli import main


def test_cli(capsys):
    with patch("sys.argv", ["run", "-l"]):
        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert captured.out.strip()

    with patch("sys.argv", ["run", "-V"]):
        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "0.0.1"

    with patch("sys.argv", ["run", "test"]):
        main()
    captured = capsys.readouterr()
    # NOTE: Does not capture subprocess.run output...
    assert captured.out.strip() == ""

    with patch("sys.argv", ["run", "print"]):
        main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "test"

    with patch("sys.argv", ["run", ""]):
        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert captured

    with patch("sys.argv", ["run", "fake"]):
        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert captured.err == "\nError: Script not found: fake\n"

    with patch("sys.argv", ["run", "one", "-v"]):
        main()
    captured = capsys.readouterr()
    assert captured.out.strip().startswith("--- preone ---")

    # with patch("sys.argv", ["run", "-D"]):
    #     main()
