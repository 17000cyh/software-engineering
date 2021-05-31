import "./App.css";
import { Route, Switch, Redirect } from "react-router-dom";
import HomePage from "./pages/homePage/homePage";
import LoginPage from "./pages/loginPage/loginPage";
import SignupPage from "./pages/signupPage/signupPage";
import NotFoundPage from "./pages/notFoundPage/notFoundPage";

function App() {
  return (
    <div className="App">
      <Switch>
        <Route path="/login" component={LoginPage} />
        <Route path="/signup" component={SignupPage} />
        <Route path="/home" component={HomePage} />
        <Route path="/not-found" component={NotFoundPage} />
        <Route path="/" component={HomePage} />
        {/* <Redirect to="/not-found" /> */}
      </Switch>
    </div>
  );
}

export default App;
