#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of the codewars-api-py package.

This module contains the main function of the package.

Functions:
    main() -> int: Main function.
"""

from rich import print
from rich.traceback import install

from .cli import exit_session, get_parsed_args
from .consts import DEBUG, EXIT_SUCCESS, PROFILE
from .api import CodewarsAPI
from .logs import logger


def main() -> int:
    """
    Main function
    """
    logger.info("Start of session")
    
    args = get_parsed_args()

    # Example Usage
    codewars_api = CodewarsAPI()

    username = input("Enter your username: ")

    # Get user information
    user_info = codewars_api.get_user(username)
    print("User Info:")
    print(user_info)

    # List completed challenges
    completed_challenges = codewars_api.list_completed_challenges(username)
    print("\nCompleted Challenges:")
    print(completed_challenges)

    # List authored challenges
    authored_challenges = codewars_api.list_authored_challenges(username)
    print("\nAuthored Challenges:")
    print(authored_challenges)

    # Get code challenge information
    code_challenge_info = codewars_api.get_code_challenge("valid-braces")
    print("\nCode Challenge Info:")
    print(code_challenge_info)

    exit_session(EXIT_SUCCESS)


if __name__ == "__main__":
    # Enable rich error formatting in debug mode
    install(show_locals=DEBUG)
    if DEBUG:
        print("[yellow]Debug mode is enabled[/yellow]")
    if PROFILE:
        import cProfile

        print("[yellow]Profiling is enabled[/yellow]")
        cProfile.run("main()")
    else:
        main()
