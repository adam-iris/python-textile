import six
import subprocess
import sys

def test_console_script():
    command = [sys.executable, '-m', 'textile', 'README.textile']
    try:
        result = subprocess.check_output(command)
    except AttributeError:
        command[2] = 'textile.__main__'
        result = subprocess.Popen(command,
                stdout=subprocess.PIPE).communicate()[0]
    with open('tests/fixtures/README.txt') as f:
        expect = ''.join(f.readlines())
    if type(result) == bytes:
        result = result.decode('utf-8')
    assert result == expect
