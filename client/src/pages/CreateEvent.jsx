import React from "react";
import "../css/CreateEvent.css";
import Header from "../components/Header";
// import IconsGrid from "../components/IconsGrid";
import { Redirect } from "react-router-dom";
import { RadioGroup, RadioButton, ReversedRadioButton } from 'react-radio-buttons';

export default class CreateEvent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            type: "group",
            event_name: "Event_name",
            is_private: false,
            datetime: "17.1.2020 15:30",
            // new Date(this.props.match.params.year, this.props.match.params.month,
            //     this.props.match.params.day, 24, 0, 30, 500),//час мин сек мс
            address: "Советский Союз",
            description: "Desciption",
            icon: "/load_icon/bell.svg"
        };
        this.privateChange = this.privateChange.bind(this);
        this.typeChange = this.typeChange.bind(this);
        this.sendNewEvent = this.sendNewEvent.bind(this);
        this.nameChange = this.nameChange.bind(this);
        this.addressChange = this.addressChange.bind(this);
        this.descriptionChange = this.descriptionChange.bind(this);
    }

    sendNewEvent() {
        console.log("зашел в sendNewEvent()");
        console.log(this.state);
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

    typeChange(event) {
        this.setState({ type: event });
    }
    privateChange(event) {
        this.setState({ is_private: event });
    }
    nameChange(event){
        this.setState({ event_name: event.target.value });
    }
    addressChange(event){
        this.setState({ address: event.target.value });
    }
    descriptionChange(event){
        this.setState({ description: event.target.value });
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
                        <input className="create-event-title-input create-event-input" type="text"
                            value={this.state.event_name} onChange={this.nameChange} />

                        <h3 className="create-event-type">Тип события</h3>
                        <RadioGroup onChange={this.typeChange} horizontal>
                            <ReversedRadioButton value="group">
                                Групповой
                            </ReversedRadioButton>
                            <ReversedRadioButton value="single">
                                Одиночный
                            </ReversedRadioButton>
                        </RadioGroup>

                        <h3 className="create-event-isPrivate">Приватный</h3>
                        <RadioGroup onChange={this.privateChange} horizontal>
                            <ReversedRadioButton value={"true"}>
                                Да
                            </ReversedRadioButton>
                            <ReversedRadioButton value={"false"}>
                                Нет
                            </ReversedRadioButton>
                        </RadioGroup>

                        <h3 className="create-event-Address">Адрес</h3>
                        <input className="create-event-Address-input create-event-input" type="text"
                            value={this.state.address} onChange={this.addressChange} />

                        <h3 className="create-event-descr">Описание</h3>
                        <input className="create-event-descr-input create-event-input" type="text"
                            value={this.state.description} onChange={this.descriptionChange} />
                    </div>
                    <div className="create-button" onClick={this.sendNewEvent}>
                        Создать
                    </div>
                </main>
            </div>
        );


    }

}