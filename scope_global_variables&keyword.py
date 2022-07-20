


def saimon():
    x = 20
    def nabin():
        global x
        x = 40
    print("Call Saimon before nabin",x)
    nabin()
    print("Call nabin before saimon",x)
saimon()