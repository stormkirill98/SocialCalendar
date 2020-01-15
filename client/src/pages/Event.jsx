import React from "react";
import "../css/EventPage.css";
import Header from "../components/Header"
import EventMember from "../components/EventMember"
import EventAvatar from "../img/w512h5121371227427events.png"
import Button from "@material-ui/core/Button";
import AddIcon from '@material-ui/icons/Add';
import FriendForEvent from "../components/FriendForEvent"

export default class Event extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            access: false,
            eventID: this.props.match.params.id,
            eventAvatarUrl: EventAvatar,
            eventTitle: "_eventTitle",
            eventFullDesr: "_eventFullDesr",
            eventShortDescr: "_eventShortDescr",
            isPrivate: false,
            datetime: new Date(),
            address: "_address",
            members: [],
            chatID: -1
        };

        fetch(`/event?id=${this.props.match.params.id}`).then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    console.log(data.member_id_list);
                    this.setState({
                        access: true,
                        eventAvatarUrl: data.icon,
                        eventTitle: data.name,
                        eventFullDesr: data.description,
                        eventShortDescr: data.short_descr, //i eto
                        isPrivate: data.is_private,
                        datetime: data.datetime,
                        address: data.address,
                        chatID: data.chat_id,
                        members: data.member_id_list,
                        myFriends: []
                        // members: typeof data.member_id_list === "object"
                        //     ? [data.member_id_list["$oid"]]
                        //     : data.member_id_list
                    });
                });


            } else {
                console.log(response.statusText);
                this.state.access = false;
            }
        });
        this.inviteFriends = this.inviteFriends.bind(this);
    }


    inviteFriends() {
        fetch("/friends").then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    console.log(data);
                    this.setState({
                        MyFriends: data
                    });
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    render() {
        if (this.state.access && this.state.members) {
            console.log(this.state.members);
            const listItems = this.state.members.map((val) => <EventMember key={val} id={val} />);
            let listFriends;
            if (this.state.myFriends)
                listFriends = this.state.myFriends.map((val) => <FriendForEvent key={val} friend={val} />);
            return (
                <div className="page-container-event">
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
                                <div className="event-members-top">
                                    <h4 className="members-title">Участники</h4>
                                    <Button color="primary" className="settings-btn" variant="contained"
                                        onClick={this.inviteFriends}>
                                        <AddIcon fontSize="small" />
                                    </Button>
                                </div>
                                <div className="members-list">{listItems}</div>
                            </div>
                            <div className="event-body event-page-wrap">
                                <h4 className="event-body-title">Описание</h4>
                                <div className="event-full-descr">{this.state.eventFullDesr}</div>
                            </div>
                        </div>
                        <div className="chat-main-box">
                            <h4 className="event-chat">Чат</h4>
                            <div className="chat-box" />
                        </div>
                    </main>

                    <div id="invite-friends" className="invite-friends-shadow">
                        <div className="invite-friends-window">
                            <h4 className="invite-friends-title">Пригласить друзей</h4>
                            <div className="friends-box">
                                {listFriends}
                            </div>
                        </div>
                    </div>
                </div>
            );
        } else {
            return (
                <div className="no-access">
                    Событие не существует<br />/недоступно для вас
                </div>
            );
        }

    }

}