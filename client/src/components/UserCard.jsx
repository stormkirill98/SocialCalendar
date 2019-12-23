import React from "react";
import Avatar from 'react-avatar';
import Grid from "@material-ui/core/Grid";
import {Card} from "@material-ui/core";
import "../css/UserCard.css"
import Typography from "@material-ui/core/Typography";
import SettingsIcon from '@material-ui/icons/Settings';
import Button from "@material-ui/core/Button";
import NotificationCenter from "./NotificationCenter";

export default class UserCard extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            invites: [{
                id: 101332313,
                type: "friend",
                sender_id: 12341,
                sender_name: "Vasya Pupkin"
            }, {
                id: 10123789813,
                type: "event",
                sender_id: 12341,
                event_name: "Happy Birthday"
            }, {
                id: 101672313,
                type: "friend",
                sender_id: 12341,
                sender_name: "Artur Milasian"
            }],
            userName: "Kirill Panihin",
            pictureUrl: this.getPicture()

            //"https://lh3.googleusercontent.com/a-/AAuE7mAd99fGmysqUPELQf17X25h6P_Ovketo5vlsncv"
        };
    }

    getPicture(){
        return "https://lh3.googleusercontent.com/a-/AAuE7mAd99fGmysqUPELQf17X25h6P_Ovketo5vlsncv"
    }

    render() {
        return (
            <Grid container>
                <Avatar alt={this.state.userName} size="55" round={true} src={this.state.pictureUrl}/>
                <Grid item className="user-info">
                    <Card className="user-name">
                        <Typography className="card-title" color="textSecondary" gutterBottom>
                            {this.state.userName}
                        </Typography>
                    </Card>
                    <div className="buttons">
                        <NotificationCenter invites={this.state.invites} className="notifications-center"/>

                        <Button variant="contained" color="primary" className="settings-btn" size="small">
                            <SettingsIcon fontSize="small"/>
                        </Button>
                    </div>
                </Grid>


            </Grid>
        );
    }
}
