import React from "react";
import "../css/EventIcon.css"

export default class EventIcon extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
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
                    <img className="event-icon" src={require("../SVG_icon/burger.svg")} alt="icon"
                         onMouseEnter={() => this.toggleInfo(false)}
                         onMouseLeave={() => this.toggleInfo(true)}/> : ''}

                <div className="event-info" hidden ref={ref => this.info = ref}>
                    {this.state.name} <br/> {this.state.time}
                </div>
            </div>
        );
    }
}