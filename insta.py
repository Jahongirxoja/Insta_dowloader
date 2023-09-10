import requests
import json





def instadonwload(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "f4060406f2msh3690fe986052293p143d5bjsnf8ddaa07eeab",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    # print(rest)

    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
        if rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Story-Video':
            dict['type'] = 'story-Video'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'

# print(instadonwload('www.instagram.com/stories/uniquecarsuz/3186561888060714193/'))