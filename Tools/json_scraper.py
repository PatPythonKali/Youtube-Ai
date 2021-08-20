# External Libraries
import time
start = time.time()
import pytchat
import json
import os

# Internal Libraries
from URL.francis_leo_marcos_updates import *

# Target Input
video_id = francis_leo_marcos_updates_url

# Create, Save and Overwrite Text File
with open(os.path.abspath(f"../Harvest/FLM/") +
          channel_name.replace(" ", "") + ".JSON", 'w', encoding='utf-8') as write_file:

    # Loop between Video ID's
    for v_id in video_id:
        chat = pytchat.create(video_id=v_id)

        # Watch Videos
        while chat.is_alive():

            # Load JSON
            for c in chat.get().items:

                # JSON Objects Initiation
                obj = c.json()
                obj2 = json.loads(obj)

                date_time = obj2['datetime']
                author_name = obj2['author']['name']

                # Output to File Regular
                json.dump(obj2, write_file, indent=4)

        print(f"{date_time} | {author_name}")

end = time.time()
print(f"Total Execution Time: {round(end - start, 2)}")