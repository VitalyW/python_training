import re
import random


def test_random_contact(app):
    random_contact = random.randint(0, app.contact.count() - 1)
    contact_from_home_page = app.contact.get_contact_list()[random_contact]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_contact)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       filter(lambda x: x.strip('\n'),
                                              [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x.strip('\n'), [contact.email, contact.email2, contact.email3]))