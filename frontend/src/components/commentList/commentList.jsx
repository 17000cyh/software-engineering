import { List, ListItem, ListItemText } from "@material-ui/core";
import React, { Component } from "react";
import { fetchComments } from "../../service/articleService";
import CommentItem from "./commentItem";
class CommentList extends Component {
  state = { comments: [] };
  async componentDidMount() {
    const comments = await fetchComments(this.props.targetId);
    this.setState({ comments });
  }
  render() {
    console.log("Comments", this.state.comments);
    return (
      <List>
        {this.state.comments.map((comment) => (
          <ListItem key={Math.random() + comment.content} divider>
            {/* <ListItemText> */}

            <CommentItem comment={comment} />
            {/* </ListItemText> */}
          </ListItem>
        ))}
      </List>
    );
  }
}

export default CommentList;
