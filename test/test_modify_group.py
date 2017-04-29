from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify this grop name"))
    app.group.modify_first_group(Group(name="modified name"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(header="modify this header"))
    app.group.modify_first_group(Group(footer="modified footer"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="modify this footer"))
    app.group.modify_first_group(Group(header="modify header"))