import "./App.css";
import { Route, Switch, Redirect } from "react-router-dom";
import HomePage from "./pages/homePage/homePage";
import LoginPage from "./pages/loginPage/loginPage";
import SignupPage from "./pages/signupPage/signupPage";
import NotFoundPage from "./pages/notFoundPage/notFoundPage";

import React, { Component } from "react";
import jwtDecode from "jwt-decode";
import NavHeader from "./components/navHeader/navHeader";
import Logout from "./components/logout/logout";
import { Home } from "@material-ui/icons";

class App extends Component {
  state = { user: null };
  componentDidMount() {
    try {
      const token = localStorage.getItem("token");
      this.setState({ user: token });
    } catch (error) {
      console.log(error);
      // this.setState({ user: null });
    }
  }
  render() {
    console.log(this.state.user);
    return (
      <div className="App">
        <NavHeader user={this.state.user} />
        <Switch>
          <Route path="/login" component={LoginPage} />
          <Route path="/signup" component={SignupPage} />
          <Route
            path="/home"
            render={() => <HomePage user={this.state.user} />}
          />
          <Route path="/logout" component={Logout} />
          <Route path="/not-found" component={NotFoundPage} />
          <Redirect path="/" exact to="/home" />
          <Redirect to="/not-found" />
        </Switch>
      </div>
    );
  }
}

export default App;
