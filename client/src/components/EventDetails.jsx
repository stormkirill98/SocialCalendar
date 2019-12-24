import React from "react";
import "../css/EventDetails.css"


export default class EventDetails extends React.Component {
    
    render() {
        return (
            <>
            <li className="event-details">
                <img className="detail-icon" src={this.props.icon} alt="icon"/>
                <div className="wrap1">
                    <div className="detail-title">{this.props.title}</div>
                    <div className="detail-description">{this.props.description} </div>
                </div>
            </li>
            </>
        );
    }
}