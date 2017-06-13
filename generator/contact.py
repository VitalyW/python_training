from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_number(minlen, maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(minlen, maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", address="", company="", home="", homephone="",
                    mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="", homepage="",
                    address2="", notes="")] + \
           [
               Contact(firstname=random_string("name_", 10), middlename=random_string("middlename_", 10),
                       lastname=random_string("lastname_", 10), nickname=random_string("nickname_", 10),
                        address=random_string("address_", 10), company=random_string("company_", 10),
                        home=random_string("home_", 10), homephone=random_phone_number(7, 10),
                        mobilephone=random_phone_number(7, 10), workphone=random_phone_number(7, 10),
                        secondaryphone=random_phone_number(7, 10), email=random_string("email_", 10),
                        email2=random_string("email2_", 10), email3=random_string("email3_", 10),
                        homepage=random_string("lastname_", 10), address2=random_string("address2_", 10),
                        notes=random_string("notes_", 10))

                for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))