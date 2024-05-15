""" Question object - Attributes = Text, Answer (initialised with a value when new question value is created through
this class.)
"""
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
