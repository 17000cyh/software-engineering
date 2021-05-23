import { AppBar, Grid, makeStyles, Paper, Tabs, Tab } from "@material-ui/core";
import React from "react";
import NavHeader from "../../components/navHeader/navHeader";
import NavTabs from "../../components/navTabs/navTabs";
import ArticleItem from "../../components/articleItem/articleItem";
import { fetchArticles } from "../../service/articleService";
import ArticleList from "../../components/articleList/articleList";

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
  let articles = fetchArticles(-1);
  return (
    <React.Fragment>
      <Grid container spacing={3} direction="column">
        {/* <Grid item> */}
        <NavHeader login={false} />
        {/* </Grid> */}

        <Grid item>
          <Grid container spacing={3} direction="row">
            <Grid item xs={9}>
              <NavTabs />
              <ArticleList />
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
