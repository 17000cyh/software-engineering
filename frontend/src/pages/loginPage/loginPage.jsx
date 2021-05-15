import React from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import CopyRight from "../../components/copyRight/copyRight";
import { Link } from "react-router-dom";
import { tryLogin } from "../../service/userService";
import { useSnackbar } from "notistack";

const WRONG_EMAIL = 1;
const WRONG_PASSWORD = 2;

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function LoginPage() {
  const classes = useStyles();
  let user = {
    email: "",
    password: "",
  };
  const { enqueueSnackbar } = useSnackbar();

  const handleSubmit = (e) => {
    e.preventDefault();
    let res = tryLogin(user.email, user.password);
    console.log(res);
    if (res.status === false) {
      if (res.code === WRONG_EMAIL) {
        enqueueSnackbar("此邮箱还未注册", { variant: "error" });
      } else if (res.code === WRONG_PASSWORD) {
        enqueueSnackbar("密码错误", { variant: "error" });
      } else {
        enqueueSnackbar("未知错误", { variant: "error" });
      }
    } else {
      enqueueSnackbar("登录成功", { variant: "success" });
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          登录到 CYW
        </Typography>
        <form
          className={classes.form}
          noValidate
          onSubmit={handleSubmit.bind(this)}
        >
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="邮箱"
            name="email"
            autoComplete="email"
            autoFocus
            onChange={(event) => {
              user.email = event.target.value;
            }}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="密码"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={(event) => {
              user.password = event.target.value;
            }}
          />
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="记住邮箱和密码"
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            登 录
          </Button>
          <Grid container>
            <Grid item>
              <Link to="#" variant="body2">
                忘记密码
              </Link>
            </Grid>
            <Grid item xs></Grid>
            <Grid item>
              <Link to="/signup" variant="body2">
                现在注册
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={8}>
        <CopyRight />
      </Box>
    </Container>
  );
}
