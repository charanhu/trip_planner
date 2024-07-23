import json
import os
import requests
from langchain.tools import tool
from duckduckgo_search import DDGS


class SearchTools:

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a given topic and return relevant results"""
        top_result_to_return = 4

        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=top_result_to_return))

        if not results:
            return "Sorry, I couldn't find anything about that query."
        else:
            string = []
            for result in results:
                try:
                    string.append(
                        "\n".join(
                            [
                                f"Title: {result['title']}",
                                f"Link: {result['href']}",
                                f"Snippet: {result['body']}",
                                "\n-----------------",
                            ]
                        )
                    )
                except KeyError:
                    continue

            return "\n".join(string)
