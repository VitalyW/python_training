from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector("[name='submit']").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("[name='selected[]']")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//*[@title='Edit']")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("middlename", contact.middlename)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("nickname", contact.nickname)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("home", contact.home)
        self.change_contact_value("home", contact.homephone)
        self.change_contact_value("mobile", contact.mobilephone)
        self.change_contact_value("work", contact.workphone)
        self.change_contact_value("phone2", contact.secondaryphone)
        self.change_contact_value("email", contact.email)
        self.change_contact_value("email2", contact.email2)
        self.change_contact_value("email3", contact.email3)
        self.change_contact_value("homepage", contact.homepage)
        self.change_contact_value("address2", contact.address2)
        self.change_contact_value("notes", contact.notes)

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("[name='update']").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id='%s'']" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_css_selector("[name='selected[]']"))


    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            rows = wd.find_elements_by_css_selector("[name='entry']")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails,
                                                  address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_css_selector("[name='entry']")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_css_selector("[name='entry']")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_css_selector("[name='firstname']").get_attribute("value")
        lastname = wd.find_element_by_css_selector("[name='lastname']").get_attribute("value")
        id = wd.find_element_by_css_selector("[name='id']").get_attribute("value")
        homephone = wd.find_element_by_css_selector("[name='home']").get_attribute("value")
        mobilephone = wd.find_element_by_css_selector("[name='mobile']").get_attribute("value")
        workphone = wd.find_element_by_css_selector("[name='work']").get_attribute("value")
        secondaryphone = wd.find_element_by_css_selector("[name='phone2']").get_attribute("value")
        email = wd.find_element_by_css_selector("[name='email']").get_attribute("value")
        email2 = wd.find_element_by_css_selector("[name='email2']").get_attribute("value")
        email3 = wd.find_element_by_css_selector("[name='email3']").get_attribute("value")
        address = wd.find_element_by_css_selector("[name='address']").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                        workphone=workphone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3,
                            address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)