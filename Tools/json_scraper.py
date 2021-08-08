# External Libraries
import pytchat
import json

# Internal Libraries
from URL.francis_leo_marcos_updates import channel_name, francis_leo_marcos_updates_url

# Target Input
video_id = francis_leo_marcos_updates_url

# Create, Save and Overwrite Text File
with open('/home/ubuntu/PycharmProjects/Youtube-Ai/Harvest/FLM/' +
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


                # Objects
                yt_author_name = obj2['author']['name']
                yt_author_id = obj2['author']['channelId']
                yt_message = obj2['message']
                yt_datetime = obj2['datetime']
                yt_elapsedTime = obj2['elapsedTime']

                print(F"{yt_datetime} | {yt_elapsedTime}")
                print(F"{yt_author_name}: {yt_message} \n")

                # Output to File Regular
                json.dump(obj2, write_file, indent=4)