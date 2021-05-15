import { AppBar, Grid, makeStyles, Paper, Tabs, Tab } from "@material-ui/core";
import React from "react";
import NavHeader from "../../components/navHeader/navHeader";
import NavTabs from "../../components/navTabs/navTabs";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
  nav: {
    textAlign: "left",
  },
}));
const HomePage = (props) => {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Grid container spacing={3} direction="column">
        <Grid item>
          <NavHeader login={false} />
        </Grid>

        <Grid item>
          <Grid container spacing={3} direction="row">
            <Grid item xs={9}>
              <NavTabs />
              <Grid container spacing={3} direction="column">
                <Grid item>
                  <Paper square>
                    <Tabs
                      indicatorColor="primary"
                      textColor="primary"
                      aria-label="disabled tabs example"
                    >
                      <Tab label="推荐" />
                      <Tab label="关注" />
                      <Tab label="热榜" />
                    </Tabs>
                  </Paper>
                </Grid>
                <Grid item>
                  <Paper className={classes.paper}>
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                    Main Content
                    <br />
                  </Paper>
                </Grid>
              </Grid>
            </Grid>
            <Grid item xs={3}>
              <Paper className={classes.paper}>Sider</Paper>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </React.Fragment>
  );
};

export default HomePage;
