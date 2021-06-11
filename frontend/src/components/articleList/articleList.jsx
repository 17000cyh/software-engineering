import React, { Component } from "react";
import { fetchArticles, fetchFakeArticles } from "../../service/articleService";
import { Grid } from "@material-ui/core";
import ArticleItem from "../articleItem/articleItem";
import InfiniteScroll from "react-infinite-scroller";

class ArticleList extends Component {
  state = { hasMoreItems: true, items: [] };
  loadItems = async (page) => {
    let self = this;
    const response = await fetchArticles(1, this.props.data);

    console.log("res", response);
    const hasMore = response.hasMore;
    const newItems = response.articles;
    self.setState({
      hasMoreItems: hasMore,
      items: this.state.items.concat(newItems),
    });
    console.log(this.state.items);
  };
  render() {
    const loader = <div className="loader">Loading ...</div>;
    return (
      <InfiniteScroll
        pageStart={0}
        loadMore={this.loadItems.bind(this)}
        hasMore={this.state.hasMoreItems}
        loader={loader}
      >
        <Grid className="articles" container spacing={3} direction="column">
          {this.state.items.map(
            (article) =>
              article && (
                <Grid item key={Math.random() + article.name}>
                  <ArticleItem
                    title={article.name}
                    content={article.content}
                    targetId={article.id}
                  />
                </Grid>
              )
          )}
        </Grid>
      </InfiniteScroll>
    );
  }
}

export default ArticleList;
