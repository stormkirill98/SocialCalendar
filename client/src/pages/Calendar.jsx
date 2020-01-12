import React from "react";
import Header from "../components/Header";
import Month from "../components/Month";
import EventList from "../components/EventList";
import "../css/Calendar.css"

export default class Calendar extends React.Component {
    constructor(props) {
        super(props);

        const curDate = new Date();
        this.state = {
            curYear: curDate.getFullYear(),
            curMonth: curDate.getMonth() + 1
        };
    }

    updateEventListData = (value) => {
        this.setState({ eventsInEventsList: value })
    };

    render() {
        return (
            <div className="page-container">
                <Header/>
                <div className="flex-row calendar-main">
                    <Month year={this.state.curYear} month={this.state.curMonth} updateEventListData={this.updateEventListData}/>
                    <EventList events={this.state.eventsInEventsList} />
                </div>
            </div>
        );
    }
}