from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Last name to create if there are no contacts on the page"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Test contact Modify", middlename="A", lastname="Smith", nickname="Duck",
                        address="Washington", company="Google", home="New York", mobile="913454321", email="none@a.com",
                            homepage="www.no.no", address2="New York City", notes="Test notes")
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_first_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Nickname to create if there are no contacts on the page"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(firstname="This is the only field modified", nickname="Wwdsdasdasd"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)