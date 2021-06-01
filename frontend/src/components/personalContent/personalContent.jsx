import { Grid } from "@material-ui/core";
import React from "react";
import { Route, Switch } from "react-router-dom";
import ChatPage from "../../pages/personPage/chatPage";
import CollectPage from "../../pages/personPage/collectPage";
import CommentPage from "../../pages/personPage/commentPage";
import HistoryPage from "../../pages/personPage/historyPage";
import LikePage from "../../pages/personPage/likePage";
import ProfilePage from "../../pages/personPage/profilePage";
import NavTabs from "../navTabs/navTabs";

const PersonalContent = (props) => {
  const tabs = [
    { label: "个人信息", to: "/home/person/profile" },
    { label: "私信", to: "/home/person/chat" },
    { label: "点赞", to: "/home/person/like" },
    { label: "评论", to: "/home/person/comment" },
    { label: "收藏", to: "/home/person/collect" },
    { label: "历史", to: "/home/person/history" },
  ];
  return (
    <Grid item>
      <Grid container spacing={3} direction="column">
        <Grid item>
          <NavTabs tabs={tabs} />
        </Grid>
        <Grid item>
          <Switch>
            <Route
              path="/home/person/chat"
              render={() => <ChatPage user={1} />}
            />
            <Route
              path="/home/person/like"
              render={() => <LikePage user={1} />}
            />
            <Route
              path="/home/person/comment"
              render={() => <CommentPage user={1} />}
            />
            <Route
              path="/home/person/collect"
              render={() => <CollectPage user={1} />}
            />
            <Route
              path="/home/person/history"
              render={() => <HistoryPage user={1} />}
            />
            <Route
              path="/home/person/"
              render={() => <ProfilePage user={1} />}
            />
          </Switch>
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
