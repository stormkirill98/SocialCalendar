import React from 'react';
import '../css/Dialogues.css';


export default class Message extends React.Component {
    render() {
        return (
            <>
                <li class="wrap2">
                    <div class="message">username1: message</div>
                    <div class="time">10:35</div>
                </li>
            </>
            );
        }
    }