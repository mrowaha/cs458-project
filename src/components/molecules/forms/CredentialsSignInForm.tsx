"use client";
import { signInIcon } from "@/assets/icons";
import { Form, Item, ButtonItem, Label } from "devextreme-react/form";
import { useCallback, useState } from "react";

const CredentialsSignInForm = () => {
  const [data, setData] = useState({
    email: "",
    password: "",
  });

  const handleSubmit = useCallback(() => {}, []);

  return (
    <form onSubmit={handleSubmit}>
      <Form formData={data} labelMode="static" labelLocation="top">
        <Item dataField="email" isRequired>
          <Label text="Email" />
        </Item>
        <Item dataField="password" isRequired>
          <Label text="Password" />
        </Item>
        <ButtonItem
          buttonOptions={{
            useSubmitBehavior: true,
            stylingMode: "contained",
            icon: signInIcon,
            text: "Sign In",
          }}
        />
      </Form>
    </form>
  );
};

export default CredentialsSignInForm;
