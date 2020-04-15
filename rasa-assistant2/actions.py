# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import sys
import os
sys.path.insert(1, os.getcwd()+'/../regression/')
from test import pred_age_from_image_url


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text=json.dumps(tracker.latest_message))
        #dispatcher.utter_message(text=tracker.latest_message['text'])
        url = tracker.latest_message['text']
        if url[:5] == "https" and ".jpg" in url:
            pred_age = pred_age_from_image_url(url)
            if pred_age == "Error":
                dispatcher.utter_message(text= "There was an error detecting your face. Please try again.")
            else:
                dispatcher.utter_message(text = "Your estimated age is " + str(int(pred_age)) + " years")
        else:
            dispatcher.utter_message("Show me your pic and I will guess your age")
        return []
