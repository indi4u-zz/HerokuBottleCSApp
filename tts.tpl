<!DOCTYPE html>
<html class="no-js">
<head>


    <!-- Meta info -->
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Computer Vision API</title>
    <meta content="" name="description">
    <meta name="author" content="">
    <meta name="format-detection" content="">

    <!-- Styles -->
    <link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600' rel='stylesheet' type='text/css'>
    <link href="static/css/main.css" rel="stylesheet" media="screen, print" type="text/css">
    <script src="static/js/modernizr-2.6.2.js"></script>
     <script src="static/js/jquery-1.11.0.min.js"></script>
    <script src="static/js/pyaari-main.1.0.js"></script>
    <script src="static/js/pyaari-menu.1.0.js"></script>
     <script src="  static/js/speechToText.js" type="text/javascript"></script>
    <script src="static/js/speech.1.0.0.js" type="text/javascript"></script>
   
</head>
<body>
<div id="container" style="left: 0px;">
<section id="content">    
<header>    
	<h1>		
        Text To Speech
	</h1>
</header>
 <div id="our-work">
  <form action="/tts" method="post" enctype="multipart/form-data">
  Enter text : <input type="text" name="t"/>
  <input type="submit" value="Generate Speech" />
</form>
  <h1>    
       Speech To Text
  </h1>
  <div>
 <table width="100%">
        <tr><td/><td><h1>Speech.JS</h1><h2>Microsoft Cognitive Services : Speech Recognition</h2></td></tr>
        <tr>
            <td align="right"/>          
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
  
  </div>
</div>
</section>
 </div>
</body>
</html>
