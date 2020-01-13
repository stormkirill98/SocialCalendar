import React from "react"

export default class IconsGrid extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedElement: document.getElementById("bell.svg"),
            selected: "bell.svg"
        };
        console.log(this.state.selectedElement);
        this.selectChanged = this.selectChanged.bind(this);
    }

    selectChanged(select) {
        this.props.changeIcon(select);

        if (this.state.selectedElement)
            this.state.selectedElement.style.border = '0px'

        let el = document.getElementById(select);
        this.setState({
            selected: select,
            selectedElement: el
        });
        el.style.border = '5px solid red';
        el.style.borderRadius = '25%';
    }

    render() {
        return (
            <div className="flex-center">
                <div id="icons-grid" className="icons-grid">
                    <div id="bell.svg" onClick={() => this.selectChanged("bell.svg")}><img src="/load_icon/bell.svg" alt="1" /></div>{/*onClick={this.selectChanged("bell.svg")}/>*/}
                    <div id="burger.svg" onClick={() => this.selectChanged("burger.svg")}><img src="/load_icon/burger.svg" alt="2" /></div>{/*onClick={this.selectChanged("burger.svg")}/>*/}
                    <div id="cart.svg" onClick={() => this.selectChanged("cart.svg")}><img src="/load_icon/cart.svg" alt="3" /></div>{/*onClick={this.selectChanged("cart.svg")}/>*/}
                    <div id="coctail.svg" onClick={() => this.selectChanged("coctail.svg")}><img src="/load_icon/coctail.svg" alt="4" /></div>{/*onClick={this.selectChanged("coctail.svg")}/>*/}
                    <div id="coffee.svg" onClick={() => this.selectChanged("coffee.svg")}><img src="/load_icon/coffee.svg" alt="5" /></div>{/*onClick={this.selectChanged("coffee.svg")}/>*/}
                    <div id="confirm.svg" onClick={() => this.selectChanged("confirm.svg")}><img src="/load_icon/confirm.svg" alt="6" /></div>{/*onClick={this.selectChanged("confirm.svg")}/>*/}
                    <div id="delete.svg" onClick={() => this.selectChanged("delete.svg")}><img src="/load_icon/delete.svg" alt="7" /></div>{/*onClick={this.selectChanged("delete.svg")}/>*/}
                    <div id="doughnut.svg" onClick={() => this.selectChanged("doughnut.svg")}><img src="/load_icon/doughnut.svg" alt="8" /></div>{/*onClick={this.selectChanged("doughnut.svg")}/>*/}
                    <div id="exit.svg" onClick={() => this.selectChanged("exit.svg")}><img src="/load_icon/exit.svg" alt="9" /></div>{/*onClick={this.selectChanged("exit.svg")}/>*/}
                    <div id="gamepad.svg" onClick={() => this.selectChanged("gamepad.svg")}><img src="/load_icon/gamepad.svg" alt="10" /></div>{/*onClick={this.selectChanged("gamepad.svg")}/>*/}
                    <div id="glasses.svg" onClick={() => this.selectChanged("glasses.svg")}><img src="/load_icon/glasses.svg" alt="11" /></div>{/*onClick={this.selectChanged("glasses.svg")}/>*/}
                    <div id="heart.svg" onClick={() => this.selectChanged("heart.svg")}><img src="/load_icon/heart.svg" alt="12" /></div>{/*onClick={this.selectChanged("heart.svg")}/>*/}
                    <div id="music.svg" onClick={() => this.selectChanged("music.svg")}><img src="/load_icon/music.svg" alt="13" /></div>{/*onClick={this.selectChanged("music.svg")}/>*/}
                    <div id="pin.svg" onClick={() => this.selectChanged("pin.svg")}><img src="/load_icon/pin.svg" alt="14" /></div>{/*onClick={this.selectChanged("pin.svg")}/>*/}
                    <div id="pizza.svg" onClick={() => this.selectChanged("pizza.svg")}><img src="/load_icon/pizza.svg" alt="15" /></div>{/*onClick={this.selectChanged("pizza.svg")}/>*/}
                    <div id="plus.svg" onClick={() => this.selectChanged("plus.svg")}><img src="/load_icon/plus.svg" alt="16" /></div>{/*onClick={this.selectChanged("plus.svg")}/>*/}
                </div>
            </div>
        )
    }
}