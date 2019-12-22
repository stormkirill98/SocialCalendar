import React from 'react';
import '../css/Friends.css';
import Friend from "../components/Friend";


export default class FriendsMainBox extends React.Component {
    render() {
        return (
            <>
            <div class="friends-main-box">
            <h4 class="friends">Список друзей</h4>
            <input placeholder="Поиск друзей" type="text" name="friends-search"/>
            <ol class="friends-list">
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
                <Friend/>
            </ol>
            </div>
            </>
        );
    }
}