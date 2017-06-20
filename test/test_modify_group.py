from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="modify this group name"))
    old_groups = db.get_group_list()
    group1 = random.choice(old_groups)
    group = Group(id=group1.id, name="modified name")
    app.group.modify_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group1)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="modify this header"))
#     old_groups = app.group.get_group_list()
#     group = Group(footer="modified footer")
#     group.id = old_groups[0].id
#     app.group.modify_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#
# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(footer="modify this footer"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="modify header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)