import { googleIcon } from "@/assets/icons";
import { Button } from "devextreme-react/button";

const GoogleSignInButton = () => {
  return (
    <Button
      text="Sign In with Google"
      stylingMode="contained"
      icon={googleIcon}
    />
  );
};

export default GoogleSignInButton;
