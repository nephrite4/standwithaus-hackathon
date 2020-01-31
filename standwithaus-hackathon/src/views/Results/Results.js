import React, { Component, lazy, Suspense } from 'react';
import { Bar, Line } from 'react-chartjs-2';
import {
  Badge,
  Button,
  ButtonDropdown,
  ButtonGroup,
  ButtonToolbar,
  Card,
  CardBody,
  CardFooter,
  CardHeader,

  CardTitle,
  Col, Collapse,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  DropdownToggle, Fade, Form, FormGroup, FormText, Input, InputGroup, InputGroupAddon, InputGroupText, Label,
  Progress,
  Row,
  Table,
} from 'reactstrap';
import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';
import { getStyle, hexToRgba } from '@coreui/coreui/dist/js/coreui-utilities'
import SWABanner from "../../assets/img/standwithausbanner.png";
import axios from "axios";

const Widget03 = lazy(() => import('../../views/Widgets/Widget03'));

const brandPrimary = getStyle('--primary')
const brandSuccess = getStyle('--success')
const brandInfo = getStyle('--info')
const brandWarning = getStyle('--warning')
const brandDanger = getStyle('--danger')


class Results extends Component {
  constructor(props) {
    super(props);

    // this.toggle = this.toggle.bind(this);
    // this.onRadioBtnClick = this.onRadioBtnClick.bind(this);

    this.state = {
      similarity: {},
      match: {}
    }

  }

  // toggle() {
  //   this.setState({
  //     dropdownOpen: !this.state.dropdownOpen,
  //   });
  // }

  // onRadioBtnClick(radioSelected) {
  //   this.setState({
  //     radioSelected: radioSelected,
  //   });
  // }

  loading = () => <div className="animated fadeIn pt-1 text-center">Loading...</div>

  handleSubmit = e => {
    e.PreventDefault();
    axios.post('http://127.0.0.1:5000/', { title: this.state.title, details : this.state.details}).then(res=>{
      console.log(res);
      console.log(res.data);})
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value});
  }


  componentDidMount(){
    axios.get("http://127.0.0.1:5000/", {}) // where the api gets fetched from that API
        .then(res=>{
          console.log(res);
          this.setState({ persons: res.data});
        })
  }

  render() {

    return (
      <div className="animated fadeIn">
        <Row>
          <Col>
            <Row>
              <Card className="m-3">
              <img height="auto" width="100%" src={SWABanner}/>
              </Card>
            </Row>

          </Col>
        </Row>
        <Row>
          <Col xs="12">
            <Card>
              <CardHeader>
                <strong>CrowdFunding Form</strong>
              </CardHeader>
              <CardBody>
                <Form onSubmit={this.handleSubmit} action="http://0.0.0.0:5000/" method="post" encType="multipart/form-data" className="form-horizontal">
                  <FormGroup row>
                    <Col md="2">
                      <Label htmlFor="title">Title</Label>
                    </Col>
                    <Col xs="12" md="10">
                      <Input onChange={this.onChange} type="text" id="title" name="title" placeholder="Title"/>
                    </Col>
                  </FormGroup>
                  <FormGroup row>
                    <Col md="2">
                      <Label htmlFor="details">Details</Label>
                    </Col>
                    <Col xs="12" md="10">
                      <Input onChange={this.onChange}  type="textarea" name="details" id="details" rows="9"
                             placeholder="Details of your crowdfund" />
                    </Col>
                  </FormGroup>
                  <FormGroup row>
                    <Col md="2">
                      <Label htmlFor="file-multiple-input">Images</Label>
                    </Col>
                    <Col xs="12" md="10">
                      <Input onChange={this.onChange}  type="file" id="file" name="file" multiple />
                    </Col>
                  </FormGroup>
                  <Button type="submit" size="sm" color="primary"><i className="fa fa-dot-circle-o"></i> Submit</Button>
                  <Button type="reset" size="sm" color="danger"><i className="fa fa-ban"></i> Reset</Button>
                </Form>
              </CardBody>
              <CardFooter>
              </CardFooter>
            </Card>
          </Col>
        </Row>
      </div>
    );
  }
}

export default Results;
