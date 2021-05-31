import { Grid } from "@material-ui/core";
import React from "react";
import NavTabs from "../navTabs/navTabs";

const PersonalContent = (props) => {
  const tabs = [
    { label: "私信", to: "/home/person/chat" },
    { label: "点赞", to: "" },
    { label: "评论", to: "" },
    { label: "收藏", to: "" },
    { label: "历史", to: "" },
  ];
  return (
    <Grid item>
      <Grid container spacing={3} direction="column">
        <Grid item>
          <NavTabs tabs={tabs} />
        </Grid>
        {/* <Grid item>
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
      </Grid> */}
      </Grid>
    </Grid>
  );
};

export default PersonalContent;
