# test_hello.py
# This file contains a simple pytest test to verify the program output.
# The goal is to keep testing beginner-friendly and easy to understand.

from hello import main


def test_hello_prints_message(capsys):
    # Run the main function and capture the printed output.
    main()
    captured = capsys.readouterr()

    # Check that the output matches the required message.
    assert captured.out.strip() == "Hello MLOps"
