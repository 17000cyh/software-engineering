import React, { useState, Component } from "react";
import { fetchArticles } from "../../service/articleService";
import { Grid } from "@material-ui/core";
import ArticleItem from "../articleItem/articleItem";
import InfiniteScroll from "react-infinite-scroller";

class ArticleList extends Component {
  state = { hasMoreItems: true, items: [] };
  loadItems(page) {
    let self = this;
    const response = fetchArticles();
    const hasMore = response.hasMore;
    const newItems = response.articles;
    self.setState({
      hasMoreItems: hasMore,
      items: [...this.state.items, ...newItems],
    });
  }
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
          {this.state.items.map((article) => (
            <Grid item>
              <ArticleItem
                title={article.article_name}
                content={article.article_content}
              />
            </Grid>
          ))}
        </Grid>
      </InfiniteScroll>
    );
  }
}

export default ArticleList;