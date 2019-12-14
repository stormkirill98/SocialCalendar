import React from 'react';
import ReactDOM from 'react-dom';
import './css/Calendar.css';
//import './Header'

class Main extends React.Component {
    render() {
        return (
            <>
                <div class="title">Social Calendar</div>
                <a href="Calendar.html" class="google-auth">
                    <img src="img/SingInWithGoogle.png" alt="зайти через гугол" class="google-img" />>
                </a>
            </>
        );
    }
}

// ========================================

ReactDOM.render(
    <Main />,
    document.getElementById('root')
);
