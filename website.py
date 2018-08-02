from rasa_addons.webchat import WebChatInput, SocketInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
import os

interpreter = RasaNLUInterpreter("models/current/nlu/")
agent = Agent.load("models/current/dialogue", interpreter=interpreter)
input_channel = WebChatInput(static_assets_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'index.html'))
agent.handle_channel(SocketInputChannel(5500, "/bot", input_channel))