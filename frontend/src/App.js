import React, { Component } from "react";

import { Col, Container, Row } from "react-bootstrap";
import "./App.css";
import NavHeader from "./components/navHeader/navHeader";
import { Layout, Menu, Breadcrumb } from "antd";
import Sider from "antd/lib/layout/Sider";
import NavSider from "./components/navSider/navSider";

const { Header, Content, Footer } = Layout;

class App extends Component {
  state = {};
  render() {
    return (
      <div className="App">
        <Layout className="layout">
          <NavHeader />

          <Layout>
            <NavSider />
            <Layout style={{ padding: "0 24px 24px" }}>
              <Content
                className="site-layout-background"
                style={{
                  padding: 24,
                  margin: 0,
                  minHeight: 280,
                }}
              >
                Content
              </Content>
            </Layout>
          </Layout>
        </Layout>
      </div>
    );
  }
}
export default App;
