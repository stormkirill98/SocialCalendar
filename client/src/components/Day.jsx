import React from "react";
import "../css/Day.css"
import EventIcon from "./EventIcon";

export default class Header extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            events: props.events ? props.events : []
        }
    }

    render() {
        const style = {
            visibility: this.props.hidden ? 'hidden' : 'visible',
        };


        const icons = this.state.events.map(
            (val) => <EventIcon key={val.id} name={val.name} time={val.datetime.substr(-5).trim()} icon={val.icon}/>);

        return (
            <div className="day-plate" style={style}>
                {this.props.day}
                <div className="mini-events">
                    {icons}
                </div>
            </div>
        );
    }
}