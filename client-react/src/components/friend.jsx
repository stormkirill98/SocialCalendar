import React from 'react';
import '../css/Friends.css';


export default class Friend extends React.Component {
    render() {
        return (
            <>
                <li class="friend">
                    <div class="wrap">
                    <img class="friend-avatar" src="img/asd.png" alt="аватарка друга"/>
                        <a href="#">Катя</a>
                    </div>
                    <div class="wrap">
                        <button class="button1">Перейти к чату</button>
                        <button class="button1">Добавить/Удалить</button>
                    </div>
                </li>
            </>
        );
    }
}