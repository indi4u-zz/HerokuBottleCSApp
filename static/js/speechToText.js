// JavaScript source code

var client;
var request;
var _key = "756f8cbc3ad54b209076e4e41b51ecc2"

function useMic() {
    return true;
}

function getMode() {
    return Microsoft.CognitiveServices.SpeechRecognition.SpeechRecognitionMode.shortPhrase;
}

function getKey() {
    return _key;
}

function getLanguage() {
    return "en-us";
}

function clearText() {
    document.getElementById("output").value = "";
}

function setText(text) {
    document.getElementById("output").value += text;
}

function start() {
    var mode = getMode();

    clearText();

    if (useMic()) {
       
            client = Microsoft.CognitiveServices.SpeechRecognition.SpeechRecognitionServiceFactory.createMicrophoneClient(
                mode,
                getLanguage(),
                getKey());
        
        client.startMicAndRecognition();
        setTimeout(function () {
            client.endMicAndRecognition();
        }, 5000);
    } 

    client.onPartialResponseReceived = function (response) {
        setText(response);
    }

    client.onFinalResponseReceived = function (response) {
        setText(JSON.stringify(response));
    }

    client.onIntentReceived = function (response) {
        setText(response);
    };
}