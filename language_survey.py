"""a program that uses the survey class for testing purposes"""

from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show the question and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()