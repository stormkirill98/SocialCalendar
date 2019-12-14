import React from 'react';
import ReactDOM from 'react-dom';
import './css/Header.css';

class Header extends React.Component {
    render() {
        return (
            <>
            <header class="bg-success">
                <nav class="nav navbar-light">
                    <div class="button">
                        <input type="checkbox" id="hmt" class="hidden-menu-ticker" />>
                        <label class="btn-menu" for="hmt">
                            <span class="first"></span>
                            <span class="second"></span>
                            <span class="third"></span>
                        </label>
                        <ul class="hidden-menu">
                            <a class="hidden-menu-brand" href="Calendar.html">Social Calendar</a>
                            <li class="left-link"><a href="Calendar.html">Календарь</a></li>
                            <li class="left-link"><a href="friends.html">Друзья</a></li>
                            <li class="left-link"><a href="dialogues.html">Чаты</a></li>
                        </ul>
                    </div>
                    <a class="navbar-brand" href="Calendar.html">Social Calendar</a>
                    <li class="nav-item">
                        <a class="nav-link" href="Calendar.html">Календарь</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="friends.html">Друзья</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="dialogues.html">Чаты</a>
                    </li>
                </nav>
                <div class="auth-box">

                    <div class="auth-left">
                        <a href="Calendar.html" class="auth-img">
                            <img src="img/icon.JPG" width="50" height="50" alt="Аватарка" />>
                        </a>
                    </div>

                    <div class="auth-right">
                        <a class="auth-name" href="Calendar.html">Семён Петрович</a>
                        <div class="icons">
                            <a href="Options.html">
                                <img class="options" src="img/settings.png" alt="Настройки" />>
                            </a>
                            <a href="#">
                                <img class="notification" src="img/notifications.png" alt="Оповещения" />>
                            </a>
                        </div>
                    </div>
                </div>
            </header>
        </>
        );
    }
}

// ========================================

ReactDOM.render(
    <Main />,
    document.getElementById('root')
);
