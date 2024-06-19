from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionContactCustomerService(Action):
    def name(self) -> Text:
        return "action_contact_customer_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["inquiry", "contact_method", "urgency", "previous_interactions"]
        missing_slots = []

        for slot in required_slots:
            if tracker.get_slot(slot) is None:
                missing_slots.append(slot.replace('_', ' '))

        if missing_slots:
            missing_slots_str = ', '.join(missing_slots)
            dispatcher.utter_message(text=f"Please provide the following information: {missing_slots_str}.")
            return []

        dispatcher.utter_message(text="Thank you. We have received your inquiry.")
        return [SlotSet("requested_slot", None)]

class ActionContactHumanAgent(Action):
    def name(self) -> Text:
        return "action_contact_human_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        reason = tracker.get_slot('reason')
        urgency = tracker.get_slot('urgency')
        contact_method = tracker.get_slot('contact_method')
        availability = tracker.get_slot('availability')

        if not reason or not urgency or not contact_method or not availability:
            dispatcher.utter_message(text="Please provide the reason for contact, urgency, preferred contact method, and your availability.")
            return []
        
        dispatcher.utter_message(text="Thank you. A human agent will contact you soon.")
        return []

class ActionTechnicalSupport(Action):
    def name(self) -> Text:
        return "action_technical_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        issue_type = tracker.get_slot('issue_type')
        device = tracker.get_slot('device')
        error_message = tracker.get_slot('error_message')
        troubleshooting_steps = tracker.get_slot('troubleshooting_steps')
        urgency = tracker.get_slot('urgency')

        if not issue_type or not device or not error_message or not troubleshooting_steps or not urgency:
            dispatcher.utter_message(text="Please specify the type of technical issue, your device, any error messages, troubleshooting steps, and urgency.")
            return []
        
        dispatcher.utter_message(text="Thank you. Our technical support team will assist you shortly.")
        return []

class ActionDeliveryOptions(Action):
    def name(self) -> Text:
        return "action_delivery_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot('destination')
        special_requirements = tracker.get_slot('special_requirements')
        delivery_method = tracker.get_slot('delivery_method')

        if not destination or not special_requirements or not delivery_method:
            dispatcher.utter_message(text="Please provide the destination, any special requirements, delivery options for the location, and preferred delivery method.")
            return []
        
        dispatcher.utter_message(text="Thank you. We have noted your delivery preferences.")
        return []

class ActionDeliveryCharge(Action):
    def name(self) -> Text:
        return "action_delivery_charge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot('location')
        order_details = tracker.get_slot('order_details')
        discounts = tracker.get_slot('discounts')
        payment_method = tracker.get_slot('payment_method')

        if not location or not order_details or not discounts or not payment_method:
            dispatcher.utter_message(text="Please provide the delivery location, order details, any available discounts, and payment method.")
            return []
        
        dispatcher.utter_message(text="Thank you. We have calculated your delivery charge.")
        return []

class ActionDeliveryStatus(Action):
    def name(self) -> Text:
        return "action_delivery_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        order_number = tracker.get_slot('order_number')
        tracking_info = tracker.get_slot('tracking_info')
        status = tracker.get_slot('status')

        if not order_number or not tracking_info or not status:
            dispatcher.utter_message(text="Please provide the order number, tracking information, your contact details, and the current status.")
            return []
        
        dispatcher.utter_message(text="Thank you. Here is the current status of your delivery.")
        return []

class ActionDeliveryPeriod(Action):
    def name(self) -> Text:
        return "action_delivery_period"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        order_date = tracker.get_slot('order_date')
        expected_time = tracker.get_slot('expected_time')
        urgency = tracker.get_slot('urgency')
        tracking_info = tracker.get_slot('tracking_info')

        if not order_date or not expected_time or not urgency or not tracking_info:
            dispatcher.utter_message(text="Please provide the order date, expected delivery time, urgency, and tracking information.")
            return []
        
        dispatcher.utter_message(text="Thank you. Here is the expected delivery period for your order.")
        return []

class ActionMyCustomForm(Action):
    def name(self) -> Text:
        return "action_my_custom_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Implement your custom form logic here
        dispatcher.utter_message(text="This is the response from the custom form.")
        return []
