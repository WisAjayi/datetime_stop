import datetime

TIME = datetime.datetime.now()
print(TIME.hour)

RUN = True

while RUN:

    NEW_TIME = datetime.datetime.now()

    print(NEW_TIME.hour)

    if NEW_TIME.hour - TIME.hour == 1 and NEW_TIME.minute - TIME.minute == 0:
        RUN = False