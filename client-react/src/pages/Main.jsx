import React from "react";
import "../css/index.css";

export default class Main extends React.Component {
    render() {
        return (
            <div className="wrap-index-main">
                <div className="main">
                    <div className="title">Social Calendar</div>
                    <a href="Calendar" className="google-auth">
                        <img src="img/SingInWithGoogle.png" alt="зайти через гугол" className="google-img" />
                    </a>
                </div>
            </div>
        );
    }
}