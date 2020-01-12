import React from 'react';
import '../css/Friends.css';
import Button from "@material-ui/core/Button";
import PersonAddIcon from '@material-ui/icons/PersonAdd';
import ChatIcon from '@material-ui/icons/Chat';


export default class NotAFriend extends React.Component {
    constructor(props) {
        super(props);

        this.sendInvite = props.sendInvite;

        this.state = {
            user: props.user
        };
    }

    sendInvite(id) {
        var bodyJSON = JSON.stringify({ "type": "friend", "receiver_id": id })
        fetch("/invite",
            { method: 'POST',
            headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
            body: bodyJSON}).then((response) => {
                if (response.ok){
                    response.json().then((data) => {
                        console.log(data);
                    })
                } else {
                    console.log(response.statusText);
                }
        });
    }

    render() {
        const user = this.state.user;

        return (
            <>
                <li className="friend">
                    <div className="wrap">
                    <img className="friend-avatar" src={user.profile_pic} alt="аватарка недруга"/>
                    <div className="friend-name">{user.name}</div>
                    </div>
                    <div className="wrap">
                        <Button color="primary" className="settings-btn" variant="contained">
                            <ChatIcon fontSize="small"/>
                        </Button>
                        <Button color="primary" className="settings-btn" variant="contained" onClick={() => this.sendInvite(user._id)}>
                            <PersonAddIcon fontSize="small"/>
                        </Button>
                    </div>
                </li>
            </>
        );
    }
}