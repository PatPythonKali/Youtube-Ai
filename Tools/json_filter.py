import json
import datetime

string_date = "2021-07-09 23:35:22"
format = "%Y-%m-%d %H:%M:%S"

# with open('/home/ubuntu/Documents/youtube_ai_json/master.json') as json_file:
with open('/home/ubuntu/Dropbox/Python Projects/JSON/JSON Backup/master-aug-3.json') as json_file:
    obj = json_file.read()
    obj2 = json.loads(obj)

    # yt_verified = obj2['isVerified']
    for x in obj2:
        yt_author_name = x['author']['name']
        yt_message = x['message']

        yt_datetime = x['datetime']
        string_date = yt_datetime
        format = "%Y-%m-%d %H:%M:%S"
        datetime_object = datetime.datetime.strptime(string_date, format)

        yt_elapsed_time = x['elapsedTime']
        yt_channel_owner = x['author']['channelOwner']
        yt_channel_url = x['author']['channelUrl']

        def word_search(word):
            if word in yt_message:
                print(f"{yt_channel_owner} | {datetime_object}")
                print(f"{yt_author_name}: {yt_message} \n")

        def word_search_author(word):
            if word in yt_message:
                print(f"{yt_author_name}")

        def author_search(author):
            if author == yt_author_name:
                print(f"{yt_channel_owner} | {yt_channel_url} | {datetime_object}")
                print(f"{yt_author_name}: {yt_message} \n")

        def url_search(url):

            if url == yt_author_name:
                print(yt_channel_url)

        def word_count_author(author):
            with open('Messages/' + author.replace(" ", "") + ".txt", 'a', encoding='utf-8') as write_file:

                if author == yt_author_name:
                    write_file.write(f"{yt_message} \n")
                    print(f"{yt_message} \n")

        def author_message(author):
            if author == yt_author_name:
                print(f"{yt_author_name}: {yt_message} \n")

        # Author: Message
        # author_message("Dark Cupcake Chocolate")

        # word_search_author("ka….")
        author_search("Chismosang Dilis")

        # word_search("credibility")
        # url_search("-xx x")




        # word_count_author("The real I am Cehl")
