import React from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import CopyRight from "../../components/copyRight/copyRight";
import { Link } from "react-router-dom";
import { trySignup } from "../../service/userService";
import { useSnackbar } from "notistack";

const DUPLICATE_PHONE = 1;
const DUPLICATE_EMAIL = 2;

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
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function SignupPage() {
  let user = {
    email: "",
    tel: "",
    password: "",
    name: "",
  };

  const classes = useStyles();

  const { enqueueSnackbar } = useSnackbar();

  const handleSubmit = (e) => {
    e.preventDefault();
    let res = trySignup(user.tel, user.email, user.name, user.password);
    console.log(res);
    if (res.status === false) {
      if (res.code === DUPLICATE_PHONE) {
        enqueueSnackbar("该手机号已经被注册", { variant: "error" });
      } else if (res.code === DUPLICATE_EMAIL) {
        enqueueSnackbar("该邮箱已经被注册", { variant: "error" });
      } else {
        enqueueSnackbar("未知错误", { variant: "error" });
      }
    } else {
      enqueueSnackbar("注册成功", { variant: "success" });
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
          注册
        </Typography>
        <form
          className={classes.form}
          noValidate
          onSubmit={handleSubmit.bind(this)}
        >
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="name"
                label="用户名"
                name="name"
                onChange={(event) => {
                  user.name = event.target.value;
                }}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="tel"
                label="手机号码"
                name="tel"
                autoComplete="tel"
                onChange={(event) => {
                  user.tel = event.target.value;
                }}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label="邮箱"
                name="email"
                autoComplete="email"
                onChange={(event) => {
                  user.email = event.target.value;
                }}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
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
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            注 册
          </Button>
          <Grid container justify="flex-end">
            <Grid item>
              <Link to="/login" variant="body2">
                登入已有账号
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
        <CopyRight />
      </Box>
    </Container>
  );
}
