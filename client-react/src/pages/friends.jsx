import React from "react";
import "../css/Friends.css";
import Header from "../components/Header";
import Friend from "../components/friend";


export default class friends extends React.Component {
    render() {
        return (
          <>
          <Header/>
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