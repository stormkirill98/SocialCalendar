import React from "react";
import "../css/Dialogues.css";
import Header from "../components/Header";
import DialoguesMainBox from "../components/DialoguesMainBox";


export default class Dialogues extends React.Component {
    render() {
        return (
    <>
    <Header/>
    <DialoguesMainBox/>
    </>
        );
    }
}
