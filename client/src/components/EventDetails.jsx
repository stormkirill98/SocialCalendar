import React from "react";
import "../css/EventDetails.css"
// import {Link} from "react-router-dom";

export default class EventMember extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            id: props.id,

        };

        fetch(`https://social-calendar-tensor.herokuapp.com/friend?id=${this.props.id}}`).then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    this.state.name = data.name
                    this.state.avatar = data.profile_pic
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    render() {
        return (
                <div className="event-member">
                    <img className="event-member-ava" src={this.state.avatar} alt="Аватарка" width="20%" />
                    <div className="event-member-name">
                        {this.state.name}
                    </div>
                </div>
        );
    }
}