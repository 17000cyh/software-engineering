import React from "react";
// import logo from "../logo.png";
import { Input, Layout, Menu, Space, Form, Button } from "antd";
import { UserOutlined, HomeOutlined, ZoomInOutlined } from "@ant-design/icons";
// import HeaderSearch from "ant-design-pro/lib/HeaderSearch";
const { Header } = Layout;
const { Search } = Input;
const NavHeader = (props) => {
  return (
    <React.Fragment>
      <Header style={{ padding: 0 }}>
        <div className="logo" />
        {/* <Menu theme="dark" mode="horizontal"> */}
        <Space style={{ height: "100%" }}>
          <Button size="large" icon={<HomeOutlined />}></Button>
          <Search
            style={{ display: "block" }}
            placeholder="搜索..."
            allowClear
            size="large"
            enterButton
          />
          <Button size="large">
            高级搜索
            <ZoomInOutlined />
          </Button>
          <Button
            shape="circle"
            type="dashed"
            size="large"
            icon={<UserOutlined />}
          ></Button>
        </Space>
        {/* </Menu> */}
      </Header>
    </React.Fragment>
  );
};

export default NavHeader;
