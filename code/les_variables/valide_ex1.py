import io
import sys
import re


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def test_Verif():
    print("test_verif")
    try:
        sys.stdout=io.StringIO()
        rep = sys.stdout.getvalue().split("\n")
        print("inside the try")
        for i,reponse in enumerate(rep):
            print(str(i) + " : " + str(reponse))
            if reponse != 22:
                print("TECHIO> success false")
                send_msg("Echecs","Ce n'est pas la sortie attendu")

        print(str(rep))


    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Echecs","recommence")

if __name__ == "__main__":
    print("main")
    test_Verif()
