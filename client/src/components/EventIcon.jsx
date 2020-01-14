import React from "react";
import "../css/EventIcon.css"
import { Link } from "react-router-dom";

export default class EventIcon extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            eventID: props.eventID,
            name: props.name,
            icon: props.icon,
            time: props.time
        };
    }

    toggleInfo(hidden) {
        this.info.hidden = hidden;
    }

    render() {
        let eventId = typeof this.state.eventID === "object"
            ? this.state.eventID["$oid"]
            : this.state.eventID;
        // let eventIcon = typeof this.state.icon === "object"
        //     ? this.state.icon["$oid"]
        //     : this.state.icon;

        return (
            <div>
                {this.state.icon ?
                    <Link to={"/Event/" + eventId}>
                        <img className="event-icon" src={this.state.icon} alt="."
                            onMouseEnter={() => this.toggleInfo(false)}
                            onMouseLeave={() => this.toggleInfo(true)} />
                    </Link>
                    : ''}

                <div className="event-info" hidden ref={ref => this.info = ref}>
                    {this.state.name} <br /> {this.state.time}
                </div>
            </div>
        );
    }
}