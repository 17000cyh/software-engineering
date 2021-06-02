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

class App extends Component {
  state = {};
  componentDidMount() {
    try {
      const jwt = localStorage.getItem("token");
      const user = jwtDecode(jwt);
      this.setState({ user });
    } catch (error) {}
  }
  render() {
    return (
      <div className="App">
        <NavHeader user={this.state.user} />
        <Switch>
          <Route path="/login" component={LoginPage} />
          <Route path="/signup" component={SignupPage} />
          <Route path="/home" component={HomePage} />
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
