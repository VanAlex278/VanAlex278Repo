import pathlib
import pytest
from src.decorators import log


def test_log_in_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(2, 3)
    assert result == 5
    capture = capsys.readouterr()
    assert capture.out == "my_function ok\n"


def test_error_log_in_file(tmp_path: pathlib.Path):
    log_file = tmp_path / "mylog.txt"

    @log(str(log_file))
    def my_func(x, y):
        return x + y

    with pytest.raises(RuntimeError):
        my_func(1, "2")

    content = log_file.read_text(encoding="utf-8")
    assert content == "my_func error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2'), {}).\n"
