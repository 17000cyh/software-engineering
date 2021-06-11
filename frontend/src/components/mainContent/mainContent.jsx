import { Grid, Paper, makeStyles } from "@material-ui/core";
import React from "react";
import { Route } from "react-router";
import ArticleList from "../articleList/articleList";
import NavSider from "../navSider/navSider";
import NavTabs from "../navTabs/navTabs";

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

const MainContent = (props) => {
  const classes = useStyles();
  const tabs = props.user
    ? [
        {
          label: "推荐",
          to: "/home/recommend",
        },
        {
          label: "关注",
          to: "/home/follow",
        },
        {
          label: "热榜",
          to: "/home/hot",
        },
      ]
    : [
        {
          label: "推荐",
          to: "/home/recommend",
        },
        {
          label: "热榜",
          to: "/home/hot",
        },
      ];
  return (
    <Grid item>
      <Grid container spacing={3} direction="row">
        <Grid item xs={10}>
          <Grid container spacing={3} direction="column">
            <Grid item>
              <NavTabs tabs={tabs} />
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
          </Grid>
        </Grid>
        <Grid item xs={2}>
          <Paper className={classes.paper} style={{ position: "sticky" }}>
            <NavSider login={false} />
          </Paper>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default MainContent;
