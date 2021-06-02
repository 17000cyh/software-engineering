import { List, ListItem, ListItemText } from "@material-ui/core";
import React, { Component } from "react";
import { fetchComments } from "../../service/articleService";
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
            <ListItemText>{comment.content}</ListItemText>
          </ListItem>
        ))}
      </List>
    );
  }
}

export default CommentList;
