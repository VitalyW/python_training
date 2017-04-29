from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Test contact Modify", middlename="A", lastname="Smith",
                                             nickname="Duck", address="Washington", company="Google", home="New York",
                                             mobile="913454321", email="none@a.com", homepage="www.no.no",
                                             address2="New York City", notes="Test mptes"))


def test_modify_first_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="This is the only field modified", nickname="Wwdsdasdasd"))