import React from 'react';
import '../css/Friends.css';
import Button from "@material-ui/core/Button";
import AddIcon from '@material-ui/icons/Add';

export default class FriendForEvent extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            friend: props.friend
        };
        this.sendInvite = this.sendInvite.bind(this);
    }

    sendInvite() {
        var bodyJSON = JSON.stringify({
            "type": "event",
            "receiver_id": this.state.friend.id.$oid,
            "event_id": this.props.eventID
        })
        fetch("https://127.0.0.1:5000/invite", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: bodyJSON
        }).then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    console.log("ответ /invite POST: " + data);
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    render() {
        const friend = this.state.friend;
        return (
            <>
                <li className="friend">
                    <div className="wrap">
                        <img className="friend-avatar" src={friend.profile_pic} alt="аватарка друга" />
                        <div className="friend-name">{friend.name}</div>
                    </div>
                    <div className="wrap">
                        <Button color="primary" className="settings-btn" variant="contained" onClick={this.sendInvite}>
                            <AddIcon fontSize="small" />
                        </Button>
                    </div>
                </li>
            </>
        );
    }
}
