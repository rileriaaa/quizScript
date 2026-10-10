import random
from pathlib import Path

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

questionDir = Path(__file__).parent / "questions"
answerDir = Path(__file__).parent / "answers"
questionDir.mkdir(exist_ok=True)
answerDir.mkdir(exist_ok=True)


for quizNum in range(35):
    quizFile = open(
        questionDir / f"quizQuestionaire{quizNum + 1}.txt", "w", encoding="UTF-8"
    )
    quizAnswer = open(
        answerDir / f"quizAnswerSheet{quizNum + 1}.txt", "w", encoding="UTF-8"
    )

    quizFile.write("Name:\nDate:\nPeriod:\n\n")

    quizFile.write(f"State Capitals Quiz (Form{quizNum + 1})")
    quizFile.write("\n\n")

    states = list(capitals.keys())
    random.shuffle(states)

    for num in range(50):
        correctAnswer = capitals[states[num]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f"{num + 1}. Capital of {states[num]}\n")
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write("\n")

        quizAnswer.write(f"{num + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")

    quizFile.close()
    quizAnswer.close()
