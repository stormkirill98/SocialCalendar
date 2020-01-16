import React from "react";
import Button from "@material-ui/core/Button";
import CloseIcon from '@material-ui/icons/Close';
import CheckIcon from '@material-ui/icons/Check';
import EventIcon from '@material-ui/icons/Event';
import AccessibleIcon from '@material-ui/icons/Accessible';

export default class NotificationList extends React.Component {

    constructor(props) {
        super(props);

        this.removeInvite = props.removeInvite;

        this.state = {
            invite: props.invite
        };
        
    }

    accept() {
        const id = this.state.invite.id;
        this.handleInvite(id, "accept");
        this.removeInvite(id)
    }

    decline() {
        const id = this.state.invite.id;
        this.handleInvite(id, "decline");
        this.removeInvite(id)
    }

    handleInvite(id, action) {
        fetch(`/invite?id=${id.$oid}&action=${action}`, {method: 'DELETE'})
            .then((response) => {
                console.log(response.statusText);
            });
    }

    render() {
        const invite = this.state.invite;
        let content;
        if (invite.type === "friend") {
            content = invite.sender_name + " будет вашим другом?";
        } else {
            content = invite.sender_name + "приглашает Вас присоединиться к " + invite.event_name;
        }

        return (
            <div className="container">
                {invite.type === "friend" ? <AccessibleIcon className="type-icon"/> :
                    <EventIcon className="type-icon"/>}
                <div className="content">{content}</div>
                <Button color="primary" className={"accept-btn"} onClick={() => this.accept()}>
                    <CheckIcon fontSize={"small"}/>
                </Button>
                <Button color="secondary" className={"decline-btn"} onClick={() => this.decline()}>
                    <CloseIcon fontSize={"small"}/>
                </Button>
            </div>
        );
    }
}