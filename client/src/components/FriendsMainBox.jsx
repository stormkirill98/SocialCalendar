import React from 'react';
import '../css/Friends.css';
import Friend from "../components/Friend";
import NotAFriend from "../components/NotAFriend"


export default class FriendsMainBox extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            friends: [],
            users: []
        };
        
        this.sendInvite = this.sendInvite.bind(this);
        this.removeFriend = this.removeFriend.bind(this);
        this.getFriends = this.getFriends.bind(this);
        this.getUsers = this.getUsers.bind(this);

        this.getFriends()
        this.getUsers("а")
    }

    getUsers(search) {
        fetch(`/search/users?filtered_str=${search}`).then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    this.setState({
                        users: data
                    });
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    getFriends() {
        fetch("/friends").then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    this.setState({
                        friends: data
                    });
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    sendInvite(Uid) {
        console.log("Uid: ",Uid);
        var id = Uid;
        console.log("id: ",id);
        const users = this.state.users;
        console.log("users:",users);
        this.setState({users: users.filter((user => user._id.$oid !== id))});
    }

    removeFriend(id) {
        const friends = this.state.friends;
        this.setState({friends: friends.filter((friend => friend.id.$oid !== id))});
    }

    render() {
        console.log(this.state.friends);
        console.log(this.state.users);
        const listItems = this.state.friends.map(
            (val) => <Friend friend={val} key={val.id} removeFriend={this.removeFriend}/>);

        const listItems2 = this.state.users.map(
            (val) => <NotAFriend user={val} key={val.id} sendInvite={this.sendInvite}/>);

        return (
            <>
            <div class="friends-main-box">
                <h4 class="friends">Список друзей</h4>
                <input placeholder="Поиск друзей" type="text" name="friends-search"/>
                <ol class="friends-list">
                    {listItems}
                    {listItems2}
                </ol>
            </div>
            </>
        );
    }
}