import React from 'react';
import '../css/Friends.css';
import Button from "@material-ui/core/Button";
import DeleteIcon from '@material-ui/icons/Delete';
import ChatIcon from '@material-ui/icons/Chat';


export default class Friend extends React.Component {

    constructor(props) {
        super(props);

        this.removeFriend = props.removeFriend;

        this.state = {
            friend: props.friend
        };
    }

    deleteFriend(id) {
        fetch(`/friend?id=${id}`, {method: 'DELETE'})
            .then((response) => {
                if (response.ok){
                    response.json().then((data) => {
                        console.log(data);
                    })
                } else {
                    console.log(response.statusText);
                    }
            });
        this.removeFriend(id);
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
                        <Button color="primary" className="settings-btn" variant="contained">
                            <ChatIcon fontSize="small"/>
                        </Button>
                        <Button color="primary" className="settings-btn" variant="contained" onClick={() => this.deleteFriend(friend.id.$oid)}>
                            <DeleteIcon fontSize="small"/>
                        </Button>
                    </div>
                </li>
            </>
        );
    }
}
