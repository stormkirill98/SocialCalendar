import React from "react";
import "../css/EventIcon.css"
import {Link} from "react-router-dom";

export default class EventIcon extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            eventID: props.eventID,
            name: props.name,
            icon: props.icon,
            time: props.time
        }
    }

    toggleInfo(hidden) {
        this.info.hidden = hidden;
    }

    render() {
        return (
            <div>
                {this.state.icon ?
                    <Link to={"/Event/" + this.state.eventID}>
                        <img className="event-icon" src={this.state.icon} alt="icon"
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