import React from "react";
import "../css/Month.css"
import Day from "./Day";

import Icon1 from "../SVG_icon/burger.svg"
import Icon2 from "../SVG_icon/coctail.svg"


export default class Month extends React.Component {
    constructor(props) {
        super(props);

        const icon1 = encodeImage(Icon1), icon2 = encodeImage(Icon2);

        this.state = {
            countDays: monthDays(props.year, props.month),
            firstDayOfWeek: firstWeekDay(props.year, props.month),
            events: {
                1: [
                    {
                        id: "124412",
                        type: "group",
                        name: "First Event",
                        is_private: "true",
                        datetime: "23.11.2019 19:00",
                        address: "address",
                        description: "desciption fasadsa",
                        icon: icon1
                    },
                    {
                        id: "12422412",
                        type: "group",
                        name: "Second Event",
                        is_private: "true",
                        datetime: "23.11.2019 19:00",
                        address: "address",
                        description: "desciption fasadsa",
                        icon: icon2
                    },
                    {
                        id: "12441",
                        type: "group",
                        name: "First Event",
                        is_private: "true",
                        datetime: "23.11.2019 19:00",
                        address: "address",
                        description: "desciption fasadsa",
                        icon: icon1
                    },
                    {
                        id: "1242241",
                        type: "group",
                        name: "Second Event",
                        is_private: "true",
                        datetime: "23.11.2019 19:00",
                        address: "address",
                        description: "desciption fasadsa",
                        icon: icon2
                    }
                ],
            }
        }
    }

    render() {
        const days = [], firstDay = this.state.firstDayOfWeek, countDays = this.state.countDays,
            countDaysPrevMonth = monthDays(this.props.year, this.props.month - 1);
        const months = ["", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];

        //названия дней недели
        for (let i = 0; i < 7; i++) {
            days.push(<div className="day-name" key={100+i}></div>);
        }

        //предыдущий месяц
        for (let i = 0; i < firstDay; i++) {
            days.push(<Day key={-i}
                hidden={true} day={countDaysPrevMonth - firstDay + 1 + i} />)
        }

        //этот месяц
        for (let i = 0; i < countDays; i++) {
            days.push(<Day key={i + 1} hidden={false} day={i + 1} events={this.state.events[i + 1]} 
                updateEventListData={this.props.updateEventListData}/>)
        }

        //след месяц
        for (let i = 0; i < 42 - countDays - firstDay; i++) {
            days.push(<Day key={countDays + i + 1} hidden={true} day={i + 1} />)
        }

        return (
            <div className="flex-col">
                <div className="wrap-year-month">
                    <div className="month-year">{months[this.props.month]} {this.props.year}</div>
                </div>
                <div className="month-grid">
                    {days}
                </div>
            </div>
        );
    }
}

function monthDays(y, m)    // full year and month in range 1-12
{
    let leap = 0;
    if (m === 2) {
        if (y % 4 === 0) leap = 1;
        if (y % 100 === 0) leap = 0;
        if (y % 400 === 0) leap = 1;
    }
    return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m] + leap;
}

function firstWeekDay(y, m) {
    return new Date(y, m - 1, 0).getDay();
}

async function encodeImage(src) {
    const canvas = document.createElement('canvas'),
        ctx = canvas.getContext('2d'),
        img = new Image();

    img.onload = await function () {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0, img.width, img.height);
    };

    img.src = src;

    return canvas.toDataURL();
}