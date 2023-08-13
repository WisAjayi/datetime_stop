import datetime

TIME = datetime.datetime.now()
print(TIME.minute)

RUN = True

while RUN:

    NEW_TIME = datetime.datetime.now()

    print(NEW_TIME.minute)

    if NEW_TIME.minute - TIME.minute == 1:
        RUN = False