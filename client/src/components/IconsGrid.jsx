import React from "react"

export default class IconsGrid extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selected: null
        };
    }

    render(){
        return(
            <div className="icons-grid">
                <img src="/load_icon/bell.svg" alt="" onClick={this.props.updateData("/load_icon/bell.svg")}/>
                <img src="/load_icon/burger.svg" alt="" onClick={this.props.updateData("/load_icon/burger.svg")}/>
                <img src="/load_icon/cart.svg" alt="" onClick={this.props.updateData("/load_icon/cart.svg")}/>
                <img src="/load_icon/coctail.svg" alt="" onClick={this.props.updateData("/load_icon/coctail.svg")}/>
                <img src="/load_icon/coffee.svg" alt="" onClick={this.props.updateData("/load_icon/coffee.svg")}/>
                <img src="/load_icon/confirm.svg" alt="" onClick={this.props.updateData("/load_icon/confirm.svg")}/>
                <img src="/load_icon/delete.svg" alt="" onClick={this.props.updateData("/load_icon/delete.svg")}/>
                <img src="/load_icon/doughnut.svg" alt="" onClick={this.props.updateData("/load_icon/doughnut.svg")}/>
                <img src="/load_icon/exit.svg" alt="" onClick={this.props.updateData("/load_icon/exit.svg")}/>
                <img src="/load_icon/gamepad.svg" alt="" onClick={this.props.updateData("/load_icon/gamepad.svg")}/>
                <img src="/load_icon/glasses.svg" alt="" onClick={this.props.updateData("/load_icon/glasses.svg")}/>
                <img src="/load_icon/heart.svg" alt="" onClick={this.props.updateData("/load_icon/heart.svg")}/>
                <img src="/load_icon/music.svg" alt="" onClick={this.props.updateData("/load_icon/music.svg")}/>
                <img src="/load_icon/pin.svg" alt="" onClick={this.props.updateData("/load_icon/pin.svg")}/>
                <img src="/load_icon/pizza.svg" alt="" onClick={this.props.updateData("/load_icon/pizza.svg")}/>
                <img src="/load_icon/plus.svg" alt="" onClick={this.props.updateData("/load_icon/plus.svg")}/>
            </div>
        )
    }
}