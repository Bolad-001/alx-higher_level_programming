#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    #say_my_name(555, "White")
    #say_my_name("", "bolad")
    #say_my_name("bolad", 3344)
    say_my_name("Bolad@123", "Adebayo-123")
except Exception as e:
    print(e)
