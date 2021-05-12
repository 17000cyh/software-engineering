import React from "react";
import Typography from "@material-ui/core/Typography";
import Link from "@material-ui/core/Link";
const CopyRight = (props) => {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      <Link
        color="inherit"
        href="https://github.com/17000cyh/software-engineering"
      >
        Yuhang Chen, Chunxu Yang, Siwei Wei
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
};

export default CopyRight;
