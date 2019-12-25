import React from 'react';
import '../css/Friends.css';


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
                        <button className="button1">Перейти к чату</button>
                        <button className="button1" onClick={this.deleteFriend}>Добавить/Удалить</button>
                    </div>
                </li>
            </>
        );
    }
}
