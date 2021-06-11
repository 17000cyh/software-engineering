import {
  ListItem,
  ListItemAvatar,
  ListItemText,
  Avatar,
} from "@material-ui/core";
import PersonIcon from "@material-ui/icons/Person";
import React, { Component } from "react";
import CommentItemExtension from "./commentItemExtension";
class CommentItem extends Component {
  state = {};
  render() {
    const { comment } = this.props;
    return (
      <ListItem>
        <ListItemAvatar>
          <Avatar>
            <PersonIcon />
          </Avatar>
        </ListItemAvatar>
        <ListItemText
          primary={comment.content}
          secondary={<CommentItemExtension />}
        />
      </ListItem>
    );
  }
}

export default CommentItem;
