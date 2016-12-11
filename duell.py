from tournament import tournament
'''
Name:  Garen Loshkajian
Project:  Project #3-> Extra Credit-> Duell in Python
Class:  Organization of Programming Languages: CMPS 366
Date Submitted:  12/11/16 (Due 12/13/16)
Note: While every parameter that we pass into a function starts with "a_" as in the last two projects,
private data members (inside a class) no longer start with "m_" unlike in C++ and Android because Python makes
you write the code as: self.membername. This means that something like self.m_board would be unreadable code.
Also, unlike in C++ and Android, class names and function names no longer begin with an uppercase letter. Instead
in this project they begin with a lowercase letter.
'''
#Play the series of rounds.
tournament = tournament()
tournament.playSeries()