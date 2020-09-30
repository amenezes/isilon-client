import pytest
from cleo import CommandTester


@pytest.mark.parametrize(
    "commandline,expected",
    [
        ("-o my_container", '{\n"\nm\ne\ns\ns\na\ng\ne\n"\n:\n \n"\no\nk\n"\n}\n'),
        ("-c my_new_container", "my_new_container created.\n"),
        ("-m my_container", "X-Object-Meta: mock\n"),
        # ("-u my_container --headers {\"X-Container-Meta-Test\": \"my metadata\"}"),
        ("-d my_container", "my_container deleted.\n"),
    ],
)
def test_get_containers_command(cmd_app, commandline, expected):
    command = cmd_app.find("containers")
    command_tester = CommandTester(command)
    command_tester.execute(commandline)

    assert command_tester.io.fetch_output() == expected
