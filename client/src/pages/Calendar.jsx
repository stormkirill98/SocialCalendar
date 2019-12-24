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

        this.getCurrentUser = this.getCurrentUser.bind(this);

        this.getCurrentUser();
    }

    getCurrentUser() {
        fetch("/user").then((response) => {
            if (response.ok){
                response.json().then((data) => {
                    const curDate = new Date();
                    this.setState({
                        curYear: curDate.getFullYear(),
                        curMonth: curDate.getMonth() + 1,
                        curUser: {
                            user_id: data.id,
                            name: data.name,
                            email: data.email,
                            profile_pic: data.profile_pic,
                            birthday: data.birthday
                        }
                    });

                    this.header.updateUser(this.state.curUser);
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    updateEventListData = (value) => {
        this.setState({ eventsInEventsList: value })
    };

    render() {
        return (
            <div className="page-container">
                <Header user={this.state.curUser} ref={ref => this.header = ref}/>

                <div className="flex-row calendar-main">
                    <Month year={this.state.curYear} month={this.state.curMonth} updateEventListData={this.updateEventListData}/>
                    <EventList events={this.state.eventsInEventsList} />
                </div>
            </div>
        );
    }
}