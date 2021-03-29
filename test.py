# millis=input("Enter time in milliseconds ")
# millis = int(millis)
# seconds=(millis/1000)%60
# seconds = int(seconds)
# minutes=(millis/(1000*60))%60
# minutes = int(minutes)
# hours=(millis/(1000*60*60))%24
#
# print ("%d:%d:%d" % (hours, minutes, seconds))


def convertMillis(millis):
    seconds = (millis / 1000) % 60
    minutes = (millis / (1000 * 60)) % 60
    hours = (millis / (1000 * 60 * 60)) % 24
    return seconds, minutes, hours


def main():
    millis = input("Enter time in milliseconds ")
    con_sec, con_min, con_hour = convertMillis(int(millis))
    print("{0}:{1}:{2}".format(con_hour, con_min, con_sec))


main()