import React from "react";
import "../css/CreateEvent.css";
import Header from "../components/Header"
import EventMember from "../components/EventMember"
import EventAvatar from "../img/w512h5121371227427events.png"

export default class CreateEvent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            type: "group",
            умуте_name: "Event_name",
            is_private: "false",
            datetime: new Date(this.props.match.params.year,this.props.match.params.month,
                this.props.match.params.day,24,0,30,500),//час мин сек мс
            address: "Советский Союз",
            description: "Desciption"
        };
    }
    sendNewEvent() {
        var bodyJSON = JSON.stringify({
            "type": this.state.type,
            "name": this.state.event_name,
            "is_private": "true",
            "datetime": new Date(this.props.match.params.year,this.props.match.params.month,
                this.props.match.params.day,24,00,30,500),//час мин сек мс
            "address": "address",
            "description": "desciption fasadsa"
        })
        fetch("/event", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: bodyJSON
        }).then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    console.log(data);
                })
            } else {
                console.log(response.statusText);
            }
        });
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