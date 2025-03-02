"use client";
import { useSession } from "next-auth/react";

function Dashboard() {
  const { data: session, status } = useSession();

  if (status === "loading") {
    return <h1>Loading...</h1>;
  }

  if (status === "unauthenticated") {
    return <h1 id="dashboard__access-denied">Access Denied</h1>;
  }
  console.log(session)
  return <h1 id="dashboard__welcome-user">Welcome, {session.user.email}</h1>;
}

export default Dashboard;
