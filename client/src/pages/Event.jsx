import React from "react";
import "../css/EventPage.css";
import Header from "../components/Header"
import EventMember from "../components/EventMember"
import EventAvatar from "../img/w512h5121371227427events.png"
import Button from "@material-ui/core/Button";
import AddIcon from '@material-ui/icons/Add';
import DeleteIcon from '@material-ui/icons/Delete';
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
                    console.log(data);
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
        this.deleteEvent = this.deleteEvent.bind(this);
    }


    inviteFriends() {
        fetch("/friends").then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    this.setState({
                        myFriends: data
                    });
                })
            } else {
                console.log(response.statusText);
            }
        });
        document.getElementById("invite-friends").style.display = 'flex';
    }

    deleteEvent() {
        fetch(`/event?id=${this.state.eventID}`, {
            method: 'DELETE'
        }).then((response) => {
            if (response.ok) { } else {
                if (response.status == 403) {
                    document.getElementById("confirm-delete").style.display = 'none';
                    document.getElementById("no-rules").style.display = 'flex';
                }
            }

        });
        document.getElementById("confirm-delete").style.display = 'none';

        // window.location.replace("https://127.0.0.1:5000/");
    }

    render() {
        // && this.state.members
        if (this.state.access) {
            let listFriends, listItems;

            if (this.state.members)
                listItems = this.state.members.map((val) => <EventMember key={val} id={val} />);

            if (this.state.myFriends)
                listFriends = this.state.myFriends.map((val) => <FriendForEvent key={val} friend={val} eventID={this.state.eventID} />);

            return (
                <div className="page-container-event">
                    <Header />
                    <main className="event">
                        <div className="event-box">
                            <div className="event-img-wrap event-page-wrap">
                                <img className="event-img" src={this.state.eventAvatarUrl} alt="Аватарка" />
                            </div>
                            <div className="event-title-descr event-page-wrap">
                                <div className="event-title-and-delete-btn">
                                    <h3 className="event-title">{this.state.eventTitle}</h3>
                                    <Button className="event-delete-btn"
                                        onClick={() => { document.getElementById("confirm-delete").style.display = 'flex' }}>
                                        <DeleteIcon />
                                    </Button>
                                </div>
                                <div className="event-short-descr">{this.state.eventShortDescr}</div>
                            </div>

                            {this.state.members ?
                                <>
                                    <div className="event-members event-page-wrap">
                                        <div className="event-members-top">
                                            <h4 className="members-title">Участники</h4>
                                            <Button color="primary" className="event-members-top-btn" variant="contained"
                                                onClick={this.inviteFriends}>
                                                <AddIcon fontSize="small" />
                                            </Button>
                                        </div>
                                        <div className="members-list">{listItems}</div>
                                    </div>
                                    <div id="event-body" className="event-body event-page-wrap" >
                                        <h4 className="event-body-title">Описание</h4>
                                        <div className="event-full-descr">{this.state.eventFullDesr}</div>
                                    </div>
                                </>
                                : <>
                                    <div id="event-body" className="event-body event-page-wrap" style={{ gridColumn: 'span 2' }}>
                                        <h4 className="event-body-title">Описание</h4>
                                        <div className="event-full-descr">{this.state.eventFullDesr}</div>
                                    </div>
                                </>
                            }

                        </div>
                        <div className="chat-main-box" style={{ display: 'none' }}>
                            <h4 className="event-chat">Чат</h4>
                            <div className="chat-box" />
                        </div>
                    </main>

                    <div id="invite-friends" className="invite-friends-shadow" style={{ display: 'none' }}>
                        <div className="invite-friends-window">
                            <h4 className="invite-friends-title">Пригласить друзей</h4>
                            <div className="friends-box">
                                {listFriends}
                            </div>
                            <div className="invite-friends-flex-row">
                                <Button color="primary" className="invite-friends-close-btn" variant="contained"
                                    onClick={() => { document.getElementById("invite-friends").style.display = 'none' }} >
                                    Закрыть
                                </Button>
                            </div>
                        </div>
                    </div>

                    <div id="confirm-delete" className="confirm-delete" style={{ display: 'none' }}>
                        <div className="confirm-delete-window">
                            <h3>Вы увернны, что хотите удалить данное событие безвозвратно?</h3>
                            <div className="confirm-delete-btns">
                                <Button color="primary" className="confirm-delete-yes" variant="contained"
                                    onClick={this.deleteEvent} >
                                    Да
                                </Button>
                                <Button color="primary" className="confirm-delete-no" variant="contained"
                                    onClick={() => { document.getElementById("confirm-delete").style.display = 'none' }} >
                                    Нет
                                </Button>
                            </div>
                        </div>
                    </div>

                    <div id="no-rules" className="confirm-delete" style={{ display: 'none' }}>
                        <div className="confirm-delete-window">
                            <h3>Вы увернны, что хотите удалить данное событие безвозвратно?</h3>
                            <div className="confirm-delete-btns">

                                <Button color="primary" className="confirm-delete-no" variant="contained"
                                    onClick={() => { document.getElementById("no-rules").style.display = 'none' }} >
                                    Нет
                                </Button>
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