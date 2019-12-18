import React from "react";
import "../css/EventPage.css";
import Header from "../components/Header"

export default class Event extends React.Component {
    render() {
        return (
            <>
                <Header />
                <main className="event">
                    <div className="event-box">
                        <div className="event-img">
                            <img src="img/icon.JPG" alt="Аватарка" />
                        </div>
                        <div className="event-title-descr">
                            <h3 className="event-title">
                                Название события
                            </h3>
                            <div className="event-description">
                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. In reiciendis a iusto consectetur,
                                nostrum fugit maiores, laborum est voluptatem ipsa totam dolor earum repellendus facilis
                                corporis adipisci doloremque itaque eius perferendis quibusdam aliquid! Non nemo earum soluta
                                rerum, ab cupiditate corporis eaque excepturi nihil molestiae tempore perferendis odio labore
                                doloremque?
                            </div>
                        </div>

                        <div className="event-members">
                            <h4 className="members-title">
                                Участники
                            </h4>
                            <div className="members-list">
                                member_Vasiliy_I
                                member_Vasiliy_II
                                member_Vasiliy_III
                            </div>
                        </div>

                        <div className="event-body">
                            <h4 className="event-body-title">Тело события</h4>
                            Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что
                            должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще
                            непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть
                            Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что
                            должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще
                            непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть
                            Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть
                        </div>

                    </div>

                    <div className="chat-main-box">
                        <h4 className="event-chat">Чат</h4>
                        <div className="chat-box">
                            <p>Привет</p>
                            <p>Привет</p>
                            <p>Привет</p>
                            <p>Привет</p>
                            <p>Привет</p>
                            <p>Привет</p>
                            <p>Привет</p>
                            <p>Привет</p>
                            <p>Привет</p>
                        </div>
                    </div>
                </main>
            </>
        );
    }

    constructor(props) {
        super(props);
        this.state = {
            eventID : -1,
        };
        this.getEventData();
    }

    async getEventData() {
        console.log(this.props.match.params.id);
        // fetch(`https://127.0.0.1:5000/event?id=${this.props.match.params.id}`).then((response) => {
        //     if (response.ok) {
        //         response.json().then((data) => {
        //             console.log(data);
        //         })
        //     } else {
        //         console.log(response.statusText);
        //     }
        // });
    }

}
