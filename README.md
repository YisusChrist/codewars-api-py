<p align="center">
    <a href="https://github.com/yisuschrist/codewars-api-py/issues">
        <img src="https://img.shields.io/github/issues/yisuschrist/codewars-api-py?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-api-py/forks">
        <img src="https://img.shields.io/github/forks/yisuschrist/codewars-api-py?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-api-py/">
        <img src="https://img.shields.io/github/stars/yisuschrist/codewars-api-py?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-api-py/actions">
        <img alt="Tests Passing" src="https://github.com/yisuschrist/codewars-api-py/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-api-py/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/yisuschrist/codewars-api-py?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/gpl-3-0/">
        <img alt="License" src="https://img.shields.io/github/license/yisuschrist/codewars-api-py?color=0088ff">
    </a>
</p>

![Alt](https://repobeats.axiom.co/api/embed/6e5f320fd75dd7170566db66f681c5e4ef85db9b.svg "Repobeats analytics image")

Effortlessly interact with the Codewars API using this Python wrapper. Simplify user, challenge, and leaderboard data retrieval, making integration seamless for your projects.

<details>
<summary>Table of Contents</summary>

-   [Features](#features)
-   [Getting Started](#getting-started)
-   [Documentation](#documentation)
-   [Contributing](#contributing)
-   [License](#license)

</details>

## Features

-   **User Information:** Retrieve detailed user information including username, honor, skills, ranks, and completed challenges.
-   **Completed Challenges:** Get a list of challenges completed by a user, including details like challenge name, completion date, and programming languages used.
-   **Authored Challenges:** List challenges authored by a specific user with information on ranks, tags, and available languages.
-   **Code Challenge Details:** Obtain detailed information about a specific code challenge, including its name, description, tags, and user statistics.

## Getting Started

1. Install the package:

    ```bash
    pip install codewars-api-py
    ```

2. Use the wrapper in your Python script:

    ```python
    from codewars_api_py import CodewarsAPI

    # Initialize the Codewars API wrapper
    codewars_api = CodewarsAPI()

    # Example: Get user information
    user_info = codewars_api.get_user("some_user")
    print(user_info)

    # Example: List completed challenges
    completed_challenges = codewars_api.list_completed_challenges("some_user")
    print(completed_challenges)
    ```

## Documentation

For detailed information on available methods and usage, refer to the [Codewars API Wrapper Documentation](https://dev.codewars.com).

## Contributing

Contributions are welcome! Please check the [Contributing Guidelines](.github/CONTRIBUTING.md) for more details.

## License

This project is licensed under the GPL V3 License - see the [LICENSE](LICENSE) file for details.
