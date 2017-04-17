<!-- 
Microsoft Speech SDK
====================


FEATURES
--------
* Short-form recognition.
* Long-form dictation.
* Recognition with intent.
* Integrated microphone support.
* External audio support.
-------
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <script src="  speecchToText.js" type="text/javascript"></script>
    <script src="speech.1.0.0.js" type="text/javascript"></script>
   
</head>
<body style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
    <table width="100%">
        <tr><td/><td><h1>Speech.JS</h1><h2>Microsoft Cognitive Services</h2></td></tr>
        <tr>
            <td align="right"/>
            <td><input id="useMic" type="checkbox">Use Microphone</td>
        </tr>
        <tr>
            <td align="right"><A href="https://www.microsoft.com/cognitive-services/en-us/sign-up" target="_blank">Subscription</A>:</td>
            <td><input id="key" type="text" size="40"></td>
        </tr>
        
        <tr>
            <td />
            <td><button onclick="start()">Start</button></td>
        </tr>
        <tr><td/>
            <td>
                <textarea id="output" style='width:400px;height:200px'></textarea>
            </td>
        </tr>
        <tr><td />
            <td><a href="docs/speech.1.0.0.js/index.html" target="_blank">Speech.JS Documentation</a></td>
        </tr>
    </table>
</body>
</html>        
