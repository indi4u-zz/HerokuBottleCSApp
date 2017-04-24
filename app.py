from __future__ import print_function
import cv2
import sys
import wave
import os
from bottle import route, run,static_file,get,request
from bottle import template
import time 
import requests
import operator
import numpy as np
import matplotlib.pyplot as plt

_url = 'https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze?'
_key = 'ddd4c6b08a344f8494939e814aa45339'
_maxNumRetries = 10  
@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/images/work/")

@get("/tmp/upload/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="tmp/upload/")
    
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css/")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js/")

def processRequest( json, data, headers, params ):
    retries = 0
    result = None
    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )
        if response.status_code == 429: 

            print( "Message: %s" % ( response.json()['message'] ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['message'] ) )

        break        
    return result

# In[4]:

def renderResultOnImage( result, img ):
    """Display the obtained results onto the input image"""

    R = int(result['color']['accentColor'][:2],16)
    G = int(result['color']['accentColor'][2:4],16)
    B = int(result['color']['accentColor'][4:],16) ;
    cv2.rectangle( img,(0,0), (img.shape[1], img.shape[0]), color = (R,G,B), thickness = 25 )

    if 'description' in result:
        desc = result['description']['captions'][0]['text']
        cv2.putText( img, desc, (100,200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (73,25,180), 2 )
        print(desc)

@route('/edit')
def edit():
    info = []
    return template('simple.tpl', info)


@route('/vision')
def vision():
    return(template("vision.tpl"))
# In[7]:

@route('/vision', method = 'POST')
def upload():
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    save_path = "/tmp/upload"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    
    # Use the uploaded file for processing 
    # URL direction to image
    # urlImage = 'http://bboceansuites.com/wp-content/uploads/2015/05/sunset-beach-chairs-stock-footage.jpg'
    
    pathToFileInDisk = file_path
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()
    
    # Computer Vision parameters
    params = { 'visualFeatures' : 'Color,Categories,Faces,Description'} 

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = _key
    #headers['Content-Type'] = 'application/json' 
    headers['Content-Type'] = 'application/octet-stream'
    json = None
    #json = { 'url': urlImage } 
    #data = None
    result = processRequest( json, data, headers, params )
    if result is not None:
        # Load the original image, fetched from the URL
        data8uint = np.fromstring( data, np.uint8 ) # Convert string to an unsigned int array
        img = cv2.cvtColor( cv2.imdecode( data8uint, cv2.IMREAD_COLOR ), cv2.COLOR_BGR2RGB )
        renderResultOnImage( result, img )
        filename = os.path.join('tmp/upload/'+ name +"_out.jpg" )
        cv2.imwrite(filename,img)
        
        return template('visionWImg.tpl',image = filename)  



@route('/spellcheck')
def spellcheck():
   
    headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'baf9b2caff1849c08a4428bf637cbbb4',
    'Content-Type':  'application/x-www-form-urlencoded'
    }

    params = urllib.urlencode({
        # Request parameters
        'mode': 'proof',
        'mkt': 'en-us',
    })
    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/spellcheck/?%s" % params, "I hav no money", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
