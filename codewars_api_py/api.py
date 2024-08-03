"""Module for interacting with Codewars API."""
from typing import Dict, Optional

from requests import RequestException, Session

from .logs import logger


class CodewarsAPI:
    """
    Class for interacting with Codewars API.

    Reference from Codewars API Documentation:
    https://dev.codewars.com

    Attributes:
        BASE_URL (str): The base URL for the Codewars API.
    """

    BASE_URL = "https://www.codewars.com/api/v1"

    def __init__(self):
        """Initialize a CodewarsAPI object."""
        logger.debug("Initializing CodewarsAPI object")
        self.session = Session()

    def _handle_request(self, url: str) -> Optional[Dict]:
        """
        Handle a request to the Codewars API.

        Args:
            url (str): The URL to request.

        Returns:
            dict: The response JSON.

        Example:
            >>> codewars_api = CodewarsAPI()
            >>> url = f"{codewars_api.BASE_URL}/users/some_user"
            >>> response = codewars_api._handle_request(url)
            >>> print(response)

            ...
        """
        logger.debug(f"Handling request to {url}")
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error during request: {e}")
            logger.error(f"Error during request: {e}")
            return None

    def get_user(self, username: str) -> Optional[Dict]:
        """
        Returns a user information.

        Args:
            username (str): The username or ID to search for.

        Returns:
            dict: The user information.

        Example:
            >>> codewars_api = CodewarsAPI()
            >>> user_info = codewars_api.get_user("some_user")
            >>> print(user_info)

            {
                "username": "some_user",
                "name": "Some Person",
                "honor": 544,
                "clan": "some clan",
                "leaderboardPosition": 134,
                "skills": [
                    "ruby",
                    "c#",
                    ".net",
                    "javascript",
                    "coffeescript",
                    "nodejs",
                    "rails"
                ],
                "ranks": {
                    "overall": {
                        "rank": -3,
                        "name": "3 kyu",
                        "color": "blue",
                        "score": 2116
                    },
                    "languages": {
                        "javascript": {
                            "rank": -3,
                            "name": "3 kyu",
                            "color": "blue",
                            "score": 1819
                        },
                        "ruby": {
                            "rank": -4,
                            "name": "4 kyu",
                            "color": "blue",
                            "score": 1005
                        },
                        "coffeescript": {
                            "rank": -4,
                            "name": "4 kyu",
                            "color": "blue",
                            "score": 870
                        }
                    }
                },
                "codeChallenges": {
                    "totalAuthored": 3,
                    "totalCompleted": 230
                }
            }

        """
        logger.debug(f"Getting user information for {username}")
        url = f"{self.BASE_URL}/users/{username}"
        return self._handle_request(url)

    def list_completed_challenges(self, username: str, page: int = 0) -> Optional[Dict]:
        """
        Returns a list of completed challenges.

        Lists challenges completed by a user, 200 items per page. Use page
        parameter (zero based) to paginate.

        Args:
            username (str): The username or ID to search for.
            page (int): The page offset. Each page contains at most 200 items.
                Default is 0.

        Returns:
            dict: The list of completed challenges.

        Example:
            >>> codewars_api = CodewarsAPI()
            >>> completed_challenges = codewars_api.list_completed_challenges("some_user")

            {
                "totalPages": 1,
                "totalItems": 1,
                "data": [
                    {
                        "id": "514b92a657cdc65150000006",
                        "name": "Multiples of 3 and 5",
                        "slug": "multiples-of-3-and-5",
                        "completedAt": "2017-04-06T16:32:09Z",
                        "completedLanguages": [
                            "javascript",
                            "coffeescript",
                            "ruby",
                            "javascript",
                            "ruby",
                            "javascript",
                            "ruby",
                            "coffeescript",
                            "javascript",
                            "ruby",
                            "coffeescript"
                        ]
                    }
                ]
            }
        """
        logger.debug(f"Getting list of completed challenges for {username}")
        url = f"{self.BASE_URL}/users/{username}/code-challenges/completed?page={page}"
        return self._handle_request(url)

    def list_authored_challenges(self, username: str) -> Optional[Dict]:
        """
        List challenges authored by the user.

        Args:
            username (str): The username or ID to search for.

        Returns:
            dict: The list of authored challenges.

        Example:
            >>> codewars_api = CodewarsAPI()
            >>> authored_challenges = codewars_api.list_authored_challenges("some_user")

            {
                "data": [
                    {
                        "id": "5571d9fc11526780a000011a",
                        "name": "The builder of things",
                        "description": "For this kata you will be using some meta-programming ...",
                        "rank": -3,
                        "rankName": "3 kyu",
                        "tags": [
                            "Algorithms",
                            "Metaprogramming",
                            "Programming Paradigms",
                            "Advanced Language Features",
                            "Fundamentals",
                            "Domain Specific Languages",
                            "Declarative Programming"
                        ],
                        "languages": ["ruby", "javascript", "python", "coffeescript"]
                    },
                    {
                        "id": "51ba717bb08c1cd60f00002f",
                        "name": "Range Extraction",
                        "description": "A format for expressing an ordered list of integers ...",
                        "rank": -4,
                        "rankName": "4 kyu",
                        "tags": [
                            "Algorithms",
                            "String Formatting",
                            "Formatting",
                            "Logic",
                            "Strings"
                        ],
                        "languages": [
                            "javascript",
                            "coffeescript",
                            "ruby",
                            "go",
                            "python",
                            "java",
                            "haskell",
                            "csharp",
                            "cpp"
                        ]
                    }
                ]
            }
        """
        logger.debug(f"Getting list of authored challenges for {username}")
        url = f"{self.BASE_URL}/users/{username}/code-challenges/authored"
        return self._handle_request(url)

    def get_code_challenge(self, challenge_id_or_slug: str) -> Optional[Dict]:
        """
        Return a code challenge information.

        Args:
            challenge_id_or_slug (str): The ID or slug of the challenge.

        Returns:
            dict: The code challenge information.

        Example:
            >>> codewars_api = CodewarsAPI()
            >>> code_challenge_info = codewars_api.get_code_challenge("valid-braces")

            {
                "id": "5277c8a221e209d3f6000b56",
                "name": "Valid Braces",
                "slug": "valid-braces",
                "url": "http://www.codewars.com/kata/valid-braces",
                "category": "algorithms",
                "description": "Write a function called `validBraces` that takes a string ...",
                "tags": ["Algorithms", "Validation", "Logic", "Utilities"],
                "languages": ["javascript", "coffeescript"],
                "rank": {
                    "id": -4,
                    "name": "4 kyu",
                    "color": "blue"
                },
                "createdBy": {
                    "username": "xDranik",
                    "url": "http://www.codewars.com/users/xDranik"
                },
                "approvedBy": {
                    "username": "xDranik",
                    "url": "http://www.codewars.com/users/xDranik"
                },
                "totalAttempts": 4911,
                "totalCompleted": 919,
                "totalStars": 12,
                "voteScore": 512,
                "publishedAt": "2013-11-05T00:07:31Z",
                "approvedAt": "2013-12-20T14:53:06Z"
            }
        """
        logger.debug(f"Getting code challenge information for {challenge_id_or_slug}")
        url = f"{self.BASE_URL}/code-challenges/{challenge_id_or_slug}"
        return self._handle_request(url)
