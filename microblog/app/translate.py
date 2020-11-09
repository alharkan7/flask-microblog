import json
import requests
from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))

# Microsoft Translator has changed to Cognitive Service, and the syntaxes are different.
# Here's the updated example of request to call the Translator using the global translator resource
# Pass secret key using headers
# curl -X POST "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=es" \
#      -H "Ocp-Apim-Subscription-Key:<your-key>" \
#      -H "Content-Type: application/json" \
#      -d "[{'Text':'Hello, what is your name?'}]"