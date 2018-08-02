from unittest import TestCase
import unittest
import sys
from rasa_core.agent import Agent
from rasa_core.actions import Action
sys.path.append('../')


class TestHadoopClient(TestCase):

    def load_agent(self):
        agent = Agent.load("../models/dialogue",
                           interpreter="../models/nlu/default/current")

        return agent

    def test_greeting(self):
        agent = self.load_agent()
        bot_response = agent.handle_message("hi")
        print(bot_response)
        self.assertTrue(bot_response[0]['text'], 'Hi! How can I help you?' or 'Hey there! What would you like to know?' or 'Hello! What would you like to know?')

    def test_help(self):
        agent = self.load_agent()
        bot_response = agent.handle_message("help")
        print(bot_response)
        self.assertTrue(bot_response[0]['text'], 'I can help you lookup the health of a cluster, tell you when the name node was created, list the databases available and the tables associated with each one. Ask away!')

    def test_thanks(self):
        agent = self.load_agent()
        bot_response = agent.handle_message("thanks")
        print(bot_response)
        self.assertTrue(bot_response[0]['text'], 'You\'re welcome!')

    def test_bye(self):
        agent = self.load_agent()
        bot_response = agent.handle_message("bye")
        print(bot_response)
        self.assertTrue(bot_response[0]['text'], 'Goodbye!' or 'Cya!' or 'Bye!')

    def test_fallback(self):
        agent = self.load_agent()
        bot_response = agent.handle_message("who is the president")
        print(bot_response)
        self.assertTrue(bot_response[0]['text'], 'Can you rephrase that?' or 'I didn\'t understand that, can you rephrase?' or 'Invalid request. Please try again.' or 'Sorry, I can\'t answer this question.')


if __name__ == '__main__':
    unittest.main()