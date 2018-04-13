import React, { Component } from 'react';
import { render } from 'react-dom';

import Form from 'react-jsonschema-form';

import '../scss/main.scss';

const field = document.getElementsByName(window.foreignformField)[0];
const fieldContainerClass = `field-${window.foreignformField}`;
const fieldContainer = document.getElementsByClassName(fieldContainerClass)[0];
fieldContainer.style = 'display: none;';

const formApp = (
  <Form
    className="foreignform"
    schema={window.foreignformJSONSchema}
    uiSchema={window.foreignformUISchema}
    formData={JSON.parse(field.value)}
    onChange={(form) => {
      field.value = JSON.stringify(form.formData);
    }}
    liveValidate
  />
);

render(formApp, document.getElementById('foreignform'));
