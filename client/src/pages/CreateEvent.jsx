import React from "react";
import "../css/CreateEvent.css";
import Header from "../components/Header";
// import IconsGrid from "../components/IconsGrid";
import { Redirect } from "react-router-dom";

export default class CreateEvent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            type: "group",
            event_name: "Event_name",
            is_private: false,
            datetime: new Date(this.props.match.params.year, this.props.match.params.month,
                this.props.match.params.day, 24, 0, 30, 500),//час мин сек мс
            address: "Советский Союз",
            description: "Desciption",
        };
        this.privateChange = this.privateChange.bind(this);
    }

    sendNewEvent() {
        console.log("зашел в sendNewEvent()");
        var bodyJSON = JSON.stringify({
            "type": this.state.type,
            "name": this.state.event_name,
            "is_private": this.state.is_private,
            "datetime": this.state.datetime,
            "address": this.state.address,
            "description": this.state.description,
            "icon": this.state.icon
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
                    return <Redirect to='/Calendar' />
                })
            } else {
                console.log(response.statusText);

            }
        });
    }

    typeChange(event){
        console.log(2233);
        this.setState({type: event});
        console.log(this.state.type);
    }

    privateChange(event) {
        console.log(123);
        this.setState({is_private: event});
        console.log(this.state.is_private);
    }

    // onAvatarkaClicked(){
    //     return(
    //         <div className="icons-grid">
    //             <img src="../../../public/event_icons/bell.svg" alt=""/>
    //             <img src="../../../public/event_icons/burger.svg" alt=""/>
    //             <img src="../../../public/event_icons/cart.svg" alt=""/>
    //             <img src="../../../public/event_icons/coctail.svg" alt=""/>
    //             <img src="../../../public/event_icons/coffee.svg" alt=""/>
    //             <img src="../../../public/event_icons/confirm.svg" alt=""/>
    //             <img src="../../../public/event_icons/delete.svg" alt=""/>
    //             <img src="../../../public/event_icons/doughnut.svg" alt=""/>
    //             <img src="../../../public/event_icons/exit.svg" alt=""/>
    //             <img src="../../../public/event_icons/gamepad.svg" alt=""/>
    //             <img src="../../../public/event_icons/glasses.svg" alt=""/>
    //             <img src="../../../public/event_icons/heart.svg" alt=""/>
    //             <img src="../../../public/event_icons/music.svg" alt=""/>
    //             <img src="../../../public/event_icons/pin.svg" alt=""/>
    //             <img src="../../../public/event_icons/pizza.svg" alt=""/>
    //             <img src="../../../public/event_icons/plus.svg" alt=""/>
    //         </div>
    //     )
    // }

    render() {
        return (
            <div className="page-container-event">
                <Header />
                <main className="create-event">
                    <div className="create-event-grid">
                        {/* <IconsGrid updateData={this.selectAvatar}></IconsGrid> */}

                        <h3 className="create-event-title">Название</h3>
                        <input className="create-event-title-input create-event-input" type="text" />

                        <h3 className="create-event-type">Тип события</h3>
                        <div className="radio-field">
                            <input type="radio" id="group"
                                name="event-type" value="group" onChange={() => this.typeChange("group")} checked/>
                            <label for="private-yes">Групповой</label>

                            <input type="radio" id="single"
                                name="event-type" value="single" onChange={() => this.typeChange("single")}/>
                            <label for="private-no">Только для меня</label>
                        </div>

                        <h3 className="create-event-isPrivate">Приватный</h3>
                        <div className="radio-field">
                            <input type="radio" id="private-yes"
                                name="private" value={true} onChange={() => this.privateChange(true)} checked/>
                            <label for="private-yes">Да</label>

                            <input type="radio" id="private-no"
                                name="private" value={false} onChange={() => this.privateChange(false)}/>
                            <label for="private-no">Нет</label>
                        </div>

                        <h3 className="create-event-Address">Адрес</h3>
                        <input className="create-event-Address-input create-event-input" type="text" />

                        <h3 className="create-event-descr">Описание</h3>
                        <textarea className="create-event-descr-input create-event-input" type="text" />
                    </div>
                    <div className="create-button" onClick={this.sendNewEvent}>
                        Создать
                    </div>
                </main>
            </div>
        );


    }

}