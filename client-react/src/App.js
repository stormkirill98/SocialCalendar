import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import friends from "./pages/friends";
import dialogues from "./pages/dialogues";
import Event from "./pages/Event";
import Main from "./pages/Main"



export default class Routing extends React.Component {
    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/Calendar" component={Main} />
                    <Route path="/Event" component={Event} />
                    <Route path="/dialogues" component={dialogues} />
                    <Route path="/friends" component={friends} />
                    <Route path="/" component={Main} />
                </Switch>
            </Router>
        );
    }
}