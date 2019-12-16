import React, { Suspense, lazy } from 'react';
import ReactDOM from 'react-dom';
import './css/index.css';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
//import './Header.jsx'

//const Headerr = lazy(() => import('./Header.jsx'));
//const About = lazy(() => import('./routes/About'));

class Routing extends React.Component {
    render() {
        return (
            <Router>
                <Suspense fallback={<div>Загрузка...</div>}>
                    <Switch>
                        <Route path="/">
                            <Main />
                        </Route>

                        <Route path="/Calendar">
                            <Calendar />
                        </Route>
                    </Switch>
                </Suspense>
            </Router>
        );
    }
}

function Main() {
    return (
        <>
            <div class="title">Social Calendar</div>
            <a href="Calendar" class="google-auth">
                <img src="img/SingInWithGoogle.png" alt="зайти через гугол" class="google-img" />
            </a>
        </>
    )
}

function Calendar(){
    return(
        <div>dgsgsdgsdgsdg</div>
    )
}

function Header(){
    return(
        <div>dgsgsdgsdgsdg</div>
    )
}

// class Main extends React.Component {
//     render() {
//         return (
//             <>
//                 <div class="title">Social Calendar</div>
//                 {/* <Link to="/Calendar" className="google-auth">
//                     <img src="img/SingInWithGoogle.png" alt="зайти через гугол" class="google-img" />
//                 </Link> */}
//                 <a href="Calendar" class="google-auth">
//                     <img src="img/SingInWithGoogle.png" alt="зайти через гугол" class="google-img" />
//                 </a>
//             </>
//         );
//     }
// }


// class Header extends React.Component {
//     render() {
//         return (
//             <>
//                 <div>ujdyjsdgsdfbhdfhfhdfh</div>
//                 {/* <header class="bg-success">
//                     <nav class="nav navbar-light">
//                         <div class="button">
//                             <input type="checkbox" id="hmt" class="hidden-menu-ticker" />>
//                         <label class="btn-menu" for="hmt">
//                                 <span class="first"></span>
//                                 <span class="second"></span>
//                                 <span class="third"></span>
//                             </label>
//                             <ul class="hidden-menu">
//                                 <a class="hidden-menu-brand" href="Calendar.html">Social Calendar</a>
//                                 <li class="left-link"><a href="Calendar.html">Календарь</a></li>
//                                 <li class="left-link"><a href="friends.html">Друзья</a></li>
//                                 <li class="left-link"><a href="dialogues.html">Чаты</a></li>
//                             </ul>
//                         </div>
//                         <a class="navbar-brand" href="Calendar.html">Social Calendar</a>
//                         <li class="nav-item">
//                             <a class="nav-link" href="Calendar.html">Календарь</a>
//                         </li>
//                         <li class="nav-item">
//                             <a class="nav-link" href="friends.html">Друзья</a>
//                         </li>
//                         <li class="nav-item">
//                             <a class="nav-link" href="dialogues.html">Чаты</a>
//                         </li>
//                     </nav>
//                     <div class="auth-box">

//                         <div class="auth-left">
//                             <a href="Calendar.html" class="auth-img">
//                                 <img src="img/icon.JPG" width="50" height="50" alt="Аватарка" />>
//                         </a>
//                         </div>

//                         <div class="auth-right">
//                             <a class="auth-name" href="Calendar.html">Семён Петрович</a>
//                             <div class="icons">
//                                 <a href="Options.html">
//                                     <img class="options" src="img/settings.png" alt="Настройки" />>
//                             </a>
//                                 <a href="#">
//                                     <img class="notification" src="img/notifications.png" alt="Оповещения" />>
//                             </a>
//                             </div>
//                         </div>
//                     </div>
//                 </header> */}
//             </>
//         );
//     }
// }

ReactDOM.render(
    <Routing />,
    document.getElementById('root')
);

// ======================================== рабочая прога с роутингом

// import React from "react";
// import ReactDOM from 'react-dom';
// import {
//   BrowserRouter as Router,
//   Switch,
//   Route,
//   Link
// } from "react-router-dom";

// export default function App() {
//   return (
//     <Router>
//       <div>
//         <nav>
//           <ul>
//             <li>
//               <Link to="/">Home</Link>
//             </li>
//             <li>
//               <Link to="/about">About</Link>
//             </li>
//             <li>
//               <Link to="/users">Users</Link>
//             </li>
//           </ul>
//         </nav>

//         {/* A <Switch> looks through its children <Route>s and
//             renders the first one that matches the current URL. */}
//         <Switch>
//           <Route path="/about">
//             <About />
//           </Route>
//           <Route path="/users">
//             <Users />
//           </Route>
//           <Route path="/">
//             <Home />
//           </Route>
//         </Switch>
//       </div>
//     </Router>
//   );
// }

// function Home() {
//   return <h2>Home</h2>;
// }

// function About() {
//   return <h2>About</h2>;
// }

// function Users() {
//   return <h2>Users</h2>;
// }

// ReactDOM.render(
//     App(),
//     document.getElementById('root')
// );
