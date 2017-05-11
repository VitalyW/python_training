from model.contact import Contact

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

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath('//*[@title="Edit"]')[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
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
        self.change_contact_value("mobile", contact.mobile)
        self.change_contact_value("email2", contact.email)
        self.change_contact_value("homepage", contact.homepage)
        self.change_contact_value("address2", contact.address2)
        self.change_contact_value("notes", contact.notes)

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("[name='update']").click()
        self.app.return_to_home_page()
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
            for element in wd.find_elements_by_css_selector("[name='selected[]']"):
                text = element.text
                id = element.get_attribute("value")
                self.contact_cache.append(Contact(firstname=text, lastname=text, id=id))
        return list(self.contact_cache)