from datetime import datetime
import base64
import hashlib
import upwork
import json
from time import sleep
import os
import webbrowser


def encode(ele):
    return base64.b64encode(hashlib.sha1(str(ele)).digest())


def get_client():
    cred_file = open('credentials.json', 'r')
    cred_json = json.load(cred_file)

    cred_file.close()
    public_key = cred_json['public_key']
    secret_key = cred_json['secret_key']

    upwork_client = upwork.Client(public_key, secret_key)

    auth_url = upwork_client.auth.get_authorize_url()
    # Opens a new tab in default web browser
    webbrowser.open(url=auth_url, autoraise=True, new=2)
    print 'Go to the mentioned URL : {}'.format(auth_url)
    verifier = raw_input('Enter Verifier: ')

    (token, token_secret) = upwork_client.auth.get_access_token(verifier)

    upwork_client = upwork.Client(
        public_key, secret_key,
        oauth_access_token=token,
        oauth_access_token_secret=token_secret)

    return upwork_client


if __name__ == '__main__':

    NOTIFICATION_FILE = 'notification.wav'

    client = get_client()

    all_ids = []

    queries = ['python', 'django', 'scraping']
    initial_jobs = []

    for q in queries:
        initial_jobs.extend(client.provider_v2.search_jobs({'q': q}))

    initial_ids = [job['id'] for job in initial_jobs]
    all_ids.extend(initial_ids)
    print "Lets start to search new tasks \n"

    while True:
        # Get all latest jobs
        print '\nGetting Jobs at {} ...\n'.format(
            datetime.now().strftime('%H:%M'))
        jobs = []
        for q in queries:
            jobs.extend(client.provider_v2.search_jobs({'q': q}))

        # Iterate every job
        for job in jobs:

            # Check if not viewed; new job
            if job['id'] not in all_ids:
                all_ids.append(job['id'])
                os.system('aplay {}'.format(NOTIFICATION_FILE))
                print 'Time : {}\nJob Title : {}\nURL : {}\n'.format(
                    datetime.now().strftime('%H:%M'),
                    job['title'], job['url']
                )
                webbrowser.open(url=job['url'], autoraise=True, new=2)
        # 1.5 minutes rest
        sleep(90)
