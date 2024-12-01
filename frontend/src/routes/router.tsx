import React from "react";
import { createBrowserRouter } from "react-router-dom";
import { LandingPage } from "../app/landingpage//landingpage";
import { Login } from "../app/auth/login";
import { Register } from "../app/auth/register";
import { RestEmail } from "../app/auth/reset-email";
import { ResetPassword } from "../app/auth/reset-password";
import { VerifyEmail } from "../app/auth/verify-email";
import { Error404 } from "../components/404";
import { Loading } from "../components/loader";

/**
 * @function router - The router for the application.
 * @returns {React.ReactElement} The router for the application.
 */

export const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
    errorElement: <Error404 />
  },
  {
    path: "login",
    element: (
      <Loading>
        <Login />
      </Loading>
    ),
    errorElement: <Error404 />
  },
  {
    path: "register",
    element: (
      <Loading>
        <Register />
      </Loading>
    )
  },
  {
    path: "reset-email",
    element: (
      <Loading>
        <RestEmail />
      </Loading>
    )
  },
  {
    path: "reset-password",
    element: (
      <Loading>
        <ResetPassword />
      </Loading>
    )
  },
  {
    path: "verify-email",
    element: (
      <Loading>
        <VerifyEmail />
      </Loading>
    )
  },
  {
    path: "*",
    element: <Error404 />
  },
]);
