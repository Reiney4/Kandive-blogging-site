import React from "react";
import Logo from "../images/logo.png";

const Footer = () => {
  return (
    <footer>
      <span>
        <img src={Logo} alt="logo" />
        <br />
        Made with 🤍 by
        <br />
        <b>@valerie & @olive</b>
      </span>
    </footer>
  );
};

export default Footer;
