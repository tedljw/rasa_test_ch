from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionAnswer(Action):

    def name(self):
        return 'action_answer'

    def run(self, dispatcher, tracker, domain):
        money = tracker.get_slot("money")
        dispatcher.utter_message("这里是回答动作.")
        dispatcher.utter_message("money is “{}”".format(money))
        return []

