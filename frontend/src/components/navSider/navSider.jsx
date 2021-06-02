import { Button, Grid } from "@material-ui/core";
import React from "react";
import { Link } from "react-router-dom";

const NavSider = (props) => {
  return (
    <React.Fragment>
      <Grid container spacing={3} direction="column">
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            size="large"
            fullWidth
            component={Link}
            to="/login"
          >
            我的消息
          </Button>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            size="large"
            fullWidth
            component={Link}
            to="/login"
          >
            我的收藏
          </Button>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            fullWidth
            component={Link}
            to="/login"
          >
            历史检索
          </Button>
        </Grid>

        <Grid item>
          <Button
            variant="contained"
            color="primary"
            size="large"
            fullWidth
            component={Link}
            to="/login"
          >
            系统信息
          </Button>
        </Grid>
      </Grid>
    </React.Fragment>
  );
};

export default NavSider;
