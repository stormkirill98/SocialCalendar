import React from "react";
import "../css/Login.css"
import { Redirect } from "react-router-dom";


export default class Login extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            isAuth: false
        }

        fetch(`/invites`).then((response) => {
            if (response.ok) {
                this.setState({
                    isAuth: response.headers.get('Auth')
                });
            }
        });


    }

    signIn() {
        window.location.replace("https://social-calendar-tensor.herokuapp.com/login")
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
