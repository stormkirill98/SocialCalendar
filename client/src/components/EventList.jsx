import React from "react";
import "../css/EventList.css"


export default class EventList extends React.Component {
    render() {
        return (
            <div className="events-area">
                <div className="events-list">
                    <div className="event-details">День рождения Путина</div>
                    <div className="event-details">Годовщина смерти тёщи</div>
                    <div className="event-details">Победа Гватемалы над Р.Конго</div>
                </div>
            </div>
        );
    }
}