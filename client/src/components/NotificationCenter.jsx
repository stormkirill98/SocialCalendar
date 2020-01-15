import React from "react";
import Notification from "./Notification";
import "../css/NotificationCenter.css"
import NotificationsIcon from '@material-ui/icons/Notifications';
import NotificationsNoneIcon from "@material-ui/core/SvgIcon/SvgIcon";
import Button from "@material-ui/core/Button";

export default class NotificationCenter extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            invites: []
        };

        this.toggle = this.toggle.bind(this);
        this.removeInvite = this.removeInvite.bind(this);
        this.getInvites = this.getInvites.bind(this);

        this.getInvites()

    }

    getInvites() {
        fetch("/invites").then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    this.setState({
                        invites: data ? data : []
                    });
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    toggle() {
        this.widget.className === "hide" ? this.widget.className = "show"
            : this.widget.className = "hide";
    }

    removeInvite(id) {
        const invites = this.state.invites;

        this.setState({invites: invites.filter((value => value.id !== id))});
    }

    render() {
        const listItems = this.state.invites.map(
            (val) => <Notification invite={val} key={val.id} removeInvite={this.removeInvite}/>);

        return (
            <>
                <Button variant="contained" color="primary" size="small" className={this.props.className}
                        onClick={this.toggle}>
                    {this.state.invites.length === 0 ? "" : this.state.invites.length}
                    <NotificationsNoneIcon size="small"/>
                    <NotificationsIcon fontSize="small" />
                </Button>

                <div ref={ref => this.widget = ref} className="hide">
                    {listItems}
                </div>
            </>
        );
    }

}