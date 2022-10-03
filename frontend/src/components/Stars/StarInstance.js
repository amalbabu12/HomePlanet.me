import React from "react";
import { Container, Col, Row } from "react-bootstrap";
import { Link } from "react-router-dom";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

function StarInstance(props) {
  return (
    <div className="Container">
      <React.Fragment>
        <Container className="card-container">
          <Row className="Card">
            <Col>
              <h1 class="cardTitle">{props.data.name}</h1>
              <hr />
              <img src={props.data.img} alt="star" class="star-img" width="350"/>
              <hr />
              <Col>
                <div class="bodyText">
                  <p>
                    {" "}<strong>Mass:</strong> {props.data.st_mass} UNITS{" "}
                  </p>
                </div>
              </Col>
            </Col>
          
  <Row>
              <Col>
                <div class="model-links">
                  <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 250 }}>
                      <TableHead>
                        <TableRow>
                          <TableCell>
                            {" "}
                            <strong> Moons You Might Be Interested In: </strong>{" "}
                          </TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {props.data.moons.map((p) => (
                          <Link
                            class="link"
                            to={"/moon/" + p.moonKey}>
                            <p> {p.moonName}</p>
                          </Link>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                  <br></br>
                </div>
              </Col>
              <Col>
                <div class="model-links">
                  <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 250 }}>
                      <TableHead>
                        <TableRow>
                          <TableCell>
                            {" "}
                            <strong> Planets You Might Be Interested In: </strong>{" "}
                          </TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {props.data.planets.map((p) => (
                          <Link
                            class="link"
                            to={"/planet/" + p.planetKey}>
                            <p> {p.planetName}</p>
                          </Link>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                  <br></br>
                </div>
              </Col>
            </Row>

          </Row>
        </Container>
      </React.Fragment>
    </div>
  );
}
export default StarInstance;