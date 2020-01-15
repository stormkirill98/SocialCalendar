import React from 'react';
import '../css/Friends.css';
import Button from "@material-ui/core/Button";
import DeleteIcon from '@material-ui/icons/Delete';
import ChatIcon from '@material-ui/icons/Chat';


export default class FriendForEvent extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            friend: props.friend
        };
        this.sendInvite = this.sendInvite.bind(this);
    }

    sendInvite(){

    }

    render() {
        const friend = this.state.friend;

        return (
            <>
                <li className="friend">
                    <div className="wrap">
                    <img className="friend-avatar" src={friend.profile_pic} alt="аватарка друга"/>
                    <div className="friend-name">{friend.name}</div>
                    </div>
                    <div className="wrap">
                        <Button color="primary" className="settings-btn" variant="contained" onClick={this.sendInvite}>
                            <DeleteIcon fontSize="small"/>
                        </Button>
                    </div>
                </li>
            </>
        );
    }
}
