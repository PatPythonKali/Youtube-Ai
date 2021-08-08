import datetime

string_date = "2021-07-09 23:35:22"
format = "%Y-%m-%d %H:%M:%S"

datetime_object = datetime.datetime.strptime(string_date, format)

print("Datetime: ", datetime_object)
print(type(datetime_object))