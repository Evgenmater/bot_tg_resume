import os
import time

import requests

from core.config import settings
from core.constants import CREATE_URL, QUERY_URL, RESULT_TYPE


async def speech_to_text(file_name):
    headers = {'keyId': settings.key_id, 'keySecret': settings.key_secret}
    create_url = CREATE_URL
    query_url = QUERY_URL

    with open(file_name, 'rb') as fl:
        files = {'file': fl}
        response = requests.post(create_url, headers=headers, files=files,)

        if response.status_code == 200:
            create_result = response.json()
            query_url += create_result['taskId'] + RESULT_TYPE

            while True:
                response = requests.get(query_url, headers=headers,)

                if response.status_code == 200:
                    query_result = response.json()

                    if query_result['code'] == 11000:

                        if query_result['result']:
                            result = query_result[
                                'result'
                            ].replace('\n\n', ' ')
                            yield result
                        break

                    elif query_result['code'] == 11001:
                        time.sleep(3)
                        continue

                    else:
                        break

                else:
                    break
        fl.close()
        os.remove(file_name)
