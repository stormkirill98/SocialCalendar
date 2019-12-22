import React from "react";
import "../css/Login.css"

export default class Login extends React.Component {

    signIn() {
        fetch("/login", {
            mode: "no-cors"
        })
            .then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        console.log(data);
                    })
                } else {
                    console.log(response.statusText);
                }
            });
    }

    render() {
        return (
            <div className="wrap-index-main">
                <div className="main">
                    <div className="title">Social Calendar</div>
                    <button className="google-auth-button" onClick={this.signIn}/>
                </div>
            </div>
        );
    }
}
