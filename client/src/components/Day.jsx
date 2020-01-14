import React from "react";
import "../css/Day.css"
import EventIcon from "./EventIcon";
import { Link } from "react-router-dom";

export default class Day extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            events: (props.events && props.events.length !== 0) ? props.events : null,
            updateEventListData: props.updateEventListData ? props.updateEventListData : null,
            month: props.month,
            year: props.year,
        };

        this.updateEvents = this.updateEvents.bind(this);
    }

    updateEvents(events) {
        this.setState({
            events: (events && events.length !== 0) ? events : null,
            // updateEventListData: this.state.updateEventListData,
            // month: this.state.month,
            // year: this.state.year
        })
    }

    render() {
        const style = {
            opacity: this.props.hidden ? 0.4 : 0.92,
        };
        let icons;

        let options = {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            weekday: 'long',
            hour: 'numeric',
            minute: 'numeric',
        };

        console.log(this.state.events);

        if (this.state.events) {
            icons = this.state.events.map((val) => <EventIcon key={val.id}
                eventID={val.id}
                name={val.name}
                time={new Date(val.datetime.$date).toLocaleString("ru", options)}
                icon={val.icon} />);
        }


        return (
            <div className="day-plate" style={style}
                onClick={() => {
                    this.state.updateEventListData(this.state.events)
                }}>
                {this.props.day}
                <div className="mini-events">
                    {this.state.events ? icons : ""}
                    <Link to={"/CreateEvent/" + this.state.year + "/" + this.state.month + "/" + this.props.day}>
                        <img className="addEventButton" src="/load_icon/plus.svg"
                            alt="+" onClick={this.createEvent} />
                    </Link>
                </div>
            </div>
        );
    }
}