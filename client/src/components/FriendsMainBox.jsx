import React from 'react';
import '../css/Friends.css';
import Friend from "../components/Friend";


export default class FriendsMainBox extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            friends: []
        };

        this.removeFriend = this.removeFriend.bind(this);
        this.getFriends = this.getFriends.bind(this);

        this.getFriends()
    }

    getFriends() {
        fetch("/friends").then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    this.setState({
                        friends: data ? data : []
                    });
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    removeFriend(id) {
        const friends = this.state.friends;

        this.setState({friends: friends.filter((value => value.id !== id))});
    }

    render() {
        console.log(this.state.friends);
        const listItems = this.state.friends.map(
            (val) => <Friend friend={val} key={val.id} removeFriend={this.removeFriend}/>);

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