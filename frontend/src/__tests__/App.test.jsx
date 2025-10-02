import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import React from "react";

// Ejemplo: si tienes un App.jsx en src/
import App from "../App";

test("renders the app without crashing", () => {
  render(<App />);
  expect(screen.getByText(/Ecosoft/i)).toBeInTheDocument();
});
