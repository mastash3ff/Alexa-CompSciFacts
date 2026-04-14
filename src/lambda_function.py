import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SKILL_NAME = "Comp Sci Interview Facts"
HELP_MESSAGE = (
    "You can say tell me a comp sci fact, or you can say exit. "
    "What can I help you with?"
)
GOODBYE_MESSAGE = "Goodbye!"

FACTS = [
    "Array indexing for linear and dynamic arrays is constant time.",
    "Array search is big Oh of N.",
    "Array insertion for dynamic arrays is big Oh of N.",
    "Linked list indexing is big Oh of N.",
    "Linked list search is big Oh of N.",
    "Linked list insertion is constant time.",
    "Hash table indexing is constant time.",
    "Hash table search is constant time.",
    "Hash table insertion is constant time.",
    "Binary tree indexing is big Oh of log N.",
    "Binary tree search is big Oh of log N.",
    "Binary tree insertion is big Oh of log N.",
    "Breadth First Search runtime is big Oh of the total number of edges and vertices.",
    "Depth First Search runtime is big Oh of the total number of edges and vertices.",
    "Merge Sort best case is big Oh of N.",
    "Merge Sort average case is big Oh of N log N.",
    "Merge Sort worst case is big Oh of N log N.",
    "Quick Sort best case is big Oh of N.",
    "Quick Sort average case is big Oh of N log N.",
    "Quick Sort worst case is big Oh of N squared.",
    "Bubble Sort best case is big Oh of N.",
    "Bubble Sort average case is big Oh of N squared.",
    "Bubble Sort worst case is big Oh of N squared.",
]


def get_random_fact() -> str:
    return "Here's your comp sci fact: " + random.choice(FACTS)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch — gives a fact and ends the session."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech = get_random_fact()
        return (
            handler_input.response_builder
            .speak(speech)
            .set_should_end_session(True)
            .response
        )


class GetNewFactIntentHandler(AbstractRequestHandler):
    """Handler for GetNewFactIntent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("GetNewFactIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech = get_random_fact()
        return (
            handler_input.response_builder
            .speak(speech)
            .set_should_end_session(True)
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for AMAZON.HelpIntent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return (
            handler_input.response_builder
            .speak(HELP_MESSAGE)
            .ask(HELP_MESSAGE)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Handler for AMAZON.CancelIntent and AMAZON.StopIntent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or \
               is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return (
            handler_input.response_builder
            .speak(GOODBYE_MESSAGE)
            .set_should_end_session(True)
            .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for SessionEndedRequest."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        logger.info(
            "Session ended with reason: %s",
            handler_input.request_envelope.request.reason,
        )
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch-all exception handler for unexpected errors."""

    def can_handle(self, handler_input: HandlerInput, exception: Exception) -> bool:
        return True

    def handle(self, handler_input: HandlerInput, exception: Exception) -> Response:
        logger.error("Encountered exception: %s", exception, exc_info=True)
        speech = "Sorry, there was a problem. Please try again."
        return (
            handler_input.response_builder
            .speak(speech)
            .ask(speech)
            .response
        )


sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetNewFactIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
