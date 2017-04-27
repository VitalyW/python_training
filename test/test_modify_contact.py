from python_training.model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Test contact Modify", middlename="A", lastname="Smith",
                                             nickname="Duck", address="Washington", company="Google", home="New York",
                                             mobile="913454321", email="none@a.com", homepage="www.no.no",
                                             address2="New York City", notes="Test mptes"))
    app.session.logout()