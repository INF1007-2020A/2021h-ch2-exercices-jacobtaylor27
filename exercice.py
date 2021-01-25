#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    var = ""
    for i in range(len(mot)):
        var += chr(ord(mot[i]) - 32)
    mot = var
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
