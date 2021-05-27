import {
  Grid,
  makeStyles,
  Paper,
  useScrollTrigger,
  Zoom,
  Fab,
} from "@material-ui/core";
import KeyboardArrowUpIcon from "@material-ui/icons/KeyboardArrowUp";
import React from "react";
import NavHeader from "../../components/navHeader/navHeader";
import NavTabs from "../../components/navTabs/navTabs";
import ArticleList from "../../components/articleList/articleList";
import NavSider from "../../components/navSider/navSider";
// import { Route } from "react-router";
import { Route } from "react-router-dom";

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

function ScrollTop(props) {
  const { children, window } = props;
  const classes = useStyles();
  // Note that you normally won't need to set the window ref as useScrollTrigger
  // will default to window.
  // This is only being set here because the demo is in an iframe.
  const trigger = useScrollTrigger({
    // target: window ? window() : undefined,
    disableHysteresis: true,
    threshold: 100,
  });

  const handleClick = (event) => {
    const anchor = (event.target.ownerDocument || document).querySelector(
      "#back-to-top-anchor"
    );

    if (anchor) {
      anchor.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

  return (
    <Zoom in={trigger}>
      <div onClick={handleClick} role="presentation" className={classes.root}>
        {children}
      </div>
    </Zoom>
  );
}

const HomePage = (props) => {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Grid container spacing={3} direction="column">
        {/* <Grid item> */}
        <NavHeader login={false} />
        {/* </Grid> */}

        <Grid item>
          <Grid container spacing={3} direction="row">
            <Grid item xs={10}>
              <Grid container spacing={3} direction="column">
                <Grid item>
                  <NavTabs />
                </Grid>
                <Grid item>
                  <Route
                    path="/home/recommend"
                    exact
                    render={() => <ArticleList data={"recommend"} />}
                  />
                  <Route
                    path="/home/follow"
                    exact
                    render={() => <ArticleList data={"follow"} />}
                  />
                  <Route
                    path="/home/hot"
                    exact
                    render={() => <ArticleList data={"hot"} />}
                  />
                  <ArticleList />
                </Grid>
                <ScrollTop {...props}>
                  <Fab
                    color="secondary"
                    size="small"
                    aria-label="scroll back to top"
                  >
                    <KeyboardArrowUpIcon />
                  </Fab>
                </ScrollTop>
              </Grid>
            </Grid>
            <Grid item xs={2}>
              <Paper className={classes.paper} style={{ position: "sticky" }}>
                <NavSider login={false} />
              </Paper>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </React.Fragment>
  );
};

export default HomePage;
