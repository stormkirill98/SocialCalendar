import React from "react";
//import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import "../css/dialogues.css";
import Header from "../components/Header";


export default class dialogues extends React.Component {
    render() {
        return (
            <>
            <Header/>
            <div class="dialogues-main-box">
        <div class="wrap3">
            <div class="dialogues-box">
                <h4 class="title">Список диалогов</h4>
                <textarea class="text" placeholder="Поиск диалога..." rows="1"></textarea>
                <input placeholder="Поиск диалога..." type="text" name="dialogue-search"/>
                <ol class="dialogues-list">
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="dialogue">
                        <a class="a" href="#">
                            <div class="wrap">
                                <img class="dialogue-img" src="img/asd.png" alt="аватарка беседы"/>
                                <div class="dialogue-content">
                                    <div>
                                        Название беседы
                                    </div>
                                    <div class="wrap2">
                                        <div class="wrap">
                                            <img src="img/asd.png" width="15px" height="15px" alt=""/>
                                            <div>
                                                Последнее сообщение
                                            </div>
                                        </div>
                                        <div class="time">
                                            12:20
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </a>
                    </li>
                </ol>
            </div>
            <div class="selected-dialog-box">
                <h4 class="title">Выбраный диалог (его название)</h4>
                <ol class="message-list">
                    <li class="wrap2">
                        <div class="message">username1: message</div>
                        <div class="time">10:35</div>
                    </li>
                    <li class="wrap2">
                        <div class="message">username2: message</div>
                        <div class="time">10:36</div>
                    </li>
                    <li class="wrap2">
                        <div class="message">username1: message</div>
                        <div class="time">10:40</div>
                    </li>
                </ol>
                <div class="msg-area">
                    <textarea class="text" placeholder="Введите сообщение..." rows="1"></textarea>
                    <button class="button" type="submit">Отправить</button>
                </div>
            </div>
        </div>
    </div>
    </>
        );
    }
}