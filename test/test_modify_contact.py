from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test test"))
    old_contacts = db.get_contact_list()
    contact1 = random.choice(old_contacts)
    contact = Contact(id=contact1.id, firstname="test1", lastname="test2")
    app.contact.modify_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)