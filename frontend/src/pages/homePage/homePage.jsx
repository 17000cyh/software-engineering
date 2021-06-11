import { Grid } from "@material-ui/core";
import React from "react";
import NavHeader from "../../components/navHeader/navHeader";
import MainContent from "../../components/mainContent/mainContent";
import { Switch, Route } from "react-router-dom";
import PersonalContent from "../../components/personalContent/personalContent";

const HomePage = (props) => {
  return (
    <React.Fragment>
      <Grid container spacing={3} direction="column">
        {/* <NavHeader login={false} /> */}
        <Switch>
          <Route path="/home/person" render={() => <PersonalContent />} />
          <Route
            path="/home/"
            render={() => <MainContent user={props.user} />}
          />
        </Switch>
        {/* <MainContent /> */}
      </Grid>
    </React.Fragment>
  );
};

export default HomePage;
