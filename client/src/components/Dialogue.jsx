import React from 'react';
import '../css/Dialogues.css';


export default class Dialogue extends React.Component {
    render() {
        return (
            <>
            <li class="dialogue">
                        
                <div class="wrap">
                    <img class="dialogue-img" src="../img/asd.png" alt="аватарка беседы"/>
                    <div class="dialogue-content">
                        <div>
                            Название беседы
                        </div>
                        <div class="wrap2">
                            <div class="wrap">
                                <img src="../img/asd.png" width="15px" height="15px" alt=""/>
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
            </li>
            </>
            );
        }
    }
