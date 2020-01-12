import React from "react";
import "../css/Login.css"
import { Redirect } from "react-router-dom";
import Cookies from 'js-cookie';


export default class Login extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            isAuth: false
        }

        fetch(`/event?id=5dd96b8efacc0de4f9e30c50`).then((response) => {
            if (response.ok) {
                this.setState({
                    isAuth: response.headers.get('Auth')
                });
            }
        });


    }

    signIn() {
        window.location.replace("https://127.0.0.1:5000/login")
    }

    render() {
        if (this.state.isAuth) {
            return <Redirect to='/Calendar' />
        } else {
            return (
                <div className="wrap-index-main">
                    <div className="main">
                        <div className="title">Social Calendar</div>
                        <button className="google-auth-button" onClick={this.signIn} />
                    </div>
                </div>
            );
        }
    }
}
