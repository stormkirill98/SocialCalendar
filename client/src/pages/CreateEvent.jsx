import React from "react";
import "../css/CreateEvent.css";
import Header from "../components/Header";
import Button from "@material-ui/core/Button";
import IconsGrid from "../components/IconsGrid";
import { RadioGroup, ReversedRadioButton } from 'react-radio-buttons';

export default class CreateEvent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            type: "single",
            event_name: "Event_name",
            is_private: "true",
            datetime: "" + this.props.match.params.day + "." + this.props.match.params.month + "." +
            this.props.match.params.year + " 15:30",
            address: "Советский Союз",
            description: "Desciption",
            icon: "https://social-calendar-tensor.herokuapp.com/load_icon/bell.svg"
        };
        this.privateChange = this.privateChange.bind(this);
        this.typeChange = this.typeChange.bind(this);
        this.sendNewEvent = this.sendNewEvent.bind(this);
        this.nameChange = this.nameChange.bind(this);
        this.addressChange = this.addressChange.bind(this);
        this.descriptionChange = this.descriptionChange.bind(this);
        this.changeSelectedIcon = this.changeSelectedIcon.bind(this);
    }

    sendNewEvent() {
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
                    window.location.replace("https://127.0.0.1:5000/")
                    //return <Redirect push to={"event/" + data.$oid} /> не робит :(
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
    nameChange(event) {
        this.setState({ event_name: event.target.value });
    }
    addressChange(event) {
        this.setState({ address: event.target.value });
    }
    descriptionChange(event) {
        this.setState({ description: event.target.value });
    }

    changeSelectedIcon(newicon) {
        this.setState({ icon: "https://social-calendar-tensor.herokuapp.com/load_icon/" + newicon });
        console.log("сработала смена иконки " + this.state.icon);
    }

    render() {
        return (
            <div className="page-container-event">
                <Header />
                <main className="create-event">
                    <div className="create-event-grid">
                        <IconsGrid changeIcon={this.changeSelectedIcon} />
                        <h4 className="create-event-title left-column-title">Название</h4>
                        <input className="create-event-title-input create-event-input" type="text"
                            value={this.state.event_name} onChange={this.nameChange} />

                        <h4 className="create-event-type left-column-title">Тип события</h4>
                        <RadioGroup onChange={this.typeChange} horizontal>
                            <ReversedRadioButton className="radio-button-create-event" value="group" >
                                Групповой
                            </ReversedRadioButton>
                            <ReversedRadioButton className="radio-button-create-event" value="single" >
                                Одиночный
                            </ReversedRadioButton>
                        </RadioGroup>

                        <h4 className="create-event-isPrivate left-column-title">Приватный</h4>
                        <RadioGroup onChange={this.privateChange} horizontal>
                            <ReversedRadioButton className="radio-button-create-event" value={"true"} >
                                Да
                            </ReversedRadioButton>
                            <ReversedRadioButton className="radio-button-create-event" value={"false"} >
                                Нет
                            </ReversedRadioButton>
                        </RadioGroup>

                        <h4 className="create-event-Address left-column-title">Адрес</h4>
                        <input className="create-event-Address-input create-event-input" type="text"
                            value={this.state.address} onChange={this.addressChange} />

                        <h4 className="create-event-descr left-column-title">Описание</h4>
                        <input className="create-event-descr-input create-event-input" type="text"
                            value={this.state.description} onChange={this.descriptionChange} />
                    </div>
                    <Button color="primary" className="settings-btn create-button" variant="contained" onClick={this.sendNewEvent}>
                        Создать событие
                    </Button>

                </main>
            </div>
        );


    }

}