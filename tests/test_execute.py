import os
import stat


def test_execute():
    output = os.popen("/tmp/start")

    assert output.read() == "Hallo\n"


def test_is_executable():
    filename = "/tmp/start"
    executable = stat.S_IXUSR & os.stat(filename)[stat.ST_MODE]

    assert executable
