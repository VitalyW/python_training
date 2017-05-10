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

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to_alert().accept()

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

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("[name='update']").click()
        self.app.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_css_selector("[name='selected[]']"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("[name='selected[]']"):
            text = element.text
            id = element.get_attribute("value")
            contacts.append(Contact(firstname=text, id=id))
        return contacts