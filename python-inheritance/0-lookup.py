#!/usr/bin/python3
"""Obyektin atributlarını tapan modul."""


def lookup(obj):
    """Obyektin mövcud atribut və metodlarının siyahısını qaytarır.

    Args:
        obj: Yoxlanılacaq obyekt.

    Returns:
        list: Atribut və metodların adlarından ibarət siyahı.
    """
    return dir(obj)
