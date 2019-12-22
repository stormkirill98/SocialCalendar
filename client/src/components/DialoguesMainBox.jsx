import React from 'react';
import '../css/Dialogues.css';
import Dialog from "../components/Dialogue";
import Message from "../components/Message";


export default class DialoguesMainBox extends React.Component {
    render() {
        return (
    <>
    <div class="dialogues-main-box">
        <div class="wrap3">
            <div class="dialogues-box">
                <h4 class="defoult-titel">Список диалогов</h4>
                <input placeholder="Поиск диалога..." type="text" class="text" name="dialogue-search"/>
                <ol class="dialogues-list">
                    <Dialog/>
                    <Dialog/>
                    <Dialog/>
                    <Dialog/>
                    <Dialog/>
                    <Dialog/>
                    <Dialog/>
                    <Dialog/>
                </ol>
            </div>
            <div class="selected-dialog-box">
                <h4 class="defoult-titel">Выбраный диалог (его название)</h4>
                <ol class="message-list">
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                    <Message/>
                </ol>
                <div class="msg-area">
                    <textarea class="text" placeholder="Введите сообщение..." ></textarea>
                    <button class="button" type="submit">Отправить</button>
                </div>
            </div>
        </div>
    </div>
    </>
            );
        }
    }