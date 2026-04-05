#!/usr/bin/python3
"""list sinfindən miras alan MyList sinfi."""


class MyList(list):
    """Siyahı xüsusiyyətlərini genişləndirən sinif."""

    def print_sorted(self):
        """Siyahını artan sıra ilə (ascending) çap edir."""
        print(sorted(self))
