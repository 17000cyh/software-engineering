import React, { useState } from "react";
import { fetchArticles } from "../../service/articleService";
import InfinateLoading from "react-simple-infinite-loading";
import { Grid } from "@material-ui/core";
import ArticleItem from "../articleItem/articleItem";

const ArticleList = (props) => {
  const [items, setItems] = useState(fetchArticles().articles);
  const [more, setMore] = useState(false);
  const loadMoreItems = () => {
    const response = fetchArticles();
    const hasMore = response.hasMore;
    const newItems = response.articles;

    return new Promise((resolve) => {
      setTimeout(() => {
        setItems([...items, ...newItems]);
        setMore(hasMore);
        resolve();
      }, 300);
    });
  };
  const newItems = fetchArticles();
  return (
    <InfinateLoading hasMoreItems={more} loadMoreItems={loadMoreItems}>
      <Grid container spacing={3} direction="column">
        {items.map((article) => (
          <Grid item>
            <ArticleItem
              title={article.article_name}
              content={article.article_content}
            />
          </Grid>
        ))}
      </Grid>
    </InfinateLoading>
  );
};

export default ArticleList;
