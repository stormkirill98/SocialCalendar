import React from 'react';
import '../css/Friends.css';
import Friend from "../components/Friend";


export default class FriendsMainBox extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            friends: []
        };
    
        fetch("/friends").then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    this.setState({
                        friends:data
                    });
                });
            } else {
                console.log(response.statusText);
            }
        });
    }

    render() {
        console.log(this.state.friends);
        const listItems = this.state.friends.map((val) => <Friend key={val.id} id={val.id} name={val.name} profile_pic={val.profile_pic}/>);
        return (
            <>
            <div class="friends-main-box">
            <h4 class="friends">Список друзей</h4>
            <input placeholder="Поиск друзей" type="text" name="friends-search"/>
            <ol class="friends-list">
               {listItems}
            </ol>
            </div>
            </>
        );
    }
}