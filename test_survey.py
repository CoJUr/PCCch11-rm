"""Write a test case to verify aspects of anon survey class. Verify
that a single response to the survey question is stored properly using
assertIn(). Then verify three responses are stored properly."""

from survey import AnonymousSurvey
import unittest


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def test_store_single_response(self):
        """Test that a single response is store properly"""
        question = "What language did you first learn to speak?"

        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)
        # my_survey.responses = responses
        # self.assertIn('English', my_survey.responses)
        # self.assertIn('Spanish', my_survey.responses)
        # self.assertIn('Mandarin', my_survey.responses)


if __name__ == '__main__':
    unittest.main()

