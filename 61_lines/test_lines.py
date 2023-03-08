from lines import check_commandline_argument
from lines import count_lines
import pytest


def test_commandline_argument():
    with pytest.raises(SystemExit):
        check_commandline_argument(["myfile.py"])
    with pytest.raises(SystemExit):
        check_commandline_argument(["myfile.py", "file"])
    with pytest.raises(SystemExit):
        check_commandline_argument(["myfile.py", "fileThat does not exists"])
    check_commandline_argument(["myfile.py", "lines.py"])


def test_count_lines():
    assert count_lines("file1.py") == 3
    assert count_lines("file2.py") == 1
    assert count_lines("file3.py") == 3
