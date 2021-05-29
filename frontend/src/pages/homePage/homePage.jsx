import { Grid } from "@material-ui/core";
import React from "react";
import NavHeader from "../../components/navHeader/navHeader";
import MainContent from "../../components/mainContent/mainContent";

const HomePage = (props) => {
  return (
    <React.Fragment>
      <Grid container spacing={3} direction="column">
        {/* <Grid item> */}
        <NavHeader login={true} />
        {/* </Grid> */}

        <MainContent />
      </Grid>
    </React.Fragment>
  );
};

export default HomePage;
