import React from 'react';
import '../css/Header.css';

export default class Header extends React.Component {
    render() {
        return (
            <>
                <header className="bg-success">
                    <nav className="nav navbar-light">
                        <div className="button">
                            <input type="checkbox" id="hmt" className="hidden-menu-ticker" />
                            <label className="btn-menu" htmlFor="hmt">
                                <span className="first"></span>
                                <span className="second"></span>
                                <span className="third"></span>
                            </label>
                            <ul className="hidden-menu">
                                <a className="hidden-menu-brand" href="/Calendar">Social Calendar</a>
                                <li className="left-link"><a href="/Calendar">Календарь</a></li>
                                <li className="left-link"><a href="friends">Друзья</a></li>
                                <li className="left-link"><a href="dialogues">Чаты</a></li>
                            </ul>
                        </div>
                        <a className="navbar-brand" href="Calendar">Social Calendar</a>
                        <li className="nav-item">
                            <a className="nav-link" href="Calendar">Календарь</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="friends">Друзья</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="dialogues">Чаты</a>
                        </li>
                    </nav>
                    <div className="auth-box">

                        <div className="auth-left">
                            <a href="Calendar" className="auth-img">
                                <img src="img/icon.JPG" width="50" height="50" alt="Аватарка" />
                            </a>
                        </div>

                        <div className="auth-right">
                            <a className="auth-name" href="Calendar">Семён Петрович</a>
                            <div className="icons">
                                <a href="Options">
                                    <img className="options" src="img/settings.png" alt="Настройки" />
                                </a>
                                <a href="Notifications">
                                    <img className="notification" src="img/notifications.png" alt="Оповещения" />
                                </a>
                            </div>
                        </div>
                    </div>
                </header>
            </>
        );
    }
}