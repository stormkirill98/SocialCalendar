import React from "react";
import Avatar from 'react-avatar';
import Grid from "@material-ui/core/Grid";
import { Card } from "@material-ui/core";
import "../css/UserCard.css"
import Typography from "@material-ui/core/Typography";
import ExitIcon from '@material-ui/icons/ExitToApp';
import Button from "@material-ui/core/Button";
import NotificationCenter from "./NotificationCenter";
import { Redirect, Link } from "react-router-dom";

export default class UserCard extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            userName: props.user ? props.user.name : "",
            pictureUrl: props.user ? props.user.profile_pic : ""
        };

        this.updateUser = this.updateUser.bind(this);
        this.exit = this.exit.bind(this);
    }

    exit() {
        fetch("/logout").then((response) => {
            window.location.replace("https://127.0.0.1:5000/");
        });
        //return <Redirect push to='/' />; //не робит почему то
    }
    updateUser(user) {
        this.setState({
            userName: user ? user.name : "",
            pictureUrl: user ? user.profile_pic : ""
        });
    }



    render() {
        return (
            <>
                <Grid container>
                    <Avatar alt={this.state.userName} size="55" round={true} src={this.state.pictureUrl} />
                    <Grid item className="user-info">
                        <Card className="user-name">
                            <Typography className="card-title" color="textSecondary" gutterBottom>
                                {this.state.userName}
                            </Typography>
                        </Card>
                        <div className="buttons">
                            <NotificationCenter className="notifications-center" />

                            <Button variant="contained" color="primary" className="settings-btn" size="small"
                                onClick={() => { document.getElementById("app-exit").style.display = 'flex' }}>
                                <ExitIcon fontSize="small" />
                            </Button>
                        </div>
                    </Grid>
                </Grid>
                <div id="app-exit" className="app-exit" style={{ display: 'none' }}>
                    <div className="confirm-exit-window">
                        <h3>Вы точно хотите выйти?</h3>
                        <div className="confirm-delete-btns">
                            <Button color="primary" className="confirm-delete-yes" variant="contained"
                                onClick={this.exit} >
                                Да
                            </Button>
                            <Button color="primary" className="confirm-delete-no" variant="contained"
                                onClick={() => { document.getElementById("app-exit").style.display = 'none' }} >
                                Нет
                            </Button>
                        </div>
                    </div>
                </div>
            </>
        );
    }
}
