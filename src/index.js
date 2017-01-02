'use strict';

var Alexa = require('alexa-sdk');
var config = require('./config'); //store credentials - app id
var facts = require('./facts');   //array of facts
var fact_bank = facts.bank;

var APP_ID = config.APP_ID;
var SKILL_NAME = 'Comp Sci Interview Facts';

exports.handler = function(event, context, callback){
    var alexa = Alexa.handler(event,context);
    alexa.appId = APP_ID;
    alexa.registerHandlers(handlers);
    alexa.execute();
};

var handlers = {
    'LaunchRequest': function() {
	this.emit('GetFact');
    },
    'GetNewFactIntent': function() {
	this.emit('GetFact');
    },
    'GetFact': function() {
	var factIdx = Math.floor(Math.random() * fact_bank.length);
	var randFact = fact_bank[factIdx];

	var speechOutput = "Here's your fact: " + randFact;

	this.emit(':tellWithCard', speechOutput, SKILL_NAME, randFact);
    },
    'AMAZON.HelpIntent': function() {
	var speechOutput = "You can say tell me a comp sigh, or, you can say exit... What can I help you with?";
	var reprompt = "What can I help you with?";
	this.emit(':ask', speechOutput, reprompt);
    },
    'AMAZON.CancelIntent': function() {
	this.emit(':tell', 'Goodbye!');
    },
    'AMAZON.StopIntent': function(){
	this.emit(':tell', 'Goodbye!');
    }
};

