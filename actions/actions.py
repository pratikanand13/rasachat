from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet


class ActionResetPassword(Action):
    def name(self) -> Text:
        return "action_reset_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to reset the password
        dispatcher.utter_message(text="Your password has been reset.")
        return []

class ActionEditAccount(Action):
    def name(self) -> Text:
        return "action_edit_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to edit the account
        dispatcher.utter_message(text="Your account has been edited.")
        return []

class ActionCreateAccount(Action):
    def name(self) -> Text:
        return "action_create_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot('name')
        email = tracker.get_slot('email')
        mobile_number = tracker.get_slot('mobile_number')

        # Logic to create the account with name, email, and mobile number
        # Example: create_account_in_db(name, email, mobile_number)

        dispatcher.utter_message(text=f"Account created for {name} with email {email} and phone number {mobile_number}.")
        return [SlotSet("name", None), SlotSet("email", None), SlotSet("mobile_number", None)]

class ActionSwitchAccount(Action):
    def name(self) -> Text:
        return "action_switch_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to switch the account
        dispatcher.utter_message(text="You have switched accounts.")
        return []

class ActionDeleteAccount(Action):
    def name(self) -> Text:
        return "action_delete_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to delete the account
        dispatcher.utter_message(text="Your account has been deleted.")
        return []

class ActionAccountVerification(Action):
    def name(self) -> Text:
        return "action_account_verification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to verify the account
        dispatcher.utter_message(text="Your account has been verified.")
        return []

class ActionLoginError(Action):
    def name(self) -> Text:
        return "action_login_error"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to handle login errors
        dispatcher.utter_message(text="There was an error logging in.")
        return []

class ActionRecoverAccount(Action):
    def name(self) -> Text:
        return "action_recover_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to recover the account
        dispatcher.utter_message(text="Your account has been recovered.")
        return []

class ActionBankDetails(Action):
    def name(self) -> Text:
        return "action_bank_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to update bank details
        dispatcher.utter_message(text="Your bank details have been updated.")
        return []

class ActionAccountAccessIssue(Action):
    def name(self) -> Text:
        return "action_account_access_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to handle account access issues
        dispatcher.utter_message(text="Your account access issue has been resolved.")
        return []

class ActionManageAccount(Action):
    def name(self) -> Text:
        return "action_manage_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to manage the account
        dispatcher.utter_message(text="Your account has been managed.")
        return []

class ActionSecurityIssue(Action):
    def name(self) -> Text:
        return "action_security_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to handle security issues
        dispatcher.utter_message(text="Your security issue has been resolved.")
        return []

class ActionParentalControls(Action):
    def name(self) -> Text:
        return "action_parental_controls"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic to handle parental controls
        dispatcher.utter_message(text="Parental controls have been set.")
        return []

class ValidateAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_account_form"

    def validate_username(self, slot_value: Any,
                          dispatcher: CollectingDispatcher,
                          tracker: Tracker,
                          domain: Dict[Text, Any]) -> Dict[Text, Any]:
        # Validate the username slot
        if len(slot_value) > 0:
            return {"username": slot_value}
        else:
            dispatcher.utter_message(text="Please provide a valid username.")
            return {"username": None}

    def validate_email(self, slot_value: Any,
                       dispatcher: CollectingDispatcher,
                       tracker: Tracker,
                       domain: Dict[Text, Any]) -> Dict[Text, Any]:
        # Validate the email slot
        if "@" in slot_value:
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text="Please provide a valid email.")
            return {"email": None}

    def validate_name(self, slot_value: Any,
                      dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> Dict[Text, Any]:
        # Validate the name slot
        if len(slot_value) > 0:
            return {"name": slot_value}
        else:
            dispatcher.utter_message(text="Please provide a valid name.")
            return {"name": None}

    def validate_mobile_number(self, slot_value: Any,
                               dispatcher: CollectingDispatcher,
                               tracker: Tracker,
                               domain: Dict[Text, Any]) -> Dict[Text, Any]:
        # Validate the mobile number slot
        if slot_value.isdigit() and len(slot_value) == 10:
            return {"mobile_number": slot_value}
        else:
            dispatcher.utter_message(text="Please provide a valid mobile number.")
            return {"mobile_number": None}
