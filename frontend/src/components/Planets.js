import React from "react";
import PlanetList from "./Planets/PlanetList.js";
import { Container, Col, Row } from "react-bootstrap";
import PlanetSort from "./Planets/PlanetSort.js";
import PlanetFilter from "./Planets/PlanetFilter.js";
import "../App.css";

class Planets extends React.Component {
  render() {
    return (
      <Container>
          <h1>Planets</h1>
        <Row>
          <Col>
          <h2>Sort By</h2>
          <PlanetSort />
          </Col>
            <Col>
            <h2>Filter By Temperature</h2>
          <PlanetFilter />
            </Col>
          </Row>
        <Row>
          <Col>
            <PlanetList />
          </Col>
        </Row>
      </Container>
    );
  }
}
export default Planets;
