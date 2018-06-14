from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.actions.action import FormAction
from rasa_core.events import SlotSet

class ActionGetClusterStatus(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("cluster", "cluster")
        ]
    
    def name(self):
        return 'action_get_cluster_status'
    
    def 