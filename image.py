#!/usr/bin/python3

# Initialisation on web server
import cgitb
cgitb.enable()
print("Content-type: text/html\n\n")
import sys
sys.path.append('/mnt/web305/c1/31/53991431/htdocs/.local/lib/python3.8/site-packages')


import json
from flask import Flask, request, send_file
import requests

def get_bing_image(query):
    
    response = requests.get("https://www.bing.com/images/?q=" + query + "&tbm=isch", headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    try:

        image_results = soup.findAll("img", {"class":"mimg"})

        for image in image_results:

            image_url = image.attrs.get('data-src')

            if image_url:
                
                if "https://" in image_url:
                
                    full_url = image_url.split("?")[0]

                    break

    except:

        full_url = "default.png"

    return full_url




# IMAGE SEARCH
@app.route('/image', methods=['GET'])
def imagesearch():
    
    query = request.args.get("query")

    query = query.replace("Content-type: text/html")

    image = get_bing_image(query)

    return send_file(filename, mimetype='image/jpg')



