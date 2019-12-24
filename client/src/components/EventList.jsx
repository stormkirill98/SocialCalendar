import React from "react";
import "../css/EventList.css"
import EventDetails from "../components/EventDetails"


export default class EventList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            events: props.events
        };
    }

    render() {
        /*const listItems = this.state.events.map(
            (val) => <EventDetails key={val.id} eventID={val.id} name={val.name}
                time={val.datetime} icon={val.icon} address={val.address} description={val.description}
                type={val.type}/>);*/
        return (
            
            <div className="events-area">
                <ol className="events-list">
                    <EventDetails/>
                </ol>
            </div>
        );
    }
}