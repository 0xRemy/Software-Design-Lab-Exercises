"""
Program: doctor.py
Author: Ken
Conducts an interactive session of nondirective psychotherapy.
"""

import random
history = []

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please coninue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"} 

class Doctor:
    def _init_(self):
        pass
    def greeting(self):
        return "Good day!\nWhat can I do for you today?"
    def bye(self):
        return "I hope I have answered your concerns, It was nice meeeting you. Call us back if you still feel any problems."
    def reply(self,sentence):
        """Implements two different reply strategies."""
        probability = random.randint(1, 5)
        if probability in (1,2):
         answer = random.choice(hedges)
        elif probability == 3 and len(history) > 3:
            answer = "You said that " + \
            changePerson(random.choice(history))
        else:
         answer = random.choice(qualifiers) + changePerson(sentence)
         history.append(sentence)
         return answer

def changePerson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords) 

def main():
    """Handles the interaction between patient and doctor."""
    doctor=Doctor()
    print(doctor.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doctor.bye())
            break
        print(doctor.reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()

