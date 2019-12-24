import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Friends from "./pages/Friends";
import Dialogues from "./pages/Dialogues";
import Event from "./pages/Event";
import CreateEvent from "./pages/CreateEvent";
import Login from "./pages/Login"
import Calendar from "./pages/Calendar"

export default class Routing extends React.Component {
    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/Calendar/:id" component={Calendar} />
                    <Route path="/Calendar" component={Calendar} />
                    <Route path="/Event/:id" component={Event} />
                    <Route path="/Event" component={Event} />{/* Это потом убрать */}
                    <Route path="/CreateEvent/:month/:day" component={CreateEvent} />
                    <Route path="/Dialogues/:id" component={Dialogues} /> 
                    <Route path="/Dialogues" component={Dialogues} />{/* и это */}
                    <Route path="/Friends" component={Friends} />

                    {/* Новые страницы впихивать перед этим комментом   */}
                    <Route path="/" component={Login} />
                </Switch>
            </Router>
        );
    }
}
