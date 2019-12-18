import React from "react";
import "../css/EventPage.css";

export default class Event extends React.Component {
    render() {
        return (
          <>
            <main class="event">
        <div class="event-box">
            <div class="event-img">
                <img src="img/icon.JPG"  alt="Аватарка">
            </div>
            <div class="event-title-descr">
                <h3 class="event-title">
                    Название события
                </h3>

                <div class="event-description">
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. In reiciendis a iusto consectetur,
                    nostrum fugit maiores, laborum est voluptatem ipsa totam dolor earum repellendus facilis
                    corporis adipisci doloremque itaque eius perferendis quibusdam aliquid! Non nemo earum soluta
                    rerum, ab cupiditate corporis eaque excepturi nihil molestiae tempore perferendis odio labore
                    doloremque?
                </div>
            </div>

            <div class="event-members">
                <h4 class="members-title">
                    Участники
                </h4>
                <div class="members-list">
                    member_Vasiliy_I
                    member_Vasiliy_II
                    member_Vasiliy_III
                </div>
            </div>

            <div class="event-body">
                <h4 class="event-body-title">Тело события</h4>
                Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что
                должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще
                непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть
                Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что
                должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще
                непонятно что должно быть Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть
                Тут вообще непонятно что должно быть Тут вообще непонятно что должно быть
            </div>

        </div>

        <div class="chat-main-box">
            <h4 class="event-chat">Чат</h4>
            <div class="chat-box">
                <p>Привет</p>
                <p>Привет</p>
                <p>Привет</p>
                <p>Привет</p>
                <p>Привет</p>
                <p>Привет</p>
                <p>Привет</p>
                <p>Привет</p>
                <p>Привет</p>
            </div>
        </div>
    </main>
          </>
        );
    }
}
