# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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

                for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)