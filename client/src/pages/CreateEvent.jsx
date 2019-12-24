import React from "react";
import "../css/EventPage.css";
import Header from "../components/Header"
import EventMember from "../components/EventMember"
import EventAvatar from "../img/w512h5121371227427events.png"

export default class CreateEvent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <div className="page-container-event">
                <Header />
                <main className="event">
                    <div className="event-box">
                        <div className="event-img-wrap event-page-wrap">
                            <img className="event-img" src="../img/asd.png" alt="Аватарка" />
                        </div>
                        <div className="event-title-descr event-page-wrap">
                            <h3 className="event-title"></h3>
                            <div className="event-short-descr"></div>
                        </div>
                        <div className="event-members event-page-wrap">
                            <h4 className="members-title">Участники</h4>
                            <div className="members-list"></div>
                        </div>
                        <div className="event-body event-page-wrap">
                            <h4 className="event-body-title">Описание</h4>
                            <div className="event-full-descr"></div>
                        </div>
                    </div>
                    <div className="chat-main-box">
                        <h4 className="event-chat">Чат</h4>
                        <div className="chat-box" />
                    </div>
                </main>
            </div>
        );


    }

}