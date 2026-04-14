"""Tests for Comp Sci Interview Facts Alexa skill."""
from unittest.mock import MagicMock
import pytest
from ask_sdk_model import LaunchRequest, IntentRequest, Intent, Slot

import lambda_function as lf


def make_hi(request, session_attrs=None):
    hi = MagicMock()
    hi.request_envelope.request = request
    hi.attributes_manager.session_attributes = {} if session_attrs is None else dict(session_attrs)
    rb = MagicMock()
    for m in ("speak", "ask", "set_card", "set_should_end_session"):
        getattr(rb, m).return_value = rb
    hi.response_builder = rb
    return hi


def make_intent(name, slots=None):
    slot_objs = {k: Slot(name=k, value=str(v)) for k, v in (slots or {}).items()}
    return IntentRequest(intent=Intent(name=name, slots=slot_objs))


class TestLaunchRequest:
    def test_can_handle(self):
        assert lf.LaunchRequestHandler().can_handle(make_hi(LaunchRequest()))

    def test_speaks_comp_sci_fact(self):
        hi = make_hi(LaunchRequest())
        lf.LaunchRequestHandler().handle(hi)
        speech = hi.response_builder.speak.call_args[0][0]
        assert speech.startswith("Here's your comp sci fact:")

    def test_ends_session(self):
        hi = make_hi(LaunchRequest())
        lf.LaunchRequestHandler().handle(hi)
        hi.response_builder.set_should_end_session.assert_called_once_with(True)


class TestGetNewFactIntent:
    def test_can_handle(self):
        assert lf.GetNewFactIntentHandler().can_handle(make_hi(make_intent("GetNewFactIntent")))

    def test_cannot_handle_wrong_intent(self):
        assert not lf.GetNewFactIntentHandler().can_handle(make_hi(make_intent("OtherIntent")))

    def test_speaks_fact_with_prefix(self):
        hi = make_hi(make_intent("GetNewFactIntent"))
        lf.GetNewFactIntentHandler().handle(hi)
        speech = hi.response_builder.speak.call_args[0][0]
        assert speech.startswith("Here's your comp sci fact:")

    def test_ends_session(self):
        hi = make_hi(make_intent("GetNewFactIntent"))
        lf.GetNewFactIntentHandler().handle(hi)
        hi.response_builder.set_should_end_session.assert_called_once_with(True)


class TestHelpIntent:
    def test_can_handle(self):
        assert lf.HelpIntentHandler().can_handle(make_hi(make_intent("AMAZON.HelpIntent")))

    def test_keeps_session_open(self):
        hi = make_hi(make_intent("AMAZON.HelpIntent"))
        lf.HelpIntentHandler().handle(hi)
        hi.response_builder.ask.assert_called_once()
        hi.response_builder.set_should_end_session.assert_not_called()


class TestCancelStopIntent:
    @pytest.mark.parametrize("name", ["AMAZON.CancelIntent", "AMAZON.StopIntent"])
    def test_can_handle(self, name):
        assert lf.CancelOrStopIntentHandler().can_handle(make_hi(make_intent(name)))

    def test_says_goodbye(self):
        hi = make_hi(make_intent("AMAZON.StopIntent"))
        lf.CancelOrStopIntentHandler().handle(hi)
        assert "Goodbye" in hi.response_builder.speak.call_args[0][0]

    def test_ends_session(self):
        hi = make_hi(make_intent("AMAZON.CancelIntent"))
        lf.CancelOrStopIntentHandler().handle(hi)
        hi.response_builder.set_should_end_session.assert_called_once_with(True)


class TestExceptionHandler:
    def test_can_handle_any_exception(self):
        hi = make_hi(LaunchRequest())
        assert lf.CatchAllExceptionHandler().can_handle(hi, RuntimeError("boom"))

    def test_returns_error_speech(self):
        hi = make_hi(LaunchRequest())
        lf.CatchAllExceptionHandler().handle(hi, RuntimeError("boom"))
        speech = hi.response_builder.speak.call_args[0][0]
        assert "Sorry" in speech


class TestFactBank:
    def test_has_facts(self):
        assert len(lf.FACTS) >= 10

    def test_fact_includes_big_oh(self):
        assert any("big Oh" in f or "constant time" in f for f in lf.FACTS)

    def test_get_random_fact_prefix(self):
        assert lf.get_random_fact().startswith("Here's your comp sci fact:")
