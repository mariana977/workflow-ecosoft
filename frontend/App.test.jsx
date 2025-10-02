import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import React from "react";
import App from "../App";

test("muestra el mensaje de Tailwind funcionando", () => {
  render(<App />);
  expect(screen.getByText("¡Tailwind está funcionando!")).toBeInTheDocument();
});
