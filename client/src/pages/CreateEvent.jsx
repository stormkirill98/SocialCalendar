import React from "react";
import "../css/CreateEvent.css";
import Header from "../components/Header";
import IconsGrid from "../components/IconsGrid";
import {Redirect} from "react-router-dom";

export default class CreateEvent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            type: "group",
            event_name: "Event_name",
            is_private: "false",
            datetime: new Date(this.props.match.params.year,this.props.match.params.month,
                this.props.match.params.day,24,0,30,500),//час мин сек мс
            address: "Советский Союз",
            description: "Desciption",
            icon: "/load_icon/doughnut.svg"
        };
        this.handleChangddddddde = this.handleChangddddddde.bind(this);
    }

    selectAvatar = (name) => {
        this.setState({ icon: name })
     }

    sendNewEvent() {
        var bodyJSON = JSON.stringify({
            "type": this.state.type,
            "name": this.state.event_name,
            "is_private": this.state.is_pivate,
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
                    return <Redirect to='/Calendar'/>
                })
            } else {
                console.log(response.statusText);
                
            }
        });
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

    handleChangde(event) {
        this.setState({type: event.target.value});
      }

    render() {
        return (
            <div className="page-container-event">
                <Header />
                <main className="event">
                    <div className="event-box">
                        <div className="event-img-wrap event-page-wrap">
                            <IconsGrid updateData={this.selectAvatar}></IconsGrid>
                        </div>
                        <div className="event-title-descr event-page-wrap">
                            <div className="flex-row">
                                <h3 className="event-title">Название</h3>
                                <input className="event-title-input" type="text" /> {/*handleChangddddddde */}
                            </div>
                            <div className="flex-row">
                                <div className="event-short-descr">Короткое описание</div>
                                <input className="event-short-descr-input" type="text" />
                            </div>
                        </div>
                        <div className="event-page-wrap flex-row">
                            <h4 className="event-type">Тип события</h4>
                            <input className="event-type-input" type="text" />
                        </div>
                        <div className="event-body event-page-wrap">
                            <h4 className="event-descr">Описание</h4>
                            <textarea className="event-descr-input" type="text" />
                        </div>
                    </div>
                </main>
            </div>
        );


    }

}