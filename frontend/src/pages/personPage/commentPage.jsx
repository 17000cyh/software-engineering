import { Paper } from "@material-ui/core";
import React, { Component } from "react";

import { fetchReplyList } from "../../service/personalService";

class CommentPage extends Component {
  state = {
    commentList: [],
  };
  async componentDidMount() {
    const { user } = this.props;
    const commentList = await fetchReplyList(user);
    this.setState({ commentList });
  }
  render() {
    return (
      <Paper>{this.state.commentList.map((comment) => comment.content)}</Paper>
    );
  }
}

export default CommentPage;

// const CommentPage = (props) => {
//   const { user } = props;
//   const commentList = fetchReplyList(user);
//   console.log(commentList);
//   return ;
// };

// export default CommentPage;
