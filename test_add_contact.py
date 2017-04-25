# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Donald", middlename="J", lastname="Trump", nickname="Trumpy",
                        address="WhiteHouse", company="Gov", home="D.C.", mobile="123856756",
                            email="trump@gov.gov", homepage="www.gov.com", address2="New York", notes="Lalalala"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                                                address="", company="", home="", mobile="",
                                                    email="", homepage="", address2="", notes=""))
    app.logout()