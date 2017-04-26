# -*- coding: utf-8 -*-
import pytest
from python_training.fixture.application import Application
from python_training.model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Donald", middlename="J", lastname="Trump", nickname="Trumpy",
                               address="WhiteHouse", company="Gov", home="D.C.", mobile="123856756",
                               email="trump@gov.gov", homepage="www.gov.com", address2="New York", notes="Lalalala"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               address="", company="", home="", mobile="",
                               email="", homepage="", address2="", notes=""))
    app.session.logout()