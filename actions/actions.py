from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
import re

# Validation and Submission Actions for Reset Password Form
class ValidateResetPasswordForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_reset_password_form"

    def validate_Username(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) > 0:
            return {"Username": slot_value}
        dispatcher.utter_message(text="Invalid username provided.")
        return {"Username": None}

    def validate_Email(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if re.match(r"[^@]+@[^@]+\.[^@]+", slot_value):
            return {"Email": slot_value}
        dispatcher.utter_message(text="Invalid email address provided.")
        return {"Email": None}

    def validate_Reset_method(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value in ["SMS", "Email"]:
            return {"Reset_method": slot_value}
        dispatcher.utter_message(text="Invalid reset method provided.")
        return {"Reset_method": None}

class ActionSubmitResetPassword(Action):
    def name(self) -> Text:
        return "action_submit_reset_password"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your password reset request has been submitted successfully.")
        return []

# Validation and Submission Actions for Edit Account Form
class ValidateEditAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_edit_account_form"

    def validate_Info_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value in ["name", "email", "address", "payment method"]:
            return {"Info_type": slot_value}
        dispatcher.utter_message(text="Invalid info type provided.")
        return {"Info_type": None}

class ActionSubmitEditAccount(Action):
    def name(self) -> Text:
        return "action_submit_edit_account"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account edit request has been submitted successfully.")
        return []

# Validation and Submission Actions for Create Account Form
class ValidateCreateAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_create_account_form"

    def validate_Name(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) > 0:
            return {"Name": slot_value}
        dispatcher.utter_message(text="Invalid name provided.")
        return {"Name": None}

    def validate_Email(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if re.match(r"[^@]+@[^@]+\.[^@]+", slot_value):
            return {"Email": slot_value}
        dispatcher.utter_message(text="Invalid email address provided.")
        return {"Email": None}

    def validate_Password(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) >= 8:
            return {"Password": slot_value}
        dispatcher.utter_message(text="Password must be at least 8 characters long.")
        return {"Password": None}

    def validate_Mobile_number(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if re.match(r"^\d{10}$", slot_value):
            return {"Mobile_number": slot_value}
        dispatcher.utter_message(text="Invalid mobile number provided.")
        return {"Mobile_number": None}

class ActionSubmitCreateAccount(Action):
    def name(self) -> Text:
        return "action_submit_create_account"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account creation request has been submitted successfully.")
        return []

# Validation and Submission Actions for Switch Account Form
class ValidateSwitchAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_switch_account_form"

    def validate_Username(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) > 0:
            return {"Username": slot_value}
        dispatcher.utter_message(text="Invalid username provided.")
        return {"Username": None}

    def validate_Password(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) >= 8:
            return {"Password": slot_value}
        dispatcher.utter_message(text="Password must be at least 8 characters long.")
        return {"Password": None}

class ActionSubmitSwitchAccount(Action):
    def name(self) -> Text:
        return "action_submit_switch_account"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account switch request has been submitted successfully.")
        return []

# Validation and Submission Actions for Delete Account Form
class ValidateDeleteAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_delete_account_form"

    def validate_Username(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) > 0:
            return {"Username": slot_value}
        dispatcher.utter_message(text="Invalid username provided.")
        return {"Username": None}

    def validate_Password(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) >= 8:
            return {"Password": slot_value}
        dispatcher.utter_message(text="Password must be at least 8 characters long.")
        return {"Password": None}

class ActionSubmitDeleteAccount(Action):
    def name(self) -> Text:
        return "action_submit_delete_account"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account deletion request has been submitted successfully.")
        return []

# Validation and Submission Actions for Account Verification Form
class ValidateAccountVerificationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_account_verification_form"

    def validate_Email(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if re.match(r"[^@]+@[^@]+\.[^@]+", slot_value):
            return {"Email": slot_value}
        dispatcher.utter_message(text="Invalid email address provided.")
        return {"Email": None}

class ActionSubmitAccountVerification(Action):
    def name(self) -> Text:
        return "action_submit_account_verification"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account verification request has been submitted successfully.")
        return []

# Validation and Submission Actions for Login Error Form
class ValidateLoginErrorForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_login_error_form"

    def validate_Username(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) > 0:
            return {"Username": slot_value}
        dispatcher.utter_message(text="Invalid username provided.")
        return {"Username": None}

class ActionSubmitLoginError(Action):
    def name(self) -> Text:
        return "action_submit_login_error"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your login error request has been submitted successfully.")
        return []

# Validation and Submission Actions for Recover Account Form
class ValidateRecoverAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_recover_account_form"

    def validate_Username(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) > 0:
            return {"Username": slot_value}
        dispatcher.utter_message(text="Invalid username provided.")
        return {"Username": None}

    def validate_Email(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if re.match(r"[^@]+@[^@]+\.[^@]+", slot_value):
            return {"Email": slot_value}
        dispatcher.utter_message(text="Invalid email address provided.")
        return {"Email": None}

class ActionSubmitRecoverAccount(Action):
    def name(self) -> Text:
        return "action_submit_recover_account"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account recovery request has been submitted successfully.")
        return []

# Validation and Submission Actions for Bank Details Form
class ValidateBankDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bank_details_form"

    def validate_Info_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value in ["account number", "sort code", "IBAN"]:
            return {"Info_type": slot_value}
        dispatcher.utter_message(text="Invalid info type provided.")
        return {"Info_type": None}

class ActionSubmitBankDetails(Action):
    def name(self) -> Text:
        return "action_submit_bank_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your bank details request has been submitted successfully.")
        return []

# Validation and Submission Actions for Account Access Issue Form
class ValidateAccountAccessIssueForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_account_access_issue_form"

    def validate_Username(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, str) and len(slot_value) > 0:
            return {"Username": slot_value}
        dispatcher.utter_message(text="Invalid username provided.")
        return {"Username": None}

class ActionSubmitAccountAccessIssue(Action):
    def name(self) -> Text:
        return "action_submit_account_access_issue"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account access issue request has been submitted successfully.")
        return []

# Validation and Submission Actions for Manage Account Form
class ValidateManageAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_manage_account_form"

    def validate_Info_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value in ["update profile", "change settings", "manage subscriptions"]:
            return {"Info_type": slot_value}
        dispatcher.utter_message(text="Invalid info type provided.")
        return {"Info_type": None}

class ActionSubmitManageAccount(Action):
    def name(self) -> Text:
        return "action_submit_manage_account"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your account management request has been submitted successfully.")
        return []

# Validation and Submission Actions for Security Issue Form
class ValidateSecurityIssueForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_security_issue_form"

    def validate_Info_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value in ["report fraud", "suspicious activity"]:
            return {"Info_type": slot_value}
        dispatcher.utter_message(text="Invalid info type provided.")
        return {"Info_type": None}

class ActionSubmitSecurityIssue(Action):
    def name(self) -> Text:
        return "action_submit_security_issue"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your security issue request has been submitted successfully.")
        return []

# Validation and Submission Actions for Parental Controls Form
class ValidateParentalControlsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_parental_controls_form"

    def validate_Info_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value in ["set restrictions", "monitor activity"]:
            return {"Info_type": slot_value}
        dispatcher.utter_message(text="Invalid info type provided.")
        return {"Info_type": None}

class ActionSubmitParentalControls(Action):
    def name(self) -> Text:
        return "action_submit_parental_controls"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your parental controls request has been submitted successfully.")
        return []
