import React from "react";
import "../css/Friends.css";
import Header from "../components/Header";
import FriendsMainBox from "../components/FriendsMainBox";


export default class Friends extends React.Component {
    render() {
        return (
            <>
                <Header/>
                <FriendsMainBox/>
            </>
        );
    }
}
