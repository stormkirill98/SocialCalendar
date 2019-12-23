import React from "react";
import "../css/EventPage.css";
import Header from "../components/Header"
import EventMember from "../components/EventMember"
import EventAvatar from "../img/w512h5121371227427events.png"

export default class Event extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            eventID: this.props.match.params.id,
            eventAvatarUrl: EventAvatar,
            eventTitle: "_eventTitle",
            eventFullDesr: "_eventFullDesr",
            eventShortDescr: "_eventShortDescr",
            isPrivate: false,
            datetime: new Date(),
            address: "_address",
            members: [101332313, 
                      10123789813, 
                      101672313],
            chatID: -1
        };
        this.getEventData();
    }

    async getEventData() {
        console.log("id=" + this.state.eventID);
        // ${this.props.match.params.id}
        fetch("https://social-calendar-tensor.herokuapp.com/event?id=5dd15fb805b75899b9af57b1").then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    console.log(data);
                    this.setState({
                        eventAvatarUrl: data.event_img, //potom pereimenovat
                        eventTitle: data.name,
                        eventFullDesr: data.description,
                        eventShortDescr: data.short_descr, //i eto
                        isPrivate: data.is_private,
                        datetime: data.datetime,
                        address: data.address,
                        chatID: data.chat_id,
                        members: data.member_id_list
                    });
                })
            } else {
                console.log(response.statusText);
            }
        });
        // const responce = await fetch(
        //     `social-calendar-tensor.herokuapp.com/event?id=${this.props.match.params.id}`
        // );
        // const jsonData = await responce.json();
        // console.log(jsonData);
        // return 1;
    }

    

    render() {
        const listItems = this.state.members.map(
            (val) => <EventMember key={val} id={val}/>);
            
        return (
            <>
                <Header />
                <main className="event">
                    <div className="event-box">
                        <div className="event-img-wrap event-page-wrap">
                            <img className="event-img" src={this.state.eventAvatarUrl} alt="Аватарка" />
                        </div>
                        <div className="event-title-descr event-page-wrap">
                            <h3 className="event-title">{this.state.eventTitle}</h3>
                            <div className="event-short-descr">{this.state.eventShortDescr}</div>
                        </div>
                        <div className="event-members event-page-wrap">
                            <h4 className="members-title">Участники</h4>
                            <div className="members-list">{listItems}</div>
                        </div>
                        <div className="event-body event-page-wrap">
                            <h4 className="event-body-title">Описание</h4>
                            <div className="event-full-descr">{this.state.eventFullDesr}</div>
                        </div>
                    </div>
                    <div className="chat-main-box">
                        <h4 className="event-chat">Чат</h4>
                        <div className="chat-box"></div>
                    </div>
                </main>
            </>
        );
    }

}