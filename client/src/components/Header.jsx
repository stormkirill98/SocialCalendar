import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import "../css/Header.css"
import Form from "react-bootstrap/Form";
import UserCard from "./UserCard";
import {Link} from "react-router-dom";

export default class Header extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            user: null
        };

        this.getCurrentUser = this.getCurrentUser.bind(this);

        this.getCurrentUser();
    }

    getCurrentUser() {
        fetch("/user").then((response) => {
            if (response.ok){
                response.json().then((data) => {
                    this.setState({
                        user: {
                            user_id: data.id,
                            name: data.name,
                            email: data.email,
                            profile_pic: data.profile_pic,
                            birthday: data.birthday
                        }
                    });

                    this.userCard.updateUser(this.state.user);
                })
            } else {
                console.log(response.statusText);
            }
        });
    }

    render() {
        return (
            <Navbar bg="dark" variant="dark" className="navbar">
                <Navbar.Brand className="navbar-brand">
                    <Link className="header-link" to="../../../../../Calendar">Social Calendar</Link>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav>
                        <Nav.Link>
                            <Link className="header-link" to="../../../../../Calendar">Календарь</Link>
                        </Nav.Link>
                        <Nav.Link>
                            <Link className="header-link" to="../../../../../Friends">Друзья</Link>
                        </Nav.Link>
                        {/* <Nav.Link>
                            <Link className="header-link" to="../../../../../Dialogues">Чаты</Link>
                        </Nav.Link> */}
                    </Nav>
                </Navbar.Collapse>

                <Form inline>
                    <UserCard user={this.state.user} ref={ref => this.userCard = ref}/>
                </Form>
            </Navbar>
        );
    }
}
