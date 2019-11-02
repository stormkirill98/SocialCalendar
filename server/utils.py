from server.datastore import chat_dao, user_dao
from server.entities.chats.dialog import Dialog


def create_dialog(user_id_1, user_id_2):
    dialog = Dialog(user_id_1, user_id_2)
    dialog = chat_dao.save_dialog(dialog)

    user_dao.add_chat(user_id_1, dialog.id)
    user_dao.add_chat(user_id_2, dialog.id)

    return dialog



