import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import "../css/Header.css"
import Form from "react-bootstrap/Form";
import UserCard from "./UserCard";

export default class Header extends React.Component {
    render() {
        return (
            <Navbar bg="dark" variant="dark" className="navbar">
                <Navbar.Brand href="../Calendar" className="title">Social Calendar</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav>
                        <Nav.Link href="../Calendar">Календарь</Nav.Link> {/*Хз href так или не так, но он робит */}
                        <Nav.Link href="../Friends">Друзья</Nav.Link>
                        <Nav.Link href="../Dialogues">Чаты</Nav.Link>
                    </Nav>
                </Navbar.Collapse>

                <Form inline>
                    <UserCard/>
                </Form>
            </Navbar>
        );
    }
}
