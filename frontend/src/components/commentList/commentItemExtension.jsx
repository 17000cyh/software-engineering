import React from "react";
import ThumbUpIcon from "@material-ui/icons/ThumbUp";
import { Button, Grid } from "@material-ui/core";

const CommentItemExtension = (props) => {
  return (
    <Grid container spacing={2} direction="row">
      <Grid item>
        <ThumbUpIcon fontSize="small" />
      </Grid>
      <Grid item>
        <Button>查看回复</Button>
      </Grid>
    </Grid>
  );
};

export default CommentItemExtension;
