# SPDX-FileCopyrightText: 2026 KIT Environmental Circle Earth
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The API tools"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Super MCP Server')


@mcp.resource('vocabulary')
def vocabulary() -> list[str]:
    """Returns the special vocablary for recording.

    Returns
    -------
    vocab : list[str]
        The vocabulary word list.
    """
    return [
        'あーす',
        '京都工芸繊維大学',
        '工繊',
        '府大',
    ]


if __name__ == '__main__':
    mcp.run()
