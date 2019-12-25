import React from 'react';
import '../css/Friends.css';
import Button from "@material-ui/core/Button";
import DeleteIcon from '@material-ui/icons/Delete';
import ChatIcon from '@material-ui/icons/Chat';


export default class Friend extends React.Component {

    deleteFriends(){
        fetch(`/friends?id=5dfd1dd64bd7592818b25abb`).then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                   
                });
            } else {
                console.log(response.statusText);
            }
        });
    }

    deleteFriend() {
        var x = document.getElementById("fr");
        x.style.display = "none"; 
       }

    render() {
        return (
            <>
                <li className="friend" id="fr">
                    <div className="wrap">
                    <img className="friend-avatar" src={this.props.profile_pic} alt="аватарка друга"/>
                    <div className="friend-name">{this.props.name}</div>
                    </div>
                    <div className="wrap">
                        <Button color="primary" className="settings-btn" variant="contained">
                            <ChatIcon fontSize="small"/>
                        </Button>
                        <Button color="primary" className="settings-btn" variant="contained" onClick={this.deleteFriend}>
                            <DeleteIcon fontSize="small"/>
                        </Button>
                    </div>
                </li>
            </>
        );
    }
}
