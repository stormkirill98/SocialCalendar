import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Event from "./pages/Event";


export default class Routing extends React.Component {
    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/" component={Main}/>>
                    <Route path="/Calendar" component={Calendar}/>>
                    <Route path="/Event" component={Event} />
                </Switch>
            </Router>
        );
    }
}