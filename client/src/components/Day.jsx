import React from "react";
import "../css/Day.css"
import EventIcon from "./EventIcon";
import { Link } from "react-router-dom";

export default class Header extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            events: props.events ? props.events : [],
            updateEventListData: props.updateEventListData ? props.updateEventListData : null,
            month: props.month,
            year: props.year
        }
    }



    render() {
        const style = {
            opacity: this.props.hidden ? 0.4 : 0.92,
        };
        let icons;

        console.log(this.state.events);
        if (this.state.events) {
            icons = this.state.events.map(
                (val) => <EventIcon key={val.id} eventID={val.id} name={val.name} time={val.datetime.substr(-5).trim()} icon={val.icon} />);
        }


        return (
            <div className="day-plate" style={style}
                onClick={() => { this.state.updateEventListData(this.state.events) }}>
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