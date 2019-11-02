from server.datastore import chat_dao, user_dao
from server.entities.chats.dialog import Dialog


def create_dialog(user_id_1, user_id_2):
    """Create and save dialog to mongoDB,
       then add this dialog to users on mongoDB"""

    # TODO check that users id is validate and users already is created

    # create and save dialog
    dialog = Dialog(user_id_1, user_id_2)
    dialog = chat_dao.save_dialog(dialog)

    # add chat to users
    user_dao.add_chat(user_id_1, dialog.id)
    user_dao.add_chat(user_id_2, dialog.id)

    return dialog


def delete_dialog(dialog_id):
    """Delete dialog, remove it in users, remove all msg's in it"""

    # get dialog by id
    dialog = chat_dao.get_dialog(dialog_id)

    # TODO check that dialog is not null
    # delete dialog from user
    user_dao.delete_chat(dialog.user_id_1, dialog_id)
    user_dao.delete_chat(dialog.user_id_2, dialog_id)

    # delete msg's
    for msg_id in dialog.msg_id_list:
        chat_dao.delete_msg(msg_id)

    # delete dialog
    chat_dao.delete_dialog(dialog_id)
